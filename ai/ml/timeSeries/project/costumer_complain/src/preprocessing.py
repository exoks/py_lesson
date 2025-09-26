#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀        𓐓  preprocessing.py 𓐔           
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀       Eng: oezzaou <oussama.ezzaou@gmail.com>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2025/07/24 13:45:35 by oezzaou
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2025/08/31 16:10:21 by oezzaou
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# ===[ Imports: ]==============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import month_plot, quarter_plot
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from utils.logger import getLogger
# INFO:[ VERY IMPORTANT INFO ]-------------------------------------------------
# import package are always relative to entry point (main), always look where |
# is the main and path starts from it, dima chof scope dyalha lta7t ay haja   |
# lfuq matay3rafhax.                                                          |
# -----------------------------------------------------------------------------


# ===[ clean_data: ]===========================================================
def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    logger = getLogger(__name__)
    columns = {"week": "Date"}
    logger.info(f"-> Label manipulation: renaming labels: {columns}")
    data.rename(columns=columns, inplace=True)
    logger.info("-> Cleaning Dataset ...")
    # 1|> Checking for missing values
    logger.debug(f"Checking for Missing Values ...\n{data.isna().sum()}")
    # 2|> Fixing inconsistant formats and parse dates
    data['Date'] = pd.to_datetime(data['Date'])
    # convert 'complaints' column from 'object' dtype to 'int64' dtype
    data['complaints'] = data['complaints'].str.replace(
        ",", "").astype(np.int64)
    logger.debug(f"Parsing 'Date' column => {data['Date'].dtype}")
    # 3|> setting 'Date' column to index
    logger.debug("Setting 'Date' column as the index")
    return data.set_index('Date')


# INFO:------------------------------------------------------------------------
# - Let's do some time series (exploring data) indexing, where the date is the
#   index.

# ===[ exp_data_analysis ]=====================================================
def exp_data_analysis(data: pd.DataFrame):
    '''
      this function explore a time series data, This function teach you how to
      explore a time series data where the index is a 'Date'.
    '''
    logger = getLogger(__name__)
    logger.info("-> Exploring the data")
    logger.debug(f"data shape > {data.shape}")
    logger.debug("=============[Data Info]================")
    data.info()
    # Resampling data by 'month'
    logger.debug('Resampling data monthly')
    # NOTE:--------------------------------------------------------------------
    # I can clearly a monthly seasonality, with type of 'multiplicative model'
    # where the 'variance' are proportional to the trend.

    # data.loc['2018', ['complaints']].resample('ME').mean().plot(
    #     title="Montly Seasonality")
    # logger.debug("Ploting `month_plot` ...")
    # print(data.loc['2018', ['complaints']].resample('ME').mean())
    # month_plot(data['complaints'].resample('ME').mean(), ylabel="Monthly")

    logger.debug("Ploting `quarter_plot` ...")
    # NOTE:-------------------------------------------------------------------
    # Quarter Seasonality are clearly seen, where the the number of complains
    # get increased in the 'second quarter' and the 'final quarter'.
    print(data['complaints'].resample('Q').mean())
    # >>> quarter_plot(data['complaints'].resample('Q').mean(), ylabel="Quarter")
    # INFO:--------------------------------------------------------------------
    # - index in case to time series, has a lot of informations like:
    #   . dtype = datetime64
    #   . name = 'Date' (index column)
    #   . lenght = number of observations
    #   . freq = None (means that does not know the frequency of data)
    #     > this part should be handled properly
    logger.debug("Setting Index freq to  weekly starting from monday ...")
    # print(data.asfreq('W'))  # default ('W-Sun')
    # logger.debug(f"data index:\n{data.index}")
    # NOTE:--------------------------------------------------------------------
    # - As you can see data are 'Nan', since it starts count the begining of
    #   the week from 'sunday' but in our data, our week starts from monday
    #   so we are going to change the 'freq' from 'sunday' to 'monday'
    data = data.asfreq('W-Mon')  # default ('W-Sun')
    logger.debug(f"data index:\n{data.index}")
    # >>> data.loc['2018', ['complaints']].plot()
    logger.debug("Seasonal Decomposition plot...")
    # A year has 52 week, seeing the seasonality each for each year
    # >>> seasonal_decompose(data['complaints'], model='mul', period=52).plot()
    logger.debug("Auto-Correlation function plot ...")
    >> plot_acf(x=data['complaints'], lags=52)  # there is a 'SPIKE' in november
    logger.debug("Partial Auto-Correlation function plot ...")
    >> plot_pacf(x=data['complaints'], lags=52)
    plt.show()


# ===[ create_feature ]========================================================
def create_feature(data: pd.DataFrame) -> pd.DataFrame:
    logger = getLogger(__name__)
    logger.info("-> Creating Features ...")
    return data


# ===[ preprocess_data: ]======================================================
def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    # 1. Cleaning dataset (sum + date creation)
    cleaned_data = clean_data(data)
    # 2. EDA (Exploratory Data Analysis) => Summarize & visualize the data
    exp_data_analysis(cleaned_data)
    # 4. Feature Engineering (Create Features)
    return create_feature(cleaned_data)

# INFO:[ Measure Effect (problem behind partial correlation) ]=================
# * We have a set (or dataset) of values and we want to know
#   . Does each value influence the others ?
#   . If so, how much?
#     - This boils down to measuring 'relationshps' among values.
# > [ Different Mahematical tools for this? ]
#   1|> Correlation (linear association)
#       . If you have multiple variables, correlation measures 'how much two'
#         'move together'
#     > Correlation matrix -> shows the pairwise relationship between every pair
#       of variables
#   2|> Partial Correlation (Direct effect)
#       . Goes one step further: measures the 'direct effect of one variable on'
#         'on another, controlling for the rest'
#     > useful to separate direct vs indirect relationships
#   3|> Regression Models (Predictive influences)
#       . Put one variable as the 'outcome' and see how others explain it
#       Ex:                 Y = B1 * X1 + B2 * X2 + ... + e
#     >> The coefficients Bi measure the effect of each Xi on Y <<
#      NOTE:----------------------------------------------------------------
#       This method has a great ADVANTAGE => Bi is the 'quantitive measured'
#       'effect' not only a 'quentitive correlation'.
#   4|> Linear algebra view
#       - Covariance matrix (spread and relationshp structure)
#       - ReadMore about this approach when you need to
#   5|> Graphical modles
#       ReadMore about this approach when you need to
