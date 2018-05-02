def mobile_phone (color, brand, storage_space, size):
    phone = {
        'color':color,
        'brand':brand,
        'storage_space':storage_space,
        'size':size,
        }
    return phone

my_phone = mobile_phone ('white', 'LG', '22 gigs', '5.5 in')

other_phone = mobile_phone ('black', 'apple', '128 gigs', '6.6 in')

def display_phone(phone):
    for key, value in phone.items():
        print(key + ": " + value)
    print("\n")

display_phone(my_phone)
display_phone(other_phone)
