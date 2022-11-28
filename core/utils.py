def get_date_joined(date):
    current_date = date
    current_date_no_time = current_date.strftime('%d.%m.%Y')
    return current_date_no_time