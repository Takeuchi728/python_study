counter = 0

while counter < 10:
    counter += 1
    print(counter)

for num in range(100):
    print(num)

    if num == 10:
        break

for num in range(100):

    if num % 10:
        continue

    print(num)

for i in range(-2, 5):
    print(i)
