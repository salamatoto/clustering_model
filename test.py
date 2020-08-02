
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as  np
df = pd.DataFrame({"a":[10,15,20,25,30,35,40,45]})

m = np.mean(df.a)
print('This Distribution of Pupalution:' ,m)


sns.distplot(df.a)
plt.show()


for i in df.a:
    if i >=30:
        print('this number more then 30kr : {}'.format(i))


