class Manchester_United:
    def Goals(self):
        print("scored 7")
class Chelsea:
    def Scores(self):
        print("scored 2")
        

class Liverpool(Manchester_United,Chelsea):
    def position(self):
        print("position 3")
d=Liverpool()
d.position()
d.Goals()
d.Scores()