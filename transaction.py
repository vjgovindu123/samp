[2:01 PM] RevathiReddy (Guest)
for i in tmp:

    if(i.TransactionType=="INN"):

        sum+=i.Transaction_Amount

        if(sum1>1000):

            flag="High_risk"

        sum1

        for i in tmp:

            if(i.TransactionType=="OUT"):

                sum1+=i.Transaction_Amount

            if(sum1>800):

                flag="High_risk"

            for(i in Transaction_Date):

                if(count(account_key)>20):

                    flag="High_risk"

[#2:03 PM] RevathiReddy (Guest)
if request.method=="POST":

tmp=Transactions.object.filter{​​​​​

account_key=request.POST.get(('accountid'))

sum=0

sum1=0

flag=""

for i in tmp:

if(i.TransactionType=="INN"):

    sum+=int(i.Transaction_Amount)

else:

    sum!+=int(i.Transaction_Amount)

if(sum<600):

    flag="Low_risk"

else:

    flag="High_risk"

return

render(request,'home.html',{​​​​​

    'flag'.flag

}​​​​​)

}​​​​​

