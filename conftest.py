import pytest


@pytest.fixture  # фикстура, которая возвращает словарь в формате {книга:''}
def only_books():
    only_books = {'Spacebred Generations': '',
                  'The Shining': '',
                  'The Bourne Identity': '',
                  'Aladdin': '',
                  'Tartuffe': ''}
    return only_books


@pytest.fixture  # фикстура, которая возвращает словарь в формате {книга:жанр}
def filled_books_genre():
    filled_books_genre = {'Spacebred Generations': 'Фантастика',
                          'The Shining': 'Ужасы',
                          'The Bourne Identity': 'Детективы',
                          'Aladdin': 'Мультфильмы',
                          'Tartuffe': 'Комедии'}
    return filled_books_genre


@pytest.fixture  # фикстура, которая возвращает список избранных книг
def filled_favorites():
    filled_favorites = ['Spacebred Generations', 'The Bourne Identity', 'Aladdin']
    return filled_favorites
