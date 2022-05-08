import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.txt')
print(data.head(250))

degisken = data[["Sports", "Religious", "Nature", "Theatre", "Shopping", "Picnic"]]

K = int(input("\nK değeri= \n"))
Centroids = (degisken.sample(n=K))
cent_diff = 1
j = 0
while (cent_diff != 0):
    i = 1
    for index1, row_c in Centroids.iterrows():
        Euclidean = []
        for index2, row_d in degisken.iterrows():
            d1 = (row_c["Sports"] - row_d["Sports"]) ** 2
            d2 = (row_c["Religious"] - row_d["Religious"]) ** 2
            d3 = (row_c["Nature"] - row_d["Nature"]) ** 2
            d4 = (row_c["Theatre"] - row_d["Theatre"]) ** 2
            d5 = (row_c["Shopping"] - row_d["Shopping"]) ** 2
            d6 = (row_c["Picnic"] - row_d["Picnic"]) ** 2

            d = np.sqrt(d1 + d2+d3 +d4 +d5 +d6)
            Euclidean.append(d)
        degisken[i] = Euclidean
        i = i + 1
    C = []
    for index, row in degisken.iterrows():
           min_dist= row[1]
           group =1
           for i in range(K):
               if row[i+1] < min_dist:
                   min_dist = row[i+1]
                   group =i+1
           C.append(group)
    degisken["Cluster"] = C

    Centroids_new = degisken.groupby(["Cluster"]).mean()[["Sports", "Religious", "Nature", "Theatre", "Shopping", "Picnic"]]
    if j == 0:
       cent_diff=1
       j=j+1
    else:
        cent_diff = (Centroids_new['Sports'] - Centroids['Sports']).sum() + (Centroids_new['Religious'] - Centroids['Religious']).sum() \
               + (Centroids_new['Nature'] - Centroids['Nature']).sum() + (Centroids_new['Theatre'] - Centroids['Theatre']).sum() \
               + (Centroids_new['Shopping'] - Centroids['Shopping']).sum() + (Centroids_new['Picnic'] - Centroids['Picnic']).sum()
        print(cent_diff.sum())
    Centroids = degisken.groupby(["Cluster"]).mean()[["Sports", "Religious", "Nature", "Theatre", "Shopping", "Picnic"]]

colors=['cornflowerblue', 'gold', 'coral', 'green', 'purple', 'cadetblue', 'crimson']
for k in range(K):
    data=degisken[degisken["Cluster"]==k+1]
    print("\ncluster " + str(k+1) + "deki değişken sayısı")
    print(len(data["Sports"]))
    print("cluster " + str(k+1) + "deki değiskenler")
    print(data["Religious"])
    plt.scatter(data["Sports"], data["Religious"], c=colors[k])
plt.scatter(Centroids["Sports"],Centroids["Religious"],c='black', marker = 'X')
print("\ncentroid merkezleri: ")
print(Centroids)
print(C)
plt.show()
