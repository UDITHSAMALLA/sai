def seconds_convertor(seconds):
    hours = seconds//3600
    minutes = (seconds - hours*3600)//60
    rem_seconds = seconds - hours*3600 - minutes*60
    return hours,minutes,rem_seconds
hours,minutes,seconds=seconds_convertor(10000)
print(hours,minutes, seconds)