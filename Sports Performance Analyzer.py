name = input("Enter your name:")

sport = input("Enter your sport:")
scores = []

for i in range(1, 6):
    while True:
        try:
            s = int(input(f"Enter match {i} score:"))
            scores.append(s)
            break
        except ValueError:
            print("Invalid input! Please enter a whole number.")

print("Scores:", scores)

highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)

print("Highest score:", highest)
print("Lowest Score:", lowest)
print("Average Score:", average)

if average >= 80:
    rating = "Excellent"
elif average >= 60:
    rating = "Good"
else:
    rating = "Improvement"

with open("sabu.txt", "w") as file:
    file.write(
        f"\nAthlete: {name}"
        f"\nSport: {sport}"
        f"\nScores: {scores}"
        f"\nHighest: {highest}"
        f"\nLowest: {lowest}"
        f"\nAverage: {average}"
        f"\nRating: {rating}\n"
    )

print("Data saved")
