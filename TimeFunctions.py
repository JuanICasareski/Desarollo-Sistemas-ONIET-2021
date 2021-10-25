from datetime import date, datetime, time
import calendar

class weekday:
    pass
class day:
    pass

def getWeekDay() -> weekday:  
    '''Devuelve el dia de la semana en ingles'''
    my_date = date.today()
    a = calendar.day_name[my_date.weekday()]
    return a.lower()

def getDay() -> day:
    '''Devuelve la fecha del dia de hoy, en formato "%d-%m-%Y"'''
    return date.today().strftime("%d-%m-%Y")

def getTime() -> time:
    '''Devuelve la hora actual, en formato "%H:%M:%S"'''
    return datetime.now().time().strftime("%H:%M:%S")
