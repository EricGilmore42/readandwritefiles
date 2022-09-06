def main(): 
    y = 1 

    name = open('clients.txt', 'r')

    for x in name:
        print(str(y) +  '. ', x.rstrip('\n'), sep='')
        y += 1 

main()