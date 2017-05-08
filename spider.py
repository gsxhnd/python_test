import requests
import os
import requests.packages.urllib3
import queue
import requests.packages.idna.idnadata

def dest_File(path,name=''):
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)
    pos = target_dir.rindex('\\')
    print(pos)
    if name =='':
        t = os.path.join(target_dir,path[pos+1])
    else:
        t = os.path.join(target_dir,name)
    return(t)
