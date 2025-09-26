#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀                 𓐓  main.py 𓐔           
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀       Dev: oezzaou </var/spool/mail/oezzaou>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2025/07/24 16:43:38 by oezzaou
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2025/07/29 07:23:35 by oezzaou
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# ===[ Imports: ]==============================================================
from src import data_loader
from src import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns


# ===[ main: ]=================================================================
def main():
    # 1. Loading the raw dataset
    titanic_raw = data_loader.load_raw_data()
    # 2. clean the raw data
    titanic_processed = preprocessing.clean_data(titanic_raw)
    # 3. saving the titanic_processed dataframe
    data_loader.save_processed_data(titanic_processed)
    # titanic_processed.info()
    sns.countplot(x='Survived', data=titanic_processed, hue='Port')
    plt.show()
    print(titanic_processed.head(50))


if __name__ == '__main__':
    main()

# NOTE:> It is a good practice to add a logger (use built-in logging module)

# ml-project/
# ├── data/
# │   ├── raw/                  # Original, immutable data dump
# │   ├── processed/            # Cleaned data for modeling
# │   └── external/             # Any 3rd-party or API data
# ├── notebooks/            # Jupyter notebooks for exploration & prototyping
# │   ├── 01_eda.ipynb
# │   ├── 02_feature_engineering.ipynb
# │   └── 03_modeling.ipynb
# ├── src/                      # Core Python source code
# │   ├── __init__.py
# │   ├── config.py             # Global config variables
# │   ├── data_loader.py        # Load and save data
# │   ├── preprocessing.py      # Feature engineering, data cleaning
# │   ├── train.py              # Model training
# │   ├── evaluate.py           # Evaluation metrics and visualization
# │   └── model.py              # Model class, pipelines
# ├── models/                   # Trained model binaries (e.g., .pkl, .h5)
# │   └── final_model.pkl
# ├── reports/                  # Results, plots, performance metrics
# │   ├── figures/
# │   └── metrics.txt
# ├── tests/                    # Unit and integration tests
# │   └── test_model.py
# ├── scripts/                  # CLI scripts (optional)
# │   └── run_pipeline.py
# ├── .gitignore
# ├── README.md
# ├── requirements.txt
# ├── setup.py                  # Optional for packaging
# └── LICENSE
