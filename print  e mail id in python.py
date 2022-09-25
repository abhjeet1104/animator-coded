# initializing strings
test_str = 'Abhijeetsinghoberoi1104@gmail.com'
 
# printing original string
print("The original string is : " + str(test_str))
 
res=test_str[test_str.find('@')+1:]
 
# printing result
print("The extracted domain name : " + str(res))
