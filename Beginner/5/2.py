total = 100
set_size = 10
completed = 0

for i in range(0, total, set_size):
    completed += set_size
    print(f"\nYou completed {completed} jumping jacks.")
    
    if completed == total:
        print("🎉 Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()
    
    if tired in ['yes', 'y']:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ['yes', 'y']:
            print(f"\nYou completed a total of {completed} jumping jacks.")
            break
        else:
            remaining = total - completed
            print(f"{remaining} jumping jacks remaining. Let's continue!")
    else:
        remaining = total - completed
        print(f"{remaining} jumping jacks remaining. Let's continue!")
