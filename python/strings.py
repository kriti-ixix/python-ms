print("hello")
s1=str("h")
print(s1)
s2="hello"
print(s2[4])
print(min(s2))
print(len(s2))
print(s2[-3])
s=("python")
for ch in s:
    print(ch, end="")

st="india"
i=0
while i<len(st):
    print(st[i])
    i=i+1

print(st[1:3])
s5="hello, i love python"
print(s5[0:len(s5):3])
print(s5[::])
print(s5[::-1])
s4=4*s2
print(s4)
s1="onetwothree"
s2=s1[0:3]+2*s1[3:6]+3*s1[6:11]
print(s2)
n= int(input('enter i'))
string = input('enter str')
start = 1
j=0
for i in range(0, n+1):
    
        print (string[0:i])
