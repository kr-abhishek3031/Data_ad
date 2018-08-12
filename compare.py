import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('50k.csv')

data = df.iloc[0:, :11]
dataset = data[data.duplicated(keep=False)]
data = np.array(data)
dataset = np.array(dataset)
x, y = np.shape(dataset)
x1, y1 = np.shape(data)
tem = [0]
for i in range(5):
	temp = []
	for j in range(x1):
		if np.array_equal(dataset[i], data[j]) == True:
			temp.append(j)
		j+=1
	i+=1
	print(i)
	tem.append(len(temp))
plt.hist(tem)
plt.title("Frequency of Users")
plt.xlabel("Repetitions")
plt.ylabel("Frequency")
plt.show()
print(tem)
