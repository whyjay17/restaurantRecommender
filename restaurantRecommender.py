from numpy import *
from scipy import optimize

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

#get X and theta matrix from xtheta based on their dimensions
def unroll(xtheta, numUsers, numRestuarants, numFeatures):
	first30 = xtheta[:numRestuarants * numFeatures]
	X = first30.reshape((numFeatures, numRestuarants)).transpose()
	last18 = xtheta[numRestuarants * numFeatures:]
	theta = last18.reshape(numFeatures, numUsers).transpose()

	return X, theta

#total sum of squared errors
def getCost(xtheta, ratings, rated, numUsers, numRestuarants, numFeatures, regParam):
	X, theta = unroll(xtheta, numUsers, numRestuarants, numFeatures)
	cost = sum((X.dot(theta.T) * rated - ratings) ** 2) / 2

	return cost

#get gradient(slope)
def getGrad(xtheta, ratings, rated, numUsers, numRestuarants, numFeatures, regParam):
	X, theta = unroll(xtheta, numUsers, numRestuarants, numFeatures)
	#
	diff = X.dot(theta.T) * rated - ratings
	Xgrad = diff.dot(theta) + regParam * X
	thetaGrad = diff.T.dot(X) + regParam * theta

	return r_[Xgrad.T.flatten(), thetaGrad.T.flatten()]

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

ratings, ratingsMean = normailize(ratings, rated)

#update variables
numUsers = ratings.shape[1]
numFeatures = 3

#linear regression

featureMat = random.randn(numRestuarants, numFeatures)
preferences = random.randn(numUsers, numFeatures)
# y = X * Theta // X = feature, Theta = user preference

initXtheta = r_[featureMat.T.flatten(), preferences.T.flatten()]

print(featureMat)
print(preferences)

regParam = 30

minCost_optimalParams = optimize.fmin_cg(getCost, fprime=getGrad, x0=initXtheta,
 args=(ratings, rated, numUsers, numRestuarants, regParam),
 maxiter = 100, disp = True, full_output=True)

cost, optimalfeatures = minCost_optimalParams[1], minCost_optimalParams[0]

featureMat, preferences = unroll(optimalfeatures, numUsers, numRestuarants, numFeatures)

print(featureMat)
print(preferences)

finalPredictions = featureMat.dot(preferences.T)

myPrediction = finalPredictions[:, 0:1] + ratingsMean
print(finalPredictions)