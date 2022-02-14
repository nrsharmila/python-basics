import datetime
#datetime = module; datetime = class; today() = method
current_date_day = datetime.datetime.today().date()
current_date_time = datetime.datetime.today().time()
current_datetime_day = datetime.datetime.today()
print(current_date_day)
print(current_date_time)
print(current_datetime_day)
filename = current_datetime_day.strftime('%Y-%m-%d-%H-%M-%S-%f')
print(filename)