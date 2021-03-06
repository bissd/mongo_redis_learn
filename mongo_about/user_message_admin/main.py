#-*- coding:utf-8 -*-

"""
# __author__ = 'hitler'
# time : '2019/4/28 5:41 PM'

#info:


"""
import json
from flask import Flask, render_template, request
from test_data.basic_find import DataBaseManager
from util.Checker import Checker


app = Flask(__name__)
manager = DataBaseManager()
checker = Checker()


@app.route('/')
def index():
    data_list = manager.query_info()
    return render_template('index.html', data_list=data_list)


@app.route('/add', methods=['POST'])
def add_info():

    # 获取 添加用户 的配置
    info = request.json
    # 检测字段是否完整
    if not checker.check_add_fields_exists(info):
        return json.dumps({"success":False, "reason":"字段不完整"}, ensure_ascii=False)

    # 检测 值 状态
    fail_reason = checker.check_value_valid(info)
    if fail_reason :
        return json.dumps({"success":False, "reason":fail_reason}, ensure_ascii=False)

    # 添加 删除值
    info['deleted'] = 0
    insert_result = manager.add_info(info)
    return json.dumps({'success': insert_result})


@app.route('/update', methods=['POST'])
def update_info():
    info = request.json
    if not checker.check_update_fields_exists(info):
        return json.dumps({'success':False, 'reason':'字段不完整'}, ensure_ascii=False)

    people_id = checker.transfer_people_id(info['people_id'])
    if people_id == -1:
        return json.dumps({'success':False, 'reason': 'ID必须为数字'})

    dict_tobe_updated = info['updated_info']
    fail_reason = checker.check_value_valid(dict_tobe_updated)
    if fail_reason:
        return json.dumps({'success':False, 'reason':fail_reason}, ensure_ascii=False)

    update_result = manager.update_info(people_id, dict_tobe_updated)
    return json.dumps({'success':update_result})


@app.route('/delete/<people_id>', methods=['GET'])
def delete(people_id):
    people_id = checker.transfer_people_id(people_id)
    if people_id >0:
        delete_result = manager.del_info(people_id)
        return json.dumps({'success':delete_result})
    return json.dumps({'success':False, 'reason':'ID有误'})

if __name__ == '__main__':
    app.run(port=5000,debug=True)