from CommunicationDiagram import CommunicationDiagram

class CommunicationDiagramComparator:

    # Right is the "correct" diagram
    def __init__(self, left, right, extractElements=True):
        if extractElements:
            self.leftLifelines, self.rightLifelines = left.getLifelines(False), right.getLifelines(False)
            self.leftMessages, self.rightMessages = left.getMessages(False), right.getMessages(False)
    
    def getMissingLifelines(self):
        missingLifelines = []
        for n in self.rightLifelines:
            if n not in self.leftLifelines:
                missingLifelines.append(n)
        return missingLifelines

    def getMissingMessages(self):
        missingMessages = []
        for n in self.rightMessages:
            if n not in self.leftLifelines:
                missingMessages.append(n)
        return missingMessages



        
