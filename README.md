# 113-1 Database

**Name:** 呂沛修  
**Lecturer:** 蔡芸琤教授  
**Department and Grade:** 科技系三年級  

---

## Final Project

---

## Homework

---

## Notes
- [1. Week 1: Course Introduction (0902-0908)](#1-week-1-course-introduction-0902-0908)  
- [2. Week 2: Install MySQL + Flask (0909-0915)](#2-week-2-install-mysql--flask-0909-0915)  

### 1. Week 1: Course Introduction(0902-0908)  

### 2. Week 2: Install MySQL + Flask (0909-0915) 

**Create Flask environment:**  
建立簡單的 Flask "Hello World" 專案。

---

我使用 **Visual Studio Code** 作為我的開發工具。

1. 首先，按照自己喜愛的名稱創建一個資料夾。  
2. 接著，打開終端機輸入以下指令來安裝虛擬環境工具：  
   ```bash
   pip install virtualenv
![image](https://github.com/user-attachments/assets/3c7f5b42-5126-43d7-b025-cf668ffbb8f9)  
  
  
![image](https://github.com/user-attachments/assets/607d42dd-7d62-4b7b-87c3-91ec44e7e43f)  

3. 利用 virtualenv 在當前目錄下建立名為 env 的虛擬環境。
   ```bash
   virtualenv env
4. 在 windows 環境下，輸入以下指令已啟動虛擬環境：
   ```bash
   .\env\Scripts\Activate
   ```

   在linux環境下，則是在終端機輸入以下指令啟動虛擬環境  
   ```bash
   source env/bin/activate
   ```
5. 接著在虛擬環境下安裝 Flask-SQLAlchemy
   ```bash
   pip install flask Flask-SQLAlchemy
   ```
6. 在最原始創建的資料夾底下創建一個.py檔，用來測試 "Hello World"，並輸入以下代碼：
    ```bash
   from flask import Flask #導入flask套件

   app = Flask(__name__)
   
   @app.route('/')
   
   def index():
       return "Hello world!"
   
   if __name__ == "__main__":
       app.run(debug=True)
   ```
7. 在終端機輸入 python 檔名.py 執行檔案。此時，終端機會出現一個網址 (ex.  http://127.0.0.1:5000)並顯示一行文字：Running on...(網址)。點擊後即可進入利用 Flask 架好的網站。  
   ![image](https://github.com/user-attachments/assets/f4eeb081-89ac-4f92-a1fa-655491fd2f3b)


   ![image](https://github.com/user-attachments/assets/34338605-001b-4dfe-8f37-72ce67ee9f62)


**Flask + MySQL**  
如何將 Flask 與 SQL 連結？  
[可參考代碼：Task Master](https://github.com/PeiHsiuLu/Database/tree/master)  
[參考教學影片：Learn Flask for Python - Full Tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA)  

#### 1. 安裝 Flask 和 SQLAlchemy

首先，確保你已經安裝了 Flask 和 SQLAlchemy。可以使用以下命令安裝：

```bash
pip install Flask SQLAlchemy
---



   
