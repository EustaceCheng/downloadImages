import requests
import os

def DownloadImages(imageSrc,folder_path,img_name): 
    r = requests.get(imageSrc)
    os.makedirs(folder_path, exist_ok=True)

    with open(img_name, 'wb') as f:
            f.write(r.content)
            print('Download:' + img_name + '  ......')
