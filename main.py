from datetime import datetime, date
def get_days_from_today(date_str):
    try:
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = date.today()
        difference = today - given_date
        return difference.days
    except ValueError:
        return "Invalid date format"
    
print(get_days_from_today("2021-10-09"))