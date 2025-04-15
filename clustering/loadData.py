import csv

# validate the input "percentage_num_of_rows" -> percentage of the data needed to be read
# if he put invalid number will be "50%"
def validateNumOfRowsInput(percentage_num_of_rows):
    try:
        percentage_num_of_rows = float(percentage_num_of_rows)
        if(percentage_num_of_rows < 0 or percentage_num_of_rows > 100):
            percentage_num_of_rows = 50
    except:
        print("invalid number, will take default")
        percentage_num_of_rows = 50

    return percentage_num_of_rows


# load the data from the file, and also put it in the data structure of "Point" 
def loadDataFromFile(file_path, percentage_num_of_rows):
    pass


