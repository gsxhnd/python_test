import requests
import chromecookies
import json
import os
from math import ceil
import requests.packages.urllib3
import queue
import requests.packages.idna.idnadata


class json_file():
    # def __init__(self,user_id):
    #     file_path = os.getcwd()
    #     self.target_name = file_path +'\\'+user_id +'\\'

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
    def __init__(self, save_file = True, **custom_value):
        """
        custom_value["domain_name"]
        custom_value["url"]
        custom_value["user_id"]
        custom_value["json_file_path"]
        custom_value["json_file_name"] 

        json_file_name 添加json的路径，如果存在会调用本地的json文，如果不添加文件路径，则不会主动读取文件
        save_file 选择是否保存json文件，默认选择保存
        """

        user_id = custom_value["user_id"]
        json_file_path = custom_value["json_file_path"] 
        json_file_name = custom_value["json_file_name"]
        json_full_name = json_file_path + "\\" + str(user_id) + "\\" + json_file_name
        if os.path.isdir(json_file_path + "\\" + str(user_id)):
            pass
        else:
            os.mkdir(json_file_path + "\\" + str(user_id) )

        if os.path.isfile(json_full_name):
            pass
        else:
            domain_name = custom_value["domain_name"]
            url = custom_value["url"]
            cookies = chromecookies.get_chrome_cookie(domain_name)
            response = requests.get(url, cookies=cookies)  
            self.html_doc = response.text.encode('utf-8','ignore').decode('utf-8')
            # print(self.html_doc)
            if save_file:
                save_json = json_file.save_json_file(json_full_name,self.html_doc)

class analyze_json():
    def __init__(self, json_file_name):
        self.html_doc = json_file.read_json_file(json_file_name)

    def analyze_ablum_data(self):
        album_total = self.html_doc["data"]["total"]
        album_list = self.html_doc["data"]["album_list"]
        album_data = []
        for i in range(int(album_total)):
            album_dict = {}
            album_dict["album_id"] = album_list[i]["album_id"]
            album_dict["caption"] = album_list[i]["caption"]
            album_dict["album_number"] = str(i+1)
            album_data.append(album_dict)
        return album_dict

    def analyze_photo_data(self):
        # mw690
        self.photo_total = self.html_doc["data"]["total"]
        photo_list = self.html_doc["data"]["photo_list"]
        photo_data = []
        for i in range(len(photo_list)):
            photo_dict = {}
            photo_dict["caption"] = photo_list[i]["caption"]
            photo_dict["pic_host"] = photo_list[i]["pic_host"]
            photo_dict["pic_name"] = photo_list[i]["pic_name"]
            photo_dict["timestamp"] = photo_list[i]["timestamp"]
            photo_data.append(photo_dict)
        return photo_data

    def check_page(self):
        page = ceil(self.photo_total/30)
        return page
