# Python Module 7  
## *Submitted 3/1/2022*   
## Brandon Lorge

### Objective:

From the course assignment: “… create a new script that demonstrates how Pickling and Structured error handling work.”  This module did not contain a starter file as in module 6, nor did it indicate the need for a menu.


### Approach:

For the separation of concerns, I created the sections: Data, Processing, and Presentation. The exceptions are performed in the presentation rather than processing, so that may not be the most strict separation of concerns. I created a while true loop to present a menu in order to give some interface for reading/writing to the file and entering more records into the list.

There are two data inputs: ID and Name and both are comparing to the builtin Python isnumeric(). If ID is false, it will raise an exception. If Name is true, it will raise an exception.

The other part of the assignment is to work with pickling. Although there were only two functions, I chose to create the class PickleFile to practice working with classes, and in case I want to expand on the program in the future and add exception classes. I noticed that the pickle.load(file) only reads one row so it was only returning the first input line on the file to the human. Using a try loop gave it the ability to keep going until all rows were read. (I could not get a for loop to work on this)

def read_data_from_file(file_name):
    file = open(file_name, "rb")
    while True:
        try:
            list_of_data = pickle.load(file) # load() only loads one row of data.
            print(list_of_data)
        except Exception as e:
            print("Here's confirmation that all contents of file were loaded!")
            break
    file.close()
    print("=" * 60)


### Data Considerations:


Since I used the  isnumeric() as the builtin, it will accept blank/null. I tried using “None” but that didn’t work. A future enhancement would be to raise errors for cases where the user hits Enter instead of inputting any value for either input.

Additionally, the pickle loop prints “None” at the end of the list. I put in the repeating equal sign in the function outside the try loop to see if it was related and it does not appear to be. I have tried other steps to track it down and have not yet found it so it would be a future enhancement to remove the “none”

https://github.com/blorge01/ITFnd100-Module07/blob/main/Extra%20None%20after%20read%20from%20pickle.png

Lastly, the structured error handling is in place, however it does not prevent the file from getting bad data. If it raises an error, it still writes to the file. For instance I can enter “ “ and “ “ and get a row with two empty values. I can also enter Id 9B and get an error, but it still saves it to the file and reads it back.


### Run from Terminal:

 
https://github.com/blorge01/ITFnd100-Module07/blob/main/Run%20from%20Console.png





