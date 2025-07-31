#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀             𓐓  datasets.py 𓐔           
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀       Dev: oezzaou </var/spool/mail/oezzaou>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2025/07/31 13:30:23 by oezzaou
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2025/07/31 18:47:07 by oezzaou
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# ===[ Imports: ]==============================================================
from sklearn import datasets


# ===[ main: ]=================================================================
def main():
    # 1|> Toy datasets: quick demos used for learning
    iris_data = datasets.load_iris()
    print("======================[Toy Datasets]=======================")
    print(type(iris_data))  # sklearn.utils._bunch.Bunch
    # Extract Data from Bunch Object
    X = iris_data.data  # present the inputer features 'X' in NDArray Object
    print(f"X : {X}")
    print(f"X type: {type(X)}")
    Y = iris_data.target  # represent the target labels Y in NDArray Object
    print(f"Y : {Y}")
    print(f"Y type: {type(X)}")

    # NOTE:--------------------------------------------------------------------
    # - These kind of datasets can be called 'Toy Datasets' or 'Built-in'
    #   datasets.
    # - There is no available built-in method the list all the available
    #   datasets.

    print("======================[Real Datasets]======================")
    # 2|> Real / Download Datasets
    # These datasets are larger and the are fetched from the internet
    cal_data = datasets.fetch_california_housing()
    print(type(cal_data))
    print(f"X : {cal_data.data}\nX type: {type(cal_data.data)}")
    print(f"Y: {cal_data.target}\nY Type: {type(cal_data.target)}")
    # NOTE:> These datasets are called 'Fetched' or 'real-world' datasets

    print("====================[Generated Datasets]======================")
    gen_data = datasets.make_classification()
    print(type(gen_data))  # NOTE:> It is type is "Tuple"
    print(gen_data)
    print(f">>> tupe len: {len(gen_data)}")
    # NOTE:----------------------------------------------------------------
    # the generated datasets is a 'Tuple Object' instead of 'Bunch' Object
    # gen_data = (data, label)  => (X, Y)
    data = gen_data[0]
    print(f"X data: {data}\nX type: {type(data)}")
    label = gen_data[1]
    print(f"label: {label}\nlabel: {type(label)}")
    # NOTE:> These datasets are called 'generated' or 'asthytic' datasets

    # INFO:[ Summary: ]========================================================
    # Toy & Real datasets generates   => 'Bunch' object Bunch(data, label, ...)
    # Generated datasets generateds   => 'Tuple' object (data, label)


if __name__ == '__main__':
    main()
