from flask import Flask, request, jsonify, render_template, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# 設定 MongoDB 連線
client = MongoClient("mongodb://localhost:27017/")
db = client['hrms']  # 資料庫名稱
employees = db['employees']

@app.route('/')
def index():
    # 取得員工列表
    employee_list = list(employees.find())
    return render_template('index.html', employees=employee_list)

@app.route('/employee', methods=['POST'])
def add_employee():
    # 從表單獲取資料
    name = request.form.get("name")
    department = request.form.get("department")
    position = request.form.get("position")
    salary = request.form.get("salary")

    # 檢查必填欄位
    if not all([name, department, position, salary]):
        return jsonify({"error": "All fields are required"}), 400

    # 確保薪資為數字
    try:
        salary = int(salary)
    except ValueError:
        return jsonify({"error": "Salary must be a number"}), 400

    # 插入新的員工資料，MongoDB 會自動生成 `_id`
    new_employee = {
        "name": name,
        "department": department,
        "position": position,
        "salary": salary
    }
    employees.insert_one(new_employee)
    return redirect('/')

@app.route('/employee/<id>', methods=['POST', 'PUT'])
def update_employee(id):
    # 更新員工資料
    try:
        updated_data = {
            "name": request.form.get("name"),
            "department": request.form.get("department"),
            "position": request.form.get("position"),
            "salary": int(request.form.get("salary")) if request.form.get("salary") else None,
        }
    except ValueError:
        return jsonify({"error": "Salary must be a number"}), 400

    # 確認所有欄位都有效
    if not all(updated_data.values()):
        return jsonify({"error": "All fields are required"}), 400

    # 使用 ObjectId 尋找並更新資料
    result = employees.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    if result.matched_count == 0:
        return jsonify({"error": "No matching document found"}), 404
    if result.modified_count == 0:
        return jsonify({"message": "No changes made to the document"}), 200

    return redirect('/')

@app.route('/employee/<id>/delete', methods=['POST'])
def delete_employee(id):
    # 刪除員工資料
    try:
        result = employees.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({"error": "No matching document found"}), 404
    except Exception as e:
        return jsonify({"error": f"Invalid ID: {str(e)}"}), 400

    return redirect('/')
@app.route('/employee/search', methods=['GET', 'POST'])
def search_employee():
    if request.method == 'POST':
        # 從表單獲取搜尋關鍵字
        search_term = request.form.get('search_term')
        if not search_term:
            return redirect('/')

        # 在 MongoDB 中搜尋，支援部分匹配 (模糊搜尋)
        search_results = employees.find({
            "$or": [
                {"name": {"$regex": search_term, "$options": "i"}},
                {"department": {"$regex": search_term, "$options": "i"}},
                {"position": {"$regex": search_term, "$options": "i"}}
            ]
        })
        return render_template('search_results.html', employees=list(search_results), search_term=search_term)

    # 如果是 GET 請求，直接返回搜尋頁面
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
