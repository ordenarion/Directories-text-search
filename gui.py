from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from parse import ParseDude


class GUIDude:
    def __init__(self):
        self.new_folders = []
        self.parser = ParseDude()

        self.new_folders = []
        self.parser = ParseDude()

        self.win1 = Tk()
        self.win1.resizable(False, False)
        self.win1.geometry("900x500")
        # self.win1.iconbitmap(r"Logo_SPbFTU_RGB_rus.ico")
        self.win1.title("")
        self.win1.columnconfigure(0, weight=1)
        self.win1.columnconfigure(1, weight=5)
        self.win1.columnconfigure(2, weight=5)
        self.win = LabelFrame(self.win1, text="", labelanchor="se")
        self.first_col_frame = LabelFrame(self.win, relief="groove", text="Keylist.txt", labelanchor="n")
        self.first_col_frame_buttons = LabelFrame(self.win, text="*", labelanchor="e")
        self.add_ind = Button(self.first_col_frame_buttons, text="Добавить", height=0, width=25,
                              command=self.show_indexes)
        self.add_entry = Entry(self.first_col_frame_buttons, width=25)
        self.find_ind = Button(self.first_col_frame_buttons, text="Найти", height=0, width=25,
                               command=self.show_good_txt)
        self.clear_button = Button(self.first_col_frame_buttons, width=25, text="Очистить", command=self.clear)
        self.add_new_folder_button = Button(self.first_col_frame_buttons, width=25, text="Добавить папку",
                                            command=self.add_new_folder)
        self.delete_folder_button = Button(self.first_col_frame_buttons, width=25, text="Удалить папку",
                                           command=self.delete_folder)
        self.found_txt_frame = LabelFrame(self.win, text="Подходящие файлы, добавленные папки", labelanchor="n")

        self.indexes = Listbox(self.first_col_frame, relief="groove", height=15, width=35, borderwidth=3)
        self.found_txt = Listbox(self.found_txt_frame, relief="groove", height=15, width=45, borderwidth=3)
        self.folders_box = Listbox(self.found_txt_frame, relief="groove", height=9, width=45, borderwidth=3)
        self.found_txt.bind("<Double-Button-1>", self.show_highlighted_txt)
        self.found_txt.bind("<Button-3>", self.delete_txt)
        self.highlighted_txt_frame = LabelFrame(self.win, text="Выбранный текст", labelanchor="n")
        self.highlighted_txt = Text(self.highlighted_txt_frame, relief="groove", height=25, width=40, borderwidth=3)
        self.highlighted_txt.config(state="disabled")

        self.show_indexes()
        self.indexes.grid(column=0, row=0, pady=1)

        self.found_txt.grid(column=0, row=1, pady=1, sticky="n", )
        self.folders_box.grid(column=0, row=2, pady=4, sticky="e", )
        self.highlighted_txt.grid(column=0, row=1, pady=1, sticky="n")
        self.add_ind.grid(column=0, row=0, sticky="s")
        self.add_entry.grid(column=0, row=1, sticky="s")
        self.find_ind.grid(column=0, row=2, sticky="s")
        self.clear_button.grid(column=0, row=5, sticky="s",ipady=10)
        self.add_new_folder_button.grid(column=0, row=3, sticky="s", )
        self.delete_folder_button.grid(column=0, row=4, sticky="s", )

        self.win.grid(column=0, row=0, padx=10, pady=10, ipadx=10, ipady=10)
        self.first_col_frame.grid(column=0, row=1, sticky="n")
        self.first_col_frame_buttons.grid(column=0, row=2, sticky="n")
        self.found_txt_frame.grid(column=1, row=1, sticky="n", rowspan=2)
        self.highlighted_txt_frame.grid(column=2, row=1, sticky="n", rowspan=2)
        self.win.mainloop()

    def add_new_folder(self):
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        open_file = filedialog.askdirectory()
        self.parser.all_paths += [open_file]
        self.folders_box.delete(0, END)
        try:
            for i in self.parser.all_paths:
                self.folders_box.insert(END, i)
        except:
            pass

    def delete_folder(self):
        try:
            a = self.folders_box.curselection()[0]
            self.parser.all_paths.pop(a)
            self.folders_box.delete(a, a)
        except:
            pass
    def delete_txt(self,event):
        try:
            self.choosen_ind = self.found_txt.curselection()[0]
            self.found_txt.delete(self.choosen_ind, self.choosen_ind)
            print(self.parser.choosen_txt ,self.found_txt.get(self.choosen_ind))
            if self.iddd == self.choosen_ind:
                self.highlighted_txt.config(state="normal")
                self.highlighted_txt.delete("1.0", END)
                self.highlighted_txt.config(state="disabled")
        except:
            pass




    def show_indexes(self):
        self.flag = False
        with open(f'{self.parser.path}\\keylist.txt', 'r', encoding='utf-8') as f:
            self.data = f.read().split("\n")
        self.indexes.delete(0, END)
        for index in self.data:
            self.indexes.insert(END, index)
        self.indexes.delete(END, END)

        self.new_key = self.add_entry.get()
        if self.new_key not in self.data:
            self.parser.word = self.new_key
            self.parser.add_key_word()
            self.add_entry.delete(0, END)
            self.flag = True
            self.indexes.insert(END, self.new_key)

    def show_good_txt(self):
        self.clear_boxes()
        self.good_txt = []
        try:
            self.choosen_ind = self.indexes.get(self.indexes.curselection()[0])

            self.parser.key = self.choosen_ind
            self.parser.find_index()

            for file, count in self.parser.res[self.choosen_ind].items():
                if count != []:
                    self.good_txt += [[file, count]]
            self.found_txt.delete(0, END)
            for txt, count in self.good_txt:
                self.found_txt.insert(END, txt)
        except:
            pass

    def clear(self):
        self.indexes.delete(0, END)
        self.clear_boxes()
        with open(f'{self.parser.path}\\keylist.txt', 'w', encoding='utf-8') as f:
            f.write("")

    def show_highlighted_txt(self, event):
        self.highlighted_txt.config(state="normal")
        self.highlighted_txt.delete("1.0", END)
        try:
            self.iddd = self.found_txt.curselection()[0]
            self.parser.choosen_txt = self.found_txt.get(self.iddd)
            for txt,count in self.good_txt:
                if self.parser.choosen_txt == txt:
                    self.parser.ct = count
                    break

            i, j = self.parser.prepare_to_highlight()



            self.highlighted_txt.insert(INSERT, self.parser.data)
            self.highlighted_txt.config(state="disabled")
            try:
                self.highlighted_txt.tag_add('start', i, j)
                self.highlighted_txt.tag_config("start", background="red",
                                                foreground="white")
            except:
                pass
        except:
            pass
    def clear_boxes(self):
        self.found_txt.delete(0, END)
        self.highlighted_txt.config(state="normal")
        self.highlighted_txt.delete("1.0", END)
        self.highlighted_txt.config(state="disabled")
