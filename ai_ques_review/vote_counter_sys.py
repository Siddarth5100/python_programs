votes = [
    "Arun", "Bala", "Arun", "Charu",
    "Bala", "Arun", "Deepa", "Charu",
    "Arun", "Bala", "Deepa", "Deepa", "Deepa"
]

'''
1. Count votes for each person

{
    "Arun": 4,
    "Bala": 3
}
'''

count_vote = {}

for vote in votes:
    if vote not in count_vote:
        count_vote[vote] = 0
    count_vote[vote] += 1

# print(count_vote)

'''
2. Find winner
Winner: Arun - 4 votes
'''

count = 0
name = ""
for key, val in count_vote.items():
    if val > count:
        count = val
        name = key

# print(f"Winner: {name} - {count} votes")

'''
3. Print candidates with LESS THAN 2 votes
'''

for key, val in count_vote.items():
    if val < 2:
        # print(key)
        pass

same_count = []
'''
Tie detected
'''

print(count)

for key, val in count_vote.items():
    print(key, val)
    if val == count:
        same_count.append(key)

if len(same_count) > 1:
    print("Tie detected")