"""
self.master.geometry(window_size)   # Sets the size of the main window in "WIDTHxHEIGHT" format
self.master.title(title)            # Sets the title of the main window
self.__frame = None                 # This variable is used to save the current frame of the master window
self.__current_file = None          # This variable is used to save the path and name of the loaded/created file
self.__curr_table = None            # This variable is used to store the current table that was created with pandastable
"""

import tkinter as tk
import os
from pandastable import Table
from tkinter import filedialog
from MainModel import MainModel

class MainGUI(tk.Frame):
    def __init__(self, window_size, title):
        super().__init__()
        self.default_path = os.getcwd()
        self.master.geometry(window_size)
        self.master.title(title)
        self.__frame = None
        self.__current_file = None
        self.__curr_table = None

        self._create_menu()

        self.mainloop()

    def _create_menu(self):
        self.menu_bar = tk.Menu(self.master)
        file_menu = tk.Menu(self.menu_bar, tearoff=0, font=10)
        file_menu.add_command(label="New", command=self._create_new_table)
        file_menu.add_command(label="Open", command=self._open_file)
        file_menu.add_command(label="Save", command=self._save_file)
        file_menu.add_command(label="Close", command=self._close_table)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self._quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        self.master.config(menu=self.menu_bar)

        plot_menu = tk.Menu(self.menu_bar, tearoff=0, font=10)
        plot_menu.add_command(label="Line", command=lambda: self._create_plot("Line"))
        plot_menu.add_command(label="Hist", command=lambda: self._create_plot("Hist"))
        plot_menu.add_command(label="Bar", command=lambda: self._create_plot("Bar"))
        self.menu_bar.add_cascade(label="Create Plot", menu=plot_menu)

        self.master.config(menu=self.menu_bar)

    def _create_plot(self, label):
        if self.__curr_table:
            MainModel(self.__curr_table.getSelectedDataFrame()).create_plot(label)

    def _create_new_table(self):
        self._close_table()
        frame = tk.Frame(self.master)
        self.__frame = frame

        frame.pack(fill='both', expand=True)

        self.__curr_table = Table(frame, showtoolbar=True, showstatusbar=True)
        self.__curr_table.show()

    def _save_file(self):
        if self.__frame:
            if not self.__current_file:
                self.__current_file = filedialog.asksaveasfilename(initialdir=self.default_path, filetypes=[('CSV File', '*.csv'),
                                                                                                            ('Textfile', '*.txt')])

            MainModel(self.__curr_table.model.df).save_file(self.__current_file)

            tk.messagebox.showinfo(title="INFO", message="Saving successful.".upper())

    def _close_table(self):
        if self.__frame:
            self.__frame.destroy()
            self.__frame = None

    def _open_file(self):
        file_path = filedialog.askopenfilename(initialdir=self.default_path, filetypes=[('CSV File', '*.csv'),
                                                                                        ('Textfile', '*.txt')])

        if file_path:
            self._close_table()
            frame = tk.Frame(self.master)
            frame.pack(fill='both', expand=True)

            self.__curr_table = Table(frame, dataframe=MainModel().open_file(file_path), showtoolbar=True, showstatusbar=True)
            self.__frame = frame
            self.__current_file = file_path
            self.__curr_table.show()

    def _quit(self):
        self.master.quit()