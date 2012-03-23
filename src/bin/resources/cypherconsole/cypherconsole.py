#!/usr/bin/env python
# -*- mode: Python; coding: utf-8 -*-

import sys

title = ''
if len(sys.argv) > 1:
  active = sys.argv[1].startswith('1')
for i in [2, 3]:
  if len(sys.argv) > i:
    key,value = sys.argv[i].split('=')
    if key == 'title':
      title = value
    elif key == 'db':
      db = value

if active:
  data = sys.stdin.readlines()
  query = data.pop(0) 
  body = []
  if len(title) > 1:
    body.append('<formalpara role="cypherconsole"><title>')
    body.append(title)
    body.append('</title><para>')
  else:
    body.append('<simpara role="cypherconsole">')
  body.append('<database>')
  body.append(db)
  body.append('</database>')
  body.append('<command>')
  body.append(query)
  body.append('</command>')
  if len(title) > 1:
    body.append('</para></formalpara>')
  else:
    body.append('</simpara>')
  sys.stdout.write(''.join(body))
else:
  sys.stdout.write(' ')
  