# ls -lRh | wc -l
from pathlib import Path
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

p = Path('/Users/dmitry')
file_list = []
file_df = pd.DataFrame({'name':[], 'size':[]})

def get_file_list(path):
    file_list = []
    for child in path.iterdir():
        if child.is_dir()    and child.exists() and not child.is_symlink():
            file_list += (get_file_list(child))
        elif child.is_file() and child.exists() and not child.is_symlink():
            file_list.append( {'name':str(child), 'size':child.stat().st_size / 1024 / 1024} )# size in MB
    return file_list

file_list = get_file_list(p)
if len(file_list) != 0:
    file_df = file_df.append(file_list, ignore_index=True)

big_files_df = file_df[ (file_df['size'] > 10) & (file_df['size'] <= 1024)]
print(big_files_df)
sns.set(color_codes=True)
sns.distplot(big_files_df['size'], bins=10, kde=False)
plt.show()
