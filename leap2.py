def main():
    year = input("Input the year you want to check: ")
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