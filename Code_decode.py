# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

st = input("Enter message ")
words = st.split(" ")
selec = int(input("Enter 1 for coding and 2 for decoding : "))
if(selec == 1):
    print("## Coding ##")
    new = []
    for word in words:
      if(len(word)>=3):
        r1 = "skd"
        r2 = "edk"
        stnew = r1 + word[1:] + word[0] + r2
        new.append(stnew)
      else:
        new.append(word[::-1])
    print(" ".join(new))    

if(selec == 2):
    print("## Decoding ##")
    new = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            new.append(stnew)
        else:
            new.append(word[::-1])
    print(" ".join(new))
        
else:
   print("please Enter valid choice")
   exit(0)        
  