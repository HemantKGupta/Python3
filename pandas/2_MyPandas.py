
import numpy as np
import pandas as pd


# In[2]:

from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4))
df
df = pd.DataFrame(randn(5,4), index='A B C D E'.split(),columns='W X Y Z'.split())
df
df>0
df[df>0]
df.reset_index()
df
newind = 'CA NY WY OR CO'.split()
df['states'] = newind
df
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
zip(outside, inside)
print(list(zip(outside, inside)))
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
hier_index
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df
df.loc['G1']
df.loc['G1'].loc[1]
df.index.names
df.index.names = ['Group','Num']
df


