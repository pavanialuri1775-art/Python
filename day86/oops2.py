#single inheritance
class pet_animal:
    def dog(self):
        print("lives in houses")
class wild_animal(pet_animal):
    def lion(self):
        print("lives in forest")
c1=wild_animal()
c1.dog()#lives in houses
c1.lion()#lives in forest

#Multilevel inheritance
class animal:
    def herbivore(self):
        print("eats grass")
class wild_animal(animal):
    def carnivore(self):
        print("eats meat")
class pet_animal(wild_animal):
    def omnivore(self):
        print("eats both meat and grass")
p1=pet_animal()
p2=wild_animal()
p1.carnivore()#eats meat
p2.herbivore()#eats grass

#Multiple inheritance
class parentA:
    def mother(self):
        print("she is 35 years old")
class parentb:
    def father(self):
        print("he is 40 years old")
class child2(parentA,parentb):
    def sister(self):
        print("she is  21 years old")
s1=child2()
s1.mother()#she is 35 years old
s1.father()#he is 40 years old

#heirarchial inheritance
class parent:
     def mother(self):
            print("she is 35 years old")
class child1(parent):
    def brother(self):
        print("he is 21  years old")
class child2(parent):
    def sister(self):
        print("she is 21 years old")
c1=child1()
c1.mother()
c2=child2()
c2.mother()
        