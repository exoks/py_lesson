#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀   𓐓  datetime_accessors.py 𓐔           
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀      Eng: oezzaou <oussama.ezzaou@gmail.com>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2025/11/29 16:40:35 by oezzaou
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2025/11/29 18:53:27 by oezzaou
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# ===[ Imports ]===============================================================
import pandas as pd


# ===[ main ]==================================================================
def main():
    # Creating a time-based DataFrame
    data = pd.DataFrame({
        'date': ['01-01-2017', '02-01-2017', '03-01-2017', '04-01-2017'],
        'value': ['male', 'male', 'female', 'male'],
    })
    print(f"===[Data]===: {data}")

    # Parsing date column
    data['date'] = pd.to_datetime(data['date'], dayfirst=True)

    # Operations:  Content Exraction
    print(f"===[hour]===:\n{data['date'].dt.hour}")
    print(f"===[Min]===:\n{data['date'].dt.minute}")
    print(f"===[Sec]===:\n{data['date'].dt.second}")
    print(f"===[weekday]===:\n{data['date'].dt.weekday}")
    print(f"===[day]===:\n{data['date'].dt.day}")
    print(f"===[month]===:\n{data['date'].dt.month}")
    print(f"===[year]===:\n{data['date'].dt.year}")
    print(f"===[day_name]===:\n{data['date'].dt.day_name()}")
    print(f"===[month_name]===:\n{data['date'].dt.month_name()}")

    # NOTE:--------------------------------------------------------------------
    # - `datetime` is not as simple strings, so we need more tools to
    #   manuplicate it, there is where `.dt` (datetime accecessor) comes in.
    # - `.dt` is a powerful tool to manipulate the datetime object and apply
    #   serveral operations on dates

    # print(f"normalized data:\n{data['date'].dt.normalize()}")
    # Timedelta Operations

    # Boolean Check
    print(f"===[is_month_start]===\n{data['date'].dt.is_month_start}")
    print(f"===[is_year_start]===\n{data['date'].dt.is_year_start}")
    print(f"===[is_year_end]===\n{data['date'].dt.is_year_end}")
    print(f"===[is_leap_year]===\n{data['date'].dt.is_leap_year}")

    print("===[data info]===")
    data.info()

    # NOTE:--------------------------------------------------------------------
    # - The following systnax return a new data frame with concerning only
    #   one-hoted.

    print("===[Seperated One-hot data]===")
    print(pd.get_dummies(data['value']))

    # NOTE:--------------------------------------------------------------------
    # - The following syntax add the one-hoted data to the the existing
    #   dataframe.
    # -------------------------------------------------------------------------

    print("===[Seperated One-hot data]===")
    data = pd.get_dummies(data, columns=['value'])
    print(data)

    # Resampling and Frequency Changing to 'Monthly Frequency'
    resampled_data = data.set_index('date').resample('ME').sum()
    print(f"===[Resampled Data]===:\n{resampled_data}")


if __name__ == "__main__":
    main()
