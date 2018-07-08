import xml.etree.ElementTree as ET

class XmiFile:

    def __init__(self, path, inittree=True):
        self.path = path
        if inittree:
            self.initTree()

    def initTree(self):
        self.tree = ET.parse(self.path)

    def getPath(self):
        return self.path

    def getXmiVersion(self):
        if self.tree:
            root = self.tree.getroot()
            return root.attrib['{http://www.omg.org/spec/XMI/20131001}version'] # Need to fix hardcoded xmlns