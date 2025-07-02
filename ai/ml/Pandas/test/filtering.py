#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀            𓐓  filtering.py 𓐔           
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀       Dev: oezzaou </var/spool/mail/oezzaou>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2025/07/02 16:14:47 by oezzaou
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2025/07/02 17:16:14 by oezzaou
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# ===[ Imports: ]==============================================================
import numpy as np
import pandas as pd


# ===[ main ]==================================================================
def main():
    df = pd.read_csv(
        r"/home/oezzaou/py_lesson/ai/ml/Pandas/test/datasets/City_Types.csv")

    print("==============[df]====================")
    print(df)
    # 1. Boolean Indexing Technique
    print("==========[Boolean Indexing]============")
    # generating boolean mask [true, false, true, ...]
    mask = df['CO'] < 10
    print(f"mask: {mask}")
    # There is only one sample that has df['CO'] < 0
    print(f"filtered: {df[mask]}")

    # 2. Using `df.isin()` filtering function, check for values
    print("==========[df.isin()]============")
    # check if lst is in lst = ['CO', 'N02', 2]
    mask = df.isin(['CO', 'NO2', 2])
    print(f"filtered: {df[mask]}")

    # 3. Using `fd.str.contains()`: check of substring in column
    print("==========[df.str.contains()]============")
    # used to check if 'Mo' regrex or substring exist in 'City' column
    mask = df['City'].str.contains('Mo')
    print(mask)

    # 4. Using `fd.filter()`: select specific rows or columns by labels
    #    not values
    print("============[fd.filter()]===============")
    # 0: columns
    filtered = df.filter(items=['CO', 100], axis=0)
    print(f"filtered: {filtered}")
    # 1: rows
    filtered = df.filter(items=['CO', 100], axis=0)
    print(f"filtered: {filtered}")

    # 5. Using df.loc[]/df.iloc[] for filtering
    print("==========[df.loc[]/df.iloc[]]===========")
    # Using df.loc[] with boolean indexing df['CO'] < 10
    print(df.loc[df['CO'] < 10])
    # You can't use iloc[] directly with boolean mask,
    # Use iloc[] instead
    # TIP: convert boolean mask to positions (integers)
    mask = df['CO'] < 10
    print(df.iloc[np.where(mask)])


if __name__ == '__main__':
    main()
