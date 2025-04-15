import csv

class LoadData():
    defaultPercentage = 50
    
    def __init__(self, file_path, percentage_num_of_rows):
        self.file_path = file_path

        # validate percentage_num_of_rows
        try:
            percentage_num_of_rows = float(percentage_num_of_rows)
            if(percentage_num_of_rows < 0 or percentage_num_of_rows > 100):
                percentage_num_of_rows = LoadData.defaultPercentage
        except:
            print("invalid number, will take default")
            percentage_num_of_rows = LoadData.defaultPercentage

        self.percentage_num_of_rows = percentage_num_of_rows


    # load the data from the file
    def loadDataFromFile(self):
        pass


