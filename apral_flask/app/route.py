""" Specifies routing for the application"""
from flask import render_template, request, jsonify, redirect, url_for
from app import app
from app import database as db_helper

GAME_OPT = 0
DEV_OPT = 1
PUB_OPT = 2
PLAT_OPT = 3
USER_OPT = 4
UP_OPT = 5
PLAY_OPT = 6
BSD_OPT = 7

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
    items = db_helper.show(GAME_OPT, condition=condition)
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
    db_helper.delete_entity(game_name, GAME_OPT)

    return redirect('/game')


@app.route('/game_update', methods=['POST'])
def game_update():

    game_name = request.form.get('upd_game_name', '')
    release_year = request.form.get('upd_release_year', '')
    genre= request.form.get('upd_genre', '')
    dev_name = request.form.get('upd_dev_name', '')
    pub_name = request.form.get('upd_pub_name', '')
    NA_sales = request.form.get('upd_NA_sales', '')
    EU_sales = request.form.get('upd_EU_sales', '')
    JP_sales = request.form.get('upd_JP_sales', '')
    Global_Sales = request.form.get('upd_global_sales', '')
    user_score = request.form.get('upd_user_score', '')
    user_count = request.form.get('upd_user_count', '')
    rating = request.form.get('upd_rating', '')

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
    db_helper.update_game(game)
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
    items = db_helper.show(BSD_OPT, condition=condition)
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
    db_helper.delete_relationship(based, BSD_OPT)

    return redirect('/based')


@app.route('/developer', methods=['GET', 'POST'])
def developer_search():
    condition = request.form.get('developer_name', '')
    if condition != '':
        condition = 'WHERE DevName="' + condition + '"'
    items = db_helper.show(DEV_OPT, condition=condition)
    return render_template('table_views/developer.html', items=items)


@app.route('/developer_insert', methods=['POST'])
def developer_insert():

    developer_name = request.form.get('ins_developer_name', '')
    active = request.form.get('ins_active', '')
    city = request.form.get('ins_city', '')
    country = request.form.get('ins_country', '')
    establish_time = request.form.get('ins_establish_time', '')
    notable_games = request.form.get('ins_notable_games', '')
    notes = request.form.get('ins_notes', '')   

    developer = {
        "DevName": developer_name,
        "Active": active,
        "City": city,
        "Country": country,
        "EstablishTime": establish_time,
        "Notable_games": notable_games,
        "Notes": notes,
    }
    db_helper.insert_developer(developer)
    return redirect('/developer')


@app.route("/developer_delete", methods=['POST'])
def developer_delete():

    developer_name = request.form.get('del_developer_name', '')
    db_helper.delete_entity(developer_name, DEV_OPT)

    return redirect('/developer')


@app.route('/developer_update', methods=['POST'])
def developer_update():

    developer_name = request.form.get('upd_developer_name', '')
    active = request.form.get('upd_active', '')
    city = request.form.get('upd_city', '')
    country = request.form.get('upd_country', '')
    establish_time = request.form.get('upd_establish_time', '')
    notable_games = request.form.get('upd_notable_games', '')
    notes = request.form.get('upd_notes', '')   

    developer = {
        "DevName": developer_name,
        "Active": active,
        "City": city,
        "Country": country,
        "EstablishTime": establish_time,
        "Notable_games": notable_games,
        "Notes": notes,
    }
    db_helper.update_developer(developer)
    return redirect('/developer')


@app.route('/publisher', methods=['GET', 'POST'])
def publisher_search():
    condition = request.form.get('publisher_name', '')
    if condition != '':
        condition = 'WHERE PubName="' + condition + '"'
    items = db_helper.show(PUB_OPT, condition=condition)
    return render_template('table_views/publisher.html', items=items)


@app.route('/publisher_insert', methods=['POST'])
def publisher_insert():

    publisher_name = request.form.get('ins_publisher_name', '')
    headquarters = request.form.get('ins_headquarters', '')
    establishTime = request.form.get('ins_establishTime', '')
    notable_games = request.form.get('ins_notable_games', '')
    notes = request.form.get('ins_notes', '')


    publisher = {
        "PubName": publisher_name,
        "Headquarters": headquarters,
        "EstablishTime": establishTime,
        "Notable_games": notable_games,
        "Notes": notes,
    }
    db_helper.insert_publisher(publisher)
    return redirect('/publisher')


@app.route("/publisher_delete", methods=['POST'])
def publisher_delete():

    publisher_name = request.form.get('del_publisher_name', '')
    db_helper.delete_entity(publisher_name, PUB_OPT)

    return redirect('/publisher')

@app.route('/publisher_update', methods=['POST'])
def publisher_update():

    publisher_name = request.form.get('upd_publisher_name', '')
    headquarters = request.form.get('upd_headquarters', '')
    establishTime = request.form.get('upd_establishTime', '')
    notable_games = request.form.get('upd_notable_games', '')
    notes = request.form.get('upd_notes', '')


    publisher = {
        "PubName": publisher_name,
        "Headquarters": headquarters,
        "EstablishTime": establishTime,
        "Notable_games": notable_games,
        "Notes": notes,
    }
    db_helper.update_publisher(publisher)
    return redirect('/publisher')





@app.route('/platform', methods=['GET', 'POST'])
def platform_search():
    condition = request.form.get('platform_name', '')
    if condition != '':
        condition = 'WHERE Initial="' + condition + '"'
    items = db_helper.show(PLAT_OPT, condition=condition)
    return render_template('table_views/platform.html', items=items)


@app.route('/platform_insert', methods=['POST'])
def platform_insert():

    initial = request.form.get('ins_initial', '')
    fullName = request.form.get('ins_fullName', '')
    manufacturer = request.form.get('ins_manufacturer', '')
    num_JA_EU_US = request.form.get('ins_num_JA_EU_US', '')

    platform = {
        "Initial":initial,
        "FullName": fullName,
        "Manufacturer": manufacturer,
        "Num_JA_EU_US": num_JA_EU_US,
    }
    db_helper.insert_platform(platform)
    return redirect('/platform ')


@app.route("/platform_delete", methods=['POST'])
def platform_delete():

    platform_name = request.form.get('del_platform_name', '')
    db_helper.delete_entity(platform_name, PLAT_OPT)

    return redirect('/platform')

@app.route('/platform_update', methods=['POST'])
def platform_update():

    initial = request.form.get('upd_initial', '')
    fullName = request.form.get('upd_fullName', '')
    manufacturer = request.form.get('upd_manufacturer', '')
    num_JA_EU_US = request.form.get('upd_num_JA_EU_US', '')

    platform = {
        "Initial":initial,
        "FullName": fullName,
        "Manufacturer": manufacturer,
        "Num_JA_EU_US": num_JA_EU_US,
    }
    db_helper.update_platform(platform)
    return redirect('/platform ')

@app.route('/userplatform', methods=['GET', 'POST'])
def userplatform_search():
    condition1 = request.form.get('userid', '')
    condition2 = request.form.get('initial', '')  
    if condition1 != '' and condition2 == '':
        condition = 'WHERE UserId="' + condition1 + '"' 
    elif condition1 == '' and condition2 != '':
        condition = 'WHERE Initial="' + condition2 + '"'
    elif condition1 != '' and condition2 != '':
        condition = 'WHERE UserId="' + condition1 + '"' + ' AND Initial="' + condition2 + '"'
    elif condition1 == '' and condition2 == '':
        condition = ''
    items = db_helper.show(UP_OPT, condition=condition)
    return render_template('table_views/userplatform.html', items=items)


@app.route('/userplatform_insert', methods=['POST'])
def userplatform_insert():

    userid = request.form.get('ins_userid', '')
    initial = request.form.get('ins_initial', '')
    userplatform = {
        "UserId": userid,
        "Initial": initial,
    }
    db_helper.insert_use_platform(userplatform)
    return redirect('/userplatform')


@app.route("/userplatform_delete", methods=['POST'])
def userplatform_delete():

    userid = request.form.get('del_userid', '')
    initial = request.form.get('del_initial', '')
    userplatform = {
        "UserId": userid,
        "Initial": initial,
    }
    db_helper.delete_relationship(userplatform, UP_OPT)

    return redirect('/userplatform')


@app.route('/play', methods=['GET', 'POST'])
def play_search():
    condition1 = request.form.get('userid', '')
    condition2 = request.form.get('game_name', '')  
    if condition1 != '' and condition2 == '':
        condition = 'WHERE UserId="' + condition1 + '"' 
    elif condition1 == '' and condition2 != '':
        condition = 'WHERE GameName="' + condition2 + '"'
    elif condition1 != '' and condition2 != '':
        condition = 'WHERE UserId="' + condition1 + '"' + ' AND GameName="' + condition2 + '"'
    elif condition1 == '' and condition2 == '':
        condition = ''
    items = db_helper.show(PLAY_OPT, condition=condition)
    return render_template('table_views/play.html', items=items)


@app.route('/play_insert', methods=['POST'])
def play_insert():

    userid = request.form.get('ins_userid', '')
    game_name = request.form.get('ins_game_name', '')
    time_length = request.form.get('ins_time_length', '')
    proficiency = request.form.get('ins_proficiency', '')    

    play = {
        "UserId": userid,
        "GameName": game_name,
        "Time_length":time_length,
        "Proficiency":proficiency 
    }

    db_helper.insert_play(play)
    return redirect('/play')


@app.route("/play_delete", methods=['POST'])
def play_delete():

    userid = request.form.get('del_userid', '')
    game_name = request.form.get('del_game_name', '')
    play = {
        "UserId": userid,
        "GameName": game_name,
    }
    db_helper.delete_relationship(play, PLAY_OPT)

    return redirect('/play')


@app.route('/play_update', methods=['POST'])
def play_update():

    userid = request.form.get('upd_userid', '')
    game_name = request.form.get('upd_game_name', '')
    time_length = request.form.get('upd_time_length', '')
    proficiency = request.form.get('upd_proficiency', '')    

    play = {
        "UserId": userid,
        "GameName": game_name,
        "Time_length":time_length,
        "Proficiency":proficiency 
    }

    db_helper.update_play(play)
    return redirect('/play')

@app.route("/advquery1")
def advquery1():
    items = db_helper.show_advanced_query1()
    return render_template('table_views/advquery1.html', items=items)

@app.route("/advquery2")
def advquery2():
    items = db_helper.show_advanced_query2()
    return render_template('table_views/advquery2.html', items=items)

