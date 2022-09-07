# read file
f=open("funny.txt","r")
for line in f:
    print(line)
f.close()

# with statement
with open("funny.txt","r") as f:
    for line in f:
        print(line)
        
# readlines()
with open("funny.txt","r") as f:
    lines = f.readlines()
    print(lines)

# write file
with open("love.txt","w") as f:
    f.write("I love python")

# same file when you write i love javascript the previous line goes away
with open("love.txt","w") as f:
    f.write("I love python")

# You can use append mode to stop having previous lines overwritten
with open("love.txt","a") as f:
    f.write("I love python")

# show a picture of file open modes (12:12 in old video)

# writelines
with open("love.txt","w") as f:
    f.writelines(["I love C++\n","I love scala"])

# program to perform data analytics on cricket player's performance
player_scores = {}
with open("scores.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        player = tokens[0]
        score = int(tokens[1])
        if player in player_scores:
            player_scores[player].append(score)
        else:
            player_scores[player] = [score]

print(player_scores)

for player, score_list in player_scores.items():
    min_score=min(score_list)
    max_score=max(score_list)
    avg_score=sum(score_list)/len(score_list)

    print(f"{player}==>Min:{min_score}, Max:{max_score}, Avg:{avg_score}")
