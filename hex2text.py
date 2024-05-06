#import bytes
import sys, os
from colored import fg, bg, attr, stylize
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("HEX2TEXT | TEXT2HEX - topVL.net")

bg = bg("white")
blue = fg('blue')
red = fg('red')
green = fg('green')
white = fg('white')
yellow = fg('yellow')
redbold = fg("blue") + attr("bold") + attr("underlined")
blackbold = fg(0) + attr("res_bold") + attr("underlined")
reset = attr('reset')

chosen = input(bg+stylize("Chọn:\n1.Hex to text"+"\n2.Text to Hex\nLựa chọn: ",blackbold))
if chosen == "1":
	hex_string = input(bg+stylize("Nhập hex code:\n",blackbold))

	bytes_object = bytes.fromhex(hex_string)
	#Convert to bytes object
	ascii_string = bytes_object.decode("ASCII")

	#Convert to ASCII representation
	print("\n"+bg+stylize("==================KẾT QUẢ GIẢI MÃ==================",redbold)+"")
	print("\t\t\t"+bg+green+ascii_string+reset+"\n===================================================\n")
else:
	data = input(bg+stylize("Nhập text:\n",blackbold))
	table = [item.encode('utf-8').hex() for item in data]
	#print(table)
	output = ''.join(str(item) for item in table)
	print("\n"+bg+stylize("==================KẾT QUẢ MÃ HÓA HEX CODE==================",redbold)+"")
	print("\t\t\t"+bg+green+output+reset+"\n===========================================================\n")

import readchar
print("Press Any Key To Exit")
k = readchar.readchar()