rows = int(input("Enter the number of rows:"))
current_number = int(1)

for i in range(rows):

    for j in range(i + 1):
        print(current_number, end=' ')

        current_number += 1
    print ()