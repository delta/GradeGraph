from bs4 import BeautifulSoup

soup = BeautifulSoup(open("civil_sr.html"))
subs = soup.find_all("tr", class_="DataGridItem") + soup.find_all("tr", class_="DataGridAlternatingItem")

#print(subs[0].find_all("td")[2].find_all("font")[0].contents[0])  this is sub
#print(subs[0].find_all("td")[4].find_all("font")[0].contents[0])  this is grade

def retsubname(sub):
    return sub.find_all("td")[2].find_all("font")[0].contents[0]

def retgrade(sub):
    return sub.find_all("td")[4].find_all("font")[0].contents[0]

arrsubs = {} #dict with the grades

#initialising the empty arrays
for sub in subs:
    arrsubs[retsubname(sub)] = {'S':0,'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}

#adding the grades to the arrays
for sub in subs:
    arrsubs[retsubname(sub)][retgrade(sub)] = arrsubs[retsubname(sub)][retgrade(sub)]+1

#print(arrsubs)   #arrsubs is a dictionary with all the grades along with subject name
#print(arrsubs.values()[0].values())   #printing the splitup of marks

def drawpie(arr,fname):
    from reportlab.graphics.charts.piecharts import Pie
    from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
    from reportlab.lib.colors import Color, magenta, cyan

    class pietests(_DrawingEditorMixin,Drawing):
        def __init__(self,width=400,height=200,*args,**kw):
            Drawing.__init__(self,width,height,*args,**kw)
            self._add(self,Pie(),name='pie',validate=None,desc=None)
            self.pie.sideLabels       = 1
            self.pie.labels           = ['S', 'A', 'B', 'C','D','E','F']
            self.pie.data             = arr
            self.pie.width            = 140
            self.pie.height           = 140
            self.pie.y                = 35
            self.pie.x                = 125

    if __name__=="__main__":
        drawing = pietests()
        # you can do all sorts of things to drawing, lets just save it as pdf and png.
        drawing.save(formats=['pdf'],outDir='./graphs/'+fname,fnRoot=None)

for subname in arrsubs.keys():
    for sub in arrsubs.values():
        drawpie(arrsubs[subname].values(),subname)

