import time
import urllib.request as urllib
import mysql.connector

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/csardana/Desktop/ENG 4K/chromedriver")

driver.get("https://www.sunglasshut.com/ca-en/womens-sunglasses?currentPage=3")
time.sleep(10)
href_img = driver.find_elements_by_tag_name("source")
brands = driver.find_elements_by_tag_name("span")

p=0
j=[]
k=[]
t=[]
c=[]

# for i in href_img:
#     # print(i.get_attribute("src"))
#     if("assets.sunglasshut.com" in str(i.get_attribute("srcset"))):
#         # with open('mens_'+str(p)+'.png', 'wb') as file:
#         #     file.write(i.get_attribute("srcset").screenshot_as_png)
#         # urllib.urlretrieve(i.get_attribute("srcset"),'mens_'+str(p)+'.png' )
#         # with open('mens_'+str(p)+'.png', 'wb') as file:
#         #     # identify image to be captured
#         #
#         #     # write file
#         #     file.write((i.get_attribute("srcset")).screenshot_as_png)
#
#         # urllib.urlretrieve((i.get_attribute("srcset")),'mens_'+str(p)+'.png')
#
#
#
#
#         reponse = requests.get(i.get_attribute("srcset"))
#         if reponse.status_code == 200:
#             with open('womens_'+str(p)+'.png', "wb") as file:
#                 file.write(reponse.content)
#         print(str(i.get_attribute("srcset")))
#         p=p+1


for f in brands:
    # print(i.get_attribute("src"))
    if("sgh-tile__brand" in str(f.get_attribute("class"))):
        print(str(f.text))
        j.append(str(f.text))
    if(("sgh-tile__model-name" in str(f.get_attribute("class"))) and ("pt-2" in str(f.get_attribute("class")))):
        print(str(f.text))
        c.append(str(f.text))
    if("sgh-tile__model-name text-tiny text-emperor leading-6 pt-0" in str(f.get_attribute("class"))):
        print(str(f.text))
        k.append(str(f.text))
    if("sgh-tile__price" in str(f.get_attribute("class"))):
        print(str(f.text))
        t.append(str(f.text))




print(len(j))
print(len(k))
print(len(t))
print(len(c))

#
# #
mydb = mysql.connector.connect(
  host="classic-optics.cgm5gah7vb4m.us-east-1.rds.amazonaws.com",
  user="root",
  password="Cs$$2022",
  database="EECS4413",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()
for a in range(len(j)):
    sql = "INSERT INTO product (prodid, catid , company, deleted ,expirydate,mfgdate, pic ,pname ,price ,qty,salt,category_catid,review) VALUES (%s, %s , %s , %s ,%s ,%s,%s, %s , %s , %s ,%s ,%s,%s)"
    val = (a + 54, 2,j[a],0,'2022-03-01','2022-03-01','/pics/'+'womens_'+str(a)+'.png',j[a]+" | "+c[a],t[a][1:],25,k[a],2,"")
    mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
