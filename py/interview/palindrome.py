

str = "oussama"

for end in range(len(str), 0, -1):
    for start in range(len(str) - end + 1):
        print(str[start: start + end])
        print(f"start: {start} | end: {end}")
    print("==================================")
