
import requests
from bs4 import BeautifulSoup

targetUrl = "https://hcmus.edu.vn/category/dao-tao/dai-hoc/thong-tin-danh-cho-sinh-vien/"

headers = {
    "User-Agent": "Mozilla/5.0 Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
}

response = requests.get(targetUrl, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

number = 17
ch = "*"
border = ch * number

# read file
fin = open('hcmus.txt', 'r')



# write file
fout = open('hcmus.txt', 'w')

# get newest posts

fout.write(f"{border} THONG TIN MOI NHAT {border}\r\n")

targetBlock = soup.find(string="Bài viết mới")

targetBlock = targetBlock.parent.parent
targetBlock = targetBlock.ul

data = targetBlock.find_all("li")

for post in data:
  fout.write(f"{post.span.string} _ [ {post.a.string} ]\r\n{post.a['href']}\r\n\r\n")

# get info relate to students

fout.write(f"{border} THONG TIN SV {border}\r\n")

targetBlock = soup.find("div", class_="cmsmasters_archive")

fout.write(f"Newest post's id = {targetBlock.article['id']}\r\n\r\n\r\n")

articles = targetBlock.find_all("article")

for article in articles:
  content = article.find("div", class_="cmsmasters_archive_item_cont_wrap")
  data = content.header.h2.a
  date = content.footer.span.abbr

  fout.write(f"{date.string} _ [ {data.string.get_text(strip=True)} ]\r\n{data['href']}\r\n\r\n")