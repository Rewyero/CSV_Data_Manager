import pandas as pd

class FileManager:
    def __init__(self):
        pass

    # Write Dataframe into File
    def create_csv_file(self, file_path, dataframe):
        df = pd.DataFrame(dataframe)
        df.to_csv(file_path, index=False)

    # Read file and return pandas Dataframe
    def read_file(self, filePath):
        return pd.read_csv(filePath, delimiter=',')
