s='aaabbbbcccccccceeeee'
l=list(s)
s1=list(set(l))

if len(s1)==2:
    print("Invalid")
else:
    sv=""
    sl=-1
    for i in s1:
        n=l.count(i)
        if n>sl:
            sl=n
            sv=i
    s1.remove(sv)
    sv=""
    sl=-1
    for i in s1:
        n=l.count(i)
        if n>sl:
            sl=n
            sv=i
    print(sv)
