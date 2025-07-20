#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀         𓐓  matrix_plots.py 𓐔           
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀       Dev: oezzaou </var/spool/mail/oezzaou>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2025/07/19 13:14:50 by oezzaou
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2025/07/20 17:27:42 by oezzaou
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# ===[ Imports: ]==============================================================
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ===[ Main: ]=================================================================
def main():
    # display all available datasets in seaborn
    datasets = sns.get_dataset_names()
    print("========[Datasets]========")
    print(datasets)
    # load tips data base
    tips = sns.load_dataset('tips')
    print("======[Tips dataset]=======")
    print(tips)
    # Explore tips dataset
    print("=======[Quick Exploration]=======")
    tips.info()

    # Selection (indexing my dataframe) Indexing a new dataFrame
    ntips = tips.loc[:, 'total_bill': 'tip']
    print("=================[new tips]===============")
    print(ntips)
    corr_matrix = ntips.corr()
    print("==========[CrossTAb]==========")
    # NOTE:-------------------------------------------------------------
    # Corr() function is done between quentitive variables/numerical
    # to visualize the correlation quentitiy between numerical variables
    # crosstab(): is used to categorical variables
    print(corr_matrix)

    # 1. visualize the matrix data using heatmap()
    # sns.heatmap(corr_matrix, annot=True, cmap='Blues')

    # 2. using clustermap() to find groups and clusters
    # df = pd.DataFrame({
    #     'Math': [90, 91, 30, 35],
    #     'Physics': [92, 89, 20, 25],
    #     'Art': [30, 35, 95, 98],
    # }, index=['Alice', 'Bob', 'Charlie', 'Diana'])

    # sns.clustermap(df, cmap='Blues')

    # # 3. PairGrid (pairplot() kamlat qraytha)
    # # Creating and empty grid system
    # grid = sns.PairGrid(tips)
    # # apply scatter plots on upper diagonal
    # grid.map_upper(plt.scatter)
    # # apply kdeplot in lower diagonal
    # grid.map_lower(sns.kdeplot)
    # # apply histogram in the diagoanl level
    # grid.map_diag(plt.hist)
    # print(grid)

    # 4. FacetGrid (kaywarini face mn data dyali li endha bzff faces)
    # ghadi n9assmo dataset dyalna l 4 parts based 3la sex and wach
    # o lwa9t li mcha fih
    facet = sns.FacetGrid(tips, col='sex', hue='time')
    # o db ghadi nchofo kol group xhal kaykhaless o tip li kay3ti m3aha
    facet.map(plt.scatter, 'total_bill', 'tip')
    facet.add_legend()

    # NOTE:-----------------------------------------------------
    # You can split the groups based on one categorical variable
    # or more than one variable

    plt.show()


if __name__ == '__main__':
    main()
