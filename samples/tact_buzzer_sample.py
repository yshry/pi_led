import sys
sys.path.append('../src')

from tact import Tact
from led import Led
from buzzer import Buzzer
from time import sleep

mybuzzer = Buzzer(18)
mytact0 = Tact(21)
mytact1 = Tact(20)

myled = Led(16)

song = [
	['c', 'c', 'g', 'g', 'a', 'a', 'g', 'f', 'f', 'e', 'e', 'd', 'd', 'c'],
	['c', 'd', 'e', 'c', 'd', 'e', 'g', 'e', 'd', 'c', 'd', 'e', 'd']
	]

index = 0
push = False
scale = 2
count = 0
select = 0
switch = False
scount = 0

try:
	while True:
		if select == 1:
			myled.on()
		else:
			myled.off()

		if mytact0.get():
			if not push:
				mybuzzer.softtonewrite(song[select][index], 2)
				push = True
				count = 0
		else:
			if push and count >=3:
				count = 0
				push = False
				index = index + 1 if (index < len(song[select]) -1) else 0
			mybuzzer.softtonestop()
			count = count + 1 if (count <3) else 0
		if mytact1.get():
			if not switch:
				switch = True
				select = select + 1 if (select < len(song) -1) else 0
				index = 0
				scount = 0
		else:
			if scount >=3 and switch:
				switch = False
				scount = 0
			scount = scount +1 if (scount <3) else 0
		print '%i: %i, %s' %(index, select, switch)
	sleep(0.2)
except KeyboardInterrupt:
	pass
