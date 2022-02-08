#! /usr/bin/env python
# author: Zhongjie Wang
# date: 2022-02-08
# description: mapping metabolites to public SMPDB (The Small Molecule Pathway Database) database locally
# SMPDB (The Small Molecule Pathway Database): https://smpdb.ca/

# usage: python mapping_metabolites2database.py own_metabolites.csv db_metabolites.csv output.csv

import sys
from collections import defaultdict

own_input = open(sys.argv[1], 'r')
db_input = open(sys.argv[2], 'r')
output = open(sys.argv[3], 'w')

db_lines = db_input.readlines()
own_lines = own_input.readlines()
for line in own_lines[1:]:
	metabolite_name = line.split(",")[2].split(" :: ")[0].strip('"')
	#print(metabolite_name)
	for line_db in db_lines:
		if metabolite_name in line_db:
			output.write(line_db)

own_input.close()
db_input.close()
output.close()