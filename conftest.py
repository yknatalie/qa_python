import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.books_genre = {"Аэлита": "Фантастика", "Мгла": "Ужасы", "Шерлок Холмс": "Детективы",
                             "Карлсон": "Мультфильмы", "Покровские ворота": "Комедии"}
    return collector


@pytest.fixture
def collector_with_favorites(collector):
    collector_with_favorites = collector
    collector_with_favorites.favorites = ["Покровские ворота", 'Шерлок Холмс']
    return collector_with_favorites
