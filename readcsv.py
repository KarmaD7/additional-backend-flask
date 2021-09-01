import pandas as pd
import numpy as np

def read():
  pass

data = pd.read_csv('dataset/math.csv')
data = list(np.array(data))
print(data[0])
