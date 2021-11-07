""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper


@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    """ recieved post requests for entry updates """

    data = request.get_json()

    try:
        if "status" in data:
            db_helper.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            db_helper.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    db_helper.insert_new_task(data['GamenName'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/")
def homepage():
    """ returns rendered homepage """
    # items = db_helper.show_game()
    # return render_template("index.html", items=items)
    return render_template("index.html")


@app.route('/form')
def form_page():
    return render_template('form.html')


@app.route('/game_search', methods=['GET', 'POST'])
def game_search():
    # https://stackoverflow.com/questions/42154602/how-to-get-form-data-in-flask
    condition = request.form.get('game_name', '')
    if condition != '':
        condition = 'WHERE GameName="' + condition + '"'
    print(request.args)
    items = db_helper.show_game(condition)
    return render_template('game_search.html', items=items)
