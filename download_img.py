from requests import get as re_get
from analyze_sina import analyze_json
from os import getcwd

def download_img(json_name,userid,album_name):
    file_path = getcwd()
    full_filename = file_path + "\\"+ str(userid) +"\\"+ json_name
    get_data = analyze_json(full_filename).analyze_photo_data()
    for i in range(len(get_data)):
        timestamp = get_data[i]["timestamp"]
        caption = get_data[i]["caption"]
        pic_host = get_data[i]["pic_host"]
        pic_name = get_data[i]["pic_name"]
        # print(timestamp,caption,pic_host,pic_name)
        img_url = pic_host + "/large/" + pic_name
        img = re_get(img_url).content
        img_path = file_path + "\\"+ str(userid) +"\\"+album_name+"\\"
        img_name = str(timestamp)+"_"+pic_name
        with open(img_path+img_name,'wb') as f:
            print("downloading picture:"+ pic_name)
            f.write(img)

    # img = re_get(url).content
    # with open(filename,'wb') as f:
    #     f.writ(img)
