import requests
import chromecookies
import json

#http://photo.weibo.com/albums/get_all?uid=1588834507&page=1&count=20
#http://photo.weibo.com/photos/get_all?uid=1588834507&album_id=3575479750811822&count=30&page=1&type=3


domain_name = '.weibo.com'



        

class analyze_json():
    def __init__(self,url,domain_name):
        cookies = chromecookies.get_chrome_cookie(domain_name)
        response = requests.get(url, cookies=cookies)  
        html_doc = response.text.encode('gbk','ignore').decode('gbk')
        self.get_json_content = json.loads(html_doc,encoding='gbk')

    def save_json_file(self):
        
        """
        转成str，保存(可以保留，可以删除)
        可以直接return dict，无需另存为文件
        也可以选择删除下面代码。暂时保留
        """
        file_save = open("page.json","w+",encoding='utf-8')
        fp = json.dumps(self.get_jsons_content)
        file_save.write(fp)
        file_save.close()

    def read_json_file(self):
        """
        可以选择从保存的文件中读取json
        如果保留此功能，需要完善调用时的参数
        """
        json_file = open("page.json","r",encoding='utf-8').read()
        fp = json.loads(fp.read())
        return(fp)

    def get_json_data(self):
        album_conut = self.get_json_content["data"]["total"]

if __name__ == '__main__':
    # url = 'http://photo.weibo.com/albums/get_all?uid=1588834507&page=1&count=20'
    # a = get_json(url)
    json_file = 'page.json'
    a = analyze_json(json_file)
    print(a)
    