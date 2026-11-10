def reverse(string):
    if len(string) == 0:
        return ""
    return reverse(string[1:]) + string[0]

assert reverse("sony") == "ynos"
assert reverse("department") == "tnemtraped"
assert reverse("racecar") == "racecar"
assert reverse("n") == "n"
assert reverse("") == ""
print("Reverse function test successful.")