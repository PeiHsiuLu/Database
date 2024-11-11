from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# 資料庫連接配置
db_config = {
    'host': 'localhost',  # 你的 database 的 host
    'user': 'root',       # 你的 user 名稱
    'password': '1234',   # 你的密碼
    'database': 'crud_1027'  # 你使用的資料庫
}

# GPA 對應字典 - 將成績轉換為 GPA 分數
GRADE_TO_GPA = {
    'A+': 4.3, 'A': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'D': 1.0, 'X': 0.0
}

# 建立資料庫連接
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

# 首頁 - 顯示所有學生 & 搜尋功能
@app.route('/', methods=['GET'])
def index():
    search_query = request.args.get('search')
    conn = get_db_connection()
    cursor = conn.cursor()

    if search_query:
        cursor.execute("""
            SELECT student_id, first_name, last_name, birth_date, email 
            FROM students 
            WHERE first_name LIKE %s OR last_name LIKE %s OR email LIKE %s OR birth_date LIKE %s
        """, ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
    else:
        cursor.execute("SELECT student_id, first_name, last_name, birth_date, email FROM students")
        
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=students, search_query=search_query)

# 新增學生
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birth_date = request.form['birth_date']
        email = request.form['email']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (first_name, last_name, birth_date, email) VALUES (%s, %s, %s, %s)", 
                       (first_name, last_name, birth_date, email))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/')
    return render_template('create.html')


# 更新學生資料
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birth_date = request.form['birth_date']
        email = request.form['email']
        cursor.execute("UPDATE students SET first_name = %s, last_name = %s, birth_date = %s, email = %s WHERE student_id = %s", 
                       (first_name, last_name, birth_date, email, id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')
    
    cursor.execute("SELECT * FROM students WHERE student_id = %s", (id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update.html', student=student)


# 刪除學生資料
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

# 新增選課
@app.route('/enrollments/add/<int:student_id>', methods=['GET', 'POST'])
def add_enrollment(student_id):
    if request.method == 'POST':
        course_name = request.form['course_name']
        semester = request.form['semester']
        grade = request.form['grade']
        credits = request.form['credits']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Enrollments (student_id, course_name, semester, grade, credits) VALUES (%s, %s, %s, %s, %s)", 
                       (student_id, course_name, semester, grade, credits))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/')
    return render_template('add_enrollment.html', student_id=student_id)

# 更新選課
@app.route('/enrollments/update/<int:enrollment_id>/<int:student_id>', methods=['GET', 'POST'])
def update_enrollment(enrollment_id, student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        course_name = request.form['course_name']
        semester = request.form['semester']
        grade = request.form['grade']
        credits = request.form['credits']
        cursor.execute("UPDATE Enrollments SET course_name = %s, semester = %s, grade = %s, credits = %s WHERE enrollment_id = %s", 
                       (course_name, semester, grade, credits, enrollment_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')
    
    cursor.execute("SELECT course_name, semester, grade, credits, enrollment_id FROM Enrollments WHERE enrollment_id = %s", (enrollment_id,))
    enrollment_data = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update_enrollment.html', enrollment=enrollment_data, student_id=student_id)

# 查看學生詳細資料 & 搜尋選課
@app.route('/student/<int:student_id>', methods=['GET'])
def view_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # 獲取學生資料
    cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    student = cursor.fetchone()

    # 搜尋關鍵字
    search_query = request.args.get('search_enrollment')

    # 根據搜尋條件獲取選課資料
    if search_query:
        cursor.execute(
            """
            SELECT course_name, semester, grade, credits, enrollment_id 
            FROM Enrollments 
            WHERE student_id = %s AND (
                course_name LIKE %s OR 
                semester LIKE %s OR 
                grade LIKE %s OR 
                credits LIKE %s
            )
            """,
            (student_id, f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%")
        )
    else:
        cursor.execute(
            "SELECT course_name, semester, grade, credits, enrollment_id FROM Enrollments WHERE student_id = %s",
            (student_id,)
        )

    enrollments = cursor.fetchall()

    # 計算每學期的加權平均 GPA 和總學分
    semester_credits = {}
    semester_gpa_sum = {}
    
    for enrollment in enrollments:
        course_name, semester, grade, credits, enrollment_id = enrollment
        gpa = GRADE_TO_GPA.get(grade, 0)
        
        credits = credits if credits is not None else 0
        
        if semester not in semester_credits:
            semester_credits[semester] = 0
            semester_gpa_sum[semester] = 0

        semester_credits[semester] += credits
        semester_gpa_sum[semester] += gpa * credits

    # 計算每學期的加權平均 GPA
    semester_avg_gpa = {sem: round(semester_gpa_sum[sem] / semester_credits[sem], 2) if semester_credits[sem] else 0 
                        for sem in semester_credits}

    cursor.close()
    conn.close()

    return render_template('view_student.html', student=student, semester_credits=semester_credits, 
                           semester_avg_gpa=semester_avg_gpa, enrollments=enrollments, search_query=search_query)


# 刪除選課
@app.route('/enrollments/delete/<int:enrollment_id>/<int:student_id>', methods=['POST'])
def delete_enrollment(enrollment_id, student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Enrollments WHERE enrollment_id = %s", (enrollment_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

# 新增課程
@app.route('/courses/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_name = request.form['course_name']
        credits = request.form['credits']
        description = request.form['description']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO courses (course_name, credits, description) VALUES (%s, %s, %s)",
                       (course_name, credits, description))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/courses')
    return render_template('add_course.html')

# 更新課程
# 更新課程
@app.route('/courses/update/<int:course_id>', methods=['GET', 'POST'])
def update_course(course_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        course_name = request.form['course_name']
        credits = request.form['credits']
        description = request.form['description']

        cursor.execute("UPDATE courses SET course_name = %s, credits = %s, description = %s WHERE course_id = %s",
                       (course_name, credits, description, course_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/courses')

    cursor.execute("SELECT course_id, course_name, credits, description FROM courses WHERE course_id = %s", (course_id,))
    course = cursor.fetchone()
    cursor.close()
    conn.close()

    # 使用字典方式傳遞變數
    return render_template('update_course.html', 
                           course_id=course[0], 
                           course_name=course[1], 
                           credits=course[2], 
                           description=course[3])


# 刪除課程
@app.route('/courses/delete/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE course_id = %s", (course_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/courses')

# 查看所有課程 & 搜尋功能
@app.route('/courses', methods=['GET'])
def courses():
    search_query = request.args.get('search_course')
    conn = get_db_connection()
    cursor = conn.cursor()

    if search_query:
        cursor.execute(
            "SELECT * FROM courses WHERE course_name LIKE %s OR description LIKE %s",
            ('%' + search_query + '%', '%' + search_query + '%')
        )
    else:
        cursor.execute("SELECT * FROM courses")

    courses = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('courses.html', courses=courses, search_query=search_query)

# 顯示學生和選課信息（使用 JOIN）
@app.route('/join', methods=['GET'])
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
