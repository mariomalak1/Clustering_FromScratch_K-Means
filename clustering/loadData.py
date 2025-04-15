import csv

class LoadData():
    defaultPercentage = 50
    
    def __init__(self, file_path, percentage_num_of_rows = 50, isLabeled = False):
        self.file_path = file_path
        self.isLabeled = isLabeled
        # put labels names if it have 
        self.labels = []

        # validate percentage_num_of_rows
        try:
            percentage_num_of_rows = float(percentage_num_of_rows)
            if(percentage_num_of_rows < 0 or percentage_num_of_rows > 100):
                percentage_num_of_rows = LoadData.defaultPercentage
        except:
            print("invalid number, will take default")
            percentage_num_of_rows = LoadData.defaultPercentage

        self.percentage_num_of_rows = percentage_num_of_rows / 100


    # load the data from the file
    def loadDataFromFile(self):
        with open(self.file_path, newline='') as csv_file:
            data = csv.reader(csv_file)
            
            data = list(data)
            # convert percentage to number of rows
            total = len(data)
            
            if(total == 0):
                return []

            # add labels names if it has
            if(self.isLabeled):
                for label in data[0]:
                    self.labels.append(label)

            num_of_rows = int(total * (self.percentage_num_of_rows))

            listOfData = []

            if(self.isLabeled):
                if(num_of_rows == total):
                    range_ = range(1, num_of_rows)
                else:
                    range_ = range(1, num_of_rows + 1)
            else:
                range_ = range(0, num_of_rows)


            for i in range_:
                listOfData.append(data[i])

        del data

        return listOfData 
