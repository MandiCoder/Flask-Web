from os import mkdir
from requests import get
from os.path import join, basename, exists

def download_file(url:str):
    file = get(url).content
    file_root = join('downloads', basename(url))
    
    if not exists('downloads'):
        mkdir('downloads')
    
    with open(file_root, 'wb') as f:
        f.write(file)
        
    return file_root