from numpy import *

#normalize rows without considering zeros
def normailize(ratings, rated):
	numRest = ratings.shape[0]

	rmean = zeros(shape = (numRest, 1))
	norm = zeros(shape = ratings.shape) #normalized matrix

	for i in range(numRest):
		#get all the rated indices
		ratedInd = where(rated[i] == 1)[0] #rated index
		rmean[i] = mean(ratings[i, ratedInd])
		norm[i, ratedInd] = ratings[i, ratedInd] - rmean[i]

	return norm, rmean


#Part 1
#input dataset

numRestuarants = 10
numUsers = 5

ratings = random.randint(11, size = (numRestuarants, numUsers))

rated = (ratings != 0) * 1

myRating = zeros((numRestuarants, 1))

myRating[0] = 5
myRating[1] = 5
myRating[2] = 5
myRating[3] = 5
myRating[4] = 5
myRating[5] = 5
myRating[6] = 5
myRating[7] = 5
myRating[8] = 5
myRating[9] = 5

#add myRating to the actual rating matrix

ratings = append(myRating, ratings, axis = 1)
rated = append(((myRating != 0) * 1), rated, axis = 1)
print(ratings)
ratings, ratingsMean = normailize(ratings, rated)

print(ratings)