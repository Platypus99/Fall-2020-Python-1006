#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import math
from matplotlib import pyplot as plt


def euclidean_distance(a,b):
    diff = a - b
    return np.sqrt(np.dot(diff, diff))

def load_data(csv_filename):
    """ 
    Returns a numpy ndarray in which each row repersents
    a wine and each column represents a measurement. There should be 11
    columns (the "quality" column cannot be used for classificaiton).
    """
    
    data_all = np.genfromtxt(csv_filename, delimiter  = ';', skip_header = 1)
    data = data_all[:,:-1]
    return data
    # pass    
    
def split_data(dataset, ratio = 0.9):
    """
    Return a (train, test) tuple of numpy ndarrays. 
    The ratio parameter determines how much of the data should be used for 
    training. For example, 0.9 means that the training portion should contain
    90% of the data. You do not have to randomize the rows. Make sure that 
    there is no overlap. 
    """
    total_rows = dataset.shape[0]
    
    num_training_rows = math.floor(total_rows * ratio)
    train = dataset[:num_training_rows,:]
    test  = dataset[num_training_rows:,:]
    
    return(train, test)   
    # pass
    
def compute_centroid(data):
    """
    Returns a 1D array (a vector), representing the centroid of the data
    set. 
    """
    total_of_wines = sum(data)
    length_list = data.shape[0]
    average = total_of_wines / length_list
    return average
    
    
    # pass
    
def experiment(ww_train, rw_train, ww_test, rw_test):
    """
    Train a model on the training data by creating a centroid for each class.
    Then test the model on the test data. Prints the number of total 
    predictions and correct predictions. Returns the accuracy. 
    """
    ww_centroid = compute_centroid(ww_train)
    rw_centroid = compute_centroid(rw_train)
    
    total_ww_predictions = 0
    correct_ww_predictions = 0
    
    # go through each line (entry) in testing set
    ww_test_array_length = ww_test.shape[0]
    for row in range(ww_test_array_length):
        dist_to_ww = euclidean_distance(ww_test[row], ww_centroid)
        dist_to_rw = euclidean_distance(ww_test[row], rw_centroid)
        if dist_to_ww < dist_to_rw:
            correct_ww_predictions +=1
            total_ww_predictions+=1
        else:
            total_ww_predictions+=1
    
    ww_accuracy = correct_ww_predictions / total_ww_predictions        
            
            
    # repeat for rw       
    total_rw_predictions = 0
    correct_rw_predictions = 0        
    x = 0
    rw_test_array_length = rw_test.shape[0]
    
    # go through each line (entry) in testing set
    for rows in range(rw_test_array_length):
        dist_to_rw = euclidean_distance(rw_test[rows], rw_centroid)
        dist_to_ww = euclidean_distance(rw_test[rows], ww_centroid)
        x+=1
        if dist_to_rw < dist_to_ww:
            correct_rw_predictions+=1
            total_rw_predictions+=1
        else:
            total_rw_predictions+=1
            
    rw_accuracy = correct_rw_predictions / total_rw_predictions
            
            
    overall_correct_predictions = correct_ww_predictions + correct_rw_predictions
    overall_total_predictions = total_ww_predictions + total_rw_predictions
    overall_accuracy = overall_correct_predictions / overall_total_predictions
     
    # predictions fro total
    print("predictions made: ", overall_total_predictions)
    print("number correct predictions: ", overall_correct_predictions)
    print("accuracy of model: ", overall_accuracy)
     
    
    # predictions for ww
    print("\n")
    print("ww predictions made: ", total_ww_predictions)
    print("ww number correct predictions: ", correct_ww_predictions)
    print("ww accuracy of model: ", ww_accuracy)
    
    # predictions for rw
    print("\n")
    print("rw predictions made: ", total_rw_predictions)
    print("rw number correct predictions: ", correct_rw_predictions)
    print("rw accuracy of model: ", rw_accuracy)
     
     
         
     return overall_accuracy
    
    
    
    pass
    
def cross_validation(ww_data, rw_data, k):
    """
    Perform     qk-fold crossvalidation on the data and print the accuracy for each
    fold. 
    """
    interval = ww_data.shape[0] // k
    
    li_all_accuracies = []
    for items in range(k):
        
        
    
    
    
    pass

    
if __name__ == "__main__":
    
    ww_data = load_data('whitewine.csv')
    rw_data = load_data('redwine.csv')
    

    # Uncomment the following lines for step 2: 
    ww_train, ww_test = split_data(ww_data, 0.9)
    rw_train, rw_test = split_data(rw_data, 0.9)
    experiment(ww_train, rw_train, ww_test, rw_test)
    
    # Uncomment the following lines for step 3:
    #k = 10
    # acc = cross_validation(ww_data, rw_data, k)
    #acc = cross_validation(ww_data, rw_data) # this line has been replaced by preceding line as per update
    #print("{}-fold cross-validation accuracy: {}".format(k,acc))
    
