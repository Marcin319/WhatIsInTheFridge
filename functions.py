import os
def recipes(data):
    os.system("cls")
    print('These are recipes in data base:\n')
    x = list(data['Recipe'])
    m=0
    for i in x:
        if m != 4:
            print(i, end='; ')
            m+=1
        else:
            print(i, end=';\n')
            m=0

def products(data):
    x=list(data.columns.values)
    m=1 #variable for counting expressions
    for i in x:
         if i != 'Recipe':
             if m != 4:
                print(i, end='; ')
                m+=1
             else:
                print(i, end=';\n')
                m=0

def prodNeeded(data):

    ktora = 0
    while ktora==0:
        m = 0
        x = str(input('Products for which recipe do you want to know?:\n'))
        for i in data['Recipe']:
            m += 1
            if i == x:
                ktora=m-1
    n = 0
    wh = []
    # print(ktora)
    x = data.loc[ktora]
    z = list(data.columns.values)
    for i in x:
        n += 1
        if i == 1.0:
            wh.append(n)
    # print(wh)
    y=len(wh)-1
    print('\n')
    while y>-1:
        f = wh[y]-1
        print(z[f])
        y-=1
    input('\n\nPress ENTER to back to menu')
def findingFood(data):
    i=0
    listunia=[]

    while i<=len(data.columns.values):
        os.system('cls')
        print('\tPlease enter the names of the products you have in the fridge.\nIf you have no more products, enter \'end\'.\nHere are the products that are in the database:\n')
        products(data)
        print('\n')
        if len(listunia)!=0:
            print('\n\tWritten products:')
        p = 0
        while p < len(listunia):
            if p % 4 == 0 and p!=0:
                print(end='\n')
            print(listunia[p], end='; ')
            p += 1
        wybor3=str(input())
        if wybor3=='end':
            i=len(data.columns.values)+1
        else:
            m=0
            for o in list(data.columns.values):
                if wybor3==o:
                    k=0
                    l=0
                    while l<len(listunia):
                        if listunia[l]==wybor3:
                            k+=1
                        l+=1
                    if k==0:
                        listunia.append(wybor3)
                        m=1
                    else:
                        input('\nThe product has already been entered.\n\nPress ENTER to proceed.\n')

                    i += 1
            if m==0 and k==0:
                input('\nThis item does not exist in our database.\n\nPress ENTER to proceed.\n')

    print(listunia)
    m = 0
    x = list(data.columns.values)
    listunia2=[]

    for i in x:
        for o in listunia:
            if i==o:
                listunia2.append(m+1)
        m+=1
    print(listunia2)

    i=0
    included = []
    while i<len(data.Recipe):
        m=0
        inc = []
        for y in data.loc[i]:
            m+=1
            if y==1.0:
                inc.append(m)
        included.append(inc)
        i+=1
    print(included)

    m=0
    needed = []
    owned = []
    while m < len(included): #dopóki m jest mniejsze niż ilość wszystkich tablic
        ow = [] # wyzerowanie tablicy ow
        for i in included[m]: # dla każdego elementu pojedynczej tablicy included
            for o in listunia2: # dla każdego elementu listunia2
                if i == o: #jeżeli element tablicy w tablicy included jest taki sam, jak element tablicy listunia2, to
                    ow.append(o) #do tablicy ow dodaj element tablicy
                # else:
                #     ne.append(i)
        ne = included[m]
        for u in ow:
            ne.remove(u)
        owned.append(ow)
        needed.append(ne)
        m += 1

    print(owned)
    print(needed)
    print(len(included),'; ',len(owned), '; ',len(needed))
    print(x)

    m=0
    owW=[]
    for i in owned:
        owW2 = []
        for o in owned[m]:
            owW2.append(x[o-1])
        owW.append(owW2)
        m+=1
    print(owW)
    print(len(owW))

    m = 0
    neW = []
    for i in needed:
        neW2 = []
        for o in needed[m]:
            neW2.append(x[o - 1])
        neW.append(neW2)
        m += 1
    print(neW)
    print(len(neW))

    print(len(owned[0]))
    l=(owned[0]+needed[0])
    print(len(l))
    print(float(len(owned[0])/len(l))*100)

    m=0
    sor=[]
    while m<len(included):
        sor.append([m, int((float(len(owned[m])/len(owned[m]+needed[m]))*100)//1)])
        m+=1
    print(sor)

    m=False

    while m != True:
        n = 1
        b = 0
        while n<len(included):
            if sor[n-1][1]<sor[n][1]:
                o=sor[n-1]
                sor[n-1]=sor[n]
                sor[n]=o
                b+=1
            n+=1
        if b==0:
            m=True
    print(sor)

    os.system('cls')
    print('\tHere are recipes to do:\n')

    y=data.Recipe
    m=0
    while m<len(sor):
        if sor[m][1] != 0:
            print('\n[',y[sor[m][0]],']: [',sor[m][1],'%]', end='\n')
            print('\t[Owned]: ', end='')
            for i in owW[sor[m][0]]:
                print(i, end=', ')
            print('\n\t[Needed]: ', end='')
            for i in neW[sor[m][0]]:
                print(i, end=', ')
            print('\n')
        m+=1

    input('\nPress ENTER to continue')

























