"""Defines all the functions related to the database"""
from app import db


# search_query
def show_game(condition=''):
    """Reads all Games 

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    query_results = conn.execute("Select * from Game " + condition + ";").fetchall()
    conn.close()
    game_list = []
    for result in query_results:
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
        game_list.append(item)
    return game_list


def show_developer():
    """Reads all Developers

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    query_results = conn.execute("Select * from Developer;").fetchall()
    conn.close()
    developer_list = []
    for result in query_results:
        item = {
            "DevName": result[0],
            "Active": result[1],
            "City": result[2],
            "Country": result[3],
            "EstablishTime": result[4],
            "Notable_games": result[5],
            "Notes": result[6],
        }
        developer_list.append(item)
    return developer_list


def show_publisher():
    """Reads all Publishers

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    query_results = conn.execute("Select * from Publisher;").fetchall()
    conn.close()
    publisher_list = []
    for result in query_results:
        item = {
            "PubName": result[0],
            "Headquarters": result[1],
            "EstablishTime": result[2],
            "Notable_games": result[3],
            "Notes": result[4],
        }
        publisher_list.append(item)
    return publisher_list


def show_platform():
    """Reads all Platforms

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    query_results = conn.execute("Select * from Platform;").fetchall()
    conn.close()
    platform_list = []
    for result in query_results:
        item = {
            "Initial": result[0],
            "FullName": result[1],
            "Manufacturer": result[2],
            "Num_JA_EU_US": result[3],
        }
        platform_list.append(item)
    return platform_list


def show_user():
    """Reads all Users

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    query_results = conn.execute("Select * from User;").fetchall()
    conn.close()
    user_list = []
    for result in query_results:
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
        user_list.append(item)
    return user_list


def show_use_platform():
    """Reads all UsePlatform

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    query_results = conn.execute("Select * from UsePlatform;").fetchall()
    conn.close()
    user_platform_list = []
    for result in query_results:
        item = {
            "UserId": result[0],
            "Initial": result[1],
        }
        user_platform_list.append(item)
    return user_platform_list


def show_play():
    """Reads all UsePlatform

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    query_results = conn.execute("Select * from Play;").fetchall()
    conn.close()
    play_list = []
    for result in query_results:
        item = {
            "UserId": result[0],
            "GameName": result[1],
            "Time_length": result[2],
            "Proficiency": result[3],
        }
        play_list.append(item)
    return play_list


def show_based():
    """Reads all Based

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    query_results = conn.execute("Select * from Based;").fetchall()
    conn.close()
    based_list = []
    for result in query_results:
        item = {
            "GameName": result[0],
            "Initial": result[1],
        }
        based_list.append(item)
    return based_list


def show_advanced_query1():
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


def show_advanced_query2():
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


# insert_query
def insert_game(game):
    """
    Insert new game
    Args:
        game (dic): game
    """

    conn = db.connect()
    query = 'Insert into Game values("{}",{},"{}","{}",{},{},{},{},{},{},"{}","{}");'.format(game['GameName'],game['ReleaseYear'],game['Genre'],game['PubName'],game['NA_Sales'],game['EU_Sales'],game['JP_Sales'],game['Global_Sales'],game['User_Score'],game['User_Count'],game['DevName'],game['Rating'])
    conn.execute(query)
    conn.close()


def insert_developer(developer):
    """
    Insert new developer
    Args:
        developer (dic)
    """
    conn = db.connect()
    query = 'Insert into Developer values("{}",{},"{}","{}",{},"{}","{}");'.format(developer['DevName'],developer['Active'],developer['City'],developer['Country'],developer['EstablishTime'],developer['Notable_games'],developer['Notes'])
    conn.execute(query)
    conn.close()


def insert_publisher(publisher):
    """
    Insert new publisher
    Args:
        publisher (dic)
    """
    conn = db.connect()
    query = 'Insert into Publisher values("{}","{}",{},"{}","{}");'.format(publisher['PubName'],publisher['Headquarters'],publisher['EstablishTime'],publisher['Notable_games'],publisher['Notes'])
    conn.execute(query)
    conn.close()


def insert_platform(platform):
    """
    Insert new platform
    Args:
        platform (dic)
    """
    conn = db.connect()
    query = 'Insert into Platform values("{}","{}","{}",{});'.format(platform['Initial'],platform['FullName'],platform['Manufacturer'],platform['Num_JA_EU_US'])
    conn.execute(query)
    conn.close()


def insert_user(user):
    """
    Insert new user
    Args:
        user (dic)
    """
    conn = db.connect()
    query = 'Insert into User values("{}","{}","{}","{}","{}",{},"{}","{}");'.format(user['UserId'],user['Full_name'],user['First_name'],user['Last_name'],user['Gender'],user['Age'],user['Preference'],user['Password'])
    conn.execute(query)
    conn.close()


def insert_use_platform(useplatform):
    """
    Insert new usePlatform
    Args:
        usePlatform (dic)
    """
    conn = db.connect()
    query = 'Insert into UsePlatform values("{}","{}");'.format(useplatform['UserId'],useplatform['Initial'])
    conn.execute(query)
    conn.close()


def insert_play(play):
    """Insert new play

    Args:
        play (dic)
    """
    conn = db.connect()
    query = 'Insert into Play values("{}","{}",{},"{}");'.format(play['UserId'],play['GameName'],play['Time_length'],play['Proficiency'])
    conn.execute(query)
    conn.close()


def insert_based(based):
    """
    Insert new based
    Args:
        based (dic)
    """
    conn = db.connect()
    query = 'Insert into Based values("{}","{}");'.format(based['GameName'], based['Initial'])
    conn.execute(query)
    conn.close()


# delete_query
def delete_game(gamename):
    """
    remove game
    Args:
        gamename (str)
    """
    conn = db.connect()
    query = 'Delete From Game where GameName="{}";'.format(gamename)
    conn.execute(query)
    conn.close()


def delete_developer(devname):
    """
    remove developer
    Args:
        devname (str)
    """
    conn = db.connect()
    query = 'Delete From Developer where DevName="{}";'.format(devname)
    conn.execute(query)
    conn.close()


def delete_publisher(pubname):
    """
    remove publisher
    Args:
        pubname (str)
    """
    conn = db.connect()
    query = 'Delete From Publisher where PubName="{}";'.format(pubname)
    conn.execute(query)
    conn.close()


def delete_Platform(initial):
    """ remove platform 
    Args:
        initial (str)
    """
    conn = db.connect()
    query = 'Delete From Platform where Initial="{}";'.format(initial)
    conn.execute(query)
    conn.close()

def delete_User(userId):
    """ remove user 
    Args:
        userId (str)
    """
    conn = db.connect()
    query = 'Delete from User where UserId = "{}";'.format(userId)
    conn.execute(query)
    conn.close()

def delete_UsePlatform(userId):
    """ remove useplatform
    Args:
        userId (str)
    """
    conn = db.connect()
    query = 'Delete from UsePlatform where UserId = "{}";'.format(userId)
    conn.execute(query)
    conn.close()


def delete_play(userId):
    """ remove play
    Args:
        userId (str)
    """
    conn = db.connect()
    query = 'Delete from Play where UserId = "{}";'.format(userId)
    conn.execute(query)
    conn.close()


def delete_based(gamename):
    """
    remove based
    Args:
        gamename (str)
    """
    conn = db.connect()
    query = 'Delete From Based where GameName="{}";'.format(gamename)
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