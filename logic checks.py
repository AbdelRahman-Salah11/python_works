my_first_game=int(input("what's the value of first game "))
my_2ed_game=int(input("what's the value of 2ed game "))
if my_first_game+my_2ed_game>=10:
    print("you win with the points of",my_first_game + my_2ed_game)
elif 5<(my_first_game+my_2ed_game)<10:
    print("good one but it's not enough")
else:
    print('hard luck next time')    
    