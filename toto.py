#!/usr/bin/python3
import requests
import re
import sys
import os

def saynumber(params):
	sys.stderr.write("SAY NUMBER %s \"\"\n" % params)
	sys.stderr.flush()
	sys.stdout.write("SAY NUMBER %s \"\"\n" % params)
	sys.stdout.flush()
	result = sys.stdin.readline().strip()


def process_string(input_str):
    words = input_str.split()  # Split the input string into words
    for word in words:
        if word.isdigit():  # Check if the word is a number
            saynumber(int(word))


#reads variables that are passed from asterisk and puts them in env
env = {}

while True: 
	line = sys.stdin.readline().strip()
	if line == '':
		break
	key,data = line.split(':')
	if key[:4] != 'agi_':
		sys.stderr.write("Did not work!\n");
		sys.stderr.flush()
		continue
	key = key.strip()
	data = data.strip()
	if key != '':
		env[key] = data

sys.stderr.write("AGI Environment Dump:\n");
sys.stderr.flush()
for key in env.keys():
	sys.stderr.write(" --%s = %s\n" % (key, env[key]))
	sys.stderr.flush()

#get toto draw
url = "https://www.jogossantacasa.pt/web/SCCartazResult/totolotoNew"

response = requests.get(url)

if response.status_code == 200:
	html_content = response.text
	pattern = r'<li>[\s]*([0-9\s+]+)</li>'
	match = re.search(pattern, html_content)

	if match:
		sequence = match.group(1)
		result = sequence.strip()
		process_string(result)
	else:
		sys.stderr.write("Sequence not found")
		sys.stderr.flush()
else:
	sys.stderr.write("Failed to fetch the webpage")
	sys.stderr.flush()
