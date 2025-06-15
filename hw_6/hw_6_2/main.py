def convert_time_format(seconds):
    if seconds < 0 or seconds > 8640000:
        print("Wrong input forman")
        return

    minute = 60
    hour = minute * 60
    day = hour * 24

    days_in_input, days_reminder = divmod(seconds, day)
    hours_in_input, hours_reminder = divmod(days_reminder, hour)
    minutes_in_input, seconds_reminder = divmod(hours_reminder, minute)

    days_string = "днів"

    if days_in_input % 10 == 1 and days_in_input % 100 != 11:
        days_string = "день"
    elif (
        days_in_input % 10 >= 2
        and days_in_input % 10 <= 4
        and (days_in_input % 100 < 10 or days_in_input % 100 >= 20)
    ):
        days_string = "дні"

    return f"{days_in_input} {days_string}, {str(hours_in_input).zfill(2)}:{str(minutes_in_input).zfill(2)}:{str(seconds_reminder).zfill(2)}"


test_time_1 = 0
test_time_2 = 224930
test_time_3 = 466289
test_time_4 = 950400
test_time_5 = 1209600
test_time_6 = 1900800
test_time_7 = 8639999
test_time_8 = 22493
test_time_9 = 7948799

print(convert_time_format(test_time_1))
print(convert_time_format(test_time_2))
print(convert_time_format(test_time_3))
print(convert_time_format(test_time_4))
print(convert_time_format(test_time_5))
print(convert_time_format(test_time_6))
print(convert_time_format(test_time_7))
print(convert_time_format(test_time_8))
print(convert_time_format(test_time_9))
