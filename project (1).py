# -*- coding: utf-8 -*-
"""Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JLiJHXJZzaByvuIzurgNybGFs_ud-Jup
"""

#Installation
!pip install pyresparser

# spaCy
!python -m spacy download en_core_web_sm

 # nltk
!python -m nltk.downloader words

#Upload the file 
file = input()

import nltk
nltk.download('stopwords')


#Utilisation
from pyresparser import ResumeParser
data = ResumeParser(file).get_extracted_data()