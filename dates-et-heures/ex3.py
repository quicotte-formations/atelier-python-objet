from datetime import datetime

td = datetime.strptime('31/12/2030', '%d/%m/%Y')
print( td.strftime('%Y/%m/%d') )