from books.forms import BookForm

class TestBookForm:
    def test_form(self):
        empty_form = BookForm(data={})
        assert empty_form.is_valid() is False, 'Should be invalid without data'

        filled_form = BookForm(data={'name': 'The Magic Book', 'rating': '5'})
        assert filled_form.is_valid() is True, 'Should be valid with data'
