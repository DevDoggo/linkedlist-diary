

import datetime
#from noteObject import noteObject


class linkedlistNode:
    def __init__(self, prevNode, nextNode, name, date ="Default Date", text=""):
        self.name =         name
        self.date =         date        #datetime.datetime.now().date()
        self.text =         text
        self.next =         nextNode
        self.prev =         prevNode


    def getPrevNode(self):             #Jump to previous Node: OK
        if self.prev == None:
            return self 
        return self.prev

    def getNextNode(self):             #Jump to next Node: OK
        if self.next == None:
            return self
        return self.next       
                                    
    def addNode(self, name="Default Name", date="Default Date", text=""): #Adds another Node
        newNode = linkedlistNode(self, None, name, date, text)
        self.next = newNode
        return newNode 

    def statCall(self):
        #print("\n" + str(self.name) + "\n" + str(self.date) + "\n" + str(self.text))
        print("\n"*25)
        outputText = self.formatText()
        print(outputText)


    def formatText(self): 
        nodeText = ""
        i = 0
        while True:
            j = i
            row = self.text[i:j+50]
            if len(row) >= 50:
                while self.text[j+50] != " ":
                    j = j + 1
            nodeText = nodeText + self.text[i:j+50] + "\n" 
            i = i + j-i + 51 #moves i and also removes the blankspace for the new line.
            if len(row) < 50:
                break
        outputText = ("="*70 + "\n" + self.date + " "*(70-len(self.date)-2) + "||" + "\n"+ "="*70 + "\n" + nodeText + "\n" + "-"*70 +"\n" + self.name + "\n")
        return outputText


    def addText(self, text):
        if self.text is not "":
            self.text = self.text + " "  + text
        else:
            self.text = text

    def clearPage(self):
        self.text = ""

