print("Calculate")
x=int(input("Enter your 1st no: "));
y=int(input("Enter your 2nd no: "));

sum=x+y;
sub=y-x;
mul=x*y;
divide=y/x;
Operation=input("enter your operation to perform : (sum,sub,mul,divide) ")
if Operation=='sub':
    print("your subtraction value is ",sub)
if Operation=='sum':
    print("your sum is ",sum)
if Operation=='mul':
    print("your product is ",mul)
if Operation=='divide':
    print("your output is ",divide)