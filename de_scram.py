import mechanize
from bs4 import BeautifulSoup
import html5lib


def get_word_list(in_words):
	br = mechanize.Browser()
	print "connecting to server.."
	response1 = br.open("http://www.thewordfinder.com/scrabble.php/")
	print "Success!"

	br.select_form(nr=0)
	br.select_form(nr=0)
	br['letters'] = in_words
	response = br.submit()
	print 'submitting form..'


	soup = BeautifulSoup(response.read()) 
	word_list = []
	for i in soup.find_all('p','result'):
		word_list.append(str(i))

	for i in range(len(word_list)):
		word_list[i] = word_list[i].split('">')[1].split('<')[0]
		print word_list[i]
	print "success!"
	print 'returning Word List'
	check_for_dups(word_list)
	return word_list
	


def check_for_dups(a):
	# The bot gets confused when there are duplicate letters
	# I for some reason thought it would be quicker to implement this 
	# Than to look up how to deal with multiple dictionary entries that 
	# Have the same keys. 
	for i in range(len(a)):
		# print a[i]
		for j in range(len(a[i])):
			if a[i].count(a[i][j]) >1:
				a[i] = change_dup_chars(a[i], a[i][j])

			# print a[i][j]
	return a


changeCount = 0
def change_dup_chars(in_s, dup):
	global changeCount
	out_string = ''
	flag = 0
	for i in in_s:
		if i == dup and flag == 0:
			if changeCount<1:
				out_string += str(0)
				flag = 1
				changeCount +=1
			else: 
				out_string += str(9)
				flag = 1
		else:
			out_string += i
	return out_string

def test():
	# Testing stuff out
	a = get_word_list('gasbag')			
	# check_for_dups(a)
	for i in a:
		print i


if __name__ == '__test__':
	test()