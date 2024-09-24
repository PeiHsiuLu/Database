# 113-1 Database

**Name:** 呂沛修  
**Lecturer:** 蔡芸琤教授  
**Department and Grade:** 科技系三年級  

---

## Final Project

---


## Homework
- [HW1 簡易登入/註冊系統](#hw1-簡易登入註冊系統)  
  - [1. HW1 程式碼](https://github.com/PeiHsiuLu/Database/tree/main/Week3/mysql_and_flask)  
  - [2. HW1 影片](https://youtu.be/846RmjGRTiY)
  - 補充：MySQLWorkbench及時儲存原影片只錄製到已儲存的資料，後續有再補一隻短片放在影片簡介區證明資料可在SQL被及時儲存  
- [HW2]()
- [HW3]()
- [HW4]()
### HW1 簡易登入/註冊系統
這次作業主要是練習，利用 Flask 結合 MySQL 製作一個簡易的登入註冊頁面。同時，做到可以將已註冊的帳號、密碼利用 MySQL 儲存。  


  
**圖一：註冊畫面** 
![image](https://github.com/user-attachments/assets/81a79b28-c15e-4d1a-87b7-250ab72f9295)  

**圖二：登入畫面**  
![image](https://github.com/user-attachments/assets/a915d09b-ddb2-489f-932f-4f947ca8366d)  

**圖三：登入後出現的頁面**  
![image](https://github.com/user-attachments/assets/abc3cec6-baf8-44a8-8674-e50f0f0f7680)  

**圖四：登出畫面 (跳回登入畫面，並用flash提示)**  
![image](https://github.com/user-attachments/assets/5206a0c6-2a45-4139-81db-8d9722ed1d50)  
**圖五：WorkBench**  
![image](https://github.com/user-attachments/assets/ab0b6529-c723-4ef3-b487-91efb7f63e93)
- workbench存放公司員工的登入資料，id,name,password 照順序排列，密碼用哈希值亂數隨機儲存。
- 相同的信箱不可再被註冊







---

## Notes
- [1. Week 1: Course Introduction (0902-0908)](#week-1-course-introduction-0902-0908)  
- [2. Week 2: Install Flask & SQL in Flask (0909-0915)](#week-2-install-flask-and-sql-in-flask-0909-0915)
- [3. Week 3: Flask Connect to MySQL (0916-0922)](#week-3-flask-connect-to-mysql-0916-0922)
- [4. Week 4: MySQL instruction and introduction (0923-0930)](#week-4-mysql-instruction-and-introduction-0923-0930)

### Week 1: Course Introduction (0902-0908)  

### Week 2: Install Flask and SQL in Flask (0909-0915)


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


**Flask + SQL**  
如何將 Flask 與 SQL 連結？  
* [可參考代碼：Task Master](https://github.com/PeiHsiuLu/Database/tree/master)  
* [參考的教學影片：Learn Flask for Python - Full Tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA)  

#### 1. 安裝 Flask 和 SQLAlchemy

首先，確保安裝了 Flask 和 SQLAlchemy。可以使用以下命令安裝：

```bash
pip install Flask SQLAlchemy
```

#### 2. 設定 Flask 應用

需要設置 Flask 應用程序並配置 SQLAlchemy。以下是如何做：  

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///path/to/your/database.db'
db = SQLAlchemy(app)
```

app.config['SQLALCHEMY_DATABASE_URI']：這裡設定了資料庫的位置。這個例子使用的是 SQLite，可以根據需要改成其他資料庫。  

#### 3. 定義資料庫模型  

使用 SQLAlchemy 定義資料庫模型。這些模型會映射到資料庫中的表格：

```python
from datetime import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id
```
* id：每個任務的唯一標識符。  
* content：任務內容。  
* completed：標記任務是否完成的布林值。  
* date_created：任務創建日期和時間。  

#### 4. 創建資料庫和表格
創建資料庫表格，這樣 SQLAlchemy 才知道在哪裡存儲數據：  
```python
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
db.create_all()：會根據你定義的模型創建所有需要的表格。  

#### 5. 使用 SQLAlchemy 操作資料庫
  
**創建紀錄**  
  
```python
new_task = Todo(content="Learn Flask with SQLAlchemy")
db.session.add(new_task)
db.session.commit()
```

**讀取紀錄**  
  
```python
tasks = Todo.query.all()
```
**更新紀錄**  
  
```python
task = Todo.query.get(1)
task.content = "Update task content"
db.session.commit()
```
**刪除紀錄**  
  
```python
task = Todo.query.get(1)
db.session.delete(task)
db.session.commit()
```
#### 6. 範例：Task Master
以下利用我的代碼作為範例：  
```python
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# 初始化 Flask 應用程式
app = Flask(__name__)

# 設定 SQLAlchemy 資料庫 URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Paul2/Flask-introduction/test.db'
db = SQLAlchemy(app)

# 定義資料庫模型
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 任務的唯一標識符
    content = db.Column(db.String(200), nullable=False)  # 任務內容
    completed = db.Column(db.Integer, default=0)  # 任務是否完成，預設為 0（未完成）
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  # 任務創建日期，預設為當前時間

    def __repr__(self):
        return '<Task %r>' % self.id

# 首頁路由
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # 從表單獲取任務內容
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        
        try:
            # 將新任務添加到資料庫
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your task"
    else:
        # 獲取所有任務並按創建日期排序
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)
    
# 刪除任務的路由
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)  # 根據 ID 獲取任務
    
    try:
        # 從資料庫中刪除任務
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting that task."

# 更新任務的路由
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)  # 根據 ID 獲取任務
    
    if request.method == 'POST':
        # 更新任務內容
        task.content = request.form['content']
        
        try:
            # 提交更改到資料庫
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating your task"
    else:
        return render_template('update.html', task=task)

# 應用程式啟動
if __name__ == "__main__":
    # 使用應用程式上下文來創建資料庫表格
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Week 3: Flask connect to MySQL (0916-0922)  

今日做的小練習：設計登入+註冊介面  
* Flask + MySQL
* MySQL connector: 由於 MySQL 屬於第三方套件，所以必須利用 MySQL connector 串接 Flask，Flask 開發的網頁才能順利在 localhost 上運行
  依序安裝以下檔案在系統內，即可安裝MySQL connector：
  ```bash
  pip install mysql-connector
  pip install mysql-connector-python
  pip install mysql-connector-python-rf
  ```
* MySQL的預設值：PORT:3306；user:root 這些預設值是MySQL提前先幫你預設好的，不需要改動。

### Week 4 MySQL instruction and introduction (0923-0930)
  
#### SQL簡介
SQL = Structured(結構化)Query(詢問) Language(語言)  
SQL 主要的四大功能：Create(創建), Retrieve(檢索), Update(更新), Delete(刪除)  

SQL V.S NOSQL:  
- SQL:
  - 使用結構化的表格來存儲資料，表格有行和列，資料遵循嚴格的模式（schema）。
  - 使用結構化查詢語言（Structured Query Language, SQL）來操作資料，查詢語法固定且功能強大。
- NOSQL:
  - 沒有固定的模式，可以儲存非結構化資料
  - 沒有標準化的查詢語言，每種資料庫可能有不同的查詢方式。  
![image](https://github.com/user-attachments/assets/2f161b3c-8549-42f1-8315-9f64851cf3dd)  
參考圖片：參考自 youtube 影片：MySQL Full Course for free 🐬  
