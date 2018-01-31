from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dbmodels.models import *
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db/pms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


# ajax 展示计算模拟的页面同时包含非ajiax计算的效果
@app.route('/calc/')
def calc():
    a = int(request.args.get('num_1', 0))
    b = int(request.args.get('num_2', 0))
    result = a * b
    return render_template('calculate.html', result=result)


# 使用 ajax 模拟计算，供请求的地址
@app.route('/ajax_calc/')
def ajax_calc():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = a * b
    return str(result)


# xhr 原生最基本的 xhr 异步请求
@app.route('/xhr/')
def test_xhr():
    return render_template('xhr.html')


# xhr 请求内容的展示
@app.route('/xhr_content/')
def test_content():
    return render_template('content.html')


# jquery 的ajax 各种页面请求后端数据与ajax的对比
@app.route('/ajax-basic/')
def ajax_basic():
    return render_template('ajax-basic.html')


# 展示使用 ajax 异步查询的基础页面
@app.route('/ajax-query/')
def ajax_query():
    return render_template('emp-query.html')


# ajax 异步查询员工信息的接口
@app.route('/employees/')
def employee_query():
    name = request.args.get('name', '')

    table_header = """
        <table border='1'>
            <tr>
                <th>ID</th>
                <th>姓名</th>
                <th>地址</th>
                <th>工资</th>
            </tr>
    """

    employees = Employee.query.filter(Employee.name.contains(name)).all()

    rows = ""
    for emp in employees:
        rows += """
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
        """.format(emp.id, emp.name, emp.address, emp.salary)

    table_footer = "</table>"

    return table_header + rows + table_footer


# 无请求，本地数据模拟的 ajax 演示
@app.route('/json/')
def json_demo():
    return render_template('json-demo.html')


# 部门数据采用 ajax 异步加载页面
@app.route('/emp-json/')
def emp_json():
    return render_template('emp-query-json.html')


# 部门数据 ajax 查询接口，供部门渲染
@app.route('/departments/')
def departments():
    depts = Department.query.all()
    return jsonify([d.to_json() for d in depts])


if __name__ == '__main__':
    # 获取项目根目录
    base_path = os.path.split(os.path.abspath(__name__))[0]

    # 指定数据库保存目录在本项目的 db 文件夹下
    db_path = os.path.join(base_path, 'db')

    # 校验是否存在 db 文件夹，不存在进行创建
    if not os.path.exists(db_path):
        os.mkdir(db_path)

    app.run(debug=True)
