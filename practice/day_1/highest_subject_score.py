'''
Find all subject names that have the highest score.
'''
scores = {"Math": 78, "Science": 88, "English": 72, "History": 88}

highest_score = 0 # in que there is no high score, do i want to assume or any other way?
subject_name = []

for score in scores:
    if scores[score] > highest_score:
        highest_score = scores[score]

for score in scores:
    if scores[score] == highest_score:
        subject_name.append(score) 

print(subject_name)
