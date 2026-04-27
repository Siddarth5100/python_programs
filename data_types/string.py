
# assiging values to empty string
'''
string = ""
print("string", string, type(string))

alphabets = ["B", "A", "C"]
print("alpha", alphabets, type(alphabets))

for alpha in alphabets:
    print(alpha)
    if not alpha == "A":
        string = alpha
        print(string)
        break

print("final", string)
'''

# 
'''
name = ""
print(name, type(name))

name = "siddarth"
print(name, type(name))
print(name[0])
print(name[-1])
print(len(name))
'''

val = "Hello"
user_input = input("Enter the Name: ")

sen = f"{val}, {user_input}"

print(sen * 3)

if "i" in sen:
    print("True")
else:
    print("False")

print(sen[:3])
print(sen[-2:])

