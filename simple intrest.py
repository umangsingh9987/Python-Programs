p=int(input( "enter the marks in principal" ))
r=int(input( "enter the marks in rate of intrest" ))
t=int(input( "enter the marks in rate of time" ))
si= (p*r*t)/100

ci=p*(1+r/100)**t-p

print("si=",si)
print("ci",ci)
