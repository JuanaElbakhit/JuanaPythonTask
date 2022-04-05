""" 1. Initially, import the CSV module and sqlite3 module."""
import pandas as pd
import unittest
import numpy as np
import matplotlib.pyplot as plot
import csv, sqlite3
from IPython.display import display
# create PythonTask class the super class of my code
class PythonTask():
      def __int__():
            def cofficients():
                        #here the inhiredte classes for methods to apply it to datasets
                        print("Juana Task ")
   
class IdealFunctions():
      def __init__(self,X,Y):
            self.X=file_contents_ideal.iloc[:,0]
            self.Y=file_contents_ideal.iloc[:,11]
""" 1. Then, connect to the database using the ideal.connect() function.
 Assume DB name as "traindata.db""""
connection = sqlite3.connect('ideal.db')

# 2. Create a cursor object in order to query on the database.
cursor = connection.cursor()

# 3. Create a table with the columns matching to the contents of the CSV file.
idealDataTable = '''CREATE TABLE IF NOT EXISTS ideal(x Integer NOT NULL, y1 INTEGER NOT NULL,y2 INTEGER NOT NULL,y3 INTEGER NOT NULL, y4 INTEGER NOT NULL,y5 INTEGER NOT NULL,y6 INTEGER NOT NULL,y7 INTEGER NOT NULL, y8 INTEGER NOT NULL, y9 INTEGER NOT NULL , y10 INTEGER NOT NULL, y11 INTEGER NOT NULL ,y12 INTEGER NOT NULL, y13 INTEGER NOT NULL, y14 INTEGER NOT NULL , y15 INTEGER NOT NULL , y16 INTEGER NOT NULL , y17 INTEGER NOT NULL , y18 INTEGER NOT NULL, y19 INTEGER NOT NULL , y20 INTEGER NOT NULL , y21 INTEGER NOT NULL , y22 INTEGER NOT NULL , y23 INTEGER NOT NULL , y24 INTEGER NOT NULL ,y25 INTEGER NOT NULL , y26 INTEGER NOT NULL , y27 INTEGER NOT NULL , y28 INTEGER NOT NULL , y29 INTEGER NOT NULL , y30 INTEGER NOT NULL , y31 INTEGER NOT NULL , y32 INTEGER NOT NULL , y33 INTEGER NOT NULL , y34 INTEGER NOT NULL , y35 INTEGER NOT NULL , y36 INTEGER NOT NULL , y37 INTEGER NOT NULL , y38 INTEGER NOT NULL , y39 INTEGER NOT NULL , y40 INTEGER NOT NULL , y41 INTEGER NOT NULL , y42 INTEGER NOT NULL , y43 INTEGER NOT NULL , y44 INTEGER NOT NULL , y45 INTEGER NOT NULL , y46 INTEGER NOT NULL , y47 INTEGER NOT NULL , y48 INTEGER NOT NULL , y49 INTEGER NOT NULL , y50 INTEGER NOT NULL);'''

# Execute SQL statement to create table 
cursor.execute(idealDataTable)

# 4. Put the CSV file contents using the csv.reader() function.
file_ideal = open('ideal.csv')
file_contents_ideal = csv.reader(file_ideal)

# 5. Put the CSV file contents contents using the csv.reader() function.
insert_records_ideal = "INSERT INTO ideal (x, y1,y2,y3,y4, y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23,y24,y25,y26,y27,y28,y29,y30,y31,y32,y33,y34,y35,y36,y37,y38,y39,y40,y41,y42,y43,y44,y45,y46,y47,y48,y49,y50) VALUES(?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?);"

# executemany() replaces (?, ?) with the next two comma separated values
cursor.executemany(insert_records_ideal, file_contents_ideal)

# Cross-check the inserted records
select_all = "SELECT * FROM ideal"
rows = cursor.execute(select_all).fetchall()

print('print inserted records from ideal table')
file_contents_ideal=pd.read_csv('ideal.csv')
print(file_contents_ideal.shape)
print(file_contents_ideal)

# 6. Commit the changes to the database and close the database connection.
connection.commit()
connection.close()
def Cofficients(X,Y):
      print("cofficients of ideal function (x,y11):")
   
X=file_contents_ideal.iloc[:,0]
Y=file_contents_ideal.iloc[:,11]
plot.scatter(X,Y)
plot.show()

# building model
x_mean=np.mean(X)
y_mean=np.mean(Y)
#total number of values
#using the formula to calculate m & c
num=0
den=0
rmse=0
for i in range(len(X)):
      num+= (X[i]- x_mean)*(Y[i]- y_mean)
      den+= (X[i]- x_mean)**2
m=num/den
c= y_mean-(m*x_mean)
print('cofficients of X and Y')
print(m,c)
file_contents_ideal['cofficients value :']= m
print('RMSE result for X and Y:')
y_pred= m*X + c
print('prediction values')
print(y_pred)
rmse += (Y-y_pred)**2
rmse=np.sqrt(rmse/50)
print("RMSE")
print(rmse)
# Calculating R2 Score
ss_tot=0
ss_res=0
for i in range(len(X)):
      ss_tot += (Y- y_mean)**2
ss_res += (Y-y_pred)**2
print("sum of squares of ideal function 1:")
print(ss_res)
# Ploting Scatter Points
plot.scatter(X,Y)
plot.scatter(X,y_pred, color='red')
plot.show()

def Cofficients_idealfun2(X,Y2):
      print("cofficients of ideal function (x,y12):")
   
X=file_contents_ideal.iloc[:,0]
Y2=file_contents_ideal.iloc[:,12]
plot.scatter(X,Y2)
plot.show()

# building model
x_mean=np.mean(X)
y2_mean=np.mean(Y2)
#total number of values
#using the formula to calculate m & c
num=0
den=0
rmse=0
for i in range(len(X)):
      num+= (X[i]- x_mean)*(Y2[i]- y_mean)
      den+= (X[i]- x_mean)**2
m=num/den
c= y2_mean-(m*x_mean)
print('cofficients of X and Y2')
print(m,c)
file_contents_ideal['cofficients value :']= m
print('RMSE result for X and Y2:')
y2_pred= m*X + c
print('prediction values')
print(y2_pred)
rmse += (Y2-y2_pred)**2
rmse=np.sqrt(rmse/50)
print("RMSE")
print(rmse)
# Calculating R2 Score
ss_tot=0
ss_res2=0
for i in range(len(X)):
      ss_tot += (Y2- y2_mean)**2
ss_res2 += (Y2-y2_pred)**2
print("sum of squares of ideal function 2 ")
print(ss_res2)
# Ploting Scatter Points
plot.scatter(X,Y2)
plot.scatter(X,y2_pred, color='red')
plot.show()

def Cofficients_idealfun3(X,Y3):
      print("cofficients of ideal function (x,y13):")
   
X=file_contents_ideal.iloc[:,0]
Y3=file_contents_ideal.iloc[:,13]
plot.scatter(X,Y3)
plot.show()

# building model
x_mean=np.mean(X)
y3_mean=np.mean(Y3)
#total number of values
#using the formula to calculate m & c
num=0
den=0
rmse=0
for i in range(len(X)):
      num+= (X[i]- x_mean)*(Y3[i]- y_mean)
      den+= (X[i]- x_mean)**2
m=num/den
c= y3_mean-(m*x_mean)
print('cofficients of X and Y3')
print(m,c)
file_contents_ideal['cofficients value :']= m
print('RMSE result for X and Y3:')
y3_pred= m*X + c
print('prediction values')
print(y3_pred)
rmse += (Y3-y3_pred)**2
rmse=np.sqrt(rmse/50)
print("RMSE")
print(rmse)
# Calculating R2 Score
ss_tot=0
ss_res3=0
for i in range(len(X)):
      ss_tot += (Y3- y3_mean)**2
ss_res3 += (Y3-y3_pred)**2
print("sum of squares of ideal function 3")
print(ss_res3)
# Ploting Scatter Points
plot.scatter(X,Y3)
plot.scatter(X,y3_pred, color='red')
plot.show()
def Cofficients(X,Y4):
      print("cofficients of ideal function (x,y14):")

X=file_contents_ideal.iloc[:,0]
Y4=file_contents_ideal.iloc[:,14]
plot.scatter(X,Y4)
plot.show()
# building model
x_mean=np.mean(X)
y4_mean=np.mean(Y4)
#total number of values
#using the formula to calculate m & c
num=0
den=0
rmse=0
for i in range(len(X)):
      num+= (X[i]- x_mean)*(Y4[i]- y_mean)
      den+= (X[i]- x_mean)**2
m=num/den
c= y4_mean-(m*x_mean)
print('cofficients of X and Y')
print(m,c)
file_contents_ideal['cofficients value :']= m
print('RMSE result for X and Y:')
y4_pred= m*X + c
print('prediction values')
print(y_pred)
rmse += (Y4-y4_pred)**2
rmse=np.sqrt(rmse/50)
print("RMSE")
print(rmse)
# Calculating R2 Score
ss_tot=0
ss_res4=0
for i in range(len(X)):
      ss_tot += (Y4- y4_mean)**2
ss_res4 += (Y4-y4_pred)**2
print("sum of squares of ideal function 4:")
print(ss_res)
# Ploting Scatter Points
plot.scatter(X,Y4)
plot.scatter(X,y4_pred, color='red')
plot.show()
def mapping_test_case(X):
      X=X=file_contents_ideal.iloc[:,0]
      return(ss_res),(ss_res2),(ss_res3),(ss_res4)
print('mapping the test case to the ideal functions')
Y_idealFunctions=mapping_test_case(X)
print(Y_idealFunctions)

class traingData():
      def __init__(self,W,Z):
            W=file_contents.iloc[:,0]
            Z=file_contents.iloc[:,1]
# 2. Then, connect to the database using the sqlite3.connect() function.
# Assume DB name as "traindata.db"
connection = sqlite3.connect('traindata.db')

# 3. Create a cursor object in order to query on the database.
cursor = connection.cursor()

# 4. Create a table with the columns matching to the contents of the CSV file.
TrainingDataTable = '''CREATE TABLE IF NOT EXISTS Train(x Integer NOT NULL, y1 INTEGER NOT NULL,y2 INTEGER NOT NULL,y3 INTEGER NOT NULL, y4 INTEGER NOT NULL);'''

# Execute SQL statement to create table 
cursor.execute(TrainingDataTable)

# 5. Put the CSV file contents using the csv.reader() function.
file = open('train.csv')
file_contents = csv.reader(file)

# 6. Put the CSV file contents contents using the csv.reader() function.
insert_records = "INSERT INTO Train (x, y1,y2,y3,y4) VALUES(?, ?,?,?,?)"

# executemany() replaces (?, ?) with the next two comma separated values
cursor.executemany(insert_records, file_contents)

# Cross-check the inserted records
select_all = "SELECT * FROM Train"
rows = cursor.execute(select_all).fetchall()

print('print inserted records from TrainingData table')
file_contents=pd.read_csv('train.csv')
print(file_contents.shape)
print(file_contents)

# 7. Commit the changes to the database and close the database connection.
connection.commit()
connection.close()
def Cofficients_Training(W,Z):
      print('cofficient for training dataset')

W=file_contents.iloc[:,0]
Z=file_contents.iloc[:,1]
plot.scatter(W,Z)
plot.show()
# building model
w_mean=np.mean(W)
z_mean=np.mean(Z)
#total number of values
#using the formula to calculate m & c
num=0
den=0
rmse=0
for i in range(len(W)):
      num+= (W[i]- w_mean)*(Z[i]- z_mean)
      den+= (W[i]- w_mean)**2
m=num/den
c= y_mean-(m*w_mean)
print('cofficients of W and Z')
print(m,c)
# i store the data to new column in database
file_contents['cofficients value :']= m
print('RMSE training data')
z_pred= m*W + c
print('prediction values')
print(y_pred)
rmse += (Z-z_pred)**2
rmse=np.sqrt(rmse/50)
print("RMSE")
print(rmse)
# Calculating R2 Score
ss_tot=0
ss_res=0
for i in range(len(W)):
      ss_tot += (Z- z_mean)**2
ss_res += (Z-z_pred)**2
r2= 1-(ss_res/ss_tot)
print("R2 score")
print(r2)
# Ploting Scatter Points
plot.scatter(W,Z)
plot.scatter(W,z_pred, color='red')
plot.show()

                         
class TestData():
     def __init__(self,W,Z):
        A=file_contents_test.iloc[:,0]
        B=file_contents_test.iloc[:,1]

                              
""" 1. Then, connect to the database using the test.connect() function.
Assume DB name as "traindata.db""""
connection = sqlite3.connect('test.db')

"""2. Create a cursor object in order to query on the database."""
cursor = connection.cursor()

""" 3. Create a table with the columns matching to the contents of the CSV file."""
testDataTable = '''CREATE TABLE IF NOT EXISTS test(x Integer NOT NULL, y INTEGER NOT NULL );'''

# Execute SQL statement to create table 
cursor.execute(testDataTable)

# 4. Put the CSV file contents using the csv.reader() function.
file_test = open('test.csv')
file_contents_test = csv.reader(file_test)


# 5. Put the CSV file contents contents using the csv.reader() function.
insert_records_test = "INSERT INTO test (x, y) VALUES(?,?);"

# executemany() replaces (?, ?) with the next two comma separated values
cursor.executemany(insert_records_test, file_contents_test)

# Cross-check the inserted records
select_all = "SELECT * FROM test"
rows = cursor.execute(select_all).fetchall()

print('print inserted records from test table')
file_contents_test=pd.read_csv('test.csv')
print(file_contents_test.shape)
print(file_contents_test)


# 6. Commit the changes to the database and close the database connection.
connection.commit()
connection.close()

def cofficients_testData(A,B):
      print("Test Data:")
A=file_contents_test.iloc[:,0]
B=file_contents_test.iloc[:,1]
plot.scatter(A,B)
plot.show()
# building model
a_mean=np.mean(A)
b_mean=np.mean(B)
"""total number of values
using the formula to calculate m & c"""
num=0
den=0
rmse=0
for i in range(len(A)):
    try:
      num+= (A[i]- a_mean)*(B[i]- b_mean)
      den+= (A[i]- a_mean)**2
      m=num/den
      c= y_mean-(m*a_mean)
      print('cofficients of W and Z')
      print(m,c)
      break
    except:
      print("division by zero")
      print()
file_contents_test['cofficients value :']= m
print("RMSE for test data:")
b_pred= m*A + c
print('prediction values')
print(b_pred)
rmse += (B-b_pred)**2
rmse=np.sqrt(rmse/50)
print("RMSE")
print(rmse)
# Calculating R2 Score
ss_tot=0
ss_res=0
for i in range(len(A)):
      ss_tot += (B- b_mean)**2
ss_res += (B-b_pred)**2
r2= 1-(ss_res/ss_tot)
# Map test data
display(r2[0:100])
print("R2 score")
print(r2)
# Ploting Scatter Points
plot.scatter(A,B)
plot.scatter(A,b_pred, color='red')
plot.show()
class TestCofficients(unittest.TestCase):
    def test_Data(self):
          a=cofficients_testData(A,B)
          b=Cofficients_Training(W,Z)  
          self.assertEqual(a,b)
          a1=Cofficients_idealfun2(X,Y2)
          b1=Cofficients_idealfun3(X,Y3)
          self.assertEqual(a1,b1)
      
           
          
      
def main():
  PythonTask=PythonTask()
        
if __name__ == '__main__':
      unittest.main()
    
