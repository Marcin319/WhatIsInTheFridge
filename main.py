import os
import pandas as pd
import functions as fc
import sys
data=pd.read_csv('Składniki do potraw - Dania glowne.csv', sep=',') #taking data to application
dataz=data.fillna(0) #filling empty places in data by zeros
while True:
    os.system('cls')
    print('\tHello, what is in your fridge?\n1. Tell names of products to check recipes\n2. Check recipes in library\n3. Check products in library\nELSE: EXIT\n') #menu
    wybor=str(input())
    if wybor == '1234':
        print(dataz.loc[0])
    elif wybor == '1':
        fc.findingFood(dataz)
    elif wybor=='2':
        fc.recipes(dataz)
        print('\n\nWhat do you want to do?\n\t1. Check products to recipe\n\tELSE: Back to menu')
        wybor2=str(input())
        if wybor2=='1':
            fc.recipes(dataz)
            print('\n')
            fc.prodNeeded(dataz)
    elif wybor=='3':
        os.system('cls')
        fc.products(dataz)
        input('\n\nPress ENTER to back to menu')
    else:
        sys.exit(0)