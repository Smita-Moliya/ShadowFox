import random

rolls = 20
count_6 = 0
count_1 = 0
consecutive_6s = 0
previous_roll = 0

for i in range(rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")
    
    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            consecutive_6s += 1
    if roll == 1:
        count_1 += 1
    
    previous_roll = roll

print("\n--- Statistics ---")
print("Total rolls:", rolls)
print("Number of times 6 was rolled:", count_6)
print("Number of times 1 was rolled:", count_1)
print("Number of times two 6s were rolled in a row:", consecutive_6s)
