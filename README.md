# 113-1 Database

**Name:** 呂沛修  
**Lecturer:** 蔡芸琤教授  
**Department and Grade:** 科技系三年級  

---

## Homework

---

## Notes

### 1. Week 1: Course Introduction  

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
