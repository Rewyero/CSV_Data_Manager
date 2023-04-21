"""
----Create an Instance of FileManager and CustomPlot---
self.__file_manager = FileManager()
self.__custom_plot = CustomPlot(df=df)
---- Set the Dataframe from pandastable or ReadFile
self.__current_df = df
"""
import pandas as pd
import os
from FileManager import FileManager
from CustomPlot import CustomPlot

class MainModel:
    def __init__(self, df = None):
        self.__file_manager = FileManager()
        self.__custom_plot = CustomPlot(df=df)
        self.__current_df = df

    def create_plot(self, txt):
        self.__custom_plot.create_plot(txt)

    def create_new_df(self):
        self.__current_df = pd.DataFrame()

    def open_file(self, file_path):
        return self.__file_manager.read_file(filePath=file_path)

    def save_file(self, file_path):
        if self.__current_df is not None:
            if not file_path.endswith('.csv') and file_path:
                file_path = os.path.splitext(file_path)[0] + '.csv'
            self.__file_manager.create_csv_file(file_path, self.__current_df)