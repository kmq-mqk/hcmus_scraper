
import requests
from bs4 import BeautifulSoup

# write procedure
def writeFile(targetBlock):
  # write file
  fout = open('hcmus.txt', 'w')

  # to check if there is new post later
  fout.write(f"{targetBlock.article['id']}\r\n\r\n\r\n")
  # get info relate to students

  fout.write(f"{border} THONG TIN SV {border}\r\n")

  # targetBlock = soup.find("div", class_="cmsmasters_archive")



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

# main
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
fin = open('hcmus.txt', 'r')
newest = fin.readline().strip()
# if the file is empty
if newest == '':
  writeFile(targetBlock)
else:
  nowNewest = targetBlock.article['id']

  if newest != nowNewest:
    print("Have to update!")
    writeFile(targetBlock)
  else:
    print("Already up to date!")