from datetime import datetime
import locale

locale.setlocale( locale.LC_TIME, 'fr_FR' )# si '' en 2d param, locale système

print( datetime.strftime( datetime.now(), '%A' ) )