# qa_python_4

�������� �������:

����� BooksCollector ��������:
������� books_genre, ���� ����� �������� ���� �������� �����: ���� �����.
������ favorites, ������� �������� ��������� �����.
������ genre, ������� �������� ��������� �����.
������ genre_age_rating, ������� �������� ����� � ���������� ���������.
����� ������� ��� ������ �� �������� books_genre � ������� favorites:
add_new_book � ��������� ����� ����� � ������� ��� �������� �����. �������� ����� ����� ��������� �������� 40 ��������. ���� � �� �� ����� ����� �������� ������ ���� ���.
set_book_genre � ������������� ���� �����, ���� ����� ���� � books_genre� � ���� ������ � ������genre.
get_book_genre � ������� ���� ����� �� � �����.
get_books_with_specific_genre� ������� ������ ���� � ����������� ������.
get_books_genre � ������� ������� ������� books_genre.
get_books_for_children � ���������� �����, ������� �������� �����. � ����� ����� �� ������ ���� ����������� ��������.
add_book_in_favorites � ��������� ����� � ���������. ����� ������ ���������� � ������� books_genre. �������� �������� ����� � ��������� ������.
delete_book_from_favorites � ������� ����� �� ����������, ���� ��� ��� ����.
get_list_of_favorites_books � �������� ������ ��������� ����.


��� ��������� ����-������ ������������ ���������� pytest

conftest.py (���� � ����������):

filled_books_genre - ���������� ������� � ������� {�����:����}
filled_favorites - ���������� ������ ��������� ����

test.py (���� � ����-�������):

TestBooksCollector - ����� ������������ ����� ������, �������� �� ��������� ���� ���������� BooksCollector

test_add_new_book_add_two_books � �������� ���������� ���� ���� � ������� books_genre. 

test_add_new_book_add_valid_name - �������� ��������� ���������� ���� � ������� books_genre
- ����� �������� �����, ������������ ������� �������� 40 ��������
- ����� �������� �����, ������������ ������� �������� 1 ������

test_add_new_book_add_no_valid_name � �������� ��������� ���������� ���� � ������� books_genre
- ������ �������� �����, ������������ ������� ������ 40 ��������
- ������ �������� �����, ������������ �� �������� ��������
- ������ �������� �����, ������� ��� ������������ � ������� books_genre

- test_set_book_genre_set_genre_for_book � ��������� ��������� ����� ��� ����� � ������� books_genre

test_set_book_genre_set_miss_genre � ���������, ��� ����� ������ ���������� ����, �������� ��� � ������ genre

test_get_books_with_specific_genre_get_book_with_genre � ��������� ������� ���� �� ����� �����������

test_get_books_for_children_get_get_books_not_horror_and_detective � ��������� ������� ���� �� ������� books_genre ��� ���� � ������� ������������ � ������ genre_age_rating

test_add_book_in_favorites_add_new_book_from_books_genre � ��������� ���������� ���� � ������ favorites

test_add_book_in_favorites_add_old_and_miss_books
� ���������, ��� ������ �������� ����� � ������ favorites �������� 
� ���������, ��� ������ �������� ����� � ������ favorites, ���� � ��� � ������� books_genre

test_delete_book_from_favorites_book_in_favorites � ��������� �������� ����� �� ������ favorites

test_delete_book_from_favorites_book_not_in_favorites � ���������, ��� �� ������� favorites ������ �� ����������, ���� �� �������� ������� �� ���� �����, ������� ��� ���

������ get_books_genre, get_list_of_favorites_books - ������������ � ������������ ������, ��������� �������� �� ��������� 