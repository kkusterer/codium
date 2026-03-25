numbers = input("string num: ")

digit_sum = sum(int(digit) for digit in numbers)

if digit_sum < 10:
    int_to_string = str(digit_sum)

    zero_in_beginging = "0"

    digit_count = len(str(numbers))

    print(zero_in_beginging ,digit_sum ,digit_count)

else:
    digit_count = len(numbers)

    print(digit_sum,digit_count)

