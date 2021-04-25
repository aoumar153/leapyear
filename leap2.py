def main():
    while(True):
        year = input("Input the year you want to check: ")
    
        if(year.isdigit() == True and int(year) >= 0):
            break
        else:
            print("wront input buddy has to numbers and not negative")
    print(year)
    if(int(year)% 4 == 0):
        if(int(year)%100 ==0):
            if(int(year)% 400 == 0):
                print('This is a leap year')
            else: 
                print('not a leap year')
        else: 
            print('This is a leap year')
    else: 
        print('not a leap year') 
        
main()