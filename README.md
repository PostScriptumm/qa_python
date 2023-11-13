# qa_python_4

Описание проекта:

Класс BooksCollector содержит:
Словарь books_genre, куда можно добавить пару Название книги: Жанр книги.
Список favorites, который содержит избранные книги.
Список genre, который содержит доступные жанры.
Список genre_age_rating, который содержит жанры с возрастным рейтингом.
Набор методов для работы со словарем books_genre и списком favorites:
add_new_book — добавляет новую книгу в словарь без указания жанра. Название книги может содержать максимум 40 символов. Одну и ту же книгу можно добавить только один раз.
set_book_genre — устанавливает жанр книги, если книга есть в books_genreи её жанр входит в списокgenre.
get_book_genre — выводит жанр книги по её имени.
get_books_with_specific_genre— выводит список книг с определённым жанром.
get_books_genre — выводит текущий словарь books_genre.
get_books_for_children — возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга.
add_book_in_favorites — добавляет книгу в избранное. Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя.
delete_book_from_favorites — удаляет книгу из избранного, если она там есть.
get_list_of_favorites_books — получает список избранных книг.


Для написания юнит-тестов используется библиотека pytest

conftest.py (файл с фикстурами):

filled_books_genre - возвращает словарь в формате {книга:жанр}
filled_favorites - возвращает список избранных книг

test.py (файл с юнит-тестами):

TestBooksCollector - класс объединяющий набор тестов, которыми мы покрываем наше приложение BooksCollector

test_add_new_book_add_two_books – проверка добавления двух книг в словарь books_genre. 

test_add_new_book_add_valid_name - проверка валидации добавления книг в словарь books_genre
- можно добавить книгу, наименование которой содержит 40 символов
- можно добавить книгу, наименование которой содержит 1 символ

test_add_new_book_add_no_valid_name – проверка валидации добавления книг в словарь books_genre
- нельзя добавить книгу, наименование которой больше 40 символов
- нельзя добавить книгу, наименование не содержит символов
- нельзя добавить книгу, которая уже присутствует в словаре books_genre

- test_set_book_genre_set_genre_for_book – проверяем установку жанра для книги в словаре books_genre

test_set_book_genre_set_miss_genre – проверяем, что книге нельзя установить жанр, которого нет в списке genre

test_get_books_with_specific_genre_get_book_with_genre – проверяем возврат книг по жанру «Фантастика»

test_get_books_for_children_get_get_books_not_horror_and_detective – проверяем возврат книг из словаря books_genre без книг с жанрами находящимися в списке genre_age_rating

test_add_book_in_favorites_add_new_book_from_books_genre – проверяем добавление книг в список favorites

test_add_book_in_favorites_add_old_and_miss_books
– проверяем, что нельзя добавить книгу в список favorites повторно 
– проверяем, что нельзя добавить книгу в список favorites, если её нет в словаре books_genre

test_delete_book_from_favorites_book_in_favorites – проверяем удаление книги из списка favorites

test_delete_book_from_favorites_book_not_in_favorites – проверяем, что со списком favorites ничего не происходит, если мы пытаемся удалить из него книгу, которой там нет

Методы get_books_genre, get_list_of_favorites_books - используются в существующих тестах, отдельной проверки не требуется 