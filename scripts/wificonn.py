from wifi import Cell, Scheme
print(Cell.all('wlan0'))
for obj in Cell.all('wlan0'):
    print(obj)