print('choose countries from the given list: a. INDIA(0); b.USA(1); c.Austrilia(2)')
print('Use the code given in the bracet for respective countries and states to access them')
cnt = eval(input('enter the country code: '))
if(cnt == 0):
    print('enter the state name; choose countries from the given list: a.Andra Pradesh(0) b.Telangana(1) c. Karnataka(2) ')
    states = eval(input('enter the states: '))
    if(states == 0):
        print('The disricts are: ')
        print('Guntur')
        print('Amaravathi')
        print('Tirupathi')
        print('telani')
        print('and etc')
    elif(states == 1):
        print('The disricts are: ')
        print('Hyderabad')
        print('Warangal')
        print('Nalgonda')
        print('Khammam')
        print('and etc')
    else:
        print('The districts are')
        print('Ramanagara')
        print('Shivamogga')
        print('Davangere')
        print('Chitradurga')
        print('and etc')
elif(cnt == 1):
    print('enter the state name; choose countries from the given list: a. California(1) b. Alaska(0) c.  Georgia(2) ')
    states = eval(input('enter the states: '))
    if(states == 0):
        print('The disricts are: ')
        print(' Gateway  District')
        print('Berlin Strait  District')
        print('Dillingham City School District')
        print('Iditarod Area School District')
        print('and etc')
    elif(states == 1):
        print('The disricts are: ')
        print('Alameda')
        print('Francisco')
        print('Solano')
        print('Sacramento')
        print('and etc')
    else:
        print('the districts are: ')
        print('Atkinson County School District')
        print('Bacon County School District')
        print('Atlanta Public Schools')
        print('Appling County School District')
        print('and etc')
else:
    if(cnt == 2):
        print('enter the state name; choose countries from the given list: a. New south wales(0) b. Western austrilia(1) c.  Tusmania(2) ')
        states = eval(input('enter the states: '))
        if(states == Newsouthwales):
            print('The disricts are: ')
            print('Sydney')
            print('Broken Hill')
            print('Dubbo')
            print('Albury')
            print('and etc')
        elif(states == Westernaustrlia):
            print('The disricts are: ')
            print('Perth')
            print('Albeny')
            print('Bunbury')
            print('Broome')
            print('and etc')
        else:
            print('the districts are: ')
            print('Devonport')
            print('Burnie')
            print('Wynyard')
            print('New norfolk')
            print('and etc')
    else:
        print('The input is invalid')
    
    
        
        
