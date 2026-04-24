a=int(input("Enter Mode (1 for Even-Odd, 2 For Name Reapet: )"))

if a==1:
    ev=int(input("Enter Your Number To Find Odd Or Even :"))
    if ev%2 == 0:
        print(ev,"Is Even")

    else:
        print(ev,"Is Odd")

elif a==2:
    name=input("Enter Your Name: ")

    reap=int(input("Enter Number You Have To Raepet Your Name: "))

    for reap in range(reap):
        print(name,reap)

else:
    print("Wrong Option!",a,"Choose 1 Or 2")