"""Defines all the functions related to the database"""
from app import db

GAME_OPT = 0
DEV_OPT = 1
PUB_OPT = 2
PLAT_OPT = 3
USER_OPT = 4
UP_OPT = 5
PLAY_OPT = 6
BSD_OPT = 7
INSERT_OPT = 0
DELETE_OPT = 1
UPDATE_OPT = 2
SHOW_OPT = 3


def show(option, condition=''):
    conn = db.connect()
    query_str = None
    if option == GAME_OPT:
        query_str = "SELECT * FROM Game " + condition + ";"
    elif option == DEV_OPT:
        query_str = "Select * from Developer " + condition + ";"
    elif option == PUB_OPT:
        query_str = "Select * from Publisher " + condition + ";"
    elif option == PLAT_OPT:
        query_str = "Select * from Platform " + condition + ";"
    elif option == USER_OPT:
        query_str = "Select * from User " + condition + ";"
    elif option == UP_OPT:
        query_str = "Select * from UsePlatform " + condition + ";"
    elif option == PLAY_OPT:
        query_str = "Select * from Play " + condition + ";"
    elif option == BSD_OPT:
        query_str = "Select * from Based " + condition + ";"
    query_results = conn.execute(query_str).fetchall()
    conn.close()
    return_list = []
    for result in query_results:
        item = None
        if option == GAME_OPT:
            item = {
                "GameName": result[0],
                "ReleaseYear": result[1],
                "Genre": result[2],
                "PubName": result[3],
                "NA_Sales": result[4],
                "EU_Sales": result[5],
                "JP_Sales": result[6],
                "Global_Sales": result[7],
                "User_Score": result[8],
                "User_Count": result[9],
                "DevName": result[10],
                "Rating": result[11],
            }
        elif option == DEV_OPT:
            item = {
                "DevName": result[0],
                "Active": result[1],
                "City": result[2],
                "Country": result[3],
                "EstablishTime": result[4],
                "Notable_games": result[5],
                "Notes": result[6],
            }
        elif option == PUB_OPT:
            item = {
                "PubName": result[0],
                "Headquarters": result[1],
                "EstablishTime": result[2],
                "Notable_games": result[3],
                "Notes": result[4],
            }
        elif option == PLAT_OPT:
            item = {
                "Initial": result[0],
                "FullName": result[1],
                "Manufacturer": result[2],
                "Num_JA_EU_US": result[3],
            }
        elif option == USER_OPT:
            item = {
                "UserId": result[0],
                "Full_name": result[1],
                "First_name": result[2],
                "Last_name": result[3],
                "Gender": result[4],
                "Age": result[5],
                "Preference": result[6],
                "Password": result[7],
            }
        elif option == UP_OPT:
            item = {
                "UserId": result[0],
                "Initial": result[1],
            }
        elif option == PLAY_OPT:
            item = {
                "UserId": result[0],
                "GameName": result[1],
                "Time_length": result[2],
                "Proficiency": result[3],
            }
        elif option == BSD_OPT:
            item = {
                "GameName": result[0],
                "Initial": result[1],
            }
        return_list.append(item)
    return return_list


def show_advanced_query2():
    """Reads Select Game whose User_Score>8 and manufacturer is Sony or Game whose Use_Score<7 and manufacturer is Microsoft.

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    query_results = conn.execute("(Select GameName,Manufacturer,User_Score From Game natural join Based natural join Platform where User_Score>8 and Manufacturer = 'Sony')Union(Select GameName,Manufacturer,User_Score From Game natural join Based natural join Platform where User_Score<7 and Manufacturer = 'Microsoft')order by User_Score desc").fetchall()
    conn.close()
    result_list = []
    for result in query_results:
        item = {
            "GameName": result[0],
            "Manufacturer": result[1],
            "User_Score": result[2],
        }
        result_list.append(item)
    return result_list


def show_advanced_query1():
    """Select the top 8 popluar Developer among female or the top 7 popular Publisher among female.

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    query_results = conn.execute("(Select DevName as Name,count(*) as Num From Game natural join Play natural join User where Gender = 'FeMale' Group by DevName order by Num desc limit 8)union(Select PubName as Name,count(*) as Num From Game natural join Play natural join User where Gender = 'FeMale' Group by PubName order by Num desc limit 7)").fetchall()
    conn.close()
    result_list = []
    for result in query_results:
        item = {
            "DevPubName": result[0],
            "Number": result[1],
        }
        result_list.append(item)
    return result_list


def insert(obj, option):
    conn = db.connect()
    query = None
    if option == GAME_OPT:
        query = 'Insert into Game values("{}",{},"{}","{}",{},{},{},{},{},{},"{}","{}");'.format(
            obj['GameName'],
            obj['ReleaseYear'],
            obj['Genre'],
            obj['PubName'],
            obj['NA_Sales'],
            obj['EU_Sales'],
            obj['JP_Sales'],
            obj['Global_Sales'],
            obj['User_Score'],
            obj['User_Count'],
            obj['DevName'],
            obj['Rating']
        )
    elif option == DEV_OPT:
        query = 'Insert into Developer values("{}",{},"{}","{}",{},"{}","{}");'.format(
            obj['DevName'],
            obj['Active'],
            obj['City'],
            obj['Country'],
            obj['EstablishTime'],
            obj['Notable_games'],
            obj['Notes']
        )
    elif option == PUB_OPT:
        query = 'Insert into Publisher values("{}","{}",{},"{}","{}");'.format(
            obj['PubName'],
            obj['Headquarters'],
            obj['EstablishTime'],
            obj['Notable_games'],
            obj['Notes']
        )
    elif option == PLAT_OPT:
        query = 'Insert into Platform values("{}","{}","{}",{});'.format(
            obj['Initial'],
            obj['FullName'],
            obj['Manufacturer'],
            obj['Num_JA_EU_US']
        )
    elif option == USER_OPT:
        query = 'Insert into User values("{}","{}","{}","{}","{}",{},"{}","{}");'.format(
            obj['UserId'],
            obj['Full_name'],
            obj['First_name'],
            obj['Last_name'],
            obj['Gender'],
            obj['Age'],
            obj['Preference'],
            obj['Password']
        )
    elif option == UP_OPT:
        query = 'Insert into UsePlatform values("{}","{}");'.format(
            obj['UserId'],
            obj['Initial']
        )
    elif option == PLAY_OPT:
        query = 'Insert into Play values("{}","{}",{},"{}");'.format(
            obj['UserId'],
            obj['GameName'],
            obj['Time_length'],
            obj['Proficiency']
        )
    elif option == BSD_OPT:
        query = 'Insert into Based values("{}","{}");'.format(
            obj['GameName'],
            obj['Initial']
        )
    conn.execute(query)
    conn.close()


def delete_entity(name: str, option: int):
    conn = db.connect()
    query = None
    if option == GAME_OPT:  # game
        query = 'Delete From Game where GameName="{}";'.format(name)
    elif option == DEV_OPT:  # developer
        query = 'Delete From Developer where DevName="{}";'.format(name)
    elif option == PUB_OPT:  # publisher
        query = 'Delete From Publisher where PubName="{}";'.format(name)
    elif option == PLAT_OPT:  # platform
        query = 'Delete From Platform where Initial="{}";'.format(name)
    elif option == USER_OPT:  # user
        query = 'Delete from User where UserId = "{}";'.format(name)
    conn.execute(query)
    conn.close()


def delete_relationship(obj, option):
    conn = db.connect()
    query = None
    if option == UP_OPT:  # use platform
        query = 'Delete from UsePlatform where UserId = "{}" and Initial = "{}";'\
            .format(obj['UserId'], obj['Initial'])
    elif option == PLAY_OPT:  # play
        query = 'Delete from Play where UserId = "{}" and GameName = "{}" ;'\
            .format(obj['UserId'], obj['GameName'])
    elif option == BSD_OPT:  # based
        query = 'Delete From Based where GameName="{}" and Initial="{}";'\
            .format(obj['GameName'], obj['Initial'])
    conn.execute(query)
    conn.close()


# update_query
def update_game(game):
    """
    update game
    Args:
        game (dic): game
    """
    conn = db.connect()
    query = 'Update Game set ReleaseYear = {}, Genre = "{}", PubName = "{}", NA_Sales = {}, EU_Sales = {}, JP_Sales = {}, Global_Sales = {}, User_Score = {}, User_Count = {},DevName = "{}", Rating = "{}" where GameName = "{}";'.format(game['ReleaseYear'],game['Genre'],game['PubName'],game['NA_Sales'],game['EU_Sales'],game['JP_Sales'],game['Global_Sales'],game['User_Score'],game['User_Count'],game['DevName'],game['Rating'],game['GameName'])
    conn.execute(query)
    conn.close()


def update_developer(developer):
    """
    update developer
    Args:
        developer (dic)
    """
    conn = db.connect()
    query = 'Update Developer set Active = {}, City = "{}", Country = "{}", EstablishTime = {}, Notable_games = "{}", Notes = "{}" where DevName = "{}";'.format(developer['Active'],developer['City'],developer['Country'],developer['EstablishTime'],developer['Notable_games'],developer['Notes'],developer['DevName'])
    conn.execute(query)
    conn.close()


def update_publisher(publisher):
    """
    update publisher
    Args:
        publisher (dic)
    """
    conn = db.connect()
    query = 'Update Publisher set Headquarters="{}",EstablishTime = {}, Notable_games = "{}", Notes = "{}" where PubName = "{}";'.format(publisher['Headquarters'],publisher['EstablishTime'],publisher['Notable_games'],publisher['Notes'],publisher['PubName'])
    conn.execute(query)
    conn.close()


def update_platform(platform):
    """
    update platform
    Args:
        platform (dic)
    """
    conn = db.connect()
    query = 'Update Platform set FullName = "{}", Manufacturer = "{}", Num_JA_EU_US = {} where Initial = "{}";'.format(platform['FullName'],platform['Manufacturer'],platform['Num_JA_EU_US'],platform['Initial'])
    conn.execute(query)
    conn.close()


def update_user(user):
    """
    update user
    Args:
        user (dic)
    """
    conn = db.connect()
    query = 'Update User set Full_name = "{}", First_name = "{}",Last_name = "{}", Gender = "{}", Age = {}, Preference = "{}",Password = "{}" where UserId = "{}";'.format(user['Full_name'],user['First_name'],user['Last_name'],user['Gender'],user['Age'],user['Preference'],user['Password'],user['UserId'])
    conn.execute(query)
    conn.close()


def update_play(play):
    """
    update play
    Args:
        play (dic)
    """
    conn = db.connect()
    query = 'Update Play set Time_length = {}, Proficiency = "{}" where UserId = "{}" and GameName = "{}";'.format(play['Time_length'],play['Proficiency'],play['UserId'],play['GameName'])
    conn.execute(query)
    conn.close()