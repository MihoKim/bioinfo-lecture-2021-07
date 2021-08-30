d_persons = {'Guillaume':'Canada', 'Niklas':'Germany', 'Mark':'USA',
'Alex':'Swiss', 'Alberto':'Italia'}

class Person():
    nation = ''
    def showNation(self):
        print(self.nation)
    def setNation(self, whichNation):
        self.nation = whichNation

Guillaume = Person()
Guillaume.setNation(d_persons['Guillaume'])
Guillaume.showNation()          #Canada

Niklas = Person()
Niklas.setNation(d_persons['Niklas'])
Niklas.showNation()             #Germany

Mark = Person()
Mark.setNation(d_persons['Mark'])
Mark.showNation()               #USA

Alex = Person()
Alex.setNation(d_persons['Alex'])
Alex.showNation()               #Swiss

Alberto= Person()
Alberto.setNation(d_persons['Alberto'])
Alberto.showNation()            #Italia

