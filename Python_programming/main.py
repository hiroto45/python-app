from robot_com.roboter import questions
TalkRobot = questions.Robot()
TalkRobot.IsnameQuestios()
TalkRobot.Recommend()
# import csv
#
# with open('robot_com/recommendlist/RobotRecommendList.csv' , 'w', newline='') as csv_file:
#     fieldsnames = ['Name' , 'Count']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldsnames)
#     writer.writeheader()
#     writer.writerow({'Name' : 'apple store' , 'Count' : 1})
