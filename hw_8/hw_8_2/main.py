def is_palindrome(text):
    clear_text = [letter.lower() for letter in text if letter.isalnum()]
    reversed_clear_text = clear_text.copy()
    reversed_clear_text.reverse()
    return "".join(clear_text) == "".join(reversed_clear_text)


assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test1"
assert is_palindrome("0P") == False, "Test2"
assert is_palindrome("a.") == True, "Test3"
assert is_palindrome("aurora") == False, "Test4"
print("ОК")
