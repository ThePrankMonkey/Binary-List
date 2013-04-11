base = int(raw_input('Please enter an integer length: '))
l = [bin(i)[2:].zfill(base) for i in range(2**base)]
print l
