def total_days(days):
    years= days//365
    months= (days-years*365)//30
    rem_days=days - years*365-months*30
    return years,months,rem_days
print(total_days(800))