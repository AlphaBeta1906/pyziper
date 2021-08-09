# pyzip

pyzip a simple cli tools to help you to handle archive file ,like zipping and unzipping 


## installing 
for now the only way to install is trough this repo.

```bash
git clone https://github.com/AlphaBeta1906/pyzip.git
cd path/to/pyzip
pip install -e .
```

## usage 

### zip a folder

simple usage to zip a folder:
```bash
pyzip zip folder_name zip_name
```
complete command to zip file:
```bash
pyzip zip folder_name zip_name --type zip|7z|tar --output output_dir
```

by default your folder with zipped usig zip extension and output zip file will appear in current dir.  
there are 2 types of zip songs that are supported by pyzip, namely tar.gz and 7z, you can access them using the `-T`/`--type` option,example :  
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

you also can spicify output dir by using `-O`/`--output` options.


### unziping
simple usage of unzipping
```bash
pyzip unzip zip_name.zip|7z|tar.gz --output output_dir
```


new feature will be added soon