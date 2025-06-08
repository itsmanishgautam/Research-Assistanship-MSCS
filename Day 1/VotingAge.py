Age = int(input("Enter your Age:"))
def can_vote(Age):
    if (Age<18):
        print("You cannot Vote")
    else:
        print("You can vote")

can_vote(Age)