import requests
import chromecookies

#http://photo.weibo.com/albums/get_all?uid=1588834507&page=1&count=20
#http://photo.weibo.com/photos/get_all?uid=1588834507&album_id=3575479750811822&count=30&page=1&type=3


domain_name = '.weibo.com'
cookies = chromecookies.get_chrome_cookie(domain_name)
album_url = 
response = requests.get(album_url, cookies=cookies)  
html_doc = response.text.encode('gbk','ignore').decode('gbk')  

js = json.loads(html_doc,encoding='gbk')
print(js)