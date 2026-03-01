#DiceRoll.py
#Name:Gavin Grow
#Date:03/1/26
#Assignment:dice roll

import random

def main():
    trials = 10000
    
    # index 0–12 
    counts = [0] * 13

    # simulate dice rolls
    for i in range(trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        counts[total] += 1

    # print results
    print("Total  Count   Percentage")
    for total in range(2, 13):
        count = counts[total]
        percentage = (count / trials) * 100
        print(f"{total:>5}  {count:>5}   {percentage:>6.2f}%")

    # check totals
    print("\nTotal rolls:", sum(counts))
    print("Percent total:", sum(counts[2:13]) / trials * 100)

if __name__ == "__main__":
    main()
