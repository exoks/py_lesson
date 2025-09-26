#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀        𓐓  preprocessing.py 𓐔           
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀       Eng: oezzaou <oussama.ezzaou@gmail.com>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2025/07/24 13:45:35 by oezzaou
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2025/08/28 15:38:20 by oezzaou
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# ===[ Imports: ]==============================================================
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import month_plot, quarter_plot, plot_acf
# from scipy.stats import boxcox
# INFO:------------------------------------------------------------------------
# * Scipy stands for 'Scientific Python', It is a library built on top of     |
#   'Numpy', and it provides a huge coolection of tools for:                  |
#   - Mathematics (linear algebra, calculus, optimization)                    |
#   - Statistics (distributions, tests, correlations)                         |
#   - Signal proccessing                                                      |
#   - Scientific computing in general                                         |
# -----------------------------------------------------------------------------

from utils.logger import getLogger
# INFO:[ VERY IMPORTANT INFO ]-------------------------------------------------
# import package are always relative to entry point (main), always look where |
# is the main and path starts from it, dima chof scope dyalha lta7t ay haja   |
# lfuq matay3rafhax.                                                          |
# -----------------------------------------------------------------------------


# ===[ clean_data: ]===========================================================
def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    logger = getLogger(__name__)
    logger.info("-> Cleaning Dataset ...")
    logger.debug("Parsing 'Date' column ...")
    data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")
    logger.debug("Setting date as an index ...")
    # NOTE:--------------------------------------------------------------
    # - Setting date as the index makes the date much more easy to      |
    #   manipulate visualize and explore.                               |
    # -------------------------------------------------------------------
    data.set_index('Date', inplace=True)
    logger.debug("Changing Data Frequencty ...")
    data = data.asfreq('D')
    print(data.index)
    return data


# ===[ create_feature ]========================================================
def create_feature(data: pd.DataFrame) -> pd.DataFrame:
    logger = getLogger(__name__)
    logger.info("-> Creating Features ...")
    return data


# INFO:-------------------------------------------------------------------
# - Let's do some time series (exploring data) indexing, where the date is
#   the index.
# ===[ explore_data ]==========================================================
def explore_data(data: pd.DataFrame):
    '''
      This function explore a time series data, This function teach you how to
      explore a time series data where the index is a 'Date'.
    '''
    logger = getLogger(__name__)
    # We can index all the samples of a specific Year, month or even a Day
    logger.debug("Time series: Indexing all samples in the year 2014")
    print(data.loc['2014'])  # Direct Selection (Indexing)
    # Indexing all the samples in 2014 and november
    logger.debug("Time Series: Indexing all sample in the november 2014")
    print(data.loc['2014-09'])  # Direct Selection (Indexing)
    # NOTE:----------------------------------------------------------------
    # - This type of selection (related to time series format) is new to me
    # Resembling to Monthly Frequancy
    logger.debug('time series: resempling (grouping) weekly & mean')
    # It is lazy object, similar to concept of grouping
    print(data.resample('ME').mean())
    # INFO:----------------------------------------------------------------
    # - `resample` is 'time-series-specific function' in pandas
    # - It is like 'groupby, but for time'
    # - 'D'(daily) -> 'W' (weekly) -> 'ME' (monthly) -> 'Y' (Yearly)
    logger.debug("time series: 7-Day rolling Average")
    data['rolled_open'] = data['Open'].loc['2014'].rolling(window=7).mean()
    # data[['rolled_open', 'Open']].loc['2014'].plot()
    # plt.show()
    # Finding the heighest average month in rolled open price
    print("===============================================================")
    print(data.resample('ME').mean()['rolled_open'].idxmax())
    print("===============================================================")
    # INFO:[ Rolling Average ]-------------------------------------------------
    # . rolling(window=): return a lazy object, similar to resameple and
    #   we have to apply some aggregation function like mean, which is
    #   the appropriate one.
    # . rolling average: means pick a 'window size (say 3 days)'
    # . at each step, take the 'average of the last 3 values'.
    # . Slide ("roll") the window forward one step at a time
    # > [ Why is it used? ]
    #   - Smoothing noise
    #     . Real-World data is messy (fluctuations, outliers)
    #     . Rolling Average smooths the line, makeing 'trends easier to see'
    #   - Trend Detection: Helps identify whether values are generally going
    #     up, down, or stable.
    #   - Seasonality signals:
    #     . You can choose a window size equal to a known season (e.g 7 days
    #       for weekly seasonality)
    #   - Forecasting features: in ML models, rolling average are often used
    #     as 'features' because they carry trend information.


# ===[ plots: ]================================================================
def plots(data: pd.DataFrame):
    # fig = plt.figure(figsize=(2, 2))
    # spec = GridSpec(2, 2, figure=fig)
    # ax = fig.add_subplot(1, 1, 1)
    # Adding labels to the plot
    # ax.set_xlabel("Date")
    # ax.set_ylabel("Price")
    # ==========================================================
    # > Identify Seasonality (smooth the curve using rolling average)
    # checking for montly seasonality (it is clear that no seasonality)
    # month_plot(data['Open'].resample('ME').mean())
    # checking for quartly seasonality
    # quarter_plot(data['Open'].resample('Q').mean())
    # INFO:------------------------------------------------------------
    # - These two function are really helpful to identify or visualize
    #   seasonality.
    # > Auto-correlation (lag=3) [sheft a time series by lag and then compute
    # make the simple statistica correlation], from the plot it is abvious that
    # my data are correlated to the last 11 months ago

    # plot_acf(data.resample('ME').mean()['Open'], lags=26)

    # INFO:--------------------------------------------------------------------
    # - Shaded area tells that the area is 'statisticaly not significant'.
    # - This previous term is in the statistics => Make sure to understand
    #   this concept.
    # - for now on significant value, it is value that does not happen for
    #   coinsidence.
    # -------------------------------------------------------------------------
    plt.show()


# ===[ preprocess_data: ]======================================================
def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    # 1. Cleaning dataset (sum + date creation)
    cleaned_data = clean_data(data)
    print(cleaned_data)
    # 2. Exploring the dataset
    # explore_data(cleaned_data)
    # 3. visualize the data
    # plots(cleaned_data)
    # 4. Feature Engineering (Create Features)
    return create_feature(cleaned_data)

# INFO:[ Measure Effect (problem behind partial correlation) ]=================
# * We have a set (or dataset) of values and we want to know
#   . Does each value influence the others ?
#   . If so, how much?
#     - This boils down to measuring 'relationships' among values.
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
