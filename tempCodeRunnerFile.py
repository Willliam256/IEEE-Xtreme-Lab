def swap(stroke)->any:
#     global strokes
#     if stroke == "/":
#         return "\\"

#     elif stroke == "\\":
#         return "/"
#     elif stroke == "<":
#         return ">"
#     elif stroke == ">":
#         return "<"
#     elif stroke == "(":
#         return ")"
#     elif stroke == ")":
#         return "("
#     else:
#         return "" 

# def turn():
#     strokes[0], strokes[2] = swap(strokes[2]), swap(strokes[0])
#     strokes[3], strokes[5] = swap(strokes[5]), swap(strokes[3])
#     strokes[6], strokes[7] = swap(strokes[7]), swap(strokes[6])


# strokes = [" ", "o", " ", "/", "|", "\\", "/", "\\"]
# actionRoutine = int(input())
# for dances in range(actionRoutine):
#     numberOfActions = int(input())
#     for actions in range(numberOfActions):
#         #enter action
#         action = input().split()
        
#         actionToTake = action[0]

#         if actionToTake == "say":
#             print(' '.join(action[1::]))
#         else:
#             action = ' '.join(action)
#             if action == "left leg in":
#                 strokes[7] = ">"
#             elif action == "left leg out":
#                 strokes[7] = "\\"
#             elif action == "right leg in":
#                 strokes[6] = "<"
#             elif action == "right leg out":
#                 strokes[6] = "/"
#             elif action == "left hand to head":
#                 strokes[2] = ")"
#                 strokes[5] = " "
#             elif action == "left hand to hip":
#                 strokes[5] = ">"
#                 strokes[2] = ""
#             elif action == "left hand to start":
#                 strokes[5] = "\\"
#                 strokes[2] = ""
#             elif action == "right hand to head":
#                 strokes[0] = "("
#                 strokes[3] = " "
#                 strokes[1] = "o"
#             elif action == "right hand to hip":
#                 strokes[3] = "<"
#                 strokes[0] = ""
#                 strokes[1] = " o"
#             elif action == "right hand to start":
#                 strokes[3] = "/"
#                 strokes[0] = ""
#                 strokes[1] = " o"
#             elif action == "turn":
#                 turn()
#             else:
#                pass
        
#             print(f"{strokes[0]}{strokes[1]}{strokes[2]}\n{strokes[3]}{strokes[4]}{strokes[5]}\n{strokes[6]} {strokes[7]}")