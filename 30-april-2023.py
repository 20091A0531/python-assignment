QUESTION-1
Description - Create a small command-line program in Python to calculate the total invoice amount for the below purchases - 
Book - Introduction to Python Programming : Rs 499.00
Book - Python Libraries Cookbook : Rs. 855.00
Book - Data Science in Python : Rs. 645.00
Taxes and additional charges are described as details - 
GST : 12%
Delivery Charges : Rs. 250.00
-----------------------------

print("Introduction to Python Programming : Rs 499.00")
print("Python Libraries Cookbook : Rs. 855.00")
print("Data Science in Python : Rs. 645.00")
l=list(map(int,input("Enter number of books of each type from below you want to purchase by seperating with space").split()))
l1=[499.0,855.0,645.0]
result=0.0
for i in range(len(l)):
  result+=l[i]*l1[i]
result+=(result*20)/100+250
print("The total cost of all books is {}".format(result))
===========================================================

Question 2 - 

Description: Write a program in Python to print the number of unique letters in a string. Only new letters from the string should be counted and not duplicates.                                
Input : string1 = "India"
Output : uniqueLetters = i,n,d,a

Input : string1 = "Dedication"
Output : uniqueLetters = d,e,i,c,a,t,o,n
--------------------
s1=input("Enter the string to print the unique letters:")
uni=set(s1)
for i in uni:
  print(i,end=',')
============================================================
 
