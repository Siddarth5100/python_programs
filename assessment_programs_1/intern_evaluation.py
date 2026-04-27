# interns = [
#         {"name": "Akash", "scores": [85, 92, 78]},
#         {"name": "Arjun", "scores": [40, 35, 28]},
#         {"name": "Akash", "scores": [85, 92, 78]}
#     ]

def evaluate_batch(interns):
    final_summary = []

    # check student and add 
    for intern in interns:
        if intern["name"] not in final_summary:
            student = {"name": intern["name"]}
            final_summary.append(student)

        # calculate average of marks
        total_marks = 0
        
        for score in intern["scores"]:
            print(score)

            total_marks = total_marks + score

        avg_cal = total_marks / len(intern["scores"])
        student["average"] = round(avg_cal, 2)

        # maximum score
        max_score = max(intern["scores"])
        student["high"] = max_score

        # minimum score
        min_score = min(intern["scores"])
        student["low"] = min_score

        # add grade
        if student["average"] >= 90:
            student["grade"] = "A"
        elif avg_cal >= 75:
            student["grade"] = "B"
        elif avg_cal >= 50:
            student["grade"] = "C"
        else:
            student["grade"] = "F"

        # add tag for the grades
        if student["grade"] == "A":
            student["tag"] = "Outstanding"
        elif student["grade"] == "B":
            student["tag"] = "Competent"
        elif student["grade"] == "C":
            student["tag"] = "Needs Improvement"
        else:
            student["tag"] = "Failed"

    return final_summary

# print(evaluate_batch([
#     {"name": "Alice", "scores": [85, 92, 78]},
#     {"name": "Bob", "scores": [40, 35, 28]}
#     # {"name": "Charlie", "scores": [95, "abc", 88]}
# ]))







# # print(interns, type(interns))
# # print(interns[0], type(interns[0]))

# def evaluate_batch(interns):
#     result = []
#     for intern in interns:
#     # print(intern, type(intern)) # {'name': 'Akash', 'scores': [85, 92, 78]} <class 'dict'>
#     # print(intern["name"]) # Akash
#     # print(intern["scores"]) # [85, 92, 78]

#         if not intern["name"] in result:
#         # print(intern["name"]) # Akash
#         # print("result", result, type(result)) # result [] <class 'list'>
#             result.append({"name": intern["name"]})

#         # print(result, type(result), result[0], type(result[0])) # [{'name': 'Akash'}] <class 'list'> {'name': 'Akash'} <class 'dict'>
#         # print(intern["scores"], type(intern["scores"]))
#         total_score = 0
#         for score in intern["scores"]:
#             # print(score) 
#             total_score += score
#             # print(total_score, type(total_score)) # 255 <class 'int'>

#             percentage = total_score * 100 / (len(intern["scores"]) * 100)
#             # print(percentage, type(percentage)) # 85.0 <class 'float'>
#             # print(result, type(result))
            
#             # result["average"] = percentage # wrong one
#             # result[] = {"average": percentage} # this will create dict
#             print(percentage)
            
#         print(result, type(result))
#         # result.append({"average": percentage})      
#         # print(result, type(result))

#         print(result[0], type(result[0]))

#         result[0]["average"] = percentage
#         print("-----------", )
#         print(result, type(result))



# # evaluate_batch([
#         # {"name": "Akash", "scores": [85,92,78]}
#         # {"name": "Arjun", "scores": [70,80,90]}
#     # ])