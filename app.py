import sqlite3
import sys


def record_user_info(name, weight):
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


def exit_exe():
    print('Bye.')
    sys.exit()  # 処理は終了できるがこれでいいのか？


def main():

    command = input('command ? > ')
    if command == 'record':
        name = input('名前は？ > ')
        weight = input('体重は？ > ')
        record_user_info(name, weight)

    elif command == 'display':
        user_info = display_user_weight()
        for user in user_info:
            print(f'名前:{user[0]}, 体重:{user[1]}kg')

    elif command == 'q':
         exit_exe()



if __name__ == '__main__':
    main()