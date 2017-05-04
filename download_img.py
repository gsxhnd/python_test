from requests import get as re_get

def download_img(data):
    url = data["url"]
    filename = data["filename"]
    img = re_get(url).content
    with open(filename,'wb') as f:
        f.writ(img)
