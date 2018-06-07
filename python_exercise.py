x = int(raw_input)("Enter the first integer:")
y = int(raw_input)("enter the second integer:")

print 'x = ', x 'type is', type(x)
print 'y = ', y 'type is', type(y)

if x>y:
    maximum=int(x)
    minimum=int(y)
else:
    maximum=int(y)
    minimum=int(x)
print 'The maximum is ', maximum
print 'The minimum is', minimum
print 'Maximum - minimum = ', maximum - minimum

