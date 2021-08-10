# pyzip

pyzip a simple cli tools to help you to handle archive file ,like zipping and unzipping 


## installing 
for now the only way to install is trough this repo.

```bash
git clone https://github.com/AlphaBeta1906/pyzip.git
cd pyzip
pip install -e . # install it globally so you can use it everywhere in  your machine
```

## usage 

### zipping/archiving

simple usage to zip a folder:
```bash
pyzip zip folder_name zip_name
```

complete command to zip file(s)/folder(s):
```bash
pyzip zip folder_name zip_name --type zip|7z|tar --multi  --output output_dir
```

by default your folder is archived using standard zip method(`.zip`) and output zip file will appear in current dir.  
there are 2 other types of archive method that are supported by pyzip, that is tar.gz and 7z, you can access them using the `-T`/`--type` option,example :  
```bash
# 7z
pyzip zip folder_name zip_name -T 7z

#tar.gz
pyzip zip folder_name zip_name -T tar

#zip/default

pyzip zip folder_name zip_name -T zip

# or simply
pyzip zip folder_name zip_name
```

you also can spicify output dir by using `-O`/`--output` options,example: 
```bash 
pyzip zip folder_name zip_name -T  tar -O 
```

in version 0.2,`--multi`/`-m` was added,and used to add multiple folders or/and files separated by coma into archive,example:
```bash
pyzip zip folder1,folder2,file1,file2.... zip_file -T 7z|tar --multi --output output/dir/
```
*Note : default zip(`.zip`) currently doesnt have support to archive multiple folders or files. it only worked for 7z and tar.gz archive*


### unziping/extracting
simple usage of unzipping
```bash
pyzip unzip zip_name.zip|7z|tar.gz --output output_dir
```

#### option in pyzip(current)
| option      | function |
| ----------- | ----------- |
| `--type`/`-T`   | defining archive type,default is `.zip`  |
| `--multi`/`-M`  | if it enabled, it will allow you to archive multiple files and/or folders only for `7z` and `tar` type |
| `--output`/`-O` | defining output directory for your archived file,default is your current working directory |


new feature will be added soon