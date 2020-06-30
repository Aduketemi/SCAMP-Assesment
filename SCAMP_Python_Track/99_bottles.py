# 99 Bottles
# Create a program that prints out every line to the song "99 bottles of beer on the wall."
# Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
# Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
# Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
def bottles_song(num):
    while num > 1:
        print ("{} bottles of beer on the wall. \n{} bottles of beer, take one down pass it around".format(num,num))
        num -= 1
    if num == 1:
        print("{} bottle of beer on the wall. \n{} bottle of beer, take one down pass it around".format(num,num))
        
    print("If that bottle should happen to fall, \nNo bottle of beer on the wall")


print(bottles_song(10))