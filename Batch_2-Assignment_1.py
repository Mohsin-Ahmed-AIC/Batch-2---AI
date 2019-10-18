# -*- coding: utf-8 -*-
"""
Image Resizing Assignment
Mohsin Ahmed
AIC-035346
SAIMS - 1:15 to 5:15
"""
import glob
import numpy as np
from PIL import Image
import cv2

# Function for locating the files or folder
def image_folder():
    try:
        location = input("Please enter the complete file path to the image folder: ")
        extension = input("Please enter the extension of the files with dot: ")
        main_location = location + "/*" + extension.lower()
        if location == '':
            main_location = ('photos/*')
        
        return main_location
    except:
        print("Please provide valid path")

def num_of_files(image_folder):
    filelist = glob.glob(image_folder)
    num_of_files = len(filelist)
    print(num_of_files)
    return num_of_files

# Converting omages int
def image_list(images_conv):
    filelist1 = glob.glob(images_conv)
    return filelist1

# Creating a numpy array with respect to the file count
def creating_array(files):
    new_array = np.zeros((files, 200, 200 ,3))
    return new_array
#     print(new_array)

# Storing resized images into new array
def sizing(files_to_convert, final):
    k = 0
    for i in files_to_convert:
        x = np.array(Image.open(i))
        y = cv2.resize(x, (200, 200))
        final[k] = y
        k += 1
    return final
        
# Main function to call all the functions
def main():

        
    file_path = image_folder()
    
    files_count = num_of_files(file_path)
    
    image_list_save = image_list(file_path)
    
    array_size = creating_array(int(files_count))
    
    final_array = sizing(image_list_save, array_size)
    
    print(final_array.shape)
#     print(final_array[5])
    

if __name__ == '__main__':
    main()