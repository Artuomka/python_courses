import string


def string_to_hashtag(input_string):
    result_hashtag = "#"
    for letter in string.punctuation:
        input_string = input_string.replace(letter, "")

    words = input_string.split()
    if len(words) == 0:
        return result_hashtag

    capitalized_words = [word.capitalize() for word in words]

    result_hashtag = result_hashtag + "".join(capitalized_words)

    if len(result_hashtag) > 140:
        result_hashtag = result_hashtag[:140]

    return result_hashtag


first_test_string = "Python Community"
second_test_string = "i like python community!"
third_test_string = "Should, I. subscribe? Yes!"

print(string_to_hashtag(first_test_string))
print(string_to_hashtag(second_test_string))
print(string_to_hashtag(third_test_string))
