def bottles_song(num):
    while num > 1:
        print ("{} bottles of beer on the wall. \n{} bottles of beer, take one down pass it around".format(num,num))
        num -= 1
    if num == 1:
        print("{} bottle of beer on the wall. \n{} bottle of beer, take one down pass it around".format(num,num))
        
    print("If that bottle should happen to fall, \nNo bottle of beer on the wall")


print(bottles_song(10))