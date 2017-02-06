import requests
# import chromecookies
import os


#http://cn.python-requests.org/zh_CN/latest/user/quickstart.html#id2
#http://blog.csdn.net/jueblog/article/details/50442233

user_number = '1588834507'
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
    image = response.contant
    image_path = dest_File(image_url,name='')
    try:
        
    except expression as identifier:
        


a = dest_File(target_dir)



