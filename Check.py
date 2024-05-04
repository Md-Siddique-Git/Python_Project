print("Calculate")
x=int(input("Enter your 1st no: "));
y=int(input("Enter your 2nd no: "));

sum=x+y;
sub=y-x;
mul=x*y;
Operation=input("enter your operation to perform : (sum,sub,mul) ")
if Operation=='sub':
    print("your subtraction value is ",sub)
if Operation=='sum':
    print("your sum is ",sum)
if Operation=='mul':
    print("your product is ",mul)
