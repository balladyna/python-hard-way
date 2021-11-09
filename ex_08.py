
formatter = " {} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I will write here",
    "something unexpected,",
    "but I don't know what!",
    "Maybe you have an idea?"
))