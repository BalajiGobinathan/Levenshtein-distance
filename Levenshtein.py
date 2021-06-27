import numpy as np
import pandas as pd

# function for implementing the Levenshtein distance between 2 words

def Levfunc(str1,str2='Luca'):
    
    # creating an empty matrix with one extra row and column for null
    matrix = np.zeros((len(str1)+1, len(str2)+1))
    
    # filling up the matrix with distance values
    for i in range(0, len(str1)+1):
        for j in range(0, len(str2)+1):

            # filling up the (0,0)th value with zero
            if i==0 and j==0:
                matrix[i][j]=0
            
            # filling up the first row
            elif i==0:
                matrix[i][j] = matrix[i][j-1] + 1
            
            # filling up the first column
            elif j==0:
                matrix[i][j] = matrix[i-1][j] + 1
            
            # filling up the rest of the matrix values
            else:
                if str1[i-1]==str2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = 1 + min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])
    
    return int(matrix[len(str1)][len(str2)])
    
if __name__ == "__main__":
    
    # creating a list with columns list and reading the casv file
    col_list = ['HUNDENAME', 'GEBURTSJAHR_HUND', 'GESCHLECHT_HUND']
    df = pd.read_csv("20210103_hundenamen.csv", usecols = col_list)
    
    # calling the above function and storing the values in a set
    dognames = set()
    for str1 in df['HUNDENAME']:
        distance = Levfunc(str1)
        if distance==1:
            dognames.add(str1)

    print(dognames)
    print("Number of dognames that have a distance of 1 to Luca :", len(dognames))
    