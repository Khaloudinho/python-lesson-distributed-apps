# Input : 42 51
# Output : 43 45 47 49 51

def get_odd_numbers_between_two_numbers(nb1, nb2):
    output = []

    if nb1 % 2 == 0:
        nb1 += 1

    while nb1 <= nb2:
        output.append(nb1)
        nb1 += 2

    return output

print(get_odd_numbers_between_two_numbers(4, 13))
print(get_odd_numbers_between_two_numbers(42, 51))
print(get_odd_numbers_between_two_numbers(-1, 5))


