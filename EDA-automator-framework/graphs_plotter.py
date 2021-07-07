import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def transform_df(input_df):
    '''
    # function to check and transform the input df 
    # i/p: original df
    # o/p: transformed df to be passed to the Graphs function
    '''
    
    transformed_df = input_df.copy()
    
    # columns which have numeric values but should be considered as categorical column
    # This is not generic as it varies for every dataframe
    NUM_CATEGORICAL_EXCEPTIONS = ['zipcode', 'lat', 'long'] 
    
    for column in transformed_df:
        # convert columns with integer values but supposed to be categorical, to string type
        if ((transformed_df.dtypes[column] == np.int64 or transformed_df.dtypes[column] == np.float64) and 
            column in NUM_CATEGORICAL_EXCEPTIONS:
            transformed_df[column] = transformed_df[column].astype(np.object)
            print("Considering this column as categorical: ",column)
    
        # if column is string or date type and has unique values more than half the length of df, drop them 
        # eg: columns like car name, id don't need to be plotted
        if ((transformed_df.dtypes[column] == np.object or transformed_df.dtypes[column] == np.datetime64)
            and (transformed_df[column].nunique() > 0.5 * transformed_df.shape[0])):
            transformed_df = transformed_df.drop(column, axis=1)
            print("Not plotting for column: ", column)
    
        
    return transformed_df
    
    
    
def barplot(col_series, plots_directory):
    
    '''
    # Bar plot function plots the barplot of a categorical variable or Numeric descrete variable
    # i/p: The function takes the column & the destination directory where to save the barplot
    # o/p: The function saves the barplot into the directory '\\Plots\\Bar' under the parent directory.
    '''
    
    bar_directory = plots_directory +'\\Bar'
    
    # create directory if it doesn't exist
    if not os.path.exists(bar_directory):
        os.mkdir(bar_directory)
        
    os.chdir(bar_directory)
    
    plt.figure(figsize=(12,8))
    
    #if more than 20 categories, plot horizontal for better clarity
    if col_series.nunique() > 20:
        col_series.value_counts().plot(kind = 'barh')
    else:
        col_series.value_counts().plot(kind = 'bar')
    
    # so that x-axis values is horizontal
    plt.xticks(rotation = 'horizontal')
    
    
    plt.xlabel('Column - %s'%col_series.name)
    plt.ylabel('Count of Column - %s'%col_series.name) 
               
    plt.savefig('%s'%col_series.name)       
    plt.close() 
    
    
def boxplot(col_series, plots_directory):
    
    '''
    # Box plot function plots the boxplot of a Numeric continuous variable
    # i/p: The function takes the column & the destination directory where to save the boxplot
    # o/p: The function saves the boxplot into the directory '\\Plots\\Box' under the parent directory.
    '''
    
    box_directory = plots_directory +'\\Box'   
    
    # create directory if it doesn't exist
    if not os.path.exists(box_directory):
        os.mkdir(box_directory)  
    
    os.chdir(box_directory) 
    plt.figure(figsize=(12,8))
    
    
    plt.boxplot(col_series)           
    plt.xlabel('Column - %s'%col_series.name)            
             
    plt.savefig('%s'%col_series.name) 
    plt.close()
    


def histogram(col_series, plots_directory):
    '''
    # Histogram function plots the histogram of a Numeric continuous variable
    # i/p: The function takes the column & the destination directory where to save the histogram
    # o/p: The function saves the histogram into the directory '\\Plots\\Histogram' under the parent directory.
    '''
    hist_directory = plots_directory +'\\Histogram'
    
    # create directory if it doesn't exist
    if not os.path.exists(hist_directory):
        os.mkdir(hist_directory)
        
    os.chdir(hist_directory)
    plt.figure(figsize=(12,9))
    
    # get the edge of bins and use it to mark the x-axis values
    n, bins, edges = plt.hist(col_series,edgecolor='black')
    plt.xticks(bins)
    plt.xlabel('Column - %s'%col_series.name)
                
    plt.savefig('%s'%col_series.name)
    plt.close()
    
    


def Graphs(data, variables =[],directory = ''):
    
    '''
    # 'graph' function takes dataframe as input and plots relevant graphs and stores the plots in a directory.
    
    # i/p: The first takes 3 inputs.
    # The first argument 'data' is the dataframe which is mandatory.
    # The second argument is 'variables' which is optional. 
    # If input is specified, the plots are plotted & stored in a directory for the speciifed columns only.
    # If not specified, the plots are drawn for all the columns of the dataframe.
    # The third argument is 'directory' which is optional.
    # If input is specified, the drawn plots are saved in the specified directory/filepath,
    # else, it wil take the current directly and save them.
    # o/p: saves the .png files of plots in a directory
    '''
    # a condition is added to check whether the variables/ columns are are needed to be plotted are provided in input
    # if not the entire columns of the dataframe are taken as an input
    if not variables:
        variables = list(data.columns)
    
    # do some checks and transformation for the dataframe 
    data = transform_df(data[variables])
    
    variables = list(data.columns)
    
    # this is assigned to have a record of the parent directory
    parent_directory = os.getcwd()
    
        
    # a condition is added to check whether the path is provided in input
    # if not it will take the current working directory   
    if not directory:
        directory = parent_directory            
    
    # adding a try except block to catch exceptions
    try :
        # the directory is changed to the given directory
        # this is a way of checking whether the directory given in the input is valid or not
        os.chdir(directory)
        
        # to add a folder to the path, plots_directory is created
        plots_directory = directory + '\\Plots'
        
        # a counter is added to increament the value
        counter = 1

        # this loop is added to check whether there are existing Plots folder
        # if it exists a new folder is created and graphs are saved in that folder
        while True:

            # a check is added for the existance of the path
            # if not then create a folder with the name plots
            if not os.path.exists(plots_directory):
                os.mkdir(plots_directory)

                # breaking the loop
                break

            # id there are existing folders it will take the else route
            else:
                 # for the first instance we will be just concatinating
                if counter == 1:
                    plots_directory = plots_directory + '(%d)'%counter

                # here we will be indexing and concatinating the counter
                else:

                    # this is the starting index
                    index = plots_directory.find('(')

                     #  we are adding  a counter value to represent a new folder 
                    plots_directory = plots_directory[: index+ 1] + '%d)'%counter         

                # incrementing the counter
                counter +=1

                # continuing the loop
                continue
        
        
        print("Plotting under directory: ",plots_directory)
        
        # a check is added for the existance of the path
        # if not then create a folder with the name plots
        if not os.path.exists(plots_directory):
            os.mkdir(plots_directory)        
    
        print("\nList of column names and their corresponding plot-folder: ")
        
        # for loop to traverse the list of columns
        for column in variables:
            
            # each time, the datatype of the column is checked.
            column_type = data[column].dtype
            
            # if it is not 'object' type ie numerical then it is further checked if the numeric variable is discrete.
            if not column_type == 'object':
                
                # if a variable has less 15 unique values,
                # we will consider them as categorical, or else we consider them as numerical
                if data[column].nunique() < 15:
                    
                    # if the numeric variable has less than 15 unique values, then a bar plot is drawn calling the 
                    # Barplot function.
                    barplot(data[column], plots_directory)
                    print(column, " - Bar plot.")
                
                else:
                    # if the numeric varible has more than 15 unique values, then histogram & boxplot 
                    # are drawn by calling the Histogram & Boxplot functions.
                    histogram(data[column], plots_directory)  
                    print(column, " - Histogram.")
                    boxplot(data[column], plots_directory)
                    print(column, " - Box plot.")
                    
            # Finally, the else condition is for object type columns, 
            # for which a bar plot is drawn by calling the Barplot function.
            else:     
                barplot(data[column], plots_directory)
                print(column, " - Bar plot.")

    
    # this will be raised when the directory is not existing
    except FileNotFoundError:
        print('Not Existing Directory')
    
    # this is raised when the column given in the input is not found in the dataframe
    except KeyError:
        print('Column %s not found in DataFrame'%column)
        
    # changing it back to the initial file directory using parent directory
    os.chdir(parent_directory)
    