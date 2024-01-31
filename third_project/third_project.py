import tkinter as tk
import sqlite3

try:
    # Создание или подключение к базе данных
    conn = sqlite3.connect('people.db')
    c = conn.cursor()

    # Создание таблицы, если она не существует
    c.execute('''CREATE TABLE IF NOT EXISTS people
                 (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)''')

    # Заполнение таблицы данными из словаря при первом запуске
    c.execute("SELECT COUNT(*) FROM people")
    if c.fetchone()[0] == 0:
        people_data = [
            {'first_name': 'Иван', 'last_name': 'Иванов', 'age': 30},
            {'first_name': 'Петр', 'last_name': 'Петров', 'age': 25},
            {'first_name': 'Мария', 'last_name': 'Сидорова', 'age': 28}
        ]
        for person in people_data:
            c.execute("INSERT INTO people (first_name, last_name, age) VALUES (?, ?, ?)",
                      (person['first_name'], person['last_name'], person['age']))
        conn.commit()

    # Создание графического интерфейса Tkinter
    root = tk.Tk()
    root.title("Список людей")

    # Функция для получения и отображения списка людей
    def display_people():
        people_list.delete(0, tk.END)  # Очистка списка перед обновлением
        c.execute("SELECT * FROM people")
        for person in c.fetchall():
            full_name = f"{person[1]} {person[2]}, возраст: {person[3]}"
            people_list.insert(tk.END, full_name)

    # Создание и размещение виджетов Tkinter
    label = tk.Label(root, text="Список людей:")
    label.pack()

    people_list = tk.Listbox(root, width=40)
    people_list.pack()

    display_people()  # Отображение списка при запуске программы

    conn.close()  # Закрытие соединения с базой данных при выходе из программы

    root.mainloop()

except Exception as e:
    print(f"An error occurred: {e}")
