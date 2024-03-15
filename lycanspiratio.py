import sys
vin = []
x = lambda x: x-x/(x*2.314)
for num in range(int(sys.argv[1])):
    for integer in range(999):
        ints = str(num)+"."+str(integer)
        if (float(ints) != 0):
            vin.append(float(ints))
    if (num != 0):
        vin.append(num)
print(list(map(x, vin)))