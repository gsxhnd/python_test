import requests
import chromecookies
import json

#http://photo.weibo.com/albums/get_all?uid=1588834507&page=1&count=20
#http://photo.weibo.com/photos/get_all?uid=1588834507&album_id=3575479750811822&count=30&page=1&type=3


domain_name = '.weibo.com'
cookies = chromecookies.get_chrome_cookie(domain_name)

def get_json(url):
    response = requests.get(url, cookies=cookies)  
    html_doc = response.text.encode('gbk','ignore').decode('gbk')
    #加载成dict
    json_data = json.loads(html_doc,encoding='gbk')
    """
    转成str，保存
    可以直接return dict，无需另存为，可以选择删除下面代码
    暂时保留
    """
    file_save = open("./page.json","w+",encoding='utf-8')
    fp = json.dumps(json_data)
    file_save.write(fp)
    file_save.close()
    # return(json_data)

def analyze_json(json_1):
    json_file = open(json_1,"r",encoding='utf-8').read()
    # json_dic = eval(json_file)
    fp = open(json_1,'r',encoding='utf-8')
    json_data = json.loads(fp.read())
    return(json_data["data"])

if __name__ == '__main__':
    # url = 'http://photo.weibo.com/albums/get_all?uid=1588834507&page=1&count=20'
    # a = get_json(url)
    json_file = 'page.json'
    a = analyze_json(json_file)
    print(a)
    