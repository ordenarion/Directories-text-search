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
        self.win1.geometry("1200x500")
        # self.win1.iconbitmap(r"Logo_SPbFTU_RGB_rus.ico")
        self.win1.title("")
        self.win1.columnconfigure(0, weight=1)
        self.win1.columnconfigure(1, weight=5)
        self.win1.columnconfigure(2, weight=5)
        self.win = LabelFrame(self.win1, text="",
                              labelanchor="se")
        self.first_col_frame = LabelFrame(self.win, relief="groove", text="Keylist.txt", labelanchor="n")
        self.first_col_frame_buttons = LabelFrame(self.win, text="", labelanchor="e")
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
        self.found_txt_frame = LabelFrame(self.win, text="Статистика, менеджер папок и файлов", labelanchor="n")

        self.indexes = Listbox(self.first_col_frame, relief="groove", height=15, width=35, borderwidth=3,selectmode = "multiple")
        self.found_txt = Text(self.found_txt_frame, relief="groove", height=25, width=75, borderwidth=3)
        self.folders_box = Listbox(self.found_txt_frame, relief="groove", height=10, width=50, borderwidth=3)
        self.highlighted_txt_frame = LabelFrame(self.win, text="Выбранный текст", labelanchor="n")
        self.highlighted_txt = Listbox(self.found_txt_frame, relief="groove", height=15, width=50, borderwidth=3)


        self.show_indexes()
        self.indexes.grid(column=0, row=0, pady=1)

        self.found_txt.grid(column=2, row=1, pady=4, sticky="n",columnspan = 2,padx=4,rowspan =2)
        self.folders_box.grid(column=0, row=2, pady=1, sticky="e", )
        self.highlighted_txt.grid(column=0, row=1, pady=1, sticky="n")
        self.add_ind.grid(column=0, row=0, sticky="s")
        self.add_entry.grid(column=0, row=1, sticky="s")
        self.find_ind.grid(column=0, row=2, sticky="s")
        self.clear_button.grid(column=0, row=5, sticky="s", ipady=10)
        self.add_new_folder_button.grid(column=0, row=3, sticky="s", )
        self.delete_folder_button.grid(column=0, row=4, sticky="s", )
        self.found_txt.config(state="disabled")
        self.win.grid(column=0, row=0, padx=10, pady=10, ipadx=10, ipady=10)
        self.first_col_frame.grid(column=0, row=1, sticky="n")
        self.first_col_frame_buttons.grid(column=0, row=2, sticky="n")
        self.found_txt_frame.grid(column=1, row=1, sticky="n", rowspan=2)
       # self.highlighted_txt_frame.grid(column=2, row=2, sticky="n")
        self.win.mainloop()

    def clear_boxes(self):
        self.found_txt.config(state="normal")
        self.found_txt.delete("1.0", END)
        self.found_txt.config(state="disabled")


    def add_new_folder(self):
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        open_file = filedialog.askdirectory()
        self.parser.all_paths += [open_file]
        self.folders_box.delete(0, END)
        self.highlighted_txt.delete(0, END)
        files = self.parser.get_files()
        try:
            for i in self.parser.all_paths:
                self.folders_box.insert(END, i)
            for i in files:
                self.highlighted_txt.insert(END, i)
                print(i)
        except:
            pass

    def delete_folder(self):
        try:
            a = self.folders_box.curselection()[0]
            self.parser.all_paths.pop(a)
            self.folders_box.delete(a, a)
            self.highlighted_txt.delete(0, END)
            files = self.parser.get_files()
            for i in files:
                self.highlighted_txt.insert(END,i)
        except:
            pass

    def show_indexes(self):
        self.flag = False
        with open(f'{self.parser.path}\\keylist.txt', 'r', encoding='utf-8') as f:
            self.data = f.read().split("\n")
        self.indexes.delete(0,END)
        for index in self.data:
            self.indexes.insert(END,index)
        self.indexes.delete(END,END)
        self.new_key = self.add_entry.get()
        if self.new_key not in self.data:
            self.parser.word = self.new_key
            self.parser.add_key_word()
            self.add_entry.delete(0,END)
            self.flag = True
            self.indexes.insert(END,self.new_key)

    def show_good_txt(self):
        self.clear_boxes()
        try:
            self.good_txt = []
            self.choosen_ind = [self.indexes.get(i) for i in self.indexes.curselection()]

            for w in self.choosen_ind:
                self.found_txt.config(state="normal")
                self.found_txt.insert(END, w + ":\n\n")
                self.parser.key = w
                self.parser.find_index()
                for file, count in self.parser.res[w].items():
                    self.good_txt += [[file, len(count)]]

                for txt, count in self.good_txt:
                    self.found_txt.insert(END, txt + f": {count}\n")
                self.found_txt.insert(END, f"\n")
                self.found_txt.config(state="disabled")
                self.good_txt = []
        except:
            pass

    def clear(self):
        self.clear_boxes()
        self.indexes.delete(0, END)

        with open(f'{self.parser.path}\\keylist.txt', 'w', encoding='utf-8') as f:
            f.write("")

