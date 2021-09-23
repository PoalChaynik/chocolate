lib = {'key':{'key1':'','key2':'','key3':''}}

x = input("input something: ")
lib['key']['key1'] = [x]

print(lib['key']['key1'])
print(lib)

while True:
    print(lib['key']['key1'])
    print(lib)