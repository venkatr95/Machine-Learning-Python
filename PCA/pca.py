from sklearn.decomposition import PCA
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


df = pd.read_csv("Iris.csv")
labels = df['Species']
X = df.drop(['Id','Species'],axis=1)

X_std = StandardScaler().fit_transform(X)

pca = PCA(n_components=4)
X_transform = pca.fit_transform(X_std)

explained_var = pca.explained_variance_ratio_
for var in explained_var:
	print(var)
	plt.bar([PCA1,PCA2,PCA3,PCA4],explained_var,label=var)
	plt.xlabel("Component #")
	plt.ylabel("% Variance Contribution")
	plt.legend()
plt.show()

pca = list(zip(*X_transform))
pca1 = pca[0]
pca2 = pca[1]

color_dict = {}

color_dict["Iris-setosa"] = "green"
color_dict["Iris-versicolor"]='red'
color_dict["Iris-virginica"] = 'blue'

i=0
for label in labels.values:
	plt.scatter(pca1[i],pca2[i],color=color_dict[label])
	i=i+1

plt.title("PCA")
plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.show()


