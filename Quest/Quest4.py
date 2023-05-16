'''
[파이썬] 퀘스트: 물고기들의 움직임을 시뮬레이션하기!

난이도: ★★★☆☆

장르: 함수, 컴프리헨션, 이터레이터, 제너레이터

---

다음 조건을 활용하여 물고기가 물 속에서 움직이는 것을 시뮬레이션해보자!

조건 :
물고기의 움직임을 출력하는 함수를 컴프리헨션과 이터레이터, 제너레이터를 활용해서 만듭니다.
물고기 객체의 움직임을 시뮬레이션하는 클래스를 구현해야 합니다.
물고기 객체는 이름과 속도 속성을 가져야합니다.
물고기 리스트를 활용하셔야합니다.
물고기 객체의 움직임은 랜덤하게 선택된 방향으로 이루어지며, 물고기 객체가 움직이는 동안에는 그 움직임이 출력되어야 합니다.
물고기 객체의 움직임은 일정 시간 간격으로 반복되어야 합니다.

---

입력값 : 

# 물고기 리스트
fish_list = [
    Fish("Nemo", 3),
    Fish("Dory", 5),
    Fish("Marlin", 7),
    Fish("Bubbles", 2),
    Fish("Gill", 4)
]

# 물고기들의 움직임 출력
print("Using Comprehension:")
show_fish_movement_comprehension(fish_list)

print("\nUsing Iterator:")
show_fish_movement_iterator(fish_list)

---

출력값 :

Using Comprehension:
Nemo is swimming at 3 m/s
Dory is swimming at 5 m/s
Marlin is swimming at 7 m/s
Bubbles is swimming at 2 m/s
Gill is swimming at 4 m/s

Using Iterator:
Nemo is swimming at 3 m/s
Dory is swimming at 5 m/s
Marlin is swimming at 7 m/s
Bubbles is swimming at 2 m/s
Gill is swimming at 4 m/s
'''

import time as t

# 물고기 클래스 생성
class Fish:
    def __init__(self, name, speed):
            self.name = name
            self.speed = speed

fish_list = [ Fish("Nemo", 3), Fish("Dory", 5), Fish("Marlin", 7), Fish("Bubbles", 2), Fish("Gill", 4) ]

# 이터레이터로 물고기 속성 출력\
# 이터레이터로 물고기 속성 출력\
def show_fish_movement_comprehension(a):
    fish_property = [(fish.name, fish.speed) for fish in fish_list] # 리스트 컴프리헨션으로 물고기 속성 추출
    for fish in fish_property:
        print(f"{fish[0]} is swimming at {fish[1]} m/s ")
        # t.sleep(fish[1])

def show_fish_movement_generate(fish_list):
    # 제너레이터 함수 정의
    def fish_generator(fish_list):
        for fish in fish_list:
            yield print(f"{fish.name} is swimming at {fish.speed} m/s")
            # t.sleep(fish.speed)
    

    fish_gen = fish_generator(fish_list) # 제너레이터 객체 저장
    
    for i in range(len(fish_list)): # 제너레이터 호출
        next(fish_gen)
    
print("Using Comprehension:")
show_fish_movement_comprehension(fish_list)

print("\nUsing Iterator:")
show_fish_movement_generate(fish_list)
