
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.DataFrame({"a":[10,15,20,25,30,35,40,45]})

print(df)
sns.displot(df)
plt.show()
