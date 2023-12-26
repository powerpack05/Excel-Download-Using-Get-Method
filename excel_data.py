#Importing the necessary libraries
import pandas as pd
import os

#Storing the data in the dictinary data structure
data = {'ID':[number for number in range(1,11)],'NAME':['Manish','Hayat','Hanifa','Archana','Surya','Chameli',
                                                        'Prasad','Pradeep','Mariya','Hanisha']}
#Creating a pandas data frame
df = pd.DataFrame(data)
print(df.info())

#Getting the root directory
base_dir = os.path.abspath(os.path.dirname(__file__))
print("base  dir",base_dir)

#If doesn't folder doesn't exists it will create the folder
if not os.path.exists(os.path.join(base_dir,'reports')):
    os.mkdir('reports')
    print(f'Report Folder Created Successfully')

#exporting the dataframe into excel
df.to_excel(os.path.join(base_dir,'reports','Final_data.xlsx'),index=False)


