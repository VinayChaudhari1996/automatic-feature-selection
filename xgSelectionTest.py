# plot feature importance using built-in function
from numpy import argsort
from xgboost import XGBClassifier
import model as ml
from pandas import read_csv, np
import time
import cuts

def  xgRelevancy(X,y):
	model = XGBClassifier()
	model.fit(X, y)
	featureImportance = model.feature_importances_
	indexorder = argsort(featureImportance)
	indexorder = list(indexorder)
	indexorder.reverse()
	featureImportance = list(featureImportance)
	featureImportance.sort()
	featureImportance.reverse()
	return [featureImportance, indexorder]

def xgTest(cutMethod=1, runs=3):
	#Artifial Datasets
	files = ['data1000-f1.csv', 'data1000-f2.csv','data1000-f3.csv','data1000-f4.csv','data5000-f1.csv', 'data5000-f2.csv','data5000-f3.csv','data5000-f4.csv','data20000-f1.csv', 'data20000-f2.csv','data20000-f3.csv','data20000-f4.csv','data1000-f1-r500.csv','data5000-f1-r500.csv','data20000-f1-r500.csv']
	buenos = [[0,1,2,3,4,5,6,13,14],[0,1,8,9],[0,1,6,7],[0,1,3,2],[0,1,2,3,4,5,6,13,14],[0,1,8,9],[0,1,6,7],[0,1,3,2],[0,1,2,3,4,5,6,13,14],[0,1,8,9],[0,1,6,7],[0,1,3,2],[0,1,2,3,4,5,6,13,14],[0,1,2,3,4,5,6,13,14],[0,1,2,3,4,5,6,13,14]]	
	modelsType = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	#Real Datasets
	#files = ['real/sonar_scale.csv', 'real/splice_scale.csv', 'real/colon-cancer.csv', 'real/leu.csv', 'real/duke.csv', 'real/BH20000.csv', 'real/madelon-test.csv']
	#buenos = [['?'],['?'],['?'],['?'],['?'],['?'],['?']]
	#modelsType = [0,0,0,0,0,0,0]
	i=0
	verboseClassifiers = True
	for f in files:
		modelType = modelsType[i]
		filepath = 'Data/'+f		
		data = read_csv(filepath)
		X = np.array(data.ix[:,0:-1])
		y = np.array(data.ix[:,-1])
		print filepath, buenos[i]
		startTime = time.time()
		if(modelType==0):
			acc = ml.clasificationJudge(X=X,y=y, testPerc=0.5, runs=runs)
		else:
			acc = ml.regresionJudge(X=X,y=y, testPerc=0.5, runs=runs)
		endTime = time.time()
		print "original:", acc, X.shape[1], str(round(endTime-startTime,3))+"s"
		try:
			startTime = time.time()
			[featureImportance, rank] = xgRelevancy(X,y)
			if(cutMethod==0):
				featureImportance = featureImportance[0:-1]
				cutpos = cuts.greatestDiffCut(weights=featureImportance)
			if(cutMethod==1):
				cutpos = cuts.monotonicValidationCut(X=X, y=y, modelType=modelType, rank=rank, consecutives=5, runs=runs)
			rank = rank[0:cutpos]
			endTime = time.time()
			timefs = round(endTime-startTime,3)
			X = np.array(data.ix[:,rank])
			startTime = time.time()
			if(modelType==0):
				acc = ml.clasificationJudge(X=X,y=y, testPerc=0.5, runs=runs)
			else:
				acc = ml.regresionJudge(X=X,y=y, testPerc=0.5, runs=runs)
			endTime = time.time()
			timeml = round(endTime-startTime,3)
			print "result: ",acc, timefs, timeml, len(rank), rank[0:5]
			print 	
		except Exception as inst:
			X = np.array(data.ix[:,0:-1])
			print "error"

if __name__ == '__main__':
	xgTest(1,1)

