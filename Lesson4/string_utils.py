class StringUtils:
    @staticmethod
    def is_palindrome(s: str) -> bool:
       
        return s == s[::-1]
    
    @staticmethod
    def reverse_string(s: str) -> str:
       
        return s[::-1]
