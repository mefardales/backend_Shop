from datetime import datetime

def time(option):
    # Time format 2000-12-09
    return datetime.today().strftime('%Y-%m-%d') if option == 0 else  datetime.now().strftime('%H')
