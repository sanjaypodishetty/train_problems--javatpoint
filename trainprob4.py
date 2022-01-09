ts=int(input("ENter the train speed(km/h): "))
tl=int(input("Enter the length of the train(in meters): "))
pl=int(input("Enter the length of the platform(in meters): "))
s=ts*(5/18)
d=tl+pl
t=d/s
print("TTime taken to cross the platform is",t, "seconds")