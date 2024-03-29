
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, jsonify
import os
import json
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main_form.html')


@app.route('/get_messages', methods=['POST'])
def get_messages():
    file = "/home/cloozis/mysite/messages.json"
    with open(file) as f:
        data = json.load(f)

    data_new = json.dumps(data)
    return data_new


@app.route('/send', methods=['POST'])
def parse_request():

    file = "/home/cloozis/mysite/messages.json"

    data_received = json.loads(request.data)


    id = data_received['id']
    name = data_received['name']
    msg = data_received['msg']
    time = data_received['time']

    new_data = { 'id': id, 'name': name, 'msg': msg, 'time': time }

    check_json_file(file)
    check_json_size_file(file, new_data)

    if request.method == 'POST':
        return f'done, {id}, {name}, {msg}, {time}'

    # id = request.args.get('id')
    # name = request.args.get('name')
    # msg = request.args.get('msg')
    # time = request.args.get('time')

    # id = request.args['id']
    # name = request.args['name']
    # msg = request.args['msg']
    # time = request.args['time']

    # data = request.args.get('data')




    # if request.method == 'POST':
    #     data = request.get_data()  # Получить данные POST запроса
    #     return data, 200
    # return f'POST request received with data: {data}'


    # post_data = request.data
    # # id = request.args.get('id')
    # name = request.args.get('name')
    # msg = request.args.get('msg')
    # time = request.args.get('time')


    # file = "messages.json"
    # uid = str(int(time.time()))

    # # new_data = { 'id': uid, 'name': name, 'msg': msg, 'time': time }
    # new_data = {'name': 'John1', 'age': 32, 'city': 'New York1', 'time': uid }
    # check_json_size_file(file, new_data)





def check_json_file(file):
    if os.path.exists(file):
        print("file exist")
    else:
        base_json_file = open(file, "w+")
        base_json_file.close()


def check_json_size_file(file, j_data):

    file_size = os.path.getsize(file)

    if file_size == 0:
        print(f'create')
        create_json(file, j_data)
    else:
        print(f'add')
        add_to_json(file, j_data)


def create_json(file_json, j_data):
    json_data = [j_data]
    with open(file_json, 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))



def add_to_json(file_json, j_data):
    data = json.load(open(file_json))
    data.append(j_data)
    with open(file_json, "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

# @app.route('/test_one')
# def function_page():
#     file = "/home/cloozis/mysite/messages.json"
#     uid = str(int(time.time()))
#     # new_data = {'name': 'John1', 'age': 32, 'city': 'New York1', 'time': uid }
#     name = 'username'
#     msg = 'message'
#     new_data = { 'id': uid, 'name': name, 'msg': msg, 'time': uid }


#     check_json_file(file)
#     check_json_size_file(file, new_data)
#     return 'done'


if __name__ == '__main__':
    print(get_messages())
    # file = "messages.json"
    # uid = str(int(time.time()))
    # # new_data = {'name': 'John1', 'age': 32, 'city': 'New York1', 'time': uid }
    # name = 'username'
    # msg = 'message'
    # new_data = { 'id': uid, 'name': name, 'msg': msg, 'time': uid }


    # check_json_file(file)
    # check_json_size_file(file, new_data)

    # print([new_data])
    # create_json("messages.json", new_data)
    # add_to_json("messages.json", new_data)
    # print(uid)
    # new_data = ""+uid+":{'name': 'John1', 'age': 32, 'city': 'New York1'}"

    # add_to_json("messages.json", new_data)
    # create_json_file("messages.json")
    # inert_json("messages.json", new_data)
    # read_data = read_json("messages.json")
    # print(read_data)
