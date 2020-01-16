from bs4 import BeautifulSoup
import requests
import os

class SexIMG:
    def __init__(self):
        pass
    def Get_Artitles_URL(self,uri):
        
        res = requests.get(uri+"/f/sex").text
        soup = BeautifulSoup(res,"lxml")
        mains = soup.find("main",class_="ForumListPage_content_3Z-L9Q")
        
        urls = [uri + url.get("href") for url in mains.find_all("a",class_="PostEntry_root_V6g0rd")]
        titles = [title.find("h3").text.strip("") for title in mains.find_all("a",class_='PostEntry_root_V6g0rd')]

        del titles[0]
        del titles[0]
        del urls[0]
        del urls[0]
    
        return titles , urls

    def Scrap_Images(self,titles,urls):
        
        for title, url in zip(titles,urls):
            
            res = requests.get(url).text
            soup = BeautifulSoup(res,'lxml')
            #print(title)
            """
            try:
                title = title.split(" ")[1]
            except:
                title = title.split("#")[0]
            """
            title = title.strip("#")

           
            pannel = soup.find("div",class_="Post_content_NKEl9d")
            try:
                images = [img.get("src") for img in pannel.find_all("img")]
            except :
                print("No images found")
                continue
            #print(images)
            if images == []:
                continue

            if os.path.exists(title):
                print("folder is already created")
                continue
            else:
                print("Creating folder: ",title)
                os.mkdir(title)
            
            for image in images:
                filename = image.split("/")[-1]
                r = requests.get(image,allow_redirects=True)
                open(title+"/"+filename,"wb").write(r.content)



    
