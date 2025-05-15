import requests
import json
import time

txtScholFilePath = 'chem-hcmus-scholarship.txt'
txtFilePath = txtScholFilePath

''' -----------------WRITE PROCEDURE----------------- '''

def writeFile(filePath, nowNewest, json_re):
    fout = open(filePath, 'w', encoding="utf-8")

    # write the newest's post id for later check
    fout.write(f"{nowNewest}\r\n\r\n\r\n")

    for post in json_re:
        postUrl = f"{originUrl}/blog-post/{post['id']}/{post['blogPostSlug']}"
        fout.write(f"{post['timeToPublish']} _ [ {post['blogPostTitleVi']} ]\r\n{postUrl}\r\n\r\n")

    fout.close()


''' -----------------POP-UP PROCEDURE----------------- '''

def myPopUp(filePath):
    import os
    import subprocess
    import platform

    if platform.system() == 'Linux':
        subprocess.Popen(['xdg-open', filePath])
    elif platform.system() == 'Windows':
        os.startfile(filePath)


''' -----------------NOTIFY PROCEDURE----------------- '''

def myNotify():
    from plyer import notification
    import platform
    import os

# for lovely icon on notification
    iconPath = ''
    imgName = 'panic_bocchi'
    cwd = os.getcwd()

    if "com.termux" in os.environ.get("PREFIX", ""):
        os.system('termux-notification --title "CHEM.HCMUS Scraper" --content "New post on chem.hcmus!"')

    else:
        if platform.system() == 'Linux':
            iconPath = cwd + '/' + imgName + '.png'
        elif platform.system() == 'Windows':
            iconPath = cwd + '/' + imgName + '.ico'

        # spam 3 notifications
        for _ in range(3):
            notification.notify(
                title = 'ATTENTION !!!',
                message = 'New post on chem.hcmus',
                app_name = 'Your Scraper',
                app_icon = str(iconPath),
                timeout = 60
        )


while True:
    ''' -----------------MAIN-----------------  '''


    ''' -----------------THONG TIN CHUNG    '''

    # Call API to get target JSON
    originUrl = "https://chemistry.hcmus.edu.vn"
    EndpointUrl = "https://chemistry.hcmus.edu.vn/api/blog-posts?categoryId.equals=1851&blogPostStatus.equals=ENABLED&timeToPublish.lessThan=2025-05-14T17:36:45.826Z&size=20&sort=timeToPublish,DESC"

    headers = {
        "User-Agent": "Mozilla/5.0 Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
    }

    response = requests.get(EndpointUrl, headers=headers)
    
    # Get needed data
    json_re = response.json()

    # check if there is new post, if so, notice
        # read file
    fin = open(txtFilePath, 'r', encoding="utf-8")
    newest = fin.readline().strip()

    nowNewest = json_re[0]['id']
        # if the file is empty
    if newest == '' or int(newest) != nowNewest:
        print('Have to update chem-scholarship!')
        writeFile(txtFilePath, nowNewest, json_re)
    #   notification on corner
        myNotify()
    #   aggressively pop-up the storage .txt file
    #   myPopUp(txtFilePath)
#    else:
#        print("Already up to date!")
