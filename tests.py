import pytest
from main import BooksCollector


books_list = [
    ['Дюна', 'Фантастика'],
    ['Оно', 'Ужасы'],
    ['Убийство в Восточном экспрессе', 'Детективы'],
    ['Король лев', 'Мультфильмы'],
    ['Трое в лодке, не считая собаки', 'Комедии']
    ]

safe_books = [
    ['Дюна', 'Фантастика'],
    ['Король лев', 'Мультфильмы'],
    ['Трое в лодке, не считая собаки', 'Комедии']
]    

restricted_books = [
    ['Оно', 'Ужасы'],
    ['Убийство в Восточном экспрессе', 'Детективы']
]

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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_added_new_book_do_not_have_genre(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер и Кубок огня'
        collector.add_new_book(book_name)
        book_genre = collector.get_book_genre(book_name)
        assert book_genre == ''


    def test_no_adding_new_book_with_name_length_more_than_40(self):
        collector = BooksCollector()
        collector.add_new_book('aaaaaaaaa aaaaaaaaa aaaaaaaaa aaaaaaaaa a')

        assert len(collector.get_books_genre()) == 0


    def test_no_adding_new_book_with_same_name(self):
        collector = BooksCollector()
        collector.add_new_book('Черновик')
        collector.add_new_book('Черновик')
        books_genre = collector.get_books_genre()

        assert len(books_genre) == 1 and 'Черновик' in books_genre


    @pytest.mark.parametrize('book_name, book_genre', books_list)
    def test_set_book_genre_if_genre_in_list_genre(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) in collector.genre

    @pytest.mark.parametrize('book_name, book_genre', books_list)
    def test_get_book_with_specific_genre_from_books_list(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        books_in_genre = collector.get_books_with_specific_genre(book_genre)

        assert book_name in books_in_genre

    @pytest.mark.parametrize('book_name, book_genre', safe_books)
    def test_get_books_for_children_from_safe_books_list(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        children_books = collector.get_books_for_children()
        assert book_name in children_books

    @pytest.mark.parametrize('book_name, book_genre', restricted_books)
    def test_books_for_children_not_get_from_age_rating_genre(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        children_books = collector.get_books_for_children()
        assert book_name not in children_books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга тайн')
        collector.add_book_in_favorites('Книга тайн')
        assert 'Книга тайн' in collector.favorites

    def test_deleting_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга тайн')
        collector.add_book_in_favorites('Книга тайн')
        collector.delete_book_from_favorites('Книга тайн')
        assert 'Книга тайн' not in collector.favorites

    


    

    
    



    