from datetime import datetime, date
def get_days_from_today(date_str):
    try:
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = date.today()
        difference = today - given_date
        return difference.days
    except ValueError:
        return "Invalid date format"
    
print(get_days_from_today("2022-10-09"))  

import random
def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > max or quantity > (max - min + 1):
        return []
    numbers = random.sample (range(min, max + 1), quantity)
    numbers.sort()
    return numbers
print(get_numbers_ticket(1,49,6))


import re
def normalize_phone(phone_number):
    digits = re.sub(r'\D', '' , phone_number)
    if digits.startswith("380"):
        return "+" + digits
    if digits.startswith("0"):
        return "+38" + digits
    
    return "+38" + digits

phones = ["+38(050)123 32 34","0503451234","(050)8889900","38050-111-22-22","38050 1111 22 11"]
normalized = [normalize_phone(p) for p in phones]
print(normalized)