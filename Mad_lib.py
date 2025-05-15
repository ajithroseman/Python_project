
class Madlib:
    def __init__(self):
        self.score = 0

    def planet(self):
        p = input("1.Our solar system consists of _______ planets :")
        if p == "nine":
           print("Correct Answer")
           self.score = self.score +1
        else:
            print("Wrong Answer")

    def mercury_1_1(self):
        pl1_1 = input("What is the smallest planet in our solar system :")
        if pl1_1 == "mercury":
            print("Correct Answer")
            self.score = self.score + 1
        else:
            print("Wrong Planet")
    def mercury_1_2(self):
        pl1_2 = input("Which planet is closest to sun :")
        if pl1_2 == "mercury":
            print("Correct Answer")
            self.score = self.score + 1
        else:
            print("Wrong Planet")
    def planet_5(self):
        pl5_1 = input("2.The largest planet in our solar system is _______ :")
        if pl5_1 == "jupiter":
            print("Correct Answer")
            self.score = self.score + 1
        else:
            print("Wrong Answer")
    def planet_2(self):
        pl2_1 = input("_______ is the hottest planet in our solar system :")
        if pl2_1 == "venus":
            print("Correct Answer")
            self.score = self.score + 1
        else:
                print("Wrong Answer")

pl = Madlib()
pl.planet()
pl.planet_5()
pl.planet_2()
pl.mercury_1_1()
pl.mercury_1_2()
print("Total Score :",pl.score, "out of 5")
