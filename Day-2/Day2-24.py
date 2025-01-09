#def a function find_total_avg() that takes 2 values and returns total and its average

#read two values and pass these values to the fn find_total_avg() and print total and average

def find_total_avg(n1,n2):
        total=n1+n2
        avg=total/2.0
        return (total,avg)
a=float(input("a: "))
b=float(input("b:"))
total,avg=find_total_avg(a,b)
print("Total:",total,"avg",avg)