import requests
import chromecookies
import os


domain_name = '.weibo.com'
cookie = chromecookies.get_chrome_cookie(domain_name)

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

def save_image(image_url,name=''):
    response

print(cookie)