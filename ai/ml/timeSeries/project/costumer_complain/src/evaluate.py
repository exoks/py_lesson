#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀             𓐓  evaluate.py 𓐔           
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀      Eng: oezzaou <oussama.ezzaou@gmail.com>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2025/08/27 15:05:40 by oezzaou
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2025/08/28 14:25:06 by oezzaou
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# ===[ Imports ]===============================================================
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error


# ===[ plot_forecasts ]========================================================
def plot_forecasts(train, test, forecasts, title):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(train, label="train")
    # ax.plot(test, label="test")
    ax.plot(forecasts, label="forecasts")
    ax.set_title(title)
    plt.legend()
    plt.show()


# ===[ compute_forecast_metrics ]==============================================
def compute_forecast_metrics(forecasts, actuals):
    mae = mean_absolute_error(actuals, forecasts)
    rmse = root_mean_squared_error(actuals, forecasts)
    mape = mean_absolute_percentage_error(actuals, forecasts)

    metrics = {
        'MAE': mae,
        'RMSE': rmse,
        'MAPE': mape * 100
    }
    # NOTE:-------------------------------------------------------------------
    # - We do not really have a baseline here, so what we are imporoving from
    return metrics


# ===[ evaluate_model ]========================================================
def evaluate_model(model, train_set, test_set, plot=True):
    # 1. train the model
    trained_model = model.fit()
    # 2. test the model
    forecasts = trained_model.forecast(18)
    print(forecasts)
    # 3. Compute 'metrics'
    # metrics = compute_forecast_metrics(test_set, forecasts)
    # 4. Visualize forecasts compared to `test_set`
    if plot is True:
        plot_forecasts(train_set, None, forecasts, "Holt winter forecasts")
    return forecasts, None


# INFO:[ `evaluate.py` ]-------------------------------------------------------
# - This file does:
#   1. 'regression_metrics': computes numerical evaluation metrics (MAE, RMSE
#      , R^2)
#   2. 'plot_predictions': plots actual vs predicted (especially useful for
#       time series)
#   3. 'evaluate_model': a wrapper that ties everything together:
#      [ prediction + metrics + visualization ]
# - This makes 'evaluate.py' reusable: you just call:
#   > evaluate_model(trained_model, X_test, y_test) from anywhere in your
#     pipeline

# ===[ This is a good example  for 'evaluate.py' model ]=======================
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
#
#
# def regression_metrics(y_true, y_pred):
#     """
#     Compute common regression / forecasting metrics.
#     """
#     mae = mean_absolute_error(y_true, y_pred)
#     mse = mean_squared_error(y_true, y_pred)
#     rmse = np.sqrt(mse)
#     r2 = r2_score(y_true, y_pred)
#
#     metrics = {
#         "MAE": mae,
#         "MSE": mse,
#         "RMSE": rmse,
#         "R2": r2
#     }
#
#     return metrics
#
#
# def plot_predictions(y_true, y_pred, title="Model Predictions vs Actuals"):
#     """
#     Plot actual vs predicted values.
#     Useful for time series or regression evaluation.
#     """
#     plt.figure(figsize=(10, 5))
#     plt.plot(y_true, label="Actual", marker="o")
#     plt.plot(y_pred, label="Predicted", marker="x")
#     plt.title(title)
#     plt.xlabel("Index / Time")
#     plt.ylabel("Value")
#     plt.legend()
#     plt.grid(True)
#     plt.show()
#
#
# def evaluate_model(model, X_test, y_test, plot=True):
#     """
#     Full evaluation pipeline:
#     - Generate predictions
#     - Compute metrics
#     - Optionally plot results
#     """
#     y_pred = model.predict(X_test)
#     metrics = regression_metrics(y_test, y_pred)
#
#     print("Evaluation Metrics:")
#     for k, v in metrics.items():
#         print(f"{k}: {v:.4f}")
#
#     if plot:
#         plot_predictions(y_test, y_pred)
#
#     return metrics, y_pred
#
#
# # Example usage (if running this file directly)
# if __name__ == "__main__":
#     # Fake example data
#     y_true = np.array([3, 5, 7, 9, 11])
#     y_pred = np.array([2.8, 5.1, 6.9, 9.2, 10.7])
#
#     print("Testing evaluation.py...")
#     metrics = regression_metrics(y_true, y_pred)
#     print(metrics)
#     plot_predictions(y_true, y_pred)
