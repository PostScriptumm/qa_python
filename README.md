# qa_python_4

conftest.py (файл с фикстурами):

only_books - возвращает словарь в формате {книга:''}
filled_books_genre - возвращает словарь в формате {книга:жанр}
filled_favorites - возвращает список избранных книг

test.py (файл с юнит-тестами):

1. TestBooksCollector - класс объединяющий набор тестов, которыми мы покрываем наше приложение BooksCollector

2. test_add_new_book_add_two_books – проверка добавления двух книг в словарь books_genre. 

3. test_add_new_book_add_no_valid_name – проверка валидации добавления книг в словарь books_genre
- нельзя добавить книгу, наименование которой больше 40 символов
- нельзя добавить книгу, которая уже присутствует в словаре books_genre

4. test_set_book_genre_set_horror_for_book – проверяем установку жанра для книги в словаре books_genre

5. test_set_book_genre_set_miss_genre_and_book_name – проверяем валидацию при установке жанра книги
- нельзя установить жанр, которого нет в списке genre_age_rating
- нельзя установить жанр книге, которой нет в списке books_genre

6. test_get_books_with_specific_genre_get_book_fantastic – проверяем возврат книг по жанру «Фантастика»

7. test_get_books_for_children_get_get_books_not_horror_and_detective – проверяем возврат книг из словаря books_genre без книг с жанрами находящимися в списке genre_age_rating

8. test_add_book_in_favorites_add_new_book_from_books_genre – проверяем добавление книг в список favorites

9. test_add_book_in_favorites_add_old_book_from_books_genre – проверяем, что нельзя добавить книгу в список favorites повторно 

10. test_add_book_in_favorites_add_miss_book – проверяем, что нельзя добавить книгу в список favorites, если её нет в словаре books_genre

11. test_delete_book_from_favorites_book_in_favorites – проверяем удаление книги из списка favorites

12. test_delete_book_from_favorites_book_not_in_favorites – проверяем, что со списком favorites ничего не происходит, если мы пытаемся удалить из него книгу, которой там нет

13. Методы get_books_genre, get_list_of_favorites_books - используются в существующих тестах, отдельной проверки не требуется 

