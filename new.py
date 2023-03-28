import random

class Character:        # 빵틀 설계도
    """
    모든 캐릭터의 모체가 되는 클래스
    """
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.") # 초과데미지 발생시 공격하는 이상한 점 수정할 것

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}, 파워 {self.power}")

class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)   # 빵틀
        

class Player(Character):
    def __init__(self, name, hp, power, mp, mpower):
        self.max_mp = mp
        self.mp = mp
        self.mpower = mpower
        super().__init__(name, hp, power)
        
    def magic_atk(self, other):
        damage = random.randrange(self.mpower - 2, self.mpower + 2)
        self.mp -= 2 # mp소모를 2로 정함
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

# 랜덤한 name과 랜덤한 스탯으로 monster 객체를 생성하는 코드
# 
name = ['식물','곤충','야수','수인','악마','언데드','흡혈귀']

print("네팔렘이여 그대의 이름은 무엇입니까")
nephalem = input()
monster = Monster('monster', 100, 10)  # 
player = Player(nephalem, 100, 10, 100, 10) # nephalem 변수로 지정

while 'game':
    command = input('일반공격 마법공격 : ') # command의 순서가 중요하다 맨앞에 돌아오게
    
    if command == '일반공격': # 
        player.attack(monster)
        monster.attack(player)
        player.show_status()
        monster.show_status()
        
    elif command == '마법공격':
        player.magic_atk(monster)
        monster.attack(player)
        player.show_status()
        monster.show_status()
        
    if monster.hp <= 0:
        print(f"{monster.name}이(가) 죽었습니다. 승리")
        monster = Monster('디아블로'+name[random.randint(0, 6)],
                  random.randint(10, 200), random.randint(10, 20))

    elif player.hp <= 0:
        print(f"{player.name}이(가) 죽었습니다. 게임 패배")
        break
    
    # 3. 종료 조건(승리or패배)
    # 승리의 조건
    # if 조건문으로 player가 몬스터를 이기면 
    # 몬스터를 잡았습니다란 게임종료 메세지 출력
    # break로 while문 빠져나온다. 프로그램 종료
    
    # 패배의 조건은 몬스터가 player를 이기면
    # player가 죽었습니다. 게임종료 메세지 출력
    # break로 똑같이. 종료
