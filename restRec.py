import math
from dataFile import ratings

def correlation(user1, user2):

	rated = {}

	for i in ratings[user1]:
		if(i in ratings[user2]):
			rated[i] = 1

	rateLen = len(rated)		

	if(rateLen == 0):
		return 0

	u1preference = sum([ratings[user1][i] for i in rated])
	u2preference = sum([ratings[user2][i] for i in rated])

	u1sq = sum([pow(ratings[user1][i],2) for i in rated])
	u2sq = sum([pow(ratings[user2][i],2) for i in rated])

	userSum = sum([ratings[user1][i] * ratings[user2][i] for i in rated])

	num = userSum - (u1preference * u2preference/ rateLen)
	denom = math.sqrt((u1sq - pow(u1preference, 2) / rateLen) * (u2sq - pow(u2preference,2) / rateLen))
	
	if(denom == 0):
		return 0

	if(denom != 0):

		corr = num/denom
		return corr

def rec(user):

	tot = {}
	totSim = {}

	for other in ratings:

		if(other == user):
			continue
		sim = correlation(user,other)

		if(sim <= 0): 
			continue
		for i in ratings[other]:

			if i not in ratings[user] or ratings[user][i] == 0:

				tot.setdefault(i,0)
				tot[i] += ratings[other][i]* sim

				totSim.setdefault(i,0)
				totSim[i]+= sim


	results = [(total/totSim[i], i) for i,total in tot.items()]
	results.sort()
	results.reverse()
	print("Estimated Scores:", results)

	finList = [i for score, i in results]
	return finList
		

print(rec('User001'))