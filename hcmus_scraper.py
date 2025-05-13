import requests
from bs4 import BeautifulSoup
import time

txtFilePath = 'hcmus.txt'

''' -----------------WRITE PROCEDURE----------------- '''

def writeFile(targetBlock):
    # write file
    fout = open(txtFilePath, 'w', encoding="utf-8")
  
    # to check if there is new post later
    fout.write(f"{targetBlock.article['id']}\r\n\r\n\r\n")
  
    # get info relate to students
    fout.write(f"{border} THONG TIN SV {border}\r\n")
  
    articles = targetBlock.find_all("article")
  
    for article in articles:
      content = article.find("div", class_="cmsmasters_archive_item_cont_wrap")
      data = content.header.h2.a
      date = content.footer.span.abbr
  
      fout.write(f"{date.string} _ [ {data.string.get_text(strip=True)} ]\r\n{data['href']}\r\n\r\n")
  
    # get newest posts
    fout.write(f"\r\n{border} THONG TIN MOI NHAT {border}\r\n")
  
    targetBlock = soup.find(string="Bài viết mới")
  
    targetBlock = targetBlock.parent.parent
    targetBlock = targetBlock.ul
  
    data = targetBlock.find_all("li")
  
    for post in data:
      fout.write(f"{post.span.string} _ [ {post.a.string} ]\r\n{post.a['href']}\r\n\r\n")

    fout.close()


''' -----------------POP-UP PROCEDURE----------------- '''

def myPopUp():
    import os
    import subprocess
    import platform

    if platform.system() == 'Linux':
        subprocess.Popen(['xdg-open', txtFilePath])
    elif platform.system() == 'Windows':
        os.startfile(txtFilePath)


''' -----------------NOTIFY PROCEDURE----------------- '''

def myNotify():
    from plyer import notification
    import platform
    import os

# for lovely icon on notification                         iconPath = ''
    imgName = 'panic_bocchi'
    cwd = os.getcwd()

    if "com.termux" in os.environ.get("PREFIX", ""):
        os.system('termux-notification --title "HCMUS Scraper" --content "New post on hcmus!"')
    else:
        if platform.system() == 'Linux':
            iconPath = cwd + '/' + imgName + '.png' 
        elif platform.system() == 'Windows':
            iconPath = cwd + '/' + imgName + '.ico'

        # spam 3 notifications
        for _ in range(3):
            notification.notify(
                title = 'ATTENTION !!!',
                message = 'New post on hcmus',
                app_name = 'Your Scraper',
                app_icon = str(iconPath),
                timeout = 60
        )

while True:
    ''' -----------------MAIN-----------------  '''
  
    targetUrl = "https://hcmus.edu.vn/category/dao-tao/dai-hoc/thong-tin-danh-cho-sinh-vien/"
  
    headers = {
        "User-Agent": "Mozilla/5.0 Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
    }
  
    response = requests.get(targetUrl, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
  
    number = 17
    ch = "*"
    border = ch * number
  
    targetBlock = soup.find("div", class_="cmsmasters_archive")
  
    # read file
    fin = open(txtFilePath, 'r', encoding="utf-8")
    newest = fin.readline().strip()
  
    nowNewest = targetBlock.article['id']
    # if the file is empty
    if newest != nowNewest:
        print("Have to update hcmus!")
        writeFile(targetBlock)
       
    #   notification on corner
        myNotify()

    #   aggressively pop-up the storage .txt file
#        myPopUp()
#    else:
#        print("Already up to date!")

    fin.close()

    time.sleep(900)

