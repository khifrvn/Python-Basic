# nested loops
#(x, y) --> value
#(0, 0) --> value

for x in range (4):
    for y in range (3):
        print(f'({x}, {y})')
print("=" * 30)

numbers = [5,2,5,2,2]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output )

print("=" * 30)

print("or u can use this trick on python for simple things")

nomer = [6,3,4,1,2,5]
for banyakBintang in nomer:
    print('x' * banyakBintang)
