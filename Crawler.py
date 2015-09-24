#!/usr/bin/python
import urllib2
import sh
import thread

def baseN(num, b, numerals="0123456789qwertyuiopasdfghjklzxcvbnm"):
	return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


ext = [".com", ".net", ".org", ".edu", ".gov"]
lst = "0123456789abcdefghijklmnopqrstuvwxyz"
a = 47182
b = 0
thread_num = 40

dork = "/wp-login.php"
conf = "Powered by WordPress"
def scan(ext, lst, a, b, add, dork, conf):
	while True:
		for b in range(0, len(ext)):
			try:
				address = baseN(a, len(lst), lst) + ext[b]
				sh.ping(address, "-c 1", _out="/dev/null")
				page = urllib2.urlopen("http://" + address + dork).read()
				if conf in page:
					open("index.html", "a").write(address + "<br>\n")
					open("targets.txt", "a").write(address + "\n")
					print(address + " - Found one!")
			except sh.ErrorReturnCode_1:
				print(address + " - Failed No Responce")
			except sh.ErrorReturnCode_2:
				print(address + " - Failed No Responce")
			except Exception:
				print(address + " - Failed WP Check")
		a += add

for c in range(a, a+thread_num):
	thread.start_new_thread(scan, (ext, lst, c, b, thread_num, dork, conf))

while True:
	pass
