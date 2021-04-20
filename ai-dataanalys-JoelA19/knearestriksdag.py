import numpy as np
from sklearn import preprocessing, neighbors, model_selection
import pandas as pd

df=pd.read_csv("votering.csv")
print(list(df))
df.drop(["punkt"],1, inplace= True)

df= df[["rost","parti","fodd","kon","intressent_id"]]

print(df.head(3))
input_labels=["kvinna", "man"] #kvinna ---> 0  man ---> 1
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)
df["kon"]=encoder.transform(df["kon"])

input_labels=["C", "KD", "M", "L", "MP", "V", "S", "SD", "-"] #- ---> 0     C ---> 1    KD ---> 2   L ---> 3     M ---> 4   MP ---> 5   S ---> 6    SD ---> 7   V ---> 8
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)
df["parti"]=encoder.transform(df["parti"])

input_labels=["Nej", "Ja", "Frånvarande", "Avstår"] #Avstår ---> 0  Frånvarande ---> 1  Ja ---> 2   Nej ---> 3
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)
df["rost"]=encoder.transform(df["rost"])

for i, item in enumerate(encoder.classes_):
    print(item, "--->",i)

df.replace("?", "-9999", inplace= True)

print(df.head(4))

X = np.array(df.drop(["rost"],1))
Y = np.array(df["rost"])

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X,Y, test_size = 0.2)
X_train = X_train.reshape(len(X_train), -1)
Y_train = Y_train.reshape(len(Y_train), -1)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train,Y_train)
accuracy = clf.score(X_test,Y_test)
print("accuracy is " + str(accuracy)+", nice!")

example_measure=