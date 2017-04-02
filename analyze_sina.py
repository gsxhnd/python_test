import requests
import chromecookies
import json
import os
from math import ceil

class get_json_file():
    def save_json_file(filename,json_data):
        """
        保存json文件
        """
        file_save = open(filename,"w+",encoding='utf-8')
        # fp = json.dumps(json_data)
        file_save.write(json_data)
        file_save.close()

    def read_json_file(json_file_name):
        """
        可以选择从保存的文件中读取json
        如果保留此功能，需要完善调用时的参数
        """
        json_read = open(json_file_name,"r",encoding='utf-8')
        json_content = json.loads(json_read.read())
        json_read.close()
        return(json_content)

class analyze_web():
    def __init__(self, json_file_name = '', save_file = True,**key_url):
        """
        json_file_name 添加json的路径，如果存在会调用本地的json文，如果不添加文件路径，则不会主动读取文件
        save_file 选择是否保存json文件，默认选择保存
        """
        if os.path.isfile(json_file_name):
            self.html_doc = get_json_file.read_json_file(json_file_name)
        else:
            domain_name = key_url["domain_name"]
            url = key_url["url"]
            cookies = chromecookies.get_chrome_cookie(domain_name)
            response = requests.get(url, cookies=cookies)  
            self.html_doc = response.text.encode('utf-8','ignore').decode('gbk')
            # print(response.text)
            if save_file:
                save_json = get_json_file.save_json_file(json_file_name,self.html_doc)


    def get_ablum_data(self):
        album_total = self.html_doc["data"]["total"]
        album_list = self.html_doc["data"]["album_list"]
        album_data = []
        for i in range(int(album_total)):
            album_dict = {}
            album_dict["album_id"] = album_list[i]["album_id"]
            album_dict["caption"] = album_list[i]["caption"]
            album_dict["album_number"] = str(i+1)
            album_dict["amount_of_photos"] = album_list[i]["count"]["photos"]
            album_data.append(album_dict)
        return(album_data)
    
    def get_photo_data(self):
        #mw690
        photo_total = self.html_doc["data"]["total"]
        photo_list = self.html_doc["data"]["photo_list"]
        photo_data = []
        for i in range(len(photo_list)):
            photo_dict = {}
            photo_dict["caption"] = photo_list[i]["caption"]
            photo_dict["pic_host"] = photo_list[i]["pic_host"]
            photo_dict["pic_name"] = photo_list[i]["pic_name"]
            photo_dict["timestamp"] = photo_list[i]["timestamp"]
            photo_data.append(photo_dict)
        return(photo_data)

def check_page(photo_total):
        page = ceil(photo_total/30)
        return(page)
    

if __name__ == '__main__':
    user_id = 5582985423
    url = 'http://photo.weibo.com/albums/get_all?uid='+ str(user_id)
    domain_url = {"domain_name":".weibo.com","url":url}
    get_album_json = analyze_web(json_file_name = str(user_id)+'_album_data.json',save_file=True,**domain_url)
    album_data = get_album_json.get_ablum_data()
    print(album_data)
    for i in range(len(album_data)):
        album_id = album_data[i]["album_id"]
        caption = album_data[i]["caption"]
        album_number = album_data[i]["album_number"]
        photo_url = "http://photo.weibo.com/photos/get_all?uid=" + str(user_id) +"&album_id="+ str(album_id) +"&count=30&page=1&type=" + album_number
        photo_url_dict = {"domain_name":".weibo.com","url":photo_url}
        get_photo_json = analyze_web(json_file_name = str(user_id)+'_'+caption+"_page"+str(1)+'.json',save_file=True,**photo_url_dict)
            
        


    # url = "http://photo.weibo.com/photos/get_all?uid=1588834507&album_id=3575479750811822&count=30&page=1&type=3"
    # album_json = 'page.json'
    # a = analyze_web(json_file_name = 'photo.json',domain_name = ".weibo.com",url = photo_json)