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

1. TestBooksCollector - ����� ������������ ����� ������, �������� �� ��������� ���� ���������� BooksCollector

2. test_add_new_book_add_two_books � �������� ���������� ���� ���� � ������� books_genre. 

3. test_add_new_book_add_valid_name - �������� ��������� ���������� ���� � ������� books_genre
- ����� �������� �����, ������������ ������� �������� 40 ��������
- ����� �������� �����, ������������ ������� �������� 1 ������

4. test_add_new_book_add_no_valid_name � �������� ��������� ���������� ���� � ������� books_genre
- ������ �������� �����, ������������ ������� ������ 40 ��������
- ������ �������� �����, ������������ �� �������� ��������
- ������ �������� �����, ������� ��� ������������ � ������� books_genre

5. test_set_book_genre_set_genre_for_book � ��������� ��������� ����� ��� ����� � ������� books_genre

6. test_set_book_genre_set_miss_genre � ���������, ��� ����� ������ ���������� ����, �������� ��� � ������ genre

7. test_get_books_with_specific_genre_get_book_with_genre � ��������� ������� ���� �� ����� �����������

8. test_get_books_for_children_get_get_books_not_horror_and_detective � ��������� ������� ���� �� ������� books_genre ��� ���� � ������� ������������ � ������ genre_age_rating

9. test_add_book_in_favorites_add_new_book_from_books_genre � ��������� ���������� ���� � ������ favorites

10. test_add_book_in_favorites_add_old_and_miss_books
� ���������, ��� ������ �������� ����� � ������ favorites �������� 
� ���������, ��� ������ �������� ����� � ������ favorites, ���� � ��� � ������� books_genre

11. test_delete_book_from_favorites_book_in_favorites � ��������� �������� ����� �� ������ favorites

12. test_delete_book_from_favorites_book_not_in_favorites � ���������, ��� �� ������� favorites ������ �� ����������, ���� �� �������� ������� �� ���� �����, ������� ��� ���

13. ������ get_books_genre, get_list_of_favorites_books - ������������ � ������������ ������, ��������� �������� �� ��������� 