from flask import Flask, render_template, request
import os
from CommunicationDiagram import CommunicationDiagram
from CommunicationDiagramComparator import CommunicationDiagramComparator
from CommunicationDiagramTutor import CommunicationDiagramTutor
from MappingFile import MappingFile
from MessageFlow import MessageFlow

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', output='No file part')
        file = request.files['file']
        file.save(os.path.join('/tmp/', file.filename))

        left = CommunicationDiagram('/tmp/'+file.filename)
        right = CommunicationDiagram('/home/brauneroliveira/Development/git/umltutor/PapyrusProject/UMLTutor/Oracle.uml')
        comparator = CommunicationDiagramComparator(left, right)
        cdt = CommunicationDiagramTutor(comparator, MappingFile(os.path.realpath('web/Mapping.xml')))

        return render_template('index.html', output=cdt.tutorMissingLifelines())
    else:
        return render_template('index.html')