#!/usr/bin/python
import requests
import _thread
import random


def create_common_words():
    with open('common_words.txt', 'r') as c:
        with open('new_common_words.txt', 'w') as f:
            words = set(c.read().split('\n'))
            words = sorted(words)
            for word in words:
                f.write('{}\n'.format(word))
				
def get_seen_words():
    with open('seen.txt', 'w+') as f:
        return set(f.read().split('\n'))

def get_common_words():
    with open('common_words.txt', 'r') as f:
        return f.read().split('\n')

def add_seen_word(word):
    with open('seen.txt', 'w+') as f:
        f.write('{}\n'.format(word))


def get_random_phrases(n=300, max_size=12):
    max_fails = 500000
    seen = get_seen_words()
    count = 0
    fails = 0
    while count < n and fails < max_fails:
        a = random.randint(0, len(words) - 1)
        b = random.randint(0, len(words) - 1)
        phrase = '{}{}'.format(words[a], words[b]).strip()
        if len(phrase) <= max_size and len(phrase) > 4 and phrase not in seen:
            seen.add(phrase)
            add_seen_word(phrase)
            return phrase
            count += 1
        else:
            fails += 1
		



def baseN(num, b, numerals="0123456789qwertyuiopasdfghjklzxcvbnm"):
	return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
ext = [".com", ".net", ".org", ".edu", ".gov"]
lst = "0123456789abcdefghijklmnopqrstuvwxyz"
a = 47182
b = 0
thread_num = 40
Green="color 2"
Yellow="color 6"
dork = "/wp-login.php"
conf = "wp.i18n.setLocaleData"
words = get_common_words()

def scan(ext, lst, a, b, add, dork, conf):
    
	while True:
		for b in range(0, len(ext)):
			try:
                
				address = (get_random_phrases(1, 8) + ext[b])
				
				page = requests.get("http://" + address + dork)
				if conf in page.text:
					open("index.html", "a").write(address + "<br>\n")
					open("targets_en.txt", "w+").write(address + "\n")
                    
					print(address + " - WP Detected!")
            
			except Exception:
                
				print(address + "----- ")
		a += add
        
for c in range(a, a+thread_num):
    
	_thread.start_new_thread(scan, (ext, lst, c, b, thread_num, dork, conf))

while True:
	pass


