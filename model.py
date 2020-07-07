#from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

dataset = pd.read_csv('C:\\Users\\lenovo\\Desktop\\flask\\heart.csv')

X = dataset.iloc[:, :13]


y = dataset.iloc[:, -1]

#from sklearn.naive_bayes import GaussianNB

#nb = GaussianNB()
#nb.fit(X, y)

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(X,y)

# Saving model to disk
pickle.dump(dtc, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
