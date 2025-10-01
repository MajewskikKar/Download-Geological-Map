
    #checking number length and adding 0 if needed - used for process_number function
def process_number_checker(self, number):
    if len(number) == 1:
        number_checker = '000' + number
    elif len(number) == 2:
        number_checker = '00' + number
    elif len(number) == 3:
        number_checker = '0' + number
    else:
        number_checker = number
    return number_checker
    
