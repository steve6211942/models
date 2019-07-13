import scipy.io
import pandas as pd

for i in range(1,1446):
	mat = scipy.io.loadmat('./training_dataset/training_data/annotations/VOC2010_'+str(i)+'.mat')
	mat = {k:v for k, v in mat.items() if k[0] != '_'}
	data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.items()})
	data.to_csv("./training_dataset/training_data/annotation/VOC2010_"+str(i)+".csv")
