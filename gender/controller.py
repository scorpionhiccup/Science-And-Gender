''' Aggregates the predictions of our separate sources to determine a gender
'''
from gender.sources import fbnames, wikipedianames

predictors = [fbnames.gender, wikipedianames.gender]

def majorityVote(name):
	''' Return a prediction based on a majority vote from the sources
	Does not factor in confidence
	'''
	predictions = [ f(name)[0] for f in predictors ]
	malecount = len([f for f in predictions if f == 'MALE'])
	femalecount = len([f for f in predictions if f == 'FEMALE'])
	neutralcount = len([f for f in predictions if f == 'NEUTRAL'])
	if malecount > femalecount and malecount > neutralcount:
		return 'MALE'
	elif femalecount > malecount and femalecount > neutralcount:
		return 'FEMALE'
	elif neutralcount > malecount and neutralcount > femalecount:
		return 'NEUTRAL'
	else:
		return 'UNKOWN'

def mostConfident(name):
	''' Return the prediction of the method which is the most confident in its result
	'''
	predictions = [f(name) for f in predictors]
	return [name for name, score in predictions 
		if score == max([f[1] for f in predictions])][0]
