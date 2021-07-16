import math
def equations(a,b,c):
    l=[]
    dis =b*b-4*a*c
    sqrt_val =math.sqrt(abs(dis))
    if dis>0:
        s1=((-b+sqrt_val)/(2*a))
        s2=((-b-sqrt_val)/(2*a))
        l.append(int(s1))
        l.append(int(s2))
        return tuple(l)
    elif dis == 0:
        s1=(-b/(2*a))
        s2=(-b/(2*a))
        l.append(int(s1))
        l.append(int(s2))
        return tuple(l)
    else:
        d1=(-b/(2*a))
        s1=f"{d1}+i{sqrt_val}"
        s2=f"{d1}-i{sqrt_val}"
        l.append(s1)
        l.append(s2)
        return tuple(l)

if __name__ == '__main__': 
    a =equations(2,10,8)
    print(a)