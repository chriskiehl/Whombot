import sys, os, time
import Image, ImageGrab
from numpy import *
import win32api, win32con
from de_scram import *


def load_dicts(panels):
	print "loading dictionaries"
	file_list = []
	loc = os.getcwd() + '\\letters\\'
	for i in os.listdir(loc):
		file_list.append(i)
	for i in range(6):
		f=open(loc + file_list[i], 'r')
		panels[i] = eval(f.read())
		f.close()


def save_dicts(panels):
	print "Saving Dictionaries"
	file_list = []
	loc = os.getcwd() + '\\letters\\'
	for i in os.listdir(loc):
		file_list.append(i)
	for i in range(6):
		f=open(loc + file_list[i], 'w')
		f.write(str(panels[i]))
		f.close()


def grab_boxes(panel_list, boxes):
	print "scraping screen"
	# 
	# I'll probably forget how the fudge this works..
	# 
	# 
	# This all also return the letters list for some reason
	# Bad design
	loc = os.getcwd() + '\\letters\\'
	newBoxData = []
	for i in boxes:
		im = ImageGrab.grab(i)
		a = array(im.getdata())
		newBoxData.append(a.sum())
	print "Checking dictionary for appropriate keys\n\n"
	for i in range(6):
		# looks at the new grabs. if, sum for box1 (for example) not in dict.keys
		# Add key and prompt for value
		if newBoxData[i] not in panel_list[i]:
			box_num = i+1
			out_string = "please enter letter for box %d:" % box_num
			new_letter = raw_input(out_string)
			panel_list[i][newBoxData[i]] = new_letter
	save_dicts(panel_list)

	
	return gen_string_from_grabs(panel_list, newBoxData)


def gen_string_from_grabs(panel_list, boxData):
	out_string = ''
	print boxData[0]
	for i in range(6):
		out_string += panel_list[i][boxData[i]]
	
	map_letter_locations(out_string)
	return out_string

def map_letter_locations(in_string):
	# This is poorly thought out..
	# Get the string from the gen_strinf_from.. function
	# Re-split it into individual letters, and then map that to a dict 
	# using the magic numbers below
	global letter_locations
	new_string = format_letters(in_string)
	seq_mouse_locs = [(305,570),(380,570),(455,570),(535,570),(610,570),(690,570)]
	print 'mapping letter locations'

	for i in range(6):
		letter_locations[new_string[i]] = seq_mouse_locs[i]

	return letter_locations

def format_letters(in_string):
	flag = 0
	out_string = ''
	for i in in_string:
		if in_string.count(i) >1 and flag ==0:
			print "Multiple value for : %s" % i
			out_string += str(0)
			flag+=1
			continue
		if in_string.count(i) >1 and flag ==1:
			print "Multiple value for : %s" % i
			out_string += str(9)
			flag+=1
		else:
			out_string+=i
	print out_string
	return out_string



def enter_words(word_list, letter_locations):
	for i in word_list:
		if len(i) > 2:
			print '*' * 8
			print 'Spelling: ', i
			print '*' * 8
			for j in i:
				click(letter_locations[j], .17)
				print 'clicking: ', j
				# print
			time.sleep(.25)
			print 'Submit!'
			click((500, 620))
			time.sleep(1)
	time.sleep(25)
	click((500, 620))
	time.sleep(4)




def click(cord, delay=0):
    win32api.SetCursorPos(cord)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def on_game_screen():
	im = ImageGrab.grab()
	# You won screen
	if im.getpixel(_xPad + 372, _yPad + 281) == (242,225,78))):
		print 'you won screen'
		print 'click Play Again'
		click((600,600), .1)
		time.sleep(3)
		return False

	elif im.getpixel(_xPad + 206, _yPad + 140) == (223,223,223):
		print "Ad screen..."
		time.sleep(3)
		return False
	else:
		return True






if __name__ == '__main__':
	# format_letters('aarmsd')
	"""
	README

	Change these so that the target the top left black-ish pixel of the game. 
	"""
	_xPad = 162
	_yPad = 308


	# DO **NOT** CHANGE THESE VALUES
	# *************************
	xPad = 162   # ||
	yPad = 308   # ||
	# THIS BOX SHALL PROTECT THEE
	# Basically, I F'd up early on, and set all the coordinates in stone. 
	# I was too lazy to fix those values to reflect the new relative positioning, 
	# so this is what creates the proper offset. The _pad values are the ones you have to 
	# adjust to match the screen position. 



	boxes = [(_xPad + (289-xPad), _yPad + (562-yPad), _xPad + (328-xPad), _yPad + (596-yPad)),
			(_xPad + (366-xPad), _yPad + (558-yPad), _xPad + (405-xPad), _yPad + (592-yPad)),
			(_xPad + (443-xPad), _yPad + (562-yPad), _xPad + (482-xPad), _yPad + (596-yPad)),
			(_xPad + (520-xPad), _yPad + (558-yPad), _xPad + (559-xPad), _yPad + (592-yPad)),
			(_xPad + (597-xPad), _yPad + (562-yPad), _xPad + (636-xPad), _yPad + (596-yPad)),
			(_xPad + (674-xPad), _yPad + (558-yPad), _xPad + (713-xPad), _yPad + (592-yPad))]


	b1={}
	b2={}
	b3={}
	b4={}
	b5={} 
	b6={}
	panel_list = [b1,b2,b3,b4,b5,b6]

	[(_xPad + (305 - xPad), _yPad + (570 - yPad)),(_xPad + (380 - xPad), _yPad + (570 - yPad)),
	(_xPad + (455 - xPad), _yPad + (570 - yPad)),(_xPad + (535 - xPad), _yPad + (570 - yPad)),
	(_xPad + (610 - xPad), _yPad + (570 - yPad)),(_xPad + (690 - xPad), _yPad + (570 - yPad))]
	
	letter_locations = {}

	load_dicts(panel_list)

	while True:
		if on_game_screen():
			indi_lets = grab_boxes(panel_list, boxes)
			word_list = get_word_list(indi_lets)
			enter_words(word_list, letter_locations)











