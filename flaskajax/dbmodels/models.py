from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Department(db.Model):

    '''
    <-- 部门表模型 -->
    类名：Department
    表名：department

    字段：
    id -- 部门id，int型
    name -- 部门名称，str型

    实例方法：
    to_json -> 返回 id 与 name 组成的 dict 对象
    '''

    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return "<部门 {} ： {}>".format(self.id, self.name)

    def to_json(self):
        return dict(id=self.id, name=self.name)


class Employee(db.Model):

    '''
    <-- 部门表模型 -->
    类名：Employee
    表名：employee

    字段：
    id -- 员工id，int型
    name -- 姓名，str型
    gender -- 性别，str型
    job -- 工作，str型
    birthdate -- 出生日期，datetime型
    idcard -- 身份证，str型
    address -- 地址，str型
    salary -- 薪资，float型
    release_time -- 发布时间
    department_id -- 所属部门id，外键，关联部门表id

    模型关系属性：
    department -- 员工关联的部门
    employees -- 部门关联的员工
    '''

    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    gender = db.Column(db.String)
    job = db.Column(db.String)
    birthdate = db.Column(db.DateTime)
    idcard = db.Column(db.String)
    address = db.Column(db.String)
    salary = db.Column(db.Float)
    release_time = db.Column(db.DateTime, default=datetime.now)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    department = db.relationship(
        'Department', backref=db.backref('employees', lazy='dynamic'))

    def __repr__(self):
        return '<员工 {}:{} {} {}>'.format(self.id, self.name, self.salary, self.address)
