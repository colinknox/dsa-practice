def is_palindrome(word):
    original_word = word.copy()
    if len(word) == 0:
        return word
    


assert is_palindrome("") == True
assert is_palindrome("a") == True
assert is_palindrome("abba") == True
assert is_palindrome("racecar") == True
assert is_palindrome("ab") == False
assert is_palindrome("abca") == False
print("All palindrome tests passed!")