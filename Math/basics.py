n = 6

#  ------------------------------Question 1------------------------------
#   * * * * * * * * *   
#     * * * * * * *     
#       * * * * *
#         * * *
        #   *
# for i in range(n):
#         for space in range(i+1):
#             print(" ", end=" ")
#         for j in range(2*n -(2*i +1)):  
#             print("*", end=" ")
        
#         for space in range(i+1):
#             print(" ", end=" ")
      
#         # Move to next line after printing stars for each row
#         print()

#  ------------------------------Question 2------------------------------
#   *  
#  ***
# ***** 
# *****  
#  ***
#   *   

# for i in range(n):
#     for space in range(n-i):
#         print(" ", end=" ")
    
#     for j in range(2*i +1):
#         print("*", end =" ")
#     print()
        
# for i in range(n):
#     for space in range(i+1):
#         print(" ", end=" ")
    
#     for j in range(2*n -(2*i +1)):
#         print("*", end =" ")
    
#     print()

#  ------------------------------Question 3------------------------------
    #  *
    #  **
    #  *** 
    #  ****
    #  *****
    #  ******  
    #  *****
    #  ****
    #  ***    
    #  **
    #  *

# for i in range(n):
#     for j in range(i+1):
#         print("*", end = " ")
#     print()
# for i in range(n):
#     for j in range(n-i-1):
#         print("*", end = " ")
#     print()    

#  ------------------------------Question 4 ------------------------------

# 1
# 01
# 101
# 0101
# 10101
# 010101

# for i in range(n):
#     for j in range(i+1):
#        if (i % 2 == 0):  # Even rows (0, 2, 4) should print 1s and 0s alternately
#             print(1 if j % 2 == 0 else 0, end="")
#        else:  # Odd rows (1, 3, 5) should print 0s and 1s alternately
#             print(0 if j % 2 == 0 else 1, end="")
       
#     print()    

#  ------------------------------Question 5 +++++++------------------------------
# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11  12  13  14  15
# 16  17  18  19  20  21

# for i in range(n):
#     for j in range(i+1):
#         print(i+j+1, end = " ")

#     print()


#  ------------------------------Question 6------------------------------

# ******
# *    *
# *    *
# *    *
# *    *
# ******

for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()