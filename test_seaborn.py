import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)
x = np.random.normal(size=100000)
sns.distplot(x)

plt.show()