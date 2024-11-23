# 113-1 Database

**Name:** 呂沛修  
**Lecturer:** 蔡芸琤教授  
**Department and Grade:** 科技系三年級  

**目錄(點擊以下欄位，跳轉到該位置)**  
- [Final Project](#Final-Project)
- [Homework](#Homework)
- [Database Study Notes](#Notes)

---


## Final Project

---


## Homework
- [HW1 簡易登入/註冊系統](#hw1-簡易登入註冊系統)  
  - [1. HW1 程式碼](https://github.com/PeiHsiuLu/Database/tree/main/Week3/mysql_and_flask)  
  - [2. HW1 影片](https://youtu.be/846RmjGRTiY)
  - 補充：MySQLWorkbench及時儲存原影片只錄製到已儲存的資料，後續有再補一隻短片放在影片簡介區證明資料可在SQL被及時儲存  
- [HW2 SQL CRUD 學生修課成績管理系統](#hw2-學生修課成績管理系統)
  - [ER_Diagram](https://github.com/PeiHsiuLu/Database/blob/main/students/HW2_ERdiagram.png)
  - [原始碼](https://github.com/PeiHsiuLu/Database/tree/main/students)
  - [影片](https://www.youtube.com/watch?v=REO3aCTiBXE)
  - [補充：join放置相同的webapp上執行](https://www.youtube.com/watch?v=qaqdUbbphZ0)：The join result can be shown on the same webapp right now.
- [HW3 MongoDB Flask: The Note Manager](#hw3-mongodb-flask-the-note-manager)
  - [程式碼](https://github.com/PeiHsiuLu/Database/tree/main/HW3)  
  - [影片](https://www.youtube.com/watch?v=WhY-jG7982g)  
- [HW4 MongoDB Flask: HRIS Management]()
  - [程式碼]()
  - [影片](https://www.youtube.com/watch?v=IISaKSBv3jo) 
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

### HW2 學生修課成績管理系統  
這次作業，主要是練習SQL CRUD 如何運用在專案內。  

#### studnts table
**圖一：主頁：學生清單(Read students)**  
包含所有的學生、刪除學生按鈕、搜尋學生  
![image](https://github.com/user-attachments/assets/82ec9d20-03e0-4eef-9fce-e1ffa634b0dd)  
**圖二：更新學生**  
![image](https://github.com/user-attachments/assets/ff1220e2-f3d8-4a01-9835-23656d547817)

**圖三：新增學生**  
![image](https://github.com/user-attachments/assets/e509dec8-d47c-45b4-b8e6-101127ab204d)  

**圖四：students table**  
![image](https://github.com/user-attachments/assets/c28f7e5c-7d93-4b25-9d2e-1aafc90deeb3)  


#### enrollments table
**圖五：enrollments(read, delete, update Enrollments)**  
- 讀取Enrollments的數據，其中涵蓋刪除數據、修改數據。
- GPA Records會同步每一個學期的紀錄
![image](https://github.com/user-attachments/assets/6a51d59a-4ca5-41d4-b6ba-a572b59bd574)

**圖六：Add enrollments**  
增加 Enrollments table 的數據  
![image](https://github.com/user-attachments/assets/dafc059c-623f-41f1-84a8-4e2e803a48c8)  
**圖七：更新 enrollments 數據**  
![image](https://github.com/user-attachments/assets/6bd08385-ddc0-46a6-9526-3be1964f1826)

**圖八：enrollments table**  
![image](https://github.com/user-attachments/assets/dccaecbd-000e-4972-855d-f0910e0aa508)  

#### Courses table  
**圖九：read, delete courses**  
課程列表清單(讀取、刪除、修改)  
![image](https://github.com/user-attachments/assets/88dafc00-7a36-4457-acaa-cd03b31b23ae)  

**圖十：update courses**  
刪除courses數據  
![image](https://github.com/user-attachments/assets/ccfa7fbc-a073-4698-a365-d0b7c3929dda)  
**圖十一：Add courses**  
新增courses數據  
![image](https://github.com/user-attachments/assets/5460cba4-aa7b-498a-831e-5d7852448ee9)  
**圖十二：courses table**  
![image](https://github.com/user-attachments/assets/616c2914-5076-40e1-b85b-32d8268818cf) 

# HW3 MongoDB Flask: the note manager
## 動機
- 練習 MongoDB Flask 的建置，進一部練習MongoDB的CRUD指令在Flask網頁上的運用  
- 做一個備忘錄網頁  
## 頁面
### 主頁

![image](https://github.com/user-attachments/assets/b1094939-a1e4-4f1c-a772-4b1c97486b91)  
### 編輯頁面  
![image](https://github.com/user-attachments/assets/9f2e51b4-25ab-4a44-b8d1-7c3ee91ee11d)   
## MongoDB compass  
凡是被新增的note，資料都會被儲存進MongoDB Compass  
![image](https://github.com/user-attachments/assets/a121eefa-1ceb-41d9-a665-ccde6e8d1389)   








---

## Notes
- [1. Week 1: Course Introduction (0902-0908)](#week-1-course-introduction-0902-0908)  
- [2. Week 2: Install Flask & SQL in Flask (0909-0915)](#week-2-install-flask--sql-in-flask-0909-0915)
- [3. Week 3: Flask Connect to MySQL (0916-0922)](#week-3-flask-connect-to-mysql-0916-0922)
- [4. Week 4: MySQL Instruction and Introduction (0923-0930)](#week-4-mysql-instruction-and-introduction-0923-0930)
- [5. Week 5-8: MySQL CRUD](#week-5-8-mysql-crud)
- [6. Week 9: NOSQL-MONGODB基礎語法](#Week9-nosql-mongodb基礎語法)
- [7. Week 10: MongoDB + Flask](#week-10-MongoDB-flask)



### Week 1: Course Introduction (0902-0908)  
簡單介紹資料庫系統這門課會學習到的內容：  
- MySQL + Flask + CRUD
- NoSQL + Flask + CRUD (MongoDB)
- 利用可堂所學做一份資料庫期末專題
- SQLquery    

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
![image](https://github.com/user-attachments/assets/d19399d2-a7f5-4835-9aa8-36ee83408657)
利用 GPT 生成的比較圖

常見的 DBMS (Database Management System)：  
- MySQL
- SQL Server
- Oracle
- PostgreSQL
#### SQL 指令

##### Database

- 創建資料庫
  ```SQL
  CREATE DATABASE 資料庫名稱;
  ```
- 使用資料庫
  ```SQL
  USE 要使用的資料庫;
  ```
- 丟棄資料庫
  ```SQL
  DROP DATABASE 所要刪除的資料庫;
  ```
- 改變資料庫使用權
  ```SQL
  ALTER DATABASE 資料庫 READ ONLY = 1; //變成唯讀檔，不可再做更動
  ALTER DATABASE 資料庫 READ ONLY = 0; //變回可使用的檔案(可做更動)
  ```

### Week 5-8: MySQL CRUD

#### 1. 創建 (Create)

使用 `INSERT INTO` 語法在資料庫表中插入新紀錄。

```sql
INSERT INTO students (first_name, last_name, birth_date, email)
VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com');
```

#### 2. 讀取 (Read)  
**查詢所有紀錄**    
```sql
SELECT * FROM students;
```

**使用條件查詢**  
```sql
SELECT first_name, last_name FROM students WHERE birth_date > '1995-01-01';
```

**排序查詢結果**  
限制查詢結果數量  
```sql
SELECT * FROM students LIMIT 10;
```

#### 3. 更新 (Update)  
使用 UPDATE 語法修改已存在的資料。  
```sql
UPDATE students
SET email = 'new.email@example.com'
WHERE student_id = 1;
```

#### 4. 刪除 (Delete)   
使用 DELETE FROM 語法刪除指定條件的紀錄。   
```sql
DELETE FROM students WHERE student_id = 1;
```

#### CRUD 操作範例：Task Master (Flask + MySQL)   
以下展示 Flask 應用程式如何與 MySQL 整合進行 CRUD 操作。   
```python
from flask import Flask, request, redirect, render_template
import mysql.connector

app = Flask(__name__)

# 設置資料庫連接
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'task_manager'
}

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

# 創建
@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form['content']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (content) VALUES (%s)", (task_content,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

# 讀取
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', tasks=tasks)

# 更新
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    new_content = request.form['content']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET content = %s WHERE id = %s", (new_content, task_id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

# 刪除
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
```

#### 練習：建立CRUD程式  
- 創建資料庫：
  ```sql
  CREATE DATABASE task_manager;
  USE task_manager;
  ```
- 創建表格：
  ```sql
    CREATE TABLE tasks (
      id INT AUTO_INCREMENT PRIMARY KEY,
      content VARCHAR(255) NOT NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
  ```
- 使用 Flask + MySQL 進行 CRUD 操作：
  - 創建新任務
  - 讀取並顯示所有任務
  - 更新指定任務
  - 刪除任務

#### 日常指令練習 
1. 創建資料庫：  
```sql
CREATE DATABASE test
```
2. 使用資料庫：
```sql
USE test
```
3. 創建表格：
```sql
CREATE TABLE test(
test_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL,
age INT,
email VARCHAR(100) unique
)
```
- AUTI INCREMENT: 自動增加
- PRIMARY KEY: 主鍵
- NOT NULL: 不能為空值
- VARCHAR: 字串類型
- UNIQUE: 唯一

4. 插入值：
```sql
INSERT INTO test(name,age,email)
VALUES ('John',18,'test@gmail.com');
```
5.查詢所有資料：  
```sql
select  * from test
```
6.選擇要查詢的條件(select 欄位 from 表格 where 條件):  
```sql
SELECT student_id, first_name, last_name from students WHERE student_id%2= 1 || student_id%3=1;
```

7. 限制讀取的資料筆數：
```sql
SELECT * FROM students limit 4;
```
限制讀取students表格資料4筆  

8.更新資料：  
```
UPDATE students
SET birth_date = '2023-04-07'
WHERE student_id % 2 = 1
LIMIT 2;
```
9. 刪除資料：
```sql
DELETE FROM students WHERE student_id=8
```
10. 結合資料：
-INNER JOIN:  
```sql
SELECT students.student_id, enrollments.grade
FROM students
INNER JOIN  enrollments ON  students.student_id = enrollments.student_id
```
- LEFT JOIN:  
右表若為空值，則返回NULL。  
```sql
SELECT students.student_id, enrollments.grade
FROM students
LEFT JOIN  enrollments ON  students.student_id = enrollments.student_id
```
### Week9: NOSQL-MONGODB基礎語法
這一些語法，皆需要在mongodbshell內執行  
Mongodb 資料用 json 格式儲存。  
#### databases   
- 顯示資料庫  
  ```sql
  show dbs
  ```
- 使用資料庫  
  ```sql
  use 資料庫名稱 
  ```
- 創建表格(只有創建表格，資料庫才會出現)  
  ```sql
  db.createCollection("表格名稱")
  ```
- 捨棄資料庫  
  ```sql
  db.dropDatabase()
  ```
#### insert
- 插入表格內的一個值  
  ```sql
  db.表格名稱.insertOne({name:"Louis Lin",age:20,gpa:4.2})
  ```
- 尋找表格內有多少值  
  ```sql
  db.表格名稱.find()
  ```
- 插入表格內多個值 (資料可以插入長短不一、種類不一的資料)
  ```sql
  db.表格名稱.insertMany([{name:"Lee",age:30},{name:"Hua",age:40,gpa:4.02}])
  ```
  也可以在MongodbCompass內直接新增新的值入數據集中(直接寫語法進去，或是嵌入CSV, JSON檔)  
#### datatypes
1. 字串型態(string), ex. "Larry"  
2. 整數(integer), ex. 12  
3. 小數(float), ex. 12.7  
4. 布林值：true,false  
5. 空值：null  
6. 陣列型態,ex. ["Calculus","Economics"]  
7. 時間, ex. new Date()  
8. 字典型態, ex.Record:{name:"Smith",age:17}  
   ```sql
   db.students.insertOne({name:"Larry",age:12,gpa:4.2,fulltime:true,recordtime:new Date(),graduationDate:null,courses:["Biology","Calculus"],address:{street:"Apple",city:"Hsinchu",zip:12345}})
   ```
####  sorting & limiting
1. sort: 1 (由小到大排列, a到z,大寫到小寫,短到長);sort:-1  (由大到小排列,z到a,小寫到大寫,長到短)
2. limit：限制幾筆數據 (limit(0)會返回所有數據)  
   ```sql
   db.表格名稱.find().sort({name:1}).limit(10)
   ```
也可以利用MongoDBcompass做到：  
![image](https://github.com/user-attachments/assets/cc5f813d-0143-43a3-999f-51258f68679b)  

#### find  
- 可以找到單一或多個相符的值
  ex.1:  
  ```sql
  db.students.find({gpa:4.25})
  ```
  ex.2:
  ```sql
  db.students.find({gpa:4.25,name:"Harry"})
  ```
- 可以選擇是否出現該值(true代表出現, false 代表隱藏)
  格式：   .find({query},{projection})
  ```sql
  db.students.find({},{name:true,_id:false}).limit(5)
  ```
- 在MoogoDBCompass:  
  1.圖一：  
  ![image](https://github.com/user-attachments/assets/75c772a4-9c20-45aa-9c8c-64079f26e569)  
  2.圖二：  
  ![image](https://github.com/user-attachments/assets/ece05887-0435-4018-9c10-4e85c2dad504)

#### update  
- set
  可以修改單一現有數值或是多個現有數值。
  ({filter},{update})  

  設定單一數值 name 為 "Leee"   
  ```sql
  db.students.updateOne({_id: ObjectId('6721cb2db82fc5621d86b01d')},{$set:{name:"Leee"}})
  ```
  設定許多數值為gpa:4.30  
  ```sql
  db.students.updateMany({},{$set:{gpa:4.30}})  
  ```

- unset
  可以刪除一筆數值
  ```sql
  db.students.updateOne({_id: ObjectId('6721d435b82fc5621d86b024')},{$unset:{age:"" }})
  ```
  以上範例為刪除年齡的數據(刪除的數據皆適用""代替)

  刪除多筆相同的數據
  ```sql
  db.students.updateMany({},{$unset:{gpa:4.25}})
  ```
  以上範例刪除所有GPA：4.25的數據
- exists 存在
  $exists:true >> 其值存在; $exists:false >> 其值不存在
  通常exists的作用是用來作為篩選值是否存在，否則則...   
  ```sql
  db.students.updateMany({fulltime:{$exists:false}},{$set:{fulltime:true}})
  ```
- MongodbCompass
  鉛筆可以用來變更compass內的值   
  ![image](https://github.com/user-attachments/assets/d317cb0a-8d5f-4dae-a281-aef9d4a20ab9)

#### delete  

- 刪除一筆數據  
  ```sql
  db.students.deleteOne({name:"Louis Lin})
  ```
- 刪除多筆數據
  ```sql
  db.students.deleteMany(name:{exists:false})
  ```
#### comparison operator($)   
通常是用做條件來搜尋一個特定條件的事物  
- $ne (不等於 not equal to)
  ```sql
  db.students.find({age:{$ne:17}})
  ```
- $lt, $lte (小於，小於等於)
  ```sql
   db.students.find({age:{$lte:25}})
  ```
- $gt, $gte
  ```sql
  db.students.find({age:{$gte:25}})
  ```
- 尋找範圍
  ```sql
  db.students.find({age:{$gte:20,$lt:25}})
  ```
- 尋找涵蓋在陣列中的值 ($in)
  ```sql
   db.students.find({name:{$in:["Larry","John","LEE"]}}
  ```
- 尋找不涵蓋在陣列內的值 ($nin)
  ```sql
   db.students.find({name:{$nin:["Larry"]}})
  ```
- 在MongoDBcompass內的用法
  ![image](https://github.com/user-attachments/assets/2abb78b7-ae1b-4207-9e1c-4f4b9a4f775f)

#### logic operators
- $and(且，兩個條件必須皆成立)
- $or (或，一個條件成立即可)
- $not (非)
- $nor (兩個皆不是)
```sql
db.students.find({$and:[{age:{$lte:21}},{fulltime:true}]})
```
```sql
db.students.find({$or:[{age:{$lte:21}},{fulltime:true}]})
```
```sql
db.students.find({$nor:[{age:{$lte:21}},{fulltime:true}]})
```
```sql
db.students.find({age:{$not:{$gte:20}}})
```

#### Index  
創建一個索引會非常消耗系統資源，所以要謹慎使用。(背後有大量的Binary tree 演算法在背後計算著)  
- 創建索引
  - 升冪：1
  - 降冪：-1 
```sql
db.students.createIndex({name:1})
```
- 顯示查詢的執行資料
  ```sql
   db.students.find({name:"Sarah"}).explain("executionStats")
  ```
- 顯示目前所有的索引值
  ```sql
  db.students.getIndexes()
  ```
- 捨棄索引值
  ```sql
  db.students.dropIndex("name_1")
  ```
index 在MongoDBCompass的位置  
####  collections
- 顯示 collection
  ```sql
  show collections
  ```
- 建立 collection
  ```sql
  db.createCollection("teacher",{capped:true,size:100000000,max:100},{autoIndexId:false})
  ```
  中間的值是用來建立集合。(有限集合)
- 捨棄collection
  ```sql
  db.teacher.drop()
  ```  

### Week 10 MongoDB&Flask
   
#### 關於 Python 中 Flask app 的一些基礎語法
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

# 設定 MongoDB 連線
app.config["MONGO_URI"] = "mongodb://localhost:27017/notes"
mongo = PyMongo(app)

@app.route('/')
def index():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)
```
- from flask import Flask: 從 Flask 框架中引入 Flask 類別，這是用來建立 Flask 應用程式的核心。
- render_template：用於渲染 HTML 模板文件（例如 .html 文件）。
- request: 允許 Flask 處理 HTTP 請求中的數據，例如 GET 或 POST 請求的資料。
- redirect：用來重定向使用者到不同的 URL。
- url_for：根據函數名稱生成 URL，便於路徑的動態調整。
```python
app = Flask(__name__)
```
- app = Flask(__name__)：建立一個 Flask 應用程式物件 app，並將當前模組的名稱（__name__）作為參數傳入，Flask 會根據這個名稱來決定應用程式的根路徑。
```python
# 設定 MongoDB 連線
app.config["MONGO_URI"] = "mongodb://localhost:27017/notes"
mongo = PyMongo(app)
```
- app.config["MONGO_URI"] = "mongodb://localhost:27017/notes"：設置 Flask 應用程式的 MongoDB 連線 URI，指定 MongoDB 伺服器位於本地端（localhost），使用端口 27017，並且使用名為 notes 的資料庫。
- mongo = PyMongo(app)：將 Flask 應用程式 app 與 MongoDB 進行連接，並將 MongoDB 連接實例儲存為 mongo，用於後續的數據操作。
```python
@app.route('/')
def index():
    return "hello"
```
- @app.route('/')：設置 Flask 路由，表示當用戶訪問根路徑 / 時，會執行下面的 index() 函數。
- def index():：定義 index 函數，用於處理根路徑的請求。
- return "hello"：回傳 "hello" 字串，作為訪問 / 路徑時的 HTTP 回應內容。
```python
if __name__ == "__main__":
    app.run(debug=True)
```
- if __name__ == "__main__":：這段程式碼的意思是，當此文件被直接執行時，會執行其內部的代碼。這在 Python 中用於區分模組是直接執行還是被其他模組引入。
- app.run(debug=True)：啟動 Flask 應用程式，並開啟除錯模式（debug=True），在此模式下，程式碼有變更時 Flask 會自動重啟，並在發生錯誤時顯示詳細的錯誤訊息。  
