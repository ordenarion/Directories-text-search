import os, string
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import re


class ParseDude:
    def __init__(self):
        self.path = os.path.abspath(os.getcwd())
        self.all_paths = []
        self.files = self.get_files()
        self.word = ''
        self.key = ""
        self.res = {}
        self.chosen_txt = ""
        self.ct = []

    def get_files(self):
        files = []
        for folder in self.all_paths:
            if os.path.isdir(folder):
                text_files = [f for f in os.listdir(folder) if f.endswith('.txt')]
                [files.append(f'{folder}/{new_txt}') for new_txt in text_files]
        return files

    def add_key_word(self):
        with open('keylist.txt', 'a', encoding='utf-8') as f:
            f.write(f'{self.word}\n')

    def find_index(self):
        self.files = self.get_files()
        result = {}
        for i in self.files:
            result.update([(i, [])])
            with open(i, 'r', encoding='utf-8') as f:
                data = f.read()

            text_parsed = [word for word in re.findall(r'\w+\>*|[\s\W]', data)]

            for id, word in enumerate(text_parsed):
              if self.key.lower() in word.lower():
                    result.update([(i, result[i] + [id])])

        self.res.update([(self.key, result)])

    def prepare_to_highlight(self):
        with open(f'{self.choosen_txt}', 'r', encoding='utf-8') as f:
            self.data = f.read()
        parsed = [w for w in re.findall(r'\w+\>*|[\s\W]', self.data)]
        wsd = self.key
        col = 1
        row = 0
        l = len(self.ct)
        flag = False
        for word in parsed:

            if word == '\n':
                row = 0
                col += 1
                continue
            row += len(word)

            if wsd.lower() in word.lower():
                l -= 1
                if (l == 0):
                    break
                else:
                    pass
        return (f"{col}.{row - len(word)}", f"{col}.{row}")

    def add_new_folder(self):
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        open_file = filedialog.askdirectory()
        self.all_paths += [open_file]
