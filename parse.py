import os, string
from tkinter import *
from configparser import ConfigParser
from tkinter import ttk
import re

class ParseDude:
    def __init__(self):
        self.path = os.path.abspath(os.getcwd())
        self.files = self.get_files()
        self.all_paths = []
        self.word = ''
        self.key = "ou"
        self.res = {}
        self.chosen_txt = ""
        self.rus_alp = "А,Б,В,Г,Д,Е,Ё,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я"

    def get_files(self):
        files = []
        try:
            for folder in self.all_paths:
                if os.path.isdir(folder):
                    text_files = [f for f in os.listdir(folder) if f.endswith('.txt') and f[0].upper() in self.rus_alp.split(',')]
                    [files.append(f'{folder}/{new_txt}') for new_txt in text_files]
            return files
        except:
            pass

    def add_key_word(self):
        with open(f'{self.path}\\keylist.txt', 'a', encoding='utf-8') as f:
            f.write(f'{self.word}\n')

    def find_index(self):
        self.files = self.get_files()
        result = {}
        for i in self.files:
            result.update([(i, [])])
            with open(i, 'r',encoding='utf-8') as f:
                data = f.read()

            text_parsed = [word for word in re.findall( r'\w+\>*|[\s\W]', data)]

            for id, word in enumerate(text_parsed):
                print(word)
                if self.key.isupper() or self.key.islower():
                    print("True1")
                    print(f"{self.key},{word}")
                    print(self.key.upper() == word.upper())
                    if self.key.upper() == word.upper():
                        print("True2")
                        result.update([(i, result[i] + [id])])
                elif self.key == word:
                    print("True3")
                    result.update([(i, result[i] + [id])])
        self.res.update([(self.key, result)])


x= ParseDude()
print(x.files)