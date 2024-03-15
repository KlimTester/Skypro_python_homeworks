import pytest
from string_utils import StringUtils

class TestStringUtils:
    # Positive scenarios
    def test_is_palindrome_positive(self):
        assert StringUtils.is_palindrome("racecar") == True
    
    def test_is_palindrome_negative(self):
        assert StringUtils.is_palindrome("hello") == False
    
    def test_reverse_string_positive(self):
        assert StringUtils.reverse_string("hello") == "olleh"
    
    def test_reverse_string_numbers(self):
        assert StringUtils.reverse_string("12345") == "54321"
    
    # Negative scenarios
    def test_is_palindrome_empty_string(self):
        assert StringUtils.is_palindrome("") == True
    
    def test_is_palindrome_string_with_spaces(self):
        assert StringUtils.is_palindrome("  ") == True
    
    def test_is_palindrome_none(self):
        with pytest.raises(TypeError):
            StringUtils.is_palindrome(None)
    
    def test_reverse_string_empty_string(self):
        assert StringUtils.reverse_string("") == ""
    
    def test_reverse_string_string_with_spaces(self):
        assert StringUtils.reverse_string("  ") == "  "
    
    def test_reverse_string_none(self):
        with pytest.raises(TypeError):
            StringUtils.reverse_string(None)
