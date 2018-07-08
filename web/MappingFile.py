import xml.etree.ElementTree as ET

class MappingFile:

    def __init__(self, path, inittree=True):
        self.path = path
        if inittree:
            self.tree = ET.parse(self.path)

    def getLifelineMappings(self, asEtreenode=True):
        lifelineMappingNodes = self.tree.findall('.//lifeline_mappings//mapping')
        if asEtreenode:
            return lifelineMappingNodes
        else:
            return lifelineMappingNodes


    def getMessageMappings(self, asEtreenode=True):
        return self.tree.findall('.//message_mappings//mapping')
