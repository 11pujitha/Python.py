most_frequent = "Mississipi"
all_freq = {}

for i in most_frequent:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1
print ("Count of all characters in Mississipi is :\n "
										+ str(all_freq))
