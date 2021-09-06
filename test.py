arr = []

while True:
    num = input()
    if num == ".":
        break
    else:
        arr.append(float(num))
    
    
minimum = arr[0]

for i in range(0, len(arr)):
    if arr[i] < minimum:
        minimum = arr[i]

print(minimum)
