#import featureSelector as fs
import classifiers as cf
import cuts
import binDynamic as bd
import binCreator as bc
from pandas import *
import plots as pt

def artificialTest():
	files = ['simpleCorrelations.csv']
	buenos = [[1,2,3,4,5,6]]
	i=0
	verboseClassifiers = True
	for f in files:
		filename = 'Data/'+f
		###Separate Data
		print filename, buenos[i]
		data = read_csv(filename)
		X = np.array(data.ix[:,0:-1])
		y = np.array(data.ix[:,-1])
		#print X.shape
		#print y.shape

		#Static search
		#print bc.binsStepBased(data)

		### Search
		#Dynamic search
		#X, y, method, split, useSteps, normalizeData, Debug
		bx = bd.binarySearchBins(X,y,1,0,0)
		bx = bd.binarySearchBins(X,y,1,0,1)
		bx = bd.binarySearchBins(X,y,1,0,2)
		bx = bd.binarySearchBins(X,y,1,0,3)
		bx = bd.binarySearchBins(X,y,1,0,4)
		bx = bd.binarySearchBins(X,y,1,0,5)
		#print bx
		#bx = bd.cuadratureSearchBins(X)	
		#print bx
		
		### Cuts
		#[X,y] = cuts.greatestDiff(rank,weight,data)
		#[X,y] = cuts.monotonicValidationCut(rank,weight,data)
		#[X,y] = cuts.fullValidationCut(rank,weight,data)
		
		#Classify
		#print cf.getBestClassifiers(X,y,verboseClassifiers)
		i = i+1
		print "-------------------------------------\n"

artificialTest()
