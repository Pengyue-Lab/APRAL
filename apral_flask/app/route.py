""" Specifies routing for the application"""
from flask import render_template, request, jsonify, redirect, url_for
from app import app
from app import database as db_helper



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


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/form')
def form_page():
    return render_template('form.html')


@app.route('/game', methods=['GET', 'POST'])
def game_search():
    # https://stackoverflow.com/questions/42154602/how-to-get-form-data-in-flask
    condition = request.form.get('game_name', '')
    if condition != '':
        condition = 'WHERE GameName="' + condition + '"'
    items = db_helper.show_game(condition)
    return render_template('table_views/game.html', items=items)


@app.route('/game_insert', methods=['POST'])
def game_insert():

    game_name = request.form.get('ins_game_name', '')
    release_year = request.form.get('ins_release_year', '')
    genre= request.form.get('ins_genre', '')
    dev_name = request.form.get('ins_dev_name', '')
    pub_name = request.form.get('ins_pub_name', '')
    NA_sales = request.form.get('ins_NA_sales', '')
    EU_sales = request.form.get('ins_EU_sales', '')
    JP_sales = request.form.get('ins_JP_sales', '')
    Global_Sales = request.form.get('ins_global_sales', '')
    user_score = request.form.get('ins_user_score', '')
    user_count = request.form.get('ins_user_count', '')
    rating = request.form.get('ins_rating', '')

    game = {
        "GameName": game_name,
        "ReleaseYear": release_year,
        "Genre": genre,
        "PubName": pub_name,
        "NA_Sales": NA_sales,
        "EU_Sales": EU_sales,
        "JP_Sales": JP_sales,
        "Global_Sales": Global_Sales,
        "User_Score": user_score,
        "User_Count": user_count,
        "DevName": dev_name,
        "Rating": rating,
    }
    db_helper.insert_game(game)
    return redirect('/game')


@app.route("/game_delete", methods=['POST'])
def game_delete():

    game_name = request.form.get('del_game_name', '')
    db_helper.delete_game(game_name)

    return redirect('/game')




@app.route('/based', methods=['GET', 'POST'])
def based_search():
    condition1 = request.form.get('game_name', '')
    condition2 = request.form.get('initial', '')  
    if condition1 != '' and condition2 == '':
        condition = 'WHERE GameName="' + condition1 + '"' 
    elif condition1 == '' and condition2 != '':
        condition = 'WHERE Initial="' + condition2 + '"'
    elif condition1 != '' and condition2 != '':
        condition = 'WHERE GameName="' + condition1 + '"' + ' AND Initial="' + condition2 + '"'
    elif condition1 == '' and condition2 == '':
        condition = ''
    items = db_helper.show_based(condition)
    return render_template('table_views/based.html', items=items)


@app.route('/based_insert', methods=['POST'])
def based_insert():

    game_name = request.form.get('ins_game_name', '')
    initial = request.form.get('ins_initial', '')
    game = {
        "GameName": game_name,
        "Initial": initial,
    }
    db_helper.insert_based(game)
    return redirect('/based')


@app.route("/based_delete", methods=['POST'])
def based_delete():

    game_name = request.form.get('del_game_name', '')
    initial = request.form.get('del_initial', '')
    based = {
        "GameName": game_name,
        "Initial": initial,
    }
    db_helper.delete_based(based)

    return redirect('/based')