# #Dictionary
# '''
# students={"name":"Kim Inha","age":23, "eyes":[0.9,1.1]}
#
# for i,j in students.items():
#     print(f"{i}= {j}")
#
# print(f"이름은 {students['name']}, 나이는{students['age']}",end=' ')
# print(f"시력은 좌:{students['eyes'][0]}, 우:{students['eyes'][1]}")
#
# '''
# #술안주 추천 프로그램
# #치즈: 와인 / 과일: 위스키 / 삼겹살: 소주 / 치킨: 맥주 / 과일: 보드카 /
#
# alcohol_foods={"와인":"치즈",
#                "위스키":"과일",
#                "소주":"골뱅이소면",
#                "맥주":"치킨",
#                "고량주":"짬뽕",
#                "보드카":"과일"}
#
# alcohol_list=list(alcohol_foods)  #key만 추출
# while True:
#       alcohol=input(f"1){alcohol_list[0]}\n2){alcohol_list[1]}\n3){alcohol_list[2]}\n4){alcohol_list[3]}\n5){alcohol_list[4]}\n6){alcohol_list[5]}\n7)종료하기\n술을 고르세요:")
#       for i in range(len(alcohol_list)):
#           if alcohol==i:
#               print(f"{alcohol[i-1]}에 어울리는 안주는 {alcohol_foods.values[alcohol_list[i-1]]} 입니다")
#       break




#안주 추천 프로그램 v0.2
import random

alcohol_foods={"와인":"치즈",
            "위스키":"과일",
            "소주":"골뱅이소면",
            "맥주":"치킨",
            "고량주":"짬뽕",
            "보드카":"과일"}
alcohol_list=list(alcohol_foods)
food_list=[food for food in alcohol_foods.values()]
for i in range(len(alcohol_list)):
    while True:
        alcohol = input(f"1){alcohol_list[i]}\n7)종료하기\n술을 고르세요:")
        if alcohol=="i":
            print(f"{food_list[i-1]}에 어울리는 안주는 {alcohol_foods.get(food_list[i-1])} 입니다.")
            break