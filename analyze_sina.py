import requests
import chromecookies
import json
import os

#http://photo.weibo.com/albums/get_all?uid=1588834507&page=1&count=20
#http://photo.weibo.com/photos/get_all?uid=1588834507&album_id=3575479750811822&count=30&page=1&type=3


domain_name = '.weibo.com'



        

class analyze_json():
    def __init__(self, json_file_path = '', save_file = True,**key_url):
        """
        json_file_path 添加json的路径，如果存在会调用本地的json文件
        save_file 选择是否保存json文件，默认选择保存
        """
        if os.path.isfile(json_file_path):
            self.get_json_content = self.read_json_file(json_file_path)
        else:
            cookies = chromecookies.get_chrome_cookie(domain_name)
            response = requests.get(url, cookies=cookies)  
            html_doc = response.text.encode('gbk','ignore').decode('gbk')
            self.get_json_content = json.loads(html_doc,encoding='gbk')
            save_json = self.save_json_file(filename = json_file_path)

    def save_json_file(self,filename = ''):
        """
        保存json文件
        """
        file_save = open(filename,"w+",encoding='utf-8')
        fp = json.dumps(self.get_jsons_content)
        file_save.write(fp)
        file_save.close()

    def read_json_file(self,json_file):
        """
        可以选择从保存的文件中读取json
        如果保留此功能，需要完善调用时的参数
        """
        json_read = open(json_file_path,"r",encoding='utf-8').read()
        json_content = json.loads(json_read)
        return(json_content)

    def get_ablum_data(self):
        album_conut = self.get_json_content["data"]["total"]
        album_info = self.get_json_content["data"]["album_list"]


if __name__ == '__main__':
    # url = 'http://photo.weibo.com/albums/get_all?uid=1588834507&page=1&count=20'
    # a = get_json(url)
    # json_file = 'page.json'
    a = analyze_json(url,domain_name,save_file=False)
    print(a)
    