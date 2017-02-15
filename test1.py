import requests
import chromecookies
import analyze_sina

domain_name = ".weibo.com"
url = "http://photo.weibo.com/photos/get_all?uid=1588834507&album_id=3575479750811822&count=30&page=1&type=3"
cookie = chromecookies.get_chrome_cookie(domain_name)
response = requests.get(url, cookies = cookie)  
html_doc = response.text.encode('gbk','ignore').decode('gbk')
print(html_doc)
save_json = analyze_sina.get_json_file.save_json_file("photo.json",html_doc)