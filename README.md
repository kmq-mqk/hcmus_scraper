# HCMUS SCRAPER

Là SV của VNU-HCMUS, mình hay bỏ lỡ các sự kiện vì số lượng người tham gia giới hạn và vì lười kiểm tra thông tin. Vậy nên mình tạo ra scrapers để hỗ  trợ mình ^.^

## Giới thiệu chung

Scrapers cào thông tin từ web và tổng hợp vắn tắt các bài viết trên web đối tượng, phản ứng khi có bài viết mới so với phần tương ứng trong file .txt
- Notify: hiện thông báo trên góc nếu có cập nhật file .txt.
- Pop-up: mở file .txt bằng ứng dụng mặc định (vì phiền nên đã bị comment lại).

Ở đây, mình nhắm vào 2 web: hcmus.edu.vn và fit.hcmus.edu.vn

### hcmus_scraper.py

- Thông tin dành cho sinh viên (phản ứng nếu có bài viết mới so với phần này của file hcmus.txt)
- Bài viết mới

### fit-hcmus_scraper.py

- Thông tin chung (phản ứng nếu có bài viết mới so với file fit-hcmus.txt)
- Hội thảo - Hội nghị (phản ứng nếu có bài viết mới so với file fit-hcmus-seminar.txt)

## Yêu cầu trước khi sử dụng

Đã cài các thư viện python sau:
- requests
- bs4 (nếu muốn chạy hcmus_scraper.py)
- plyer

### Cài đặt các thư viện cần sử dụng
```bash
pip install -r requirements.txt
```

## Tải về

```bash
git clone https://github.com/kmq-mqk/hcmus_scraper.git
```
```bash
cd hcmus_scraper
```

hoặc tải file .zip của repository này

## Chạy scrapers
Chạy các dòng lệnh tương ứng dưới đây trên terminal / shell

### Với Windows
```
start python fit-hcmus_scraper.py
```

```
start python hcmus_scraper.py
```

### Với Linux
```bash 
python fit-hcmus_scraper.py
```
 
```bash 
python hcmus_scraper.py
```

## LƯU Ý

- Các chương trình ở đây chỉ cào 1 LẦN duy nhất cho mỗi phần thông tin mục tiêu vì mình muốn máy của mình tự động chạy scrapers (mình không đăng lên) sau một khoảng thời gian định trước (không muốn chạy ở background vì nặng máy).
- Nếu bạn không muốn hay không biết cách để máy tự động chạy scrapers, bạn có thể đưa scrapers chạy ở background bằng cách chỉnh sửa source một chút.
    + Cho phần "--MAIN--" lặp vô hạn lần
    + Sử dụng time.sleep() để **giãn thời gian giữa các lần cào web**, theo mình thì chỉ nên để 30 phút/ 1 lần cào vì nếu spam qúa nhiều request trong thời gian ngắn có thể dẫn đến hậu quả không lường trước

## Về các file .txt

- Nên giữ nguyên trạng thái các file .txt và sử dụng. Tránh chỉnh tên các file .txt (nếu đã chỉnh thì phải sửa lại để dẫn source đến file .txt tương ứng), nếu không chương trình sẽ bị lỗi.

### Bố cục

- Dòng đầu: thông tin liên quan đến bài viết mới nhất để chương trình kiểm tra file .txt đã cập nhật bài viết mới chưa.
- Phần còn lại: Các thông tin sơ bộ về bài viết: thời gian, tiêu đề, link dẫn tới bài viết.

## UPDATE 06/05/2025
- Chương trình phiên bản này sẽ chạy trong background và cào thông tin trên web đối tượng mỗi 15 phút, người dùng có thể dễ dàng điều chỉnh thời gian nghỉ giữa các đợt cào bằng cách thay đổi giá trị cho time.sleep() ở cuối chương trình.
- Sử dụng thêm thư viện 'time' của python.

## UPDATE 07/05/2025 - CHẠY SCRAPERS TRÊN ANDROID
- Vì Android không dùng được plyer trong việc thông báo lên hệ thống. Vậy nên, để chạy scrapers trên Android cần phải setup một số thứ (đây là những gì mình đã làm để scrapers chạy trên điện thoại của mình, trải nghiệm chủ quan, nếu có sai sót xin mọi người thông cảm)
    - Cài đặt F-Droid
    - Bên trong F-Droid, tìm và cài đặt Termux và Termux:API
    - Mở Termux:API, Disable 2 mục đầu tiên, mục cuối bỏ qua
    - Mở Termux, gõ dòng lệnh ```termux-setup-storage``` sau đó cho phép Termux truy cập vào các thư mục và thông báo (để Termux:API có thể thông báo trên điện thoại của bạn?)
    - Ở trong Termux, sử dụng shell commands như trên máy tính để cài đặt các thư viện python cần dùng, git clone để clone repo này, truy cập vào thư mục chứa scrapers (dùng lệnh ```cd```) và chạy chúng

