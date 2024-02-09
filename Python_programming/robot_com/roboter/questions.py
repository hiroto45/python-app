import csv
from termcolor import colored
from string import Template

class Robot(object):
    def __init__(self, user_name='' , IsLikeRestrount=''):
        self.data = []
        with open('robot_com/recommendlist/RobotRecommendList.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_object = {'Name': row['Name'], 'Count': row['Count']}
                self.data.append(data_object)

    def IsnameQuestios(self):
        while True:
            with open('robot_com/robot_q1', 'r', encoding='utf-8') as f:
                text = f.read()
                print(text)

            user_name = input()
            if user_name:
                self.user_name = user_name
                break
    def print_thanks(self):
        with open('robot_com/robot_thx', 'r', encoding='utf-8') as f:
            text = f.read()
            templete = Template(text)
            result = templete.substitute(user_name=self.user_name)
            print(result)
    def isfavoriterestaurant(self):
        while True:
            with open('robot_com/robot_q2', 'r', encoding='utf-8') as f:
                text = f.read()
                templete = Template(text)
                result = templete.substitute(user_name=self.user_name)
                print(result)
            IsLikeRestrount = input()
            if IsLikeRestrount:
                IsLikeRestrount = IsLikeRestrount.title()
                with open('robot_com/recommendlist/RobotRecommendList.csv', "a", newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    #csvファイルにカウントを追加するか否かの判定
                    keys = [obj for obj in self.data if IsLikeRestrount == obj['Name']]
                    if not keys:
                        writer.writerow([IsLikeRestrount, 1])
                        self.print_thanks()
                    else:
                        for obj in self.data:
                            if obj['Name'] == IsLikeRestrount:
                                obj['Count'] = int(obj['Count']) + 1
                                with open('robot_com/recommendlist/RobotRecommendList.csv', "w", newline='') as csv_file:
                                    fieldnames = ['Name','Count']
                                    writer = csv.DictWriter(csv_file , fieldnames=fieldnames)
                                    writer.writeheader()
                                    writer.writerows(self.data)

                        self.print_thanks()
                break
    def Recommend(self):
        #まずはリストがない場合の処理
        if not self.data:
            self.isfavoriterestaurant()
        else:
            #すでにデータがあるとき( ロボットがレストランのおすすめを行うアルゴリズムを構築)
            maxcount = 0
            mostpopularrest = ""
            RestaurantList = []

            with open('robot_com/recommendlist/RobotRecommendList.csv' , 'r') as csv_file:
                reader = csv.DictReader(csv_file)#csvファイルのデータをオブジェクト型で取得する
                for row in reader:
                    RestaurantList.append(row['Name'])
                    Count = int(row['Count'])
                    if Count > maxcount:
                        maxcount = Count
                        mostpopularrest = row['Name']
            with open('robot_com/robot_recommend', 'r', encoding='utf-8') as f:
                text = f.read()
                templete = Template(text)
                result = templete.substitute(RecommendRestaurant = mostpopularrest)
                print(result)

                RobotQuestionAnswer = input()
                if RobotQuestionAnswer == 'No' or RobotQuestionAnswer == 'no' or RobotQuestionAnswer == 'n':
                    if len(RestaurantList) == 1:
                        self.isfavoriterestaurant()
                    #最初のおすすめを否定されたのでリストから削除
                    RestaurantList.remove(mostpopularrest)
                    for i in range(0 , len(RestaurantList)):
                        with open('robot_com/robot_recommend', 'r', encoding='utf-8') as f:
                            text = f.read()
                            templete = Template(text)
                            result = templete.substitute(RecommendRestaurant=RestaurantList[i])
                            print(result)
                            IsAnswer = input()
                            #おすすめのレストランを提示しYESまたはループ終了を受け取った
                            if IsAnswer in['Yes' , 'Y' , 'yes' , 'y'] or i == len(RestaurantList) - 1:
                                self.isfavoriterestaurant()
                                break
                               # while True:
                               #     with open('robot_com/robot_q2', 'r', encoding='utf-8') as f:
                               #         text = f.read()
                               #         templete = Template(text)
                               #         result = templete.substitute(user_name=self.user_name)
                               #         print(result)
                               #     IsLikeRestrount = input()
                               #     if IsLikeRestrount:
                               #         IsLikeRestrount = IsLikeRestrount.title()
                               #         with open('robot_com/recommendlist/RobotRecommendList.csv', "a",newline='') as csv_file:
                               #             writer = csv.writer(csv_file)
                               #             writer.writerow([IsLikeRestrount, 1])
                               #         self.print_thanks()
                               #         break
                elif RobotQuestionAnswer == 'Yes' or RobotQuestionAnswer == 'yes' or RobotQuestionAnswer == 'y':
                    self.isfavoriterestaurant()













