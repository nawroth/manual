#!/usr/bin/env python
# -*- mode: Python; coding: utf-8 -*-

import sys

def out_entries(entries, column_types):
  buff = []
  for entry in entries:
    buff.append('<row>')
    for index, content in enumerate(entry):
      buff.append('<entry align="left" valign="top">')
      if column_types[index] == "mono":
        buff.append('<simpara><literal>')
      buff.append(content.strip()) 
      if column_types[index] == "mono":
        buff.append('</literal></simpara>')
      buff.append('</entry>')
    buff.append('</row>')
  return buff

def table_header(title, setting_key, description, headings, default_value):
  column_count = len(headings)
  buff = []
  buff.append('<table tabstyle="table" role="configsetting" frame="all" rowsep="1" colsep="1">')
  buff.append('<title>')
  buff.append(title)
  buff.append('</title>')
  buff.append('<tgroup cols="')
  buff.append(str(column_count))
  buff.append('">')
  column_types = []
  for i in range(1, column_count + 1):
    buff.append('<colspec colname="col')
    buff.append(str(i))
    buff.append('"/>')
    column_types.append("default")
  buff.append('<thead>')
  buff.append('<row><entry align="left" valign="top" namest="col1" nameend="col')
  buff.append(str(column_count))
  buff.append('"><simpara role="configsetting-key"><literal>')
  buff.append(setting_key)
  buff.append('</literal></simpara><simpara role="configsetting-desc">')
  buff.append(description)
  buff.append('</simpara>')
  buff.append('</entry></row>') 
  buff.extend(out_entries([headings], column_types))
  buff.append('</thead>')
  if default_value is not None:
    buff.append('<tfoot><row><entry role="configsetting-default" align="left" valign="top" namest="col1" nameend="col')
    buff.append(str(column_count))
    buff.append('">Default value: <literal>')
    buff.append(default_value)
    buff.append('</literal></entry></row></tfoot>')
  return buff


data = sys.stdin.readlines()
line = data.pop(0).split(':', 1)
setting_key = line[0]
default_value = None
if len(line) > 1:
  default_value = line[1]
description = data.pop(0)

if len(sys.argv) > 1:
  title = sys.argv[1]
setting_type = "default"
if len(sys.argv) > 2:
  setting_type = sys.argv[2]

headings = ["Value"]
column_types = ["mono"]

body = []
body.append('<tbody>')

has_value_descriptions = False
rows = []
for line in data:
  parts = line.split(':', 1)
  rows.append(parts)
  if len(parts) > 1:
    has_value_descriptions = True

if len(rows) > 0:
  if setting_type in ["minmax", "min", "max"]:
      headings.insert(0, "Limit")
      column_types.insert(0, "default")
  if has_value_descriptions:
    headings.append("Description")
    column_types.append("default")  
  if setting_type == "minmax":
    rows[0].insert(0, "min")
    rows[1].insert(0, "max")
  elif setting_type == "min":
    rows[0].insert(0, "min")
  elif setting_type == "max":
    rows[0].insert(0, "max")
else:
  rows.append([""])

body.extend(out_entries(rows, column_types))
body.append('</tbody>')

sys.stdout.write(''.join(table_header(title, setting_key, description, headings, default_value)))
sys.stdout.write(''.join(body))
sys.stdout.write('</tgroup>')
sys.stdout.write('</table>')
