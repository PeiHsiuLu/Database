from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime

app = Flask(__name__)

# 設定 MongoDB 連線
app.config["MONGO_URI"] = "mongodb://localhost:27017/makeup_notes"
mongo = PyMongo(app)

# 首頁顯示所有筆記
@app.route('/')
def index():
    notes = list(mongo.db.note_data.find())
    for note in notes:
        # 格式化日期，去除小數點部分
        note['date'] = note['date'].strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', notes=notes)

# 新增筆記
@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form.get('title')
    content = request.form.get('content')
    note = {
        "title": title,
        "content": content,
        "date": datetime.datetime.now()
    }
    mongo.db.note_data.insert_one(note)
    return redirect(url_for('index'))

# 編輯筆記頁面和更新功能
@app.route('/edit_note/<note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        mongo.db.note_data.update_one(
            {"_id": ObjectId(note_id)},
            {"$set": {"title": title, "content": content, "date": datetime.datetime.now()}}
        )
        return redirect(url_for('index'))
    
    note = mongo.db.note_data.find_one({"_id": ObjectId(note_id)})
    # 格式化日期，去除小數點部分
    note['date'] = note['date'].strftime("%Y-%m-%d %H:%M:%S")
    return render_template('edit_note.html', note=note)

# 刪除筆記
@app.route('/delete_note/<note_id>', methods=['POST'])
def delete_note(note_id):
    mongo.db.note_data.delete_one({"_id": ObjectId(note_id)})
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
