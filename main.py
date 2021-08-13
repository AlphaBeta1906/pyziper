import click
from colorama import Fore, init
from os import path, walk, getcwd
from os.path import getsize, join, exists
from pathlib import Path

from pyunpack import Archive
import tarfile
import py7zr
from zipfile import ZipFile, ZIP_DEFLATED

init(autoreset=True)


@click.group()
def pyziper():
    """pyziper a simple cli tools to help you to handle archive file
    ,like zipping or unzipping

    example zip a folder :\n
    pyziper zip <folder_name> <zip_file_name> -T [zip|7z|tar] -O <output_dir>

    example unzip a archive : \n
    pyziper unzip <zip_file_name>.zip|7z|tar.gz -O <output_dir>

    version : 0.3
    """
    pass


def default_zip(output_path, zip_name, folder_name):
    with ZipFile(join(output_path, zip_name) + '.zip', 'w') as _zip:

        for _folder_name, sub_folder, files in walk(folder_name):
            for file in files:
                filepath = join(_folder_name, file)
                _zip.write(filepath, filepath, ZIP_DEFLATED)
            for subFolder in sub_folder:
                subFolder_path = join(_folder_name, subFolder)
                _zip.write(subFolder_path, subFolder_path, ZIP_DEFLATED)


def _7zip(output_path, zip_name, folder_name, multi=False):
    try:
        with py7zr.SevenZipFile(join(output_path, zip_name) + '.7z', 'w') as _7z:
            if multi:
                """ """
                files = folder_name.split(",")
                for file in files:
                    _7z.writeall(file)
            else:
                _7z.writeall(folder_name)
    except FileNotFoundError as e:
        click.echo(Fore.RED + "Error: one or more file(s) is not found")
        exit()
    except KeyboardInterrupt:
        click.echo("aborted,zip file may already created but it possibly have error ")
        exit()


def tar_zip(output_path, zip_name, folder_name, multi=False):
    try:
        with tarfile.open(join(output_path, zip_name) + '.tar.gz', 'w:gz') as tar:
            if multi:
                files = folder_name.split(",")
                for file in files:
                    tar.addfile(tarinfo)
            else:
                tar.add(folder_name, arcname=folder_name)
    except FileNotFoundError as e:
        click.echo(Fore.RED + "Error: one or more file(s) is not found")
        exit()


@click.argument("zip_name", metavar="<zip_name>")
@click.argument("folder_name", metavar="<folder_name>")
@click.option('--multi', '-M', is_flag=True, help="enable multiple Archive")
@click.option(
    '--type',
    '-T',
    default='zip',
    help="defining type of arhcive,default = zip",
    metavar="<zip/7z/tar>",
)
@click.option('--output', '-O', help="output directory", metavar="<dir>")
@pyziper.command()
def zip(folder_name, zip_name, output, type, multi):
    """zip a folder"""
    if not exists(join(getcwd(), folder_name)) and not multi:
        click.echo(join(getcwd(), folder_name) + " not exist")
        exit()

    import time

    t0 = time.process_time()

    type = type.lower()
    output_path = getcwd() if not output else join(getcwd(), output)
    if type == 'zip':
        if multi:
            click.echo(
                "default zip currently doesnt support multiple folders/files zipping"
            )
            exit()
        default_zip(output_path, zip_name, folder_name)
    elif type == '7z':
        _7zip(output_path, zip_name, folder_name, multi)
    elif type == 'tar':
        tar_zip(output_path, zip_name, folder_name, multi)
    else:
        click.echo("unknown zip type")
        exit()
    t1 = time.process_time() - t0

    extension = {"tar": ".tar.gz", "zip": ".zip", "7z": ".7z"}
    click.echo(
        Fore.GREEN
        + "folder/file(s) succesfully zipped at "
        + join(getcwd(), zip_name + extension[type])
        if output == '.'
        else "folder/file(s) succesfully zipped at "
        + join(output_path, zip_name + extension[type])
    )
    click.echo("finished at : " + str(t1 - t0))


@click.argument("zip_file", metavar="<zip_name>")
@click.option('--output', '-O', help="output directory", metavar="<dir>")
@pyziper.command()
def unzip(zip_file, output):
    """unzip a folder"""
    import time

    t0 = time.process_time()
    output_path = getcwd() if not output else join(getcwd(), output)
    zip_file_path = join(getcwd(), zip_file)
    try:
        Archive(zip_file_path).extractall(output_path)
    except FileNotFoundError as e:
        click.echo(e)
    else:
        click.echo(
            Fore.GREEN + "folder succesfully unzipped at " + getcwd()
            if output == '.'
            else "folder succesfully zipped at " + output_path
        )

    t1 = time.process_time() - t0
    print("finished at : ", t1 - t0)
