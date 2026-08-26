


# elif chains check top to bottom, and stop at the FIRST true condition.
# think about which threshold needs to be checked FIRST so it isn't skipped by a broader one below it.

speed = 70

if speed > 90:
    print("Very fast")
elif speed > 70:
    print("Fast")
else:
    print("Normal")