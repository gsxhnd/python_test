import get_json
import download_img


# user_id = 2419493220
user_id = int(input("userid:"))
album_data = get_json.check_url.get_album_json(user_id)
# print(album_data)
json_list = []
print(album_data)

for i in range(len(album_data)):
    album_id = album_data[i]["album_id"]
    caption = album_data[i]["caption"]
    album_number = album_data[i]["album_number"]
    b = get_json.check_url.get_photo_json(user_id,album_id,caption,album_number)
    print(b)
    json_list.append(b)
print(json_list)
for h in range(len(json_list)):
    # print(h)
    for j in range(len(json_list[h]["json_name"])):
        json_dir = json_list[h]["json_dir"]
        download = download_img.download_img(json_list[h]["json_name"][j],user_id,json_dir)
        print(download)
input("Complete!")