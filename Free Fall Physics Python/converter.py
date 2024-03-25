def get_hight_conversion(user_answer, height):
    if user_answer == 'km':
        height *= 1000
    elif user_answer == 'cm':
        height /= 1000
    elif user_answer == "inch":
        height /=39.37
        height /= 1000
    elif user_answer == "foot":
        height /=3.28
    elif user_answer == "yard":
        height /=3.28
    elif user_answer == "mile":
        height *= 1609.344
    return height 