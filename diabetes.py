import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
import pickle


# loading the diabetes dataset to a pandas DataFrame
df=pd.read_csv('diabetes.csv')

# seperating the data and label into X and Y respectively
X=df.iloc[:,0:8]
Y=df['Outcome']


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, stratify=Y,random_state=1)

# Building the model using Support Vector Machine classifier
classifier = svm.SVC(kernel='linear')

# training the SVM classifier
classifier.fit(X_train, Y_train)

# Save the trained Logistic Regression model with pickle
pickle.dump(classifier, open('diabetes.pkl', 'wb'))
  
