import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # добавление двух новых книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Интерстеллар')
        assert len(collector.get_books_genre()) == 2

    # добавление книги без жанра
    @pytest.mark.parametrize('name_book', ['Гордость и предубеждение и зомби', 'Живые мертвецы'])
    def test_book_has_no_genre_add_book_without_genre(self, name_book):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        assert collector.get_book_genre(name_book) == ''

    # добававление книги без названия
    def test_add_new_book_add_book_without_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    # добавление книги с названием более 41 символов(такая книга реально существует)
    def test_add_new_book_add_big_book_title(self):
        collector = BooksCollector()
        collector.add_new_book(
            'Рассвет полночи, или Созерцание славы, торжества и мудрости порфироносных, браноносных и мирных гениев России с последованием дидактических, эротических и других разного рода в стихах и прозе опытов Семена Боброва')
        assert len(collector.get_books_genre()) == 0

    # установка книге жанра и получение жанра книги по имени
    @pytest.mark.parametrize('name_book', ['Гордость и предубеждение и зомби', 'Живые мертвецы'])
    def test_set_book_genre_set_and_get_book_genre(self, name_book):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, 'Ужасы')
        assert collector.books_genre.get(name_book) == 'Ужасы'

    # вывод списка книг с опредленном жанром
    @pytest.mark.parametrize('name_book1, name_book2', [['Гордость и предубеждение и зомби', 'Повелитель стихий'],['Живые мертвецы', 'Интерстеллар']])
    def test_get_books_with_specific_genre_browsing_list_books(self, name_book1, name_book2):
        collector = BooksCollector()
        collector.add_new_book(name_book1)
        collector.add_new_book(name_book2)
        collector.set_book_genre(name_book1, 'Ужасы')
        collector.set_book_genre(name_book2, 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == [name_book2]

    # получить словарь books_genre
    @pytest.mark.parametrize('name_book1, name_book2', [['Гордость и предубеждение и зомби', 'Повелитель стихий'],['Живые мертвецы', 'Интерстеллар']])
    def test_get_books_genre_get_books(self, name_book1, name_book2):
        collector = BooksCollector()
        collector.add_new_book(name_book1)
        collector.add_new_book(name_book2)
        collector.set_book_genre(name_book1, 'Ужасы')
        collector.set_book_genre(name_book2, 'Фантастика')
        assert collector.get_books_genre() == {name_book1: 'Ужасы',
                                               name_book2: 'Фантастика'}

    # возвратить книги, подходящие детям
    @pytest.mark.parametrize('name_book1, name_book2', [['Гордость и предубеждение и зомби', 'Повелитель стихий'],['Живые мертвецы', 'Интерстеллар']])
    def test_get_books_for_children_get_books(self, name_book1, name_book2):
        collector = BooksCollector()
        collector.add_new_book(name_book1)
        collector.add_new_book(name_book2)
        collector.set_book_genre(name_book1, 'Ужасы')
        collector.set_book_genre(name_book2, 'Фантастика')
        assert collector.get_books_for_children() == [name_book2]

    # добавить книгу в Избранное и получить список избранных книг
    @pytest.mark.parametrize('name_book1, name_book2', [['Гордость и предубеждение и зомби', 'Повелитель стихий'],['Живые мертвецы', 'Интерстеллар']])
    def test_add_book_in_favorites_add_and_get_books_list(self, name_book1, name_book2):
        collector = BooksCollector()
        collector.add_new_book(name_book1)
        collector.add_new_book(name_book2)
        collector.set_book_genre(name_book1, 'Ужасы')
        collector.set_book_genre(name_book2, 'Фантастика')
        collector.add_book_in_favorites(name_book1)
        assert collector.get_list_of_favorites_books() == [name_book1]

    # удалить книгу из Избранного и получить список избранных книг
    @pytest.mark.parametrize('name_book1, name_book2', [['Гордость и предубеждение и зомби', 'Повелитель стихий'],['Живые мертвецы', 'Интерстеллар']])
    def test_delete_book_from_favorites_delete_and_get_books_list(self, name_book1, name_book2):
        collector = BooksCollector()
        collector.add_new_book(name_book1)
        collector.add_new_book(name_book2)
        collector.set_book_genre(name_book1, 'Ужасы')
        collector.set_book_genre(name_book2, 'Фантастика')
        collector.add_book_in_favorites(name_book1)
        collector.add_book_in_favorites(name_book2)
        collector.delete_book_from_favorites(name_book2)
        assert collector.get_list_of_favorites_books() == [name_book1]
