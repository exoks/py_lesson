#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀             𓐓 timesfm_model.py 𓐔       
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀  Engineer: oezzaou <oussama.ezzaou@gmail.com>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2026/08/06 09:51:49 by oezzaou
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2026/08/06 16:02:08 by oezzaou
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# ===[ imports ]===============================================================
import pandas as pd
import numpy as np
import timesfm
import torch

# ===[ Loading data ]==========================================================
data = pd.read_csv("./sales_dataset.csv")

print(f"===[ head ]===:\n{data.head()}")
data.info()

# ===[ Data Preprocessing ]====================================================
data = data.iloc[:36]


print(f"- [Shape]: {data.shape}")
for X in data.columns:
    print(f"- [{X}]: {data[X].unique().tolist()}")

# ===[ Modeling & Evaluation ]=================================================
torch.set_float32_matmul_precision("high")

# loading timesFM 2.5 model
model = timesfm.TimesFM_2p5_200M_torch.from_pretrained(
    "google/timesfm-2.5-200m-pytorch",
)

model.compile(
    timesfm.ForecastConfig(
        max_context=512,
        max_horizon=128,
        normalize_inputs=True,
        use_continuous_quantile_head=True,
        force_flip_invariance=True,
        infer_is_positive=True,
        fix_quantile_crossing=True,
        return_backcast=True,
    )
)
print(f"- [Model]: {type(model)}")

# ===[ Train Test Split ]===
TARGET = "sales"
X, y = data.drop(TARGET, axis=1), data[TARGET]

print(f"===[ X ]===\n{X}")
print(f"===[ y ]===\n{y}")

X_train, X_test = X.iloc[:-15], X.iloc[-15:]
y_train, y_test = y.iloc[:-15], y.iloc[-15:]

print(f"===[ y_train ]===\n{y_train}")

inputs = [
    y_train.tolist(),
]

# === categorical covariates ===
dynamic_categorical_covariates = {
    # "week": [
    #     X_train['week'].tolist() + X_test['week'].tolist(),
    # ],
    "holiday": [
        X_train['holiday'].tolist() + X_test['holiday'].tolist(),
    ]
}
print(f"===[ numerical covariates ]===:\n{dynamic_categorical_covariates}")

static_categorical_covariates = {
    'store_id': ['store_A']
}

point_forecasts, _ = model.forecast_with_covariates(
    inputs=inputs,
    dynamic_categorical_covariates=dynamic_categorical_covariates,
    static_categorical_covariates=static_categorical_covariates,
    dynamic_numerical_covariates={},
    static_numerical_covariates={},
    xreg_mode="xreg + timesfm",  # Fit covariates first, then forecast residuals
    # ridge=0.0,
    # force_on_cpu=True,
    normalize_xreg_target_per_input=True,
)

print(f"===[ forecasts ]===\n{point_forecasts}")


# ===[ From Documentation ]====================================================
# # Historical sales (7 days context)
# ice_cream_sales = [30.0, 30.0, 4.0, 5.0, 7.0, 8.0, 10.0]
# sunscreen_sales = [5.0, 7.0, 12.0, 13.0, 5.0, 6.0, 10.0]
#
# inputs = [ice_cream_sales, sunscreen_sales]
#
# # Static covariates
# static_categorical_covariates = {
#     "category": ["food", "skin_product"],
# }
# static_numerical_covariates = {
#     "base_price": [1.99, 29.99],
# }
#
# # Dynamic covariates (7 days context + 7 days horizon = 14 values each)
# dynamic_categorical_covariates = {
#     "weekday": [
#         [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6],
#         [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6],
#     ],
#     "has_promotion": [
#         [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
#     ],
# }
# dynamic_numerical_covariates = {
#     "temperature": [
#         [31.0, 24.3, 19.4, 26.2, 24.6, 30.0, 31.1,
#             32.4, 30.9, 26.0, 25.0, 27.8, 29.5, 31.2],
#         [31.0, 24.3, 19.4, 26.2, 24.6, 30.0, 31.1,
#             32.4, 30.9, 26.0, 25.0, 27.8, 29.5, 31.2],
#     ],
# }
#
# print(f"Context length: {len(ice_cream_sales)} days")
# print(f"Forecast horizon: {horizon} days")
# print(f"Number of products: {len(inputs)}")
#
# # 2. Forecast with covariates (XReg + TimesFM mode)
# cov_forecast, xreg_only_forecast = model.forecast_with_covariates(
#     # horizon=horizon,
#     inputs=inputs,
#     dynamic_numerical_covariates=dynamic_numerical_covariates,
#     dynamic_categorical_covariates=dynamic_categorical_covariates,
#     static_numerical_covariates=static_numerical_covariates,
#     static_categorical_covariates=static_categorical_covariates,
#     xreg_mode="xreg + timesfm",  # Fit covariates first, then forecast residuals
#     ridge=0.0,
#     force_on_cpu=False,
#     normalize_xreg_target_per_input=True,
# )
#
# print("\nTimesFM + Covariates forecast:")
# print(f"  Ice cream: {cov_forecast[0]}")
# print(f"  Sunscreen: {cov_forecast[1]}")
#
# print("\nPure XReg forecast (for reference):")
# print(f"  Ice cream: {xreg_only_forecast[0]}")
# print(f"  Sunscreen: {xreg_only_forecast[1]}")
