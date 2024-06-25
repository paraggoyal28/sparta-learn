def check_gender(pin): 
    parts = pin.split('-')
    second_part = parts[1]
    second_part_first_digit = int(second_part[0])
    if(second_part_first_digit%2 == 0):
        print('female')
    else:
        print('male')
my_pin = '200101-3012345'
check_gender(my_pin)