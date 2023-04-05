import random #random 가져오기


class Character:
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
        print(f"{other.name}의 남은 체력은 {other.hp}")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
    


    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


class Monster(Character): #몬스터 클래스 Character상속
        
    # def __init__(self, name, hp, power):
    #     # super()를 사용하면 부모 클래스의 코드를 그대로 사용할 수 있습니다.
    #     # 해당 코드는 self.hp = hp 코드를 실행시키는 것과 동일합니다.
    #     super().__init__(name, hp, power)
    def monIniti(self, initi):  # random모듈의 randrange로 주도권 결정메서드 1,21의 사이에서
        self.initi = initi.random.randrange(1, 21)
        super().__init__(name, hp, power)


class Player(Character): #플레이어 클래스 Character상속
    def __init__(self, name, hp, power, mp, magicPower):
        self.mp = mp
        self.magicPower = magicPower
        # super()를 사용하면 부모 클래스의 코드를 그대로 사용할 수 있습니다.
        # 해당 코드는 self.hp = hp 코드를 실행시키는 것과 동일합니다.
        super().__init__(name, hp, power)

    def magicAttack(self, other): #마법공격
        damage = random.randint(self.power - 4, self.power + 6)
        if self.mp < 10:
            print('mp가 부족합니다. 일반공격이 시전됩니다.')
            self.attack(other)
        else:
            self.mp -= 10 #마법공격시 mp차감 mp에 대한 조건문이 필요할 듯.
            print(f'남은 mp는 {self.mp}다!')
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 마법공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
            print(f"{other.name}의 남은 체력은 {other.hp}")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


#몬스터 임의 생성
def monsterGen():
    # 이름에 따른 체력 공격력의 변화를 주어보았음.
    nameList1 = ['크고','', '작고'] # 몬스터 이름 형용사
    nameList2 = ['강인한','평범한', '나약한'] # 몬스터 속성 리스트
    nameList3 = ['멧돼지','돼지','닭'] # 몬스터 이름 리스트
    name1 = random.randrange(0,3)
    name2 = random.randrange(0,3)
    name3 = random.randrange(0,3)
    monName = nameList1[name1]+nameList2[name2]+nameList3[name3] #monName은 몬스터 이름

    baseHp = random.randrange(80,121) #몬스터 기본체력
    addHp = ((3-name1)+(3-name2)+(3-name3))*10 #이름에 따른 추가 체력
    monHp = baseHp+addHp #몬스터 체력

    basePower = random.randrange(8,13)
    addPower = ((3-name1)+(3-name2)+(3-name3))
    monPower = basePower+addPower

    return Monster(monName, monHp, monPower)

#공격방식
def chooseAttack(num, player, monster):
    if num == 1:
        return player.attack(monster)
    elif num == 2:
        return player.magicAttack(monster)
    else:
        print("다시 입력해주세요.")
        num = int(input())
        chooseAttack(num, player, monster)

def check_initi(monster): # 플레이어는 빠졌다?
   monInitiative = random.randrange(1, 21)
   playerInitiative = random.randrange(1, 21)
   print(f'\n당신의 주도권은 {playerInitiative}. {monster.name}의 주도권은 {monInitiative}.')
   if playerInitiative >= monInitiative:
       return 1 #플레이어가 이긴상황
   else:
       return 2 #

def check_status(player, monster):
# return은 조건을 만족하는 값을 반환하거나 패스한다. 
# 즉 더이상 조건을 지정할 필요가 없다면 return자체 호출       
    if (monster.hp <= 0):
        print('You Win!')
        return 1 #죽었을 떄
    
    if(player.hp <= 0):
        print('You Lose!')
        return 1 
 
    return 2 #죽지않은 상황

def turn(player, monster):
    while(1):  
        # monInitiative = random.randrange(1,21) # random모듈의 randrange로 주도권 결정 1,21의 사이에서 
        # playerInitiative = random.randrange(1,21) # 플레이어 주도권
        # print(f'\n당신의 주도권은 {playerInitiative}. {monster.name}의 주도권은 {monInitiative}.')
        #choice_initi = check_initi(player,monster) # 선공 정해주는 함수
        if check_initi(player,monster) == 1:
            print('주도권 승! 선공!') # 플레이어선공
            choice_num = int(input("공격방식을 선택해 주세요 1: 일반공격 2: 마법공격"))
            chooseAttack(choice_num, player, monster)  # 플레이어 공격
            if check_status(player, monster) == 1:
                break
            monster.attack(player) # 몬스터 공격
            if check_status(player, monster) == 1:
                break
        else: #몬스터선공
            print('주도권 패! 후공!')
            monster.attack(player) #몬스터 공격
            if check_status(player, monster) == 1:
                break
            choice_num = int(input("공격방식을 선택해 주세요 1: 일반공격 2: 마법공격"))
            chooseAttack(choice_num, player, monster)  # 플레이어 공격
            if check_status(player, monster) == 1: 
                break

# == 같다
# >= 같거나 크다
# <= 작거나 같다
# != 같지 않다
# < 작다
# > 크다

#-----------------------------------------------------------------------            
#페어프로그래밍 목표: while 문 안의 반복되는 조건문들을 함수로 구현해 모듈화.
#-----------------------------------------------------------------------

playerName = input('당신의 이름은?')
playerHp = random.randrange(300,400)
playerPower = random.randrange(20,30)
playerMp = random.randrange(100,200)
playerMagicPower = random.randrange(20,30)
# playerHp = int(input())
# playerPower = int(input())
# playerMp = int(input())
# playerMagicPower = int(input())

newPlayer = Player(playerName, playerHp, playerPower, playerMp, playerMagicPower)
print(f'당신의 이름은 {newPlayer.name}! 체력은 {newPlayer.hp}. 파워는 {newPlayer.power}. 마나는 {newPlayer.mp}. 마법력은 {newPlayer.magicPower}이다!')

newMonster = monsterGen()
print(f'{newMonster.name}가 나타났다! 상대의 체력은{newMonster.hp}! 파워는 {newMonster.power}다!')

turn(newPlayer, newMonster)
