import analyze_sina
from os import getcwd
from math import ceil

class check_url():
    def get_album_json(user_id):
        album_url = 'http://photo.weibo.com/albums/get_all?uid=' + str(user_id)
        custom_value = {}
        custom_value["domain_name"] = ".weibo.com"
        custom_value["url"] = album_url
        custom_value["user_id"] = user_id
        custom_value["json_file_path"]  = getcwd()
        custom_value["json_file_name"] = str(user_id)+'_album_data.json'
        json_full_name = custom_value["json_file_path"] + "\\" + str(user_id) + "\\" + custom_value["json_file_name"]
        get_json = analyze_sina.analyze_web(save_file = True,**custom_value)
        get_album_data = analyze_sina.analyze_json(json_full_name).analyze_ablum_data()
        return(get_album_data)
        

    def get_photo_json(user_id,album_id,caption,album_number):
        page_number = 1
        photo_url = "http://photo.weibo.com/photos/get_all?uid=" + str(user_id) +"&album_id="+ str(album_id) +"&count=30&page="+str(page_number)+"&type=" + str(album_number)
        print(photo_url)
        custom_value = {}
        custom_value["domain_name"] = ".weibo.com"
        custom_value["url"] = photo_url
        custom_value["user_id"] = user_id
        custom_value["json_file_path"]  = getcwd()
        custom_value["json_file_name"] = str(user_id)+'_'+caption+str(page_number)+'.json'
        json_full_name = custom_value["json_file_path"] + "\\" + str(user_id) + "\\" + custom_value["json_file_name"]
        get_json = analyze_sina.analyze_web(save_file = True,**custom_value)
        get_photo = analyze_sina.analyze_json(json_full_name)
        get_photo_data = get_photo.analyze_photo_data()
        get_photo_page = get_photo.check_page()
        for i in range(2,get_photo_page+1):
            page_number = i
            photo_url = "http://photo.weibo.com/photos/get_all?uid=" + str(user_id) +"&album_id="+ str(album_id) +"&count=30&page="+str(page_number)+"&type=" + str(album_number)
            custom_value["url"] = photo_url
            custom_value["json_file_name"] = str(user_id)+'_'+caption+str(page_number)+'.json'
            get_json = analyze_sina.analyze_web(save_file = True,**custom_value)
        
        return(get_photo_data)

# def check_page(self):
#         page = ceil(self.photo_total/30)
#         return(page)


if __name__ == '__main__':
    user_id = 5582985423 
    album_data = check_url.get_album_json(user_id)
    print(album_data)
    for i in range(len(album_data)):
        album_id = album_data[i]["album_id"]
        caption = album_data[i]["caption"]
        album_number = album_data[i]["album_number"]
        b = check_url.get_photo_json(user_id,album_id,caption,album_number)
        
     
    
    


    # url = 'http://photo.weibo.com/albums/get_all?uid='+ str(user_id)
    # domain_url = {"domain_name":".weibo.com","url":url}
    # get_album_json = analyze_web(json_file_name = str(user_id)+'_album_data.json',save_file=True,**domain_url)
    # album_data = get_album_json.get_ablum_data()
    # """
    # [
    # {'album_id': '3829774022749697', 'caption': '头像相册', 'album_number': '1', 'amount_of_photos': 107}, 
    # {'album_id': '3829778021232952', 'caption': '微博配图', 'album_number': '2', 'amount_of_photos': 145}, 
    # {'album_id': '3851564883265461', 'caption': '默认专辑', 'album_number': '3', 'amount_of_photos': 0}
    # ]
    # """
    # print(album_data)
    # for i in range(len(album_data)):
    #     album_id = album_data[i]["album_id"]
    #     caption = album_data[i]["caption"]
    #     album_number = album_data[i]["album_number"]
    #     photo_url = photo_url = "http://photo.weibo.com/photos/get_all?uid=" + str(user_id) +"&album_id="+ str(album_id) +"&count=30&page=1&type=" + album_number
    #     photo_url_dict = {"domain_name":".weibo.com","url":photo_url}
    #     get_photo_json = analyze_web(json_file_name = str(user_id)+'_'+caption+'.json',save_file=True,**photo_url_dict)
    #     photo_data = get_photo_json.get_photo_data()

            
        


    # url = "http://photo.weibo.com/photos/get_all?uid=1588834507&album_id=3575479750811822&count=30&page=1&type=3"
    # album_json = 'page.json'
    # a = analyze_web(json_file_name = 'photo.json',domain_name = ".weibo.com",url = photo_json)