# qa_python
### Тесты
1. **test_add_new_book_new_book_added** - добавляется новая книга
2. **test_add_new_book_invalid_length** - книга не добавляется если, длина имени не соответствует диапазону
(пустое, больше дипазона)
3. **test_add_new_book_value_is_empty_string** - при добавлении книги значение ключа в словаре - пустая строка

4. **test_set_book_genre_genre_is_set** - присваивает книжке жанр
5. **test_set_book_genre_not_existing_name_false** - нельзя установить жанр несуществующим книгам
6. **test_set_book_genre_invalid_genre** - жанр не присваивается, если такого жанра нет в списке жанров

7. **test_get_book_genre_true** - Получен жанр для переданной книжки

8. **test_get_books_with_specific_genre_true** - Получен список книг по жанру из словаря с книжками.

9. **test_get_books_genre_true** - Получен словарь books_genre

10. **test_get_books_for_children_no_adult_genres** - В списке книг для детей нет книг, жанр которых Детективы, Ужасы

11. **test_add_book_in_favotites_negative_book_added_two_times** - Проверка что книжку нельзя добавить два раза в Избранное
12. **test_add_book_in_favorites_not_exist**: проверяет, что нельзя добавить несуществующую книгу в избранное.

13. **test_delete_book_from_favorites** - Книга удаляется из избранного

14. **test_get_list_of_favorites_books_true** - Возвращается список избранного