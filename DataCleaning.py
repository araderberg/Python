#Step 1: Import libraries.
##pandas, numpy. These are the necessary libraries when it comes to data science.

# Importing the necessary libraries.
import pandas as pd
import numpy as np

#Step 2: Getting the data-set from a different source and displaying the data-set.
##Jupyter Notebook to practice this tutorial then there should be no problem to read the CSV file.

# Reading a CSV file
df = pd.read_csv("death.csv",
                                  dtype = {'mrn': int, 'batch_id': int, 'dose_number': int, 'date_time_of_service': str,
                                                   'date_of_death': str, 'vaccine_name': str, 'date_of_birth': str,
                                                   'age': str, 'Days_until_death_from_this_dose': str})  #low_memory=False
df.head(5)

#Step 3: Removing the unused or irrelevant columns
##This step involves removing irrelevant columns such as mrn, date_of_birth, Days_until_death_from_this_dose, mand many more,

# Dropping unused columns.
to_drop = ['mrn',
          'date_of_birth',
          'Days_until_death_from_this_dose']

df.drop(to_drop, inplace = True, axis = 1)
df.head(5)

#Step 4: Renaming the column names as per our convenience.
##This step involves renaming the column names as they could be confusing and hard to understand.

# Renaming the column names
new_name = {'age': 'Age',
           'vaccine_name': 'VaccineName',
           'dose_number': 'DoseNo',
           'batch_id': 'BatchID',
            'date_time_of_service':'DateOfService',
           'date_of_death':'DeathDate'
            }

df.rename(columns = new_name, inplace = True)
df.head()

#Step 5: Replacing the value of the rows if necessary.
##This step involves replacing the incomplete values or making the values more readable, such as in here
###the Dose number field consists of the values 1 thru 11 being 1 as One and 2 as Two an so on (since we don't have Sex or any other coded data, we will use the dose number as an example.

# Replacing the values in the row
replace_values = {1: 'One', 2: 'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven'}

df = df.replace({"DoseNo": replace_values})                                                                                             

df.head()
