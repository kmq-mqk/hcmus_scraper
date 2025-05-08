import requests
import json
import time

txtNormFilePath = 'fit-hcmus.txt'
txtSemFilePath = 'fit-hcmus-seminar.txt'
txtFilePath = txtNormFilePath

''' -----------------WRITE PROCEDURE----------------- '''

def writeFile(filePath, nowNewest, json_re):
    fout = open(filePath, 'w')

    # write the newest's post id for later check
    fout.write(f"{nowNewest}\r\n\r\n\r\n")

    for post in json_re["Results"]["Posts"]:
        PostUrl = originUrl + post['PostDetailsUrl']
        fout.write(f"{post['LastUpdate']} _ [ {post['PostTitle']} ]\r\n{PostUrl}\r\n\r\n")

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
        os.system('termux-notification --title "FIT@HCMUS Scraper" --content "New post on fit@hcmus!"')

    else:
        if platform.system() == 'Linux':
            iconPath = cwd + '/' + imgName + '.png'
        elif platform.system() == 'Windows':
            iconPath = cwd + '/' + imgName + '.ico'

        # spam 3 notifications
        for _ in range(3):
            notification.notify(
                title = 'ATTENTION !!!',
                message = 'New post on fit@hcmus',
                app_name = 'Your Scraper',
                app_icon = str(iconPath),
                timeout = 60
        )


while True:
    ''' -----------------MAIN-----------------  '''


    ''' -----------------THONG TIN CHUNG    '''

    # Call API to get target JSON
    originUrl = "https://www.fit.hcmus.edu.vn/"
    endPointUrl = "https://www.fit.hcmus.edu.vn/vn/Default.aspx?tabid=57"
    boundary = "----"

    headers = {
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        "Origin": "https://www.fit.hcmus.edu.vn",
        "Referer": "https://www.fit.hcmus.edu.vn/vn/Default.aspx?tabid=57",
        "User-Agent": "Mozilla/5.0 Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
        "X-OFFICIAL-REQUEST": "TRUE",
    }

    payload = (
        f"--{boundary}\r\n"
        'Content-Disposition: form-data; name="action"\r\n\r\n'
        "getPosts\r\n"
        f"--{boundary}\r\n"
        'Content-Disposition: form-data; name="data"\r\n\r\n'
        '{"CategoryId":1,"PageSize":20,"PageIndex":1,"Keyword":""}\r\n'
        f"--{boundary}--\r\n"
    )

    response = requests.post(endPointUrl, headers=headers, data=payload.encode())
    json_re = response.json()

    # check if there is new post, if so, notice
        # read file
    fin = open(txtFilePath, 'r')
    newest = fin.readline().strip()

    nowNewest = (json_re["Results"]["Posts"][0])["PostID"]
        # if the file is empty
    if newest == '' or int(newest) != nowNewest:
        print("Have to update fit-general!")
        writeFile(txtFilePath, nowNewest, json_re)
    #   notification on corner
        myNotify()
    #   aggressively pop-up the storage .txt file
    #   myPopUp(txtFilePath)
#    else:
#        print("Already up to date!")



    ''' -----------------HOI THAO _ HOI NGHI    '''

    payload = (
        f"--{boundary}\r\n"
        'Content-Disposition: form-data; name="action"\r\n\r\n'
        "getPosts\r\n"
        f"--{boundary}\r\n"
        'Content-Disposition: form-data; name="data"\r\n\r\n'
        '{"CategoryId":20,"PageSize":20,"PageIndex":1,"Keyword":""}\r\n'
        f"--{boundary}--\r\n"
    )

    response = requests.post(endPointUrl, headers=headers, data=payload.encode())
    json_re = response.json()

    # check if there is new post, if so, notice
    txtFilePath = txtSemFilePath
        # read file
    fin = open(txtFilePath, 'r')
    newest = fin.readline().strip()

    nowNewest = (json_re["Results"]["Posts"][0])["PostID"]
        # if the file is empty
    if newest == '' or int(newest) != nowNewest:
        print("Have to update fit-seminar!")
        writeFile(txtFilePath, nowNewest, json_re)
    #   notification on corner
        myNotify()
    #   aggressively pop-up the storage .txt file
    #   myPopUp(txtFilePath)
#    else:
#        print("Already up to date!")

    # reset variables
    txtFilePath = txtNormFilePath

    fin.close()

    time.sleep(900)
