import analyze_sina

class check_url():
    def __init__(self,user_id):
        self.album_url = 'http://photo.weibo.com/albums/get_all?uid=' + str(user_id)
        photo_url = photo_url = "http://photo.weibo.com/photos/get_all?uid=" + str(user_id) +"&album_id="+ str(album_id) +"&count=30&page="+page_number+"&type=" + str(album_number)

    def get_album_json(self):
        pass

    def get_photo_json(parameter_list):
        pass


if __name__ == '__main__':
    user_id = 5582985423

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