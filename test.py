

file = open("sales-report.txt")

sales_person_dict = {}

for line in file:
	line = line.rstrip()
	line = line.split('|')

    

	sales_person_dict[line[0]] = sales_person_dict.get(line[0],0) +  int(line[2])
	#else:
		#sales_person_dict[line[0]]= int(line[2])


print(sales_person_dict)
