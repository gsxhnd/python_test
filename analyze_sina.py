import requests
import chromecookies
import json
import os

class get_json_file(self):
    def save_json_file(self,filename = '',json_data):
        """
        保存json文件
        """
        file_save = open(filename,"w+",encoding='utf-8')
        fp = json.dumps(json_data)
        file_save.write(fp)
        file_save.close()

    def read_json_file(self,json_file_path):
        """
        可以选择从保存的文件中读取json
        如果保留此功能，需要完善调用时的参数
        """
        json_read = open(json_file_path,"r",encoding='utf-8')
        json_content = json.loads(json_read.read())
        json_read.close()
        return(json_content)

class analyze_web():
    def __init__(self, json_file_path = '', save_file = True,**key_url):
        """
        json_file_path 添加json的路径，如果存在会调用本地的json文件
        save_file 选择是否保存json文件，默认选择保存
        """
        if os.path.isfile(json_file_path):
            self.get_json_content = get_json_file.read_json_file(json_file_path)
        else:
            cookies = chromecookies.get_chrome_cookie(domain_name)
            response = requests.get(url, cookies=cookies)  
            html_doc = response.text.encode('gbk','ignore').decode('gbk')
            self.get_json_content = json.loads(html_doc,encoding='gbk')
            save_json = get_json_file.save_json_file(filename = json_file_path)


    def get_ablum_data(self):
        album_conut = self.get_json_content["data"]["total"]
        album_info = self.get_json_content["data"]["album_list"]
        album_data = []
        for i in range(album_conut):
            album_number = "album_" + str(i)
            album_id_get  = album_info[i]["album_id"]
            caption = album_info[i]["caption"]
            album_dict = {}
            album_dict["album_id"] = album_id_get
            album_dict["caption"] = caption
            album_dict["album_number"] = album_number
            album_data.append(album_dict)
            
        return(album_data)
    
    def get_photo_data(self):
        pass



    
if __name__ == '__main__':
    # photo_json = http://photo.weibo.com/photos/get_all?uid=1588834507&album_id=3575479750811822&count=30&page=1&type=3
    # album_url = 'http://photo.weibo.com/albums/get_all?uid=1588834507&page=1&count=20'
    # domain_name = '.weibo.com'
    album_json = 'page.json'
    a = analyze_web(json_file_path = album_json)
    count_album = a.get_ablum_data()
    print(count_album)
    