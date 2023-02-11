data = [1, 3, 5, 7, 9]
with open('number.txt', 'w') as f:
    for num in data:
        f.write(str(num) + '\n')