import analyze_sina
from os import getcwd,mkdir,path

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
        # print(photo_url)
        custom_value = {}
        custom_value["domain_name"] = ".weibo.com"
        custom_value["url"] = photo_url
        custom_value["user_id"] = user_id
        custom_value["json_file_path"]  = getcwd()
        custom_value["json_file_name"] = str(user_id)+'_'+caption+str(page_number)+'.json'
        if path.isdir(str(user_id) + "\\"+ caption):
            pass
        else:
            mkdir_name = mkdir(str(user_id) + "\\"+ caption)
        json_full_name = custom_value["json_file_path"] + "\\" + str(user_id) + "\\" + custom_value["json_file_name"]
        get_json = analyze_sina.analyze_web(save_file = True,**custom_value)
        get_photo = analyze_sina.analyze_json(json_full_name)
        get_photo_data = get_photo.analyze_photo_data()
        get_photo_page = get_photo.check_page()
        json_list = {}
        json_list_json_name = []
        json_list_json_name.append(custom_value["json_file_name"])
        # print(get_photo_page)
        if get_photo_page >= 2:
            for i in range(2,get_photo_page+1):
                page_number = i
                photo_url = "http://photo.weibo.com/photos/get_all?uid=" + str(user_id) +"&album_id="+ str(album_id) +"&count=30&page="+str(page_number)+"&type=" + str(album_number)
                custom_value["url"] = photo_url
                custom_value["json_file_name"] = str(user_id)+'_'+caption+str(page_number)+'.json'
                get_json = analyze_sina.analyze_web(save_file = True,**custom_value)
                
                json_list_json_name.append(custom_value["json_file_name"])
                json_list["json_name"] = json_list_json_name
                json_list["json_dir"] = caption
        else:
            json_list["json_name"] = json_list_json_name
            json_list["json_dir"] = caption
            
        return(json_list)


# if __name__ == '__main__':
 