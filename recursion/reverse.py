def reverse(word):
    if len(word) == 0:
        return ""
    return reverse(word[1:]) + word[0]

assert reverse("repair") == "riaper"
assert reverse("courier") == "reiruoc"
assert reverse("gusto") == "otsug"
assert reverse("i") == "i"
assert reverse("") == ""
print("Reverse test successful.")