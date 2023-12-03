import os
d3={}
def bidding():
    print("Welcome to secret Auction Programme")
    i1=input("What is your Name:")
    print("Hello",i1)
    bid_= int(input("Please Enter Your Bid Amount: $"))
    d3[i1]=bid_

def bid_again():

    while 1>0:
    
        i2=input("Are there any other bidder? Type 'yes' or 'no':").lower()
        if i2=="yes":
            os.system('cls' if os.name == 'nt' else 'clear ')
            bidding()
        elif i2=="no":
            i4=0
            for i in d3:
                print(i,"=",d3[i])
                if i4<d3[i]:
                    i4=d3[i]
                else:
            
                    continue
            for i in d3:
                if d3[i]==i4:
                    print("Congratulation",i,",you are the winner of this bid with highest bid of $",i4,".")
                     
            #print("Congratulation",i1,"You Won the bid")
            break
        else:
            print("Wrong input")
            continue
bidding()
bid_again()


