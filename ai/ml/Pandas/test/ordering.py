
# ===[ Imports: ]==============================================================
import pandas as pd


# ===[ main ]==================================================================
def main():
    df = pd.read_csv(
        r'/home/oezzaou/py_lesson/ai/ml/Pandas/test/datasets/City_Types.csv')
    # print("==========[DataFrame]============")
    # print(f"dataset: {df}")
    # print("======[ Filter PM10 Column (Input Feature) ]======")
    # print(df['PM10'])
    # print("====[ Filtring only values < 3 in of input feature 'PM10']====")
    # print(df[df['PM10'] < 3])
    # print("============[ df.isin() ]================")
    # lst = ['Zurich']
    # # brings all samples with => City in list ['Zurich']
    # print(df[df['City'].isin(lst)])  # Input Feature filtring
    # print("=========[ df.str.contains() ]============")
    # # bring all samples with City contains 'Zu'
    # print(df[df['City'].str.contains("Zu")])  # Input Feature filtring
    # print("==========[ df.set_index() ]==============")
    # # Change indexing by another input feature (column)
    # df2 = df.set_index('City')
    # print(df2)
    # print("=========[ df.filter()]==========")
    # # Select specific rows or columns based on labels, not values
    # print(df2.filter(items=['City', 'PM10']))
    # print("=========[ df.loc()]==========")
    # # 1. starts from the first row label until the last row label
    # # 2. start from the 'City' label until '0#' label
    # print(df.loc[:, 'City':'O3'])
    #
    # print("=========[ df.iloc() ]==========")
    # # 1. starts from the index=0 row label until the index=100 row label
    # # 2. start from the index=0 column label until index=2 column label
    # print(df.iloc[0:100, 0: 2])
    # # NOTE: 100, 2 Indieces labels are exclusive
    print("==========[df.sort_values()]=================")
    # sorting the DataFrame based on PM10 input feature values
    print(df.iloc[0:100].sort_values(by=['PM10'], ascending=True))


if __name__ == '__main__':
    main()
