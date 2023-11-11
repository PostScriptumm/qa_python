from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # проверяем добавление уже существующих в словаре книг и книг с названием > 40 символов
    @pytest.mark.parametrize('name', ['Aladdin', 'Eta kniga soderzhit v nazvanii 41 simvol!'])
    def test_add_new_book_add_no_valid_name(self, name, only_books):
        collector = BooksCollector()
        collector.books_genre = only_books
        collector.add_new_book(name)
        assert collector.get_books_genre() == {'Spacebred Generations': '', 'The Shining': '', 'The Bourne Identity': '',
                                               'Aladdin': '', 'Tartuffe': ''}

    # проверяем установку жанра для книги
    def test_set_book_genre_set_horror_for_book(self, only_books):
        collector = BooksCollector()
        collector.books_genre = only_books
        collector.set_book_genre('The Shining', 'Ужасы')
        assert collector.get_book_genre('The Shining') == 'Ужасы'

    # проверяем установку отсутсвующего в списке жанра и отсутсвующее название книги
    @pytest.mark.parametrize('name, genre', [['Aladdin', 'Science'], ['The Arrival', 'Фантастика']])
    def test_set_book_genre_set_miss_genre_and_book_name(self, name, genre, only_books):
        collector = BooksCollector()
        collector.books_genre = only_books
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == {'Spacebred Generations': '', 'The Shining': '', 'The Bourne Identity': '',
                                               'Aladdin': '', 'Tartuffe': ''}

    # проверяем возврат книг по жанру "Фантастика"
    def test_get_books_with_specific_genre_get_book_fantastic(self, filled_books_genre):
        collector = BooksCollector()
        collector.books_genre = filled_books_genre
        assert collector.get_books_with_specific_genre('Фантастика') == ['Spacebred Generations']

    # проверяем возврат книг для детей
    def test_get_books_for_children_get_get_books_not_horror_and_detective(self, filled_books_genre):
        collector = BooksCollector()
        collector.books_genre = filled_books_genre
        assert collector.get_books_for_children() == ['Spacebred Generations', 'Aladdin', 'Tartuffe']

    # проверяем добавление книги в избранное из списка books_genre
    def test_add_book_in_favorites_add_new_book_from_books_genre(self, filled_books_genre):
        collector = BooksCollector()
        collector.books_genre = filled_books_genre
        collector.add_book_in_favorites('Tartuffe')
        assert 'Tartuffe' in collector.get_list_of_favorites_books()

    # проверяем повторное добавление книги в избранное из списка books_genre
    def test_add_book_in_favorites_add_old_book_from_books_genre(self, filled_books_genre):
        collector = BooksCollector()
        collector.books_genre = filled_books_genre
        collector.add_book_in_favorites('Tartuffe')
        collector.add_book_in_favorites('Tartuffe')
        assert len(collector.get_list_of_favorites_books()) == 1

    # проверяем добавление книги в избранное отсутсвующей в списке books_genre
    def test_add_book_in_favorites_add_miss_book(self, filled_books_genre):
        collector = BooksCollector()
        collector.books_genre = filled_books_genre
        collector.add_book_in_favorites('Pinocchio')
        assert collector.get_list_of_favorites_books() == []

    # проверяем удаление добавленной книги из списка избранного
    def test_delete_book_from_favorites_book_in_favorites(self, filled_favorites):
        collector = BooksCollector()
        collector.favorites = filled_favorites
        collector.delete_book_from_favorites('Aladdin')
        assert collector.get_list_of_favorites_books() == ['Spacebred Generations', 'The Bourne Identity']

    # проверяем удаление отсутствующей книги из списка избранного
    def test_delete_book_from_favorites_book_not_in_favorites(self, filled_favorites):
        collector = BooksCollector()
        collector.favorites = filled_favorites
        collector.delete_book_from_favorites('Pinocchio')
        assert collector.get_list_of_favorites_books() == ['Spacebred Generations', 'The Bourne Identity', 'Aladdin']
