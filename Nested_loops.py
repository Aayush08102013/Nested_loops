# take input of a word
string = input("please enter a word : ")
# take input of character 
char = input("please enter a character : ")
i = 0
count = 0
# loop will find the occurance of a character 
while(i < len(string)): # string operation
    if(string [i] == char): # condition 1
        count = count + 1
    i = i + 1
# display the result:
print(f"In the word {string}, the character {char} has occoured {count} times")

# To check wether a number is prime or not:
# take 2 inputs from the user:
low = int(input("Enter your lower range (EG 0 - 100, 0 is the lower range) : "))
upp = int(input("Enter your upper range (EG 0 - 100, 100 is the upper range) : "))
print(f"prime number between {low} and {upp} are:")
for num in range(low, upp + 1):
 # all prime numbers are greator than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# middle number:
num = int(input("Enter your number : "))
t = num
numLen = 0
# itirate the loop:
while t > 0:
    numLen = numLen + 1
    t = int(t/10)
if numLen >= 4: # condition 1
    numLen = int(numLen / 2)
    chk = 0
    while num > 0: # itirate loop
        rem = num % 10
        if chk == numLen: # nested conditon 1
            midOne = rem
        elif chk==(numLen - 1):
            midTwo = rem
        num = int(num / 10)
        chk = chk + 1
    prod = midOne * midTwo # product of two middle digits
    # display the result:
    print("\n Product of Mid Digits " + str(midOne) + str (midTwo) + " is",+ prod )
else:
    print("it is not a 4 digit number")
