class Hero():
    def __init__(self, name, hp, armor, hit, weapon):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.hit = hit
        self.weapon = weapon

    def printInfo(self):
        print("Поприветсвуйте героя ->", self.name)
        print("Уровень здоровья:", self.hp)
        print("Класс брони:",self.armor)
        print("Сила удара:", self.hit)
        print("Оружие:", self.weapon)

    def strike(self, enemy):
        print("-> УДАР! " + self.name + " атакует " + enemy.name + " с силой " + str(self.hit) + ", используя " + self.weapon + "\n")
        enemy.armor -= self.hit
        if enemy.armor < 0:
            enemy.hp += enemy.armor
            enemy.armor = 0
        print(enemy.name + " покачнулся. \nКласс его брони упал до " + str(enemy.armor) + ", а уровень здоровья до " + str(enemy.hp) + "\n")

    def fight(self, enemy):
        while self.hp and enemy.hp > 0:
            self.strike(enemy)
            if enemy.hp <= 0:
                print(enemy.name, " пал в этом нелегком бою!\n")
                break
            enemy.strike(self)
            if self.hp <= 0:
                print(self.name, " пал в этом нелегком бою! \n")
                break
    def win(self):
        if self.hp > 0:
            self.hp = 50
            self.hit *= 2
            self.armor *= 2
            print("\n"+self.name + " восстановил силы и стал опытнее. Теперь сила его удара: " + str(self.hit) + ", а класс брони: " + str(self.armor) + "\n")
        else:
            print(self.name, "- Game over")

#knight = Hero("Рыцарь", 50, 25, 20, "меч")
#thief = Hero("Разбойник", 20, 5, 5, "лук")


#knight.printInfo()
#thief.printInfo()

#knight.strike(thief)
#knight.strike(thief)