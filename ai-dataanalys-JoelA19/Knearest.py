import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
from collections import Counter
style.use("fivethirtyeight")

# def eucdist(goalplot,plot):
#     euc= sqrt((plot[0]-goalplot[0])**2+(plot[1]-goalplot[1])**2)
#     print(euc)
#     plt.scatter(plot[0], plot[1], s = 100)

# plot=[1,3]
# goalplot=[2,5]

# plt.scatter(goalplot[0],goalplot[1], s = 150)
# eucdist(goalplot,plot)
# plot2=[4,7]
# eucdist(goalplot,plot2)

# eucdist(goalplot,goalplot)
# plt.show()
dataset={"k":[[2,5],[4,1],[6,5]],"g":[[3,2],[6,3],[4,5]],"r":[[5,5],[7,7],[8,6]]}
new_feature=[8,3]

def knearest(data,predict,k=3):
    if len(data)>=k:
        warnings.warn("k is set to a value less than total number of groups!")
    distance=[        ]
    for group in data:
        for feature in data[group]:
            euclideandistance = np.linalg.norm(np.array(feature)-np.array(predict))
            distance.append([euclideandistance,group])
    votes= [i[1] for i in sorted(distance) [:k]]
    print(Counter(votes).most_common(1))
    votes_result= Counter(votes).most_common(1)[0][0]
    return votes_result

result =knearest(dataset,new_feature,k=4)

print(result)

[[plt.scatter(ii[0],ii[1], color= i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_feature[0], new_feature[1], s = 100, color=result)
plt.show()