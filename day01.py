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
    def __init__(self, name, hp, power, give_exp=100): # give_exp값은 몬스터가 죽었을 때 반환하는 경험치 값. 
        self.give_exp = give_exp #몬스터가 죽고 내뱉을 경험치
        super().__init__(name, hp, power)
        

class Player(Character):
    def __init__(self, name, hp, power, mp, mpower):
        self.max_mp = mp
        self.mp = mp
        self.mpower = mpower
        self.exp = 0  #현재 가지고 있는 경험치
        self.lvl = 1 #레벨
        self.max_exp = 100  #맥스 경험치
        super().__init__(name, hp, power)
        
    def magic_atk(self, other):
        damage = random.randrange(self.mpower - 2, self.mpower + 2)
        self.mp -= 2 # mp소모를 2로 정함
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def kill_monster(self, other): #몬스터가 죽으면 플레이어가 경험치를 얻을 수 있게 하는 함수
        self.exp += other.give_exp #self를 플레이어로 생각 other를 monster로 생각

    def level_up(self):
        if self.exp == self.max_exp:
            self.lvl += 1
            self.max_exp *= 2 #레벨업 할때마다 필요경헙치 2배
            self.exp = 0
            tmp_power = self.power # 상승량을 알기 위해 기존 파워 저장.
            tmp_mpower = self.mpower
            self.power *= 2
            self.mpower *= 2
            print(f"{self.name}이 {self.lvl}로 레벨업!\n공격력이 {tmp_power}에서 {self.power}로\n마법 공격력이 {tmp_mpower}에서 {self.mpower}로 증가하였다!")
            
#pair programming:
# 몬스터 사냥 성공시 보상에 따른 게임 진행이 되어야 합니다. 구현상 특징: 1. 플레이어 레벨업의 조건과 상태를 출력. 2. 1의 상태가 게임진행에 계속 반영 될 수 있도록 한다.         
#------------------------------------------------------------------------------------------------------------------------------------------------------------

# 랜덤한 name과 랜덤한 스탯으로 monster 객체를 생성하는 코드
# name = ['식물','곤충','야수','수인','악마','언데드','흡혈귀']

print("네팔렘이여 그대의 이름은 무엇입니까")
nephalem = input()
monster = Monster('monster', 100, 10)  
player = Player(nephalem, 100, 10, 100, 10) # nephalem 변수로 지정

while 'game':
    command = input('일반공격 마법공격 : ') # command의 순서가 중요하다 맨앞에 돌아오게
    print(f'{player.power}기존 파워')

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
        player.kill_monster(monster)
        # monster = Monster('디아블로'+name[random.randint(0, 6)],
        #           random.randint(10, 200), random.randint(10, 20))

    elif player.hp <= 0:
        print(f"{player.name}이(가) 죽었습니다. 게임 패배")
        break

    player.level_up()
    if player.lvl == 2:
        print(f'{player.power}현재 파워')
    
    # 3. 종료 조건(승리or패배)
    # 승리의 조건
    # if 조건문으로 player가 몬스터를 이기면 
    # 몬스터를 잡았습니다란 게임종료 메세지 출력
    # break로 while문 빠져나온다. 프로그램 종료
    
    # 패배의 조건은 몬스터가 player를 이기면
    # player가 죽었습니다. 게임종료 메세지 출력
    # break로 똑같이. 종료
