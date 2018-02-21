#NAME: Pablo Arroyo
#----------------------------------------------------------------------------
#PYTHON LAB 2
#----------------------------------------------------------------------------
#(1) SAVE ALL YOUR WORK IN A PYTHON FILE WITH YOUR NAME, LIKE THIS: KelleyLab2Functions.py
#       (Just do a "Save As" and add your last name to the beginning of the
#       file name.)
#(2) THE FINAL VERSION OF THE CODE SHOULD NOT HAVE ERRORS. IT SHOULD RUN IN PYTHON.
#       [NOTE: RUN THE FINAL VERSION OF THE CODE ON A CLASS MACHINE PRIOR TO SUBMISSION.]
#(3) EMAIL THE FINAL WORKING VERSION TO THE LAB EMAIL ADDRESS.
#----------------------------------------------------------------------------
#Naming conventions we will follow in class:
#   Variables are lowercase, with words separated by underscores.[Example Variable: dna_seq="TTATAGT"]
#   Functions are lowercase, with words separated by underscores.[Example Function: return_of_the_king(aragorn)]
#----------------------------------------------------------------------------
#NOTES:
#- Most questions can be answered by reading the Python book
#   and the "Python Docs" under the Python "Help" Menu.
#- Read the instructions for each function CAREFULLY.
#- It is very important to use the function names and the number of 
#   function parameters EXACTLY as they appear in the lab exercises.
#- When finished, remove any function calls or print statements inside or outside
#   of the function used to test the functions.
#----------------------------------------------------------------------------
#PART 1 - SIMPLE FUNCTIONS: DEFINING & CALLING

#FUNCTION NAME: multiply
#NUMBER OF PARAMETERS: 1 (An integer)
#PURPOSE: The function should:
#           (1) Take an integer in as an argument.One parameter, call it fx
#           (2) Multiply the integer by 10.
#           (3) Return the multiplied value.
#RETURN VALUES: A multiplied value. (An integer)


#== FUNCTION 1 ==
def multiply(fx):
    times_ten=fx*10
    return times_ten


#HINT(1): First line of the function -
#           def multiply(fx):

#HINT(2): Calling the function:
#           times_ten=multiply(98)
#           print (times_ten)

#----------------------------------------------------------------------------
#PART 2 -

#FUNCTION NAME: addition
#PARAMETERS: 2 (Two integers)
#PURPOSE: The function should:
#           (1) Take in two integers as arguments.Paramters: fx, fy
#           (2) Add the two integers together.
#           (3) Return the added value.
#RETURN VALUES: An added value. (An integer)


#== FUNCTION 2 ==
def addition(fx,fy):
    add=fx+fy
    return add


#DATASET FOR PART 2:
val1=16
val2=8

#Test the function with 8 and 16.

#Now test it with val1 and val2

#Set the returned results to a variable called "result". Then print out result.
#results = addition(val1,val2) #we are setting the addition of these to a variable
#print(results)  #we are printing the results
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#PART 3 - BIOINFORMATICS

#FUNCTION NAME: dna_splice
#PARAMETERS: 2 (Two DNA sequences)
#PURPOSE: The function should:
#           (1) Take in two DNA sequences as arguments. Parameters: fseq1, fseq2
#           (2) Concatenate the sequences together.
#           (3) Return the concatenated sequence.
#RETURN VALUES: A concatenated sequence. (A string)


#== FUNCTION 3 ==
def dna_splice(fseq1,fseq2):
    combine = fseq1+fseq2
    return combine


# Test it with these two sequences: "AGGA" and "CTTC"
#What should be returned?  _____ I obtained 'AGGACTTC'
#What did you actually get?  ______ I got the same thing.

#Use the function to splice together "dna1" and "dna2" below.
#DATASET FOR PART 3 & 4:
dna1="CGGCGGACGGGTGAGTAACACGTGGG"
dna2="GGTGAGTAACAC"

#Test the function giving "dna1" and "dna2" as arguments.
#Set the returned value to a variable called "output". Print "output".
#output=dna_splice(dna1,dna2)
#print(output)
#----------------------------------------------------------------------------
#PART 4 -

#FUNCTION NAME: three_prime_end
#PARAMETERS: 1 (A DNA sequence)
#PURPOSE: The function should:
#           (1) Take in a DNA sequence as an argument.
#           (2) Extract the last 10 bases of the DNA sequence. [HINT: Slicing strings?]
#           (3) Return the extracted bases.
#RETURN VALUES: The extracted bases of a DNA sequence. (A string)


#== FUNCTION 4 ==
def three_prime_end(fdna):
    fdna_slice=fdna[-10:]
    return fdna_slice

#Test the function with "dna1", and set the returned result to variable "my_slice".
#my_slice = three_prime_end(dna1)
#print(my_slice)
#Test it again with "dna2", and set the returned result to "my_slice2".
#my_slice2 = three_prime_end(dna2)
#print(my_slice2)
#Print "my_slice" and "my_slice2".
#print(my_slice)
#print(my_slice2)
#----------------------------------------------------------------------------
#PART 5 - BMI STUDENTS (Extra practice for others)

#FUNCTION NAME: multiply_and_divide
#PARAMETERS: 3 (Three integers)
#PURPOSE: The function should:
#           (1) Take in three integers as arguments. The first two integers will be part of the numerator.
#                   The third integer will be part of the denominator.
#           (2) Multiply the two numerator integers together.
#           (3) Divide the multiplied numerator by the denominator.
#           (4) Return the "bodmas" value.
#                   "bodmas" => [Brackets of Division, Multiplication, Addition, and Subtraction]. 
#RETURN VALUES: A "bodmas" value. (A float)


#== FUNCTION 5 ==
def multiply_and_divide(fx,fy,fz):
    multndiv= (fx*fy)/fz
    return multndiv



#DATASET FOR PART 5:
num1=2
num2=2
denom=16

#Test the function when "num1", "num2", and "denom".
#print(multiply_and_divide(num1,num2,denom))
#Set the returned results to a variable called "bodmas". Print "bodmas". What happens?
#bodmas=multiply_and_divide(num1,num2,denom)
#print(bodmas)
#Try it again with denom set to 16.0 What do you get? _____ still the same value which is 0.25
#denom=16.0
#bodmas=multiply_and_divide(num1,num2,denom)
#print(bodmas)
#Now try to adjust the function to accommodate decimal values.
#What does Python refer to decimal values as?  _____ floating points

