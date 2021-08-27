import random, time

start = int(input("Enter Starting value:"))
end = int(input("Enter Ending value:"))
t = 0
u_num = 0

start_time = time.time()

a = (random.randint(start, end))

while u_num != a:
    u_num = int(input("Guess the no =>"))

    if u_num > a:
        end = u_num
        print("think smaller than", u_num, ".Now your range is", start, "-", end)
    elif u_num < a:
        start = u_num
        print("think greater than", u_num, ".Now your range is", start, "-", end)
    t = t + 1
print(u_num, "is correct!\nYou Guessed in", t, "trials.")

end_time = time.time()
print("You finished in", int(end_time - start_time), "seconds.")
