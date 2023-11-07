import re

expr = r'^([a-zA-Z]*) ([a-zA-Z]*)$'
pattern = re.compile(expr)
match = pattern.match('Thomas Digna')
groups = match.groups()
print( groups )