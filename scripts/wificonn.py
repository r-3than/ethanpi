from wifi import Cell, Scheme
print(Cell.all('wlan0'))
for obj in Cell.all('wlan0'):
    if obj.ssid == "REAPER":
        scheme = Scheme.for_cell('wlan0', 'home', obj, "4f3cf593aa")
        scheme.save()
        scheme.activate()

