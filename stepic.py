import arrow

d = arrow.now()
year = d.format('YYYY')
START_DATE = str(d.shift(months=-1).replace(day=21).strftime('%d.%m.%Y'))
END_DATE = str(d.replace(day=20).strftime('%d.%m.%Y'))
print(START_DATE, END_DATE, type(START_DATE), type(END_DATE))