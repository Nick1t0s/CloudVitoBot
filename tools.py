import sqlite3
class User:
    def __init__(self,username,photo,balance):
        self.username=username
        self.id=self.getMaxId()+1
        self.photo=photo
        self.balance=balance


    def getMaxId(self):
        with sqlite3.connect('my_database.db') as con:
            cur=con.cursor()
            cur.execute("SELECT MAX(id) FROM users;")
            res=cur.fetchall()[0]
            return res[0]

    def write(self):
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()
        # Устанавливаем соединение с базой данных
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()

        # Добавляем нового пользователя
        cursor.execute(f"INSERT INTO Users VALUES({self.id+1}, '{self.username}', {self.balance})")

        # Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()