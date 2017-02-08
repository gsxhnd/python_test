import requests
import chromecookies
import os,re
import json


#http://cn.python-requests.org/zh_CN/latest/user/quickstart.html#id2
#http://blog.csdn.net/jueblog/article/details/50442233

user_number = '2419493220'
target_dir = 'F:\code_test\python\spider\WeiboAnalbum\\'+ user_number

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
    response = requests.get(image_url,stream=True)
    image = response.content
    image_path = dest_File(image_url,name='')
    try:
        with open(image_path,"wb") as jpg:
            jpg.write(image)
            print('save picture is completed ' + image_url)
            return
    except IOError:
        print("shipai" + image_url)
        return
        

# if __name__ == '__main__':
    