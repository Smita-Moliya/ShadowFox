# Step 1: Initial Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("1. Original Justice League members:")
print(justice_league)

# Step 2: Calculate number of members
num_members = len(justice_league)
print("\n2. Number of members:", num_members)

# Step 3: Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\n3. After adding Batgirl and Nightwing:")
print(justice_league)

# Step 4: Move Wonder Woman to the beginning (as leader)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n4. After making Wonder Woman the leader:")
print(justice_league)

# Step 5: Separate Aquaman and Flash by inserting Green Lantern in between
# First, remove Green Lantern so we can reposition it
justice_league.remove("Green Lantern")

# Get the index of Aquaman and insert Green Lantern after Aquaman
index_of_aquaman = justice_league.index("Aquaman")
justice_league.insert(index_of_aquaman + 1, "Green Lantern")
print("\n5. After separating Aquaman and Flash using Green Lantern:")
print(justice_league)

# Step 6: Crisis - Replace list with a new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\n6. New Justice League team after crisis:")
print(justice_league)

# Step 7: Sort alphabetically and assign leader at index 0
justice_league.sort()
print("\n7. After sorting alphabetically (new leader at index 0):")
print(justice_league)
print("New leader is:", justice_league[0])
