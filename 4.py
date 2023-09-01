age=int(input("Enter the age of candidate"))
re=age>=18
out="can vote"*re+"cant vote"*(1-re)
print(out)
