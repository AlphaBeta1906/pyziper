import click
from os import path, walk, getcwd
from os.path import getsize, join, exists
from pathlib import Path

import tarfile
import py7zr
from zipfile import ZipFile, ZIP_DEFLATED


@click.group()
def pyzip():
    """pyzip a simple cli tools to help you to handle archive file
    ,like zipping or unzipping

    example zip a folder :\n
    pyzip zip <folder_name> <zip_file_name> -T [zip|7z|tar] -O <output_dir>

    example unzip a archive : \n
    pyzip unzip <zip_file_name>.zip|7z|tar.gz -O <output_dir>

    version : 0.1
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


def _7zip(output_path, zip_name, folder_name):
    with py7zr.SevenZipFile(join(output_path, zip_name) + '.7z', 'w') as _7z:
        _7z.writeall(folder_name + '/')


def tar_zip(output_path, zip_name, folder_name):
    with tarfile.open(join(output_path, zip_name) + '.tar.gz', 'w:gz') as tar:
        tar.add(folder_name, arcname=folder_name)


@click.argument("zip_name", metavar="<zip_name>")
@click.argument("folder_name", metavar="<folder_name>")
@click.option('--type', '-T', default='zip')
@click.option('--output', '-O')
@pyzip.command()
def zip(folder_name, zip_name, output, type):
    """zip a folder"""
    if not exists(join(getcwd(), folder_name)):
        click.echo(join(getcwd(), folder_name) + " not exist")
        exit()

    import time

    t0 = time.process_time()

    type = type.lower()
    output_path = getcwd() if not output else join(getcwd(), output)
    if type == 'zip':
        default_zip(output_path, zip_name, folder_name)
    elif type == '7z':
        _7zip(output_path, zip_name, folder_name)
    elif type == 'tar':
        tar_zip(output_path, zip_name, folder_name)
    else:
        click.echo("unknown zip type")
        exit()
    t1 = time.process_time() - t0
    print("finished at : ", t1 - t0)
    click.echo(
        "folder succesfully zipped at " + getcwd()
        if output == '.'
        else "folder succesfully zipped at " + join(output_path)
    )


@click.argument("zip_file")
@click.option('--output', '-O')
@pyzip.command()
def unzip(zip_file, output):
    """unzip a folder"""
    import time

    output_path = getcwd() if not output else join(getcwd(), output)
    try:
        t0 = time.process_time()
        if zip_file.endswith('.zip'):
            with ZipFile(join(getcwd(), zip_file), 'r') as _unzip:
                _unzip.extractall(output_path)
        elif zip_file.endswith('.7z'):
            with py7zr.SevenZipFile(join(getcwd(), zip_file), 'r') as _7z:
                _7z.extractall(output_path)
        elif (
            zip_file.endswith('.tar.gz')
            or zip_file.endswith('.tar')
            or zip_file.endswith('.gz')
        ):
            with tarfile.open(join(getcwd(), zip_file), 'r') as tar:
                tar.extractall(output_path)
        else:
            click.echo("unknown zip type")
            exit()
    except FileNotFoundError as e:
        click.echo(e)
    else:
        click.echo(
            "folder succesfully unzipped at " + getcwd()
            if output == '.'
            else "folder succesfully zipped at " + output_path
        )

        t1 = time.process_time() - t0
        print("finished at : ", t1 - t0)
