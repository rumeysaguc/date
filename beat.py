import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://1000kitap.com/kitap/suc-ve-ceza--221003/incelemeler'
iste =requests.get(url)
dosya = open("veri.txt","w", encoding="UTF-8")


data = iste.content
soup = BeautifulSoup(data,'lxml')

tablo = soup.find_all("div",{"class":"ana-orta"})
allicerik = soup.find_all("div",{"class": "icerik"})
#allokur = soup.find_all("a", {"class":"okur-adi"})
count = 0


for icerik in allicerik:
    print(icerik.text)
    print("\n")
    count += 1
    dosya.write(icerik.text)
    dosya.write("\n") 
    print(count)



"""
for okur in allokur:
    veri = okur.text
    df = pd.DataFrame(veri, index=[1,2,3,4,5,6,7], columns = ["isimler"])
    print(df)"""


