from CommunicationDiagram import CommunicationDiagram
import re

class CommunicationDiagramComparator:

    # Right is the "correct" diagram
    def __init__(self, left, right, extractElements=True):
        if extractElements:
            self.leftLifelines, self.rightLifelines = left.getLifelines(False), right.getLifelines(False)
            self.leftMessages, self.rightMessages = left.getMessages(False), right.getMessages(False)
            self.leftMessageFlows, self.rightMessageFlows = left.getMessageFlows(), right.getMessageFlows()
    
    def getMissingLifelines(self):
        missingLifelines = []
        for n in self.rightLifelines:
            if n not in self.leftLifelines:
                missingLifelines.append(n)
        return missingLifelines

    def getMissingMessages(self):
        missingMessages = []
        for n in self.rightMessages:
            if n not in self.leftMessages:
                missingMessages.append(n)
        return missingMessages

    def validateLifelines(self):
        invalidLifelineNames = []
        for n in self.leftLifelines:
            if not re.match(r'^[a-zA-Z]*$', n):
                invalidLifelineNames.append(n)
        return invalidLifelineNames

    def validateMessages(self):
        invalidMessageNames = []
        for n in self.leftMessages:
            if not re.match(r'^\d*\.\s[a-zA-Z]*\(\)$', n):
                invalidMessageNames.append(n)
        return invalidMessageNames

    def getWrongMessageFlows(self):
        wrongMessageFlows = []
        for l_flow in self.leftMessageFlows:
            correct = False
            for r_flow in self.rightMessageFlows:
                if l_flow == r_flow:
                    correct = True
            if not correct:
                wrongMessageFlows.append(l_flow)
        return wrongMessageFlows
