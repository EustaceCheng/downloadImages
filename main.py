import requests
from bs4 import BeautifulSoup
from nanoid import generate
from lib.download import DownloadImages

input_image = 'flower'
resourceHtml = requests.get(f"https://unsplash.com/s/photos/{input_image}")
imageTags = BeautifulSoup(resourceHtml.text, "html.parser").find_all('div', {'class', "zmDAx"})
folder_path = f'./images/{input_image}/'


 
for imageTag in imageTags:  
    img_name = folder_path +f"{generate(size=10)}.jpg"
    imageSrc = (imageTag.find('img')['src']).replace('&w=1000','')  
    DownloadImages(imageSrc,folder_path,img_name)
            
  


