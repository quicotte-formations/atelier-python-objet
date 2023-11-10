import datetime

plus_10_j = datetime.timedelta(days=10)
new_date = datetime.datetime.strptime('21/03/2023', '%d/%m/%Y') + plus_10_j
print( new_date.strftime('%d/%m/%Y') )
