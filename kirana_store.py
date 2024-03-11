# kirana store business

kirana = ("oil", "aata", "sabji", "fruit", "biskyut", "gud", "aam")
sum = 0
while True:
    for i in range(0,7):
        count = kirana[i]
        userInput = print(f"The item name is {count} :")
        userInput = input("Enter its price or press q to quit : \n")
    
        if(userInput != 'q'):
            sum = sum + int(userInput)
            print(f"order total so far : {sum}\n")
            count = kirana[i + 1]    
        else:
            print(f"Your bill total is {sum}.\n")
            print("Thanks for shopping with us")
            break
    break 