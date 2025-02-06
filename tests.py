import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_new_book_added(self, collector):
        collector.add_new_book("Война и Мир")
        assert "Война и Мир" in collector.books_genre

    @pytest.mark.parametrize("length", ["Г", 'ГамарджобаГамарджоба',
                                        'ГамарджобаГамарджобаГамарджобаГамарджоба'])
    def test_add_new_book_valid_length(self, length):
        new_collector = BooksCollector()
        new_collector.add_new_book(length)
        assert length in new_collector.books_genre

    @pytest.mark.parametrize("length", ["", 'ГамарджобаГамарджобаГамарджобаГамарджобаГамар',
                                        "ГамарджобаГамарджобаГамарджобаГамарджобаГ"])
    def test_add_new_book_invalid_length(self, length):
        new_collector = BooksCollector()
        new_collector.add_new_book(length)
        assert not length in new_collector.books_genre

    def test_add_new_book_value_is_empty_string(self, collector):
        collector.add_new_book("Мастер и Маргарита")
        assert collector.books_genre["Мастер и Маргарита"] == ''

    def test_set_book_genre_genre_is_set(self, collector):
        collector.set_book_genre("Карлсон", "Детективы")
        assert collector.books_genre['Карлсон'] == "Детективы"

    def test_set_book_genre_not_existing_name_false(self, collector):
        collector.set_book_genre("Аляска", "Детективы")
        assert not "Аляска" in collector.books_genre

    def test_set_book_genre_invalid_genre(self, collector):
        collector.set_book_genre("Карлсон", "Анимэ")
        assert not collector.books_genre["Карлсон"] == "Анимэ"

    def test_get_book_genre_true(self, collector):
        genre = collector.get_book_genre("Аэлита")
        assert genre == "Фантастика"

    def test_get_books_with_specific_genre_true(self, collector):
        books = collector.get_books_with_specific_genre("Фантастика")
        assert books == ["Аэлита"]

    def test_get_books_genre_true(self, collector):
        books_genre = collector.get_books_genre()
        assert books_genre == collector.books_genre

    def test_get_books_for_children_no_adult_genres(self, collector):
        books_for_children = collector.get_books_for_children()
        assert not "Ужасы" in books_for_children and "Детективы" not in books_for_children

    def test_add_book_in_favorites_negative_book_added_two_times(self, collector_with_favorites):
        collector_with_favorites.add_book_in_favorites("Покровские ворота")
        assert collector_with_favorites.favorites.count("Покровские ворота") == 1

    def test_add_book_in_favorites_not_exist(self, collector):
        collector.add_book_in_favorites("Смарт")
        assert not "Смарт" in collector.favorites

    def test_delete_book_from_favorites(self, collector_with_favorites):
        collector_with_favorites.delete_book_from_favorites("Шерлок Холмс")
        assert "Шерлок Холмс" not in collector_with_favorites.favorites

    def test_get_list_of_favorites_books_true(self, collector_with_favorites):
        favorites = collector_with_favorites.get_list_of_favorites_books()
        assert favorites == collector_with_favorites.favorites
