
import pandas as pd
import numpy as np
import random
import csv
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.cluster import KMeans

model = KMeans()     # KNeighborsClassifier()



with open('house_classifer.csv') as f:
         reader =  csv.reader(f)
         next(reader)
         data = []
         for row in reader:
             data.append({
                  "evidence":[float(cell) for cell in row[:20]],"label":"Atuhentic" if row[20] == "0" else "Counterfeit" })


evidence = [row["evidence"] for row in data]
label = [row['label'] for row in data]


xtrain,xtest,ytrain,ytest = train_test_split(evidence,label,test_size=0.40)

model.fit(xtrain,ytrain)

predictions = model.predict(xtest)


correct = (ytest == predictions).sum()
incorrect  = (ytest != predictions).sum()
total = len(predictions)


print(f"Resulte for Model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total: .2f}%")








