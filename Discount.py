bill_amount=int(input("Enter the bill amount : "))
if bill_amount>=1000 :
    discount=5
elif bill_amount>=500 :
    discount=2
else : 
    discount=1
dis_amt=discount*bill_amount/100
print("Discounted value: %d" % dis_amt)
net_bill=bill_amount-dis_amt
print("Net Amount: %d" % net_bill)
