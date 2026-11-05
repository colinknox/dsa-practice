def reverse(string):
    if len(string) == 0:
        return ""
    return reverse(string[1:]) + string[0] 


assert reverse("") == ""
assert reverse("a") == "a"
assert reverse("cat") == "tac"
assert reverse("hello") == "olleh"
print("All reverse tests passed!")