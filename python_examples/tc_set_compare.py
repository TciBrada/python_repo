import os

f = open("tc_set_1.txt","r")
i = 0
for tc_id in f:
	print(str(i) + "." + tc_id)
	i = i+1

f.close()