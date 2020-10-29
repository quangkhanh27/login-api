from flask import Blueprint, request, json
from ..Controllers.Todo import get_all_CTL, get_by_id, add_CTL, delete_CTL, update_CLT
from ..Helper.JsonEnCode import JSONEncoder
from bson.objectid import ObjectId
from datetime import datetime

todo = Blueprint('todo', __name__)

# http://localhost:5000/api/login  method = GET


@todo.route('/api/login', methods=['GET'])
def get_all():
    print(get_all_CTL())
    return json.dumps(get_all_CTL(), cls=JSONEncoder)

# http://localhost:5000/api/login/?_id=  method = GET


@todo.route('/api/login/', methods=['GET'])
def get_by_id_todo():
    id = request.args['_id']
    return json.dumps(get_by_id(id), cls=JSONEncoder)

# http://localhost:5000/api/login  method = POST


@todo.route('/api/login', methods=['POST'])
def check_login():
    _id = request.json['_id']
    pas = request.json['pass']
    try:
        acc = get_by_id(_id)
        if acc['pass'] == pas:
            return {"status": "Đăng nhập thành công", "user": acc}
        else:
            return "Sai mật khẩu", 400
    except:
        return "Tài khoản không tồn tại", 400


@todo.route('/api/checkid/', methods=['GET'])
def check_id():
    _id = request.args['_id']
    try:
        acc = get_by_id(_id)
        if acc is None:
            return "Tài khoản không tồn tại",200
        return "Tài khoản đã tồn tại", 400
    except:
        return "Tài khoản không tồn tại"


# http://localhost:5000/api/login  method = POST


@todo.route('/api/addtodo', methods=['POST'])
def add_todo():
    id = request.json['_id']
    pass_word = request.json['pass']
    email = request.json['email']
    name = request.json['name']
    sex = request.json['sex']
    add_CTL({"_id": id, "pass": pass_word, "email": email,
             "name": name, "sex": sex})
    return 'Đăng ký thành công'

# http://localhost:5000/api/login/?id=  method = DELETE


@todo.route('/api/login/', methods=['DELETE'])
def delete_by_id_todo():
    id = request.args['id']
    json.dumps(delete_CTL(id))
    return 'ok'

# http://localhost:5000/api/login  method = GET


@todo.route('/api/login', methods=['PUT'])
def update_todo():
    id = request.json['_id']
    pass_word = request.json['pass']
    email = request.json['email']
    name = request.json['name']
    sex = request.json['sex']
    update_CLT({"_id": id, "pass": pass_word, "email": email,
                "name": name, "sex": sex})
    return 'Chỉnh sửa thành công'
