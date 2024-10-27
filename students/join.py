from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# 資料庫連接配置
db_config = {
    'host': 'localhost',  # 你的 database 的 host
    'user': 'root',       # 你的 user 名稱
    'password': '1234',   # 你的密碼
    'database': 'crud_1027'  # 你使用的資料庫
}

# 建立資料庫連接
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

# 顯示學生和選課信息（使用 JOIN）
@app.route('/', methods=['GET'])
def student_enrollments():
    conn = get_db_connection()
    cursor = conn.cursor()

    # 修改的 JOIN 查詢 - 取得 student_id, course_name 和 grade
    query = """
    SELECT 
        s.student_id, c.course_name, e.grade
    FROM students s
    INNER JOIN enrollments e ON s.student_id = e.student_id
    INNER JOIN courses c ON e.course_name = c.course_name
    ORDER BY s.student_id;
    """
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    # 渲染結果頁面
    return render_template('student_courses.html', enrollments=result)

if __name__ == '__main__':
    app.run(debug=True)
