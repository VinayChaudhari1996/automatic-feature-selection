from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import util as ut

namesc = [
		"NearestNeighbors",
		"DecisionTree",
		"RandomForest",
		"AdaBoost"
		]

classifiers = [
		KNeighborsClassifier(10),
		DecisionTreeClassifier(max_depth=5),
		RandomForestClassifier(max_depth=5, n_estimators=10),
		AdaBoostClassifier()
    ]

namesr = [
		#"LinearRegression",
		"DecisionTreeRegressor",
		"RandomForestRegressor"
		]
regressors = [
		LinearRegression(),
		DecisionTreeRegressor(max_depth=5),
		RandomForestRegressor(max_depth=5, n_estimators=10)
    ]

def modelJudge(X,y,modelType=2,testPerc=0.5, runs=3):
	global classifiers,regressors,namesc,namesr
	if(modelType>=2 or modelType<0):
		modelType = ut.datesetType(y)
	#Classification
	if(modelType==0):
		fscore = 0
		for r in range(0,runs):
			X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=testPerc, random_state=r)
			for name, clf in zip(namesc, classifiers):
				clf.fit(X_train, y_train)
				score = clf.score(X_test, y_test)
				fscore += score
		return round(fscore/(len(classifiers)*runs),3)
	#Regression
	else:
		error = 0
		for r in range(0,runs):
			X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=testPerc, random_state=r)
			for name, reg in zip(namesr, regressors):
				reg.fit(X_train, y_train)
				ypred = reg.predict(X_test)
				error += mean_squared_error(y_test, ypred)
		return round(error/(len(regressors)*runs),3)	