while 1:
    i=0
    import random
    n = random.randint(0,20)
    print("u have only 9 guesses after 9 try u will loss the game\nYou have to guess the number in range 0 to 20\n")
    while(1):
        while i<9:
            j=int(input("Enter your no.:\n"))
            if j<n:
                i=i+1
                print("u have entered smaller number")
                if(i >= 6):
                    print("Hurry Up!!! Only %s chancees left"%(9-i))
                continue
            if j>n:
                i=i+1
                print("\nu have entered bigger number")
                if(i >= 6):
                    print("Hurry Up!!! Only %s chancees left"%(9-i))
                continue
            if j == n:
                print("\ncongrates u won the game☻☻☻♥")
                print("\nu have complete the game in", i+1,end=" ")
                print("guesses")
                break
            i=i+1
            break
        if i == 9:
            print("\n\nSorry! u loss the game")
        break
    A = int(input("\n\npress 1 to play the GAME again\npress 2 to exit from the game\nEnter Your Choose:-"))
    if A ==1:
        continue
    else:
        break


    #print("Sorry! u loss the game ")
