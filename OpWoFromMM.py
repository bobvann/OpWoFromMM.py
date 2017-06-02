#!/usr/bin/env python

import xml.etree.ElementTree
import sys
import os.path

def visit(node, depth):
	for e in node.findall('node'):

		newname = ''
		curname = ''

		try:
			newname = str(e.get('TEXT'))
		except:
			newname = 'N/D'

		try:
			curname = str(node.get('TEXT'))
		except:
			curname = 'N/D'


		for i in range(0,depth):
			sys.stdout.write(';')

		toprint = newname.replace('\n', ' ')

		print(toprint)

		visit(e, depth + 1)


if len(sys.argv) < 2:
	print("1 parameter required: filename")
	sys.exit(1)

filename = sys.argv[1]

if(not os.path.isfile(filename)):
	print("Non existent file")
	sys.exit(2)


e = xml.etree.ElementTree.parse(filename).getroot()

root = e.findall('node')[0]

homepage = None
for e in root.findall('node'):
	if e.get('TEXT')=='home page':
		homepage = e


print homepage

visit(homepage, 0)
