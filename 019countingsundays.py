from datetime import date, timedelta

start_date = date(1901, 1, 1)
end_date = date(2000, 12, 31)

count = 0

current_date = start_date
while current_date <= end_date:
    if current_date.day == 1 and current_date.weekday() == 6:
        count += 1

    next_month = current_date.month + 1 if current_date.month < 12 else 1
    next_year = current_date.year if current_date.month < 12 else current_date.year + 1
    current_date = date(next_year, next_month, 1)

print(count)