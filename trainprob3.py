ts=int(input("Enter the train speed(km/h): "))
c=int(input("Crosses the brigde in(seconds): "))
tl=int(input("The length of the train is(in meters): "))
s=ts*(5/18)
x=c*s-tl
print("The length of the bridge is:",x)