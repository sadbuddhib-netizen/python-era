
name = input("Enter your name:")

sport = input("Enter your sport:")
scores = []
for i in range(1,6):
    s = int(input(f"Enter match {i} score:"))
    scores.append(s)

print("Scores:", scores)
print("Highest score:", max(scores))
print("Lowest Score",min(scores))
print("Average Score",sum(scores)/len(scores))



if sum(scores)/len(scores) >= 80:
    rating="Excellent"
elif sum(scores)/len(scores) >= 60:
    rating="Good"
else:
    rating ="Improvement"  

file = open("sabu.txt","w")
file.write(
    f"\nAthlete: {name}"
    f"\nSport: {sport}"
    f"\nScores: {scores}"
    f"\nHighest: {max(scores)}"
    f"\nLowest: {min(scores)}"
    f"\nAverage: {sum(scores)/len(scores)}"
    f"\nRating: {rating}\n"
)
print("data saved")
file.close()
    










