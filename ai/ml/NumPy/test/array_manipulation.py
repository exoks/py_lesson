#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀   𓐓  array_manipulation.py 𓐔           
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀       Dev: oezzaou </var/spool/mail/oezzaou>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2025/06/19 16:47:37 by oezzaou
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2025/06/28 19:00:57 by oezzaou
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# ===[ Import: ]===============================================================
import numpy as np


# ===[ main: ]=================================================================
def main():
    arr = np.array([1, 2, 3, 4, 5, 7])
    arr_reshaped = np.reshape(arr, (3, 2))

    print(f"arr => {arr}")
    print("=======[Reshape:(3, 2)]=============")
    print(f"reshaped array : {np.reshape(arr, (3, 2))}")
    print("=======[reshape to size=(3, 3)]=====")
    try:
        np.reshape(3, 3)
    except BaseException as e:
        print(e)

    print("======[np.append(-1)]=========")
    print(f"append to 1D array: {np.append(arr, -1)}")
    print(f"reshaped_array  :\n{arr_reshaped}")
    # Append a [1, 2] as the last row
    print(f"append row [1, 2] to 2D array: {
          np.append(arr_reshaped, [[1, 2]], axis=0)}")
    # Append a 4, as the last column of each row
    print(f"append column [[4], [4], [4]] to 2D array: {np.append(
        arr_reshaped, [[4], [4], [4]], axis=1)}")

    print("==========[np.insert()]========")
    print(f"insert 7 at index 1: 1D array {np.insert(arr, 0, [1, 2])}")
    print(f"insert row [-1, -1] at index 2:\n{
          np.insert(arr_reshaped, 2, [-1, -1], axis=0)}")
    print(f"insert columns 0 at index 2:\n{
          np.insert(arr_reshaped, 1, 0, axis=1)}")

    print("========[np.vstack()]==========")
    arr1 = np.zeros(shape=(2, 2), dtype=np.int32)
    arr2 = np.array([-1, -1])
    print(f"vstack [-1, -1] on the top of arr2\n{np.vstack((arr1, arr2))}")
    print(f"hstack [-1, -1] on the right of arr2\n"
          f"{np.hstack((arr1, np.reshape(arr2, shape=(2, 1))))}")

    print("=========[np.split()]==========")
    print(f"arr1:\n{arr1}")
    print(f"split arr1 into 2 arrays => {np.split(arr1, 2)}")

    print("=====[np.isnan()/np.inf]=======")
    arr3 = np.array([1, 4, 5, np.nan, 8, -np.inf])
    print(f"arr: {arr}")
    print(f"isnan: {np.isnan(arr3)}")
    print(f"isinf: {np.isinf(arr3)}")

    print("========[np.concatenate()]=======")
    print(f"arr1 + arr3 {np.concatenate((arr2, arr3))}")

    print("=======[np.array_equale()/equal()/not_equale]=======")
    print(f"(arr1 == arr2) => {np.array_equal(arr2, arr3)}")
    print(f"(arr1 == arr2) => {np.equal([1, 2, 4], [1, 2, 3])}")
    print(f"(arr1 == arr2) => {np.not_equal([1, 2, 4], [1, 2, 3])}")

    print("======[arr.T: Transopse array]================")
    arr = np.array([[1, 2],
                    [3, 4]])

    print(f"arr:\n{arr}")
    print(f"transposed arr =>\n{arr.T}")

    print("============[np.repeat()]=================")
    print("np.repeat([1, 2, 3], 2)")
    arr = np.repeat([1, 2, 3], 2)
    print(arr)
    print("np.repeat([1, 2, 3], [1, 2, 3])")
    arr = np.repeat([1, 2, 3], [1, 2, 3])
    print(arr)

    print("=============[np.tile()]=============")
    print("np.tile([1, 2, 3], (2, 3))")
    arr = np.tile([1, 2, 3], (2, 3))
    print(arr)

    print("np.tile([1, 2, 3], 2)")
    arr = np.tile([1, 2, 3], 2)
    print(arr)


if __name__ == '__main__':
    main()
