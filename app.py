import sqlite3


def register_user(name, weight):
    connection = sqlite3.connect('camp.db')
    cursor = connection.cursor()
    sql = f"insert into users (name, weight) VALUES (?, ?)"
    user_info = (name, weight)
    cursor.execute(sql, user_info)
    connection.commit()
    connection.close()


def display_user_weight():
    connection = sqlite3.connect('camp.db')

    cursor = connection.cursor()

    sql = f"SELECT * FROM users"

    query_result = cursor.execute(sql)
    user_info = query_result.fetchall()

    return user_info


def 終了する関数実行():
    return


def main():

    command = input('command? > ')
    if command == 'register':
        name = input('名前は？ > ')
        weight = input('体重は？ > ')
        register_user(name, weight)

    elif command == 'display':
        user_info = display_user_weight()
        for user in user_info:
            print(f'名前:{user[0]}, 体重:{user[1]}kg')

    # elif command == 'q':
    #     終了する関数実行()



if __name__ == '__main__':
    main()