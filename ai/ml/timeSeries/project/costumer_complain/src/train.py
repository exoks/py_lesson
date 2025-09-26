#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀                𓐓  train.py 𓐔           
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀       Eng: oezzaou <oussama.ezzaou@gmail.com>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2025/07/24 16:43:38 by oezzaou
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2025/08/28 14:19:51 by oezzaou
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


# ===[ Imports: ]==============================================================
from data_loader import load_raw_data, save_processed_data, train_test_split
from preprocessing import preprocess_data
import model as mod
from evaluate import evaluate_model
import config


# ===[ main: ]=================================================================
def main():
    # 1. Loading the raw dataset
    data_raw = load_raw_data()
    # 2. Data Preprocessing
    data = preprocess_data(data_raw)
    # 3. Save processed data
    save_processed_data(data)
    # 4. train-test split
    # train_set, test_set = train_test_split(data, 'complaints')
    # 5. Building Model
    model = mod.build_holt_winters(data['complaints'], config.params)
    # 6. Evaluate the Model
    forecasts, metrics = evaluate_model(model, data['complaints'], None)
    # ===[ basic exploration of the data ]===
    print(data.head())
    # ===[ basic exploration of the data ]===
    # for metric, acurancy in metrics.items():
      # print(f"{metric}: {acurancy: .2f}")


if __name__ == '__main__':
    main()


# ml-project/
# ├── data/
# │   ├── raw/                  # Original, immutable data dump
# │   ├── processed/            # Cleaned data for modeling
# │   └── external/             # Any 3rd-party or API data
# ├── notebooks/                # Jupyter notebooks for exploration & prototyping
# │   ├── 01_eda.ipynb          # You do your initial data exploration here
# |   |                           (visualizations, correlations, missing values,
# |   |                           etc)
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


# INFO:------------------------------------------------------------------------
# > 'train.py': The 'conductor' of the orchestar, it does not do everything
#   itself, but 'corrdinates': data, model preprocessing, evaluation
# > 'model.py' is to 'define and return your machine learning model' or
#   'pipeline'.
#   - It actes like a factory: you give it parameters (from 'config.py'
#     and it gives you back a ready-to-train model object
# > 'config.py': This file stores all the 'global settings', 'parameters', 'and
#   file paths' that your project needs.
# -----------------------------------------------------------------------------
