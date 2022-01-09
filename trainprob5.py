tl=int(input("enter the length of he train(meters): "))
ts=int(input("enter the speed of the train(km/h): "))
sm=int(input("Enter the speed of the person walking in the same direction(km/h): "))
rs=(ts-sm)*(5/18)
t=tl/rs
print("In",t,"seconds the train will cross the person.")