import os
import time
import random
import datetime
import requests
import json
import csv
import sqlite3
import pandas as pd
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class КНИГА:
    def __init__(self, title, author, publication_year, isbn, genre, pages):
        self.title = title  # Название
        self.author = author  # Автор
        self.publication_year = publication_year  # Год издания
        self.isbn = isbn  # ISBN
        self.genre = genre  # Жанр
        self.pages = pages  # Количество страниц

    def __str__(self):
        '''
        Возвращает строковое представление книги
        :return:
        '''
        return f"{self.title} by {self.author} ({self.publication_year})"

    def get_summary(self):
        '''
        Возвращает краткое описание книги
        :return:
        '''
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.publication_year}"

class БИБЛИОТЕКА_2_0:
    def __init__(self):
        # Создаем пустой список книг
        self.books = []

    # Добавляем книгу в библиотеку
    def add_book(self, book):
        self.books.append(book)

    def find_books_by_author(self, author):
        '''
        Возвращает список книг, написанных указанным автором
        :param author:
        :return:
        '''
        return [book for book in self.books if book.author == author]

    def find_books_published_after(self, year):
        '''
        Возвращает список книг, выпущенных после указанного года
        '''
        return [book for book in self.books if book.publication_year>year]

    def find_books_by_isbn(self, isbn):
        '''
        Возвращает список книг, выпущенных после указанного года
        '''
        return [book for book in self.books if book.isbn==isbn]

    def find_books_by_genre(self, genre):
        '''
        Возвращает список книг, выпущенных после указанного года
        '''
        return [book for book in self.books if book.genre==genre]

    def find_books_by_pages(self, pages):
        '''
        Возвращает список книг, выпущенных после указанного года
        '''
        return [book for book in self.books if book.pages==pages]

    def find_books_by_title(self, title):
        '''
        Возвращает список книг, выпущенных после указанного года
        '''
        return [book for book in self.books if book.title == title]

    def get_total_pages(self):
        return sum([book.pages for book in self.books])

    def get_genres(self):
        return list(set([book.genre for book in self.books]))


class УНИВЕРСАЛЬНОЕ_ЧТЕНИЕ_ФАЙЛА:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def read_lines(self):
        with open(self.filename, 'r') as file:
            return file.readlines()

    def read_json(self):
        import json
        with open(self.filename, 'r') as file:
            return json.load(file)

    def read_csv(self):
        import csv
        with open(self.filename, 'r') as file:
            return csv.reader(file)

    def read_excel(self):
        return pd.read_excel(self.filename)

    def read_sql(self):
        '''
        Чтение SQL файла
        :return:
        '''
        import sqlite3
        with sqlite3.connect(self.filename) as connection:
            return pd.read_sql_query("SELECT * FROM table", connection)

    def read_xml(self):
        '''
        Чтение XML файла
        :return:
        '''
        import xml.etree.ElementTree as ET
        tree = ET.parse(self.filename)
        root = tree.getroot()
        return root

    def read_yaml(self):
        '''
        Чтение YAML файла
        :return:
        '''
        import yaml
        with open(self.filename, 'r') as file:
            return yaml.load(file, Loader=yaml.FullLoader)

    def read_pickle(self):
        import pickle
        with open(self.filename, 'rb') as file:
            return pickle.load(file)

    def read_word(self):
        import docx
        return docx.Document(self.filename)

    def read_image(self):
        from PIL import Image
        return Image.open(self.filename)


def CREAT3E_sample_():
    # Создаем библиотеку
    БИБЛИОТЕКА = БИБЛИОТЕКА_2_0()
    book1 = КНИГА(
        "THE BOOK 1",
        "John. T",
        1995,
        "8274827611",
        "Fiction",
        220)
    book2 = КНИГА(
        "THE BOOK 2",
        "L.L. Horsev",
        "до н эры!!!",
        "9876543210",
        "Fiction",
        280)
    book3 = КНИГА(
        "NOU NAME",
        "G.G. Irooskf",
        2020,
        "5432109876",
        "Dystopian",
        320)
    book4 = КНИГА(
        "OKAY BOOK",
        "T.T. Orlov",
        2006,
        "5442449876",
        "Detective",
        250)
    book5 = КНИГА(
        "TAYLER",
        "-",
        2010,
        "8787319875",
        "Detective",
        500)
    book6 = КНИГА(
        "TAYLER2",
        "-",
        2014,
        "8799319875",
        "Detective",
        650)
    БИБЛИОТЕКА.add_book(book1)
    БИБЛИОТЕКА.add_book(book2)
    БИБЛИОТЕКА.add_book(book3)
    БИБЛИОТЕКА.add_book(book4)
    БИБЛИОТЕКА.add_book(book5)
    БИБЛИОТЕКА.add_book(book6)
    return БИБЛИОТЕКА

def main():
    # Создаем приложение PyQt
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Библиотека 2.0')
    # Создаем библиотеку и добавляем книги
    БИБЛИОТЕКА = CREAT3E_sample_()
    # Создаем макет для отображения книг
    layout = QVBoxLayout()
    # Выводим книги по автору
    author_label = QLabel("Books by John. T:")
    layout.addWidget(author_label)

    for book in БИБЛИОТЕКА.find_books_by_author("John. T"):
        book_label = QLabel(
            str(book))
        # Добавляем книгу на макет
        layout.addWidget(book_label)
    # Выводим книги, выпущенные после 1950 года
    year_label = (
        QLabel("Books published after 1950:"))
    layout.addWidget(year_label)
    for book in БИБЛИОТЕКА.find_books_published_after(1950):
        book_label = QLabel(str(book))
        # Добавляем книгу на макет
        layout.addWidget(book_label)
    # Выводим общее количество страниц
    total_pages_label = QLabel(f"Total Pages in Library: {БИБЛИОТЕКА.get_total_pages()}")
    layout.addWidget(total_pages_label)
    # Выводим жанры
    genres_label = QLabel(f"Genres in Library: {', '.join(БИБЛИОТЕКА.get_genres())}")
    layout.addWidget(genres_label)
    # Добавляем макет на окно
    for i in range(10):
        dummy_label = QLabel(f"Dummy Label {i}")
        layout.addWidget(dummy_label)
    # Добавляем макет на окно
    window.setLayout(layout)
    # Отображаем окно
    window.show()
    # Запускаем приложение
    sys.exit(app.exec())

if __name__ == "__main__":
    # Запускаем программу
    time.sleep(1)
    main()
    time.sleep(1)
