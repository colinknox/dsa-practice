def is_palindrome(word):
    if len(word) == 0:
        return word
    return is_palindrome(word[1:]) + word[0]

print(is_palindrome("limosss"))
# assert is_palindrome("limosss") == False
# assert is_palindrome("ram") == False
# assert is_palindrome("madam") == True
# assert is_palindrome("tattarrattat") == True
# assert is_palindrome("") == True
# print("All tests successful.")