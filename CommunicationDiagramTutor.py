from CommunicationDiagramComparator import CommunicationDiagramComparator
from MappingFile import MappingFile

class CommunicationDiagramTutor:

    MISSING_LIFELINE = 'You are missing one or more Liflines.'
    SURPLUS_LIFELINE = 'There are unnecessary Lifelines in your diagram.'
    
    MISSING_MESSAGE = 'You are missing one or more messages in yout diagram.'
    SURPLUS_MESSAGE = 'There are unnecessary Messages in your diagram.'

    GLOBAL_ORDER_OF_MESSAGES_IS_WRONG = 'The order of Messages is wrong.'
    WRONG_MESSAGE_FLOW = 'The flow (from-to) of at least one message is wrong.'

    def __init__(self, CommunicationDiagramComparator, MappingFile):
        self.comparator, self.mappingfile = CommunicationDiagramComparator, MappingFile

    def tutorMissingLifelines(self):
        missingLifeLines = self.comparator.getMissingLifelines()
        lifelineMappings = self.mappingfile.getLifelineMappings()
        useCasesHints = []
        for n in missingLifeLines:
            for m in lifelineMappings:
                xml_lifeline = m.find('lifeline').text
                if n == xml_lifeline:
                    useCasesHints.append(m.find('use_case_step').text)
        return 'You are missing {} Lifelines. Review the following steps on the use case description and try to identify them: {}'.format(len(useCasesHints), useCasesHints)


