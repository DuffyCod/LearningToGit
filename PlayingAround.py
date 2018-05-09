def cat_dog(string):
    dog = string.count("dog")
    cat = string.count("cat")
    return dog == cat

print(cat_dog("catdog"))
print(cat_dog("catcat"))
print(cat_dog("1cat1cadodog"))