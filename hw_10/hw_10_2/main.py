def first_word(text):
    filtered_text = text.replace(".", " ")
    filtered_text = filtered_text.replace(",", " ")
    words = filtered_text.split(" ")
    for word in words:
        if word:
            return word

    return None


assert first_word("Hello world") == "Hello", "Test1"
assert first_word("greetings, friends") == "greetings", "Test2"
assert first_word("don't touch it") == "don't", "Test3"
assert first_word(".., and so on ...") == "and", "Test4"
assert first_word("hi") == "hi", "Test5"
assert first_word("Hello.World") == "Hello", "Test6"
print("OK")
