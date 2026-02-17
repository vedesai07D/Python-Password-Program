def skull():
    offset_padding = 30
    width = 35
    height = 15
    
    for i in range(height):
        for j in range(width + offset_padding):

            x = j - offset_padding

            # Conditions stored in variables
            head = (i >= 1 and i <= 8 and x >= 5 and x <= 29)

            leftEye  = (i >= 3 and i <= 5 and x >= 9 and x <= 12)
            rightEye = (i >= 3 and i <= 5 and x >= 22 and x <= 25)

            nose = (i >= 6 and i <= 7 and x >= 16 and x <= 18)

            jaw = (i >= 9 and i <= 13 and x >= 10 and x <= 24)

            teeth = (i >= 10 and i <= 13 and
                     (x == 14 or x == 17 or x == 20))

            cavity = (i >= 9 and i <= 13 and
                      (x == 12 or x == 13 or x == 16 or x == 17 or x == 20 or x == 21 or x == 24))

            if (head or jaw or teeth) and not leftEye and not rightEye and not nose and not cavity:
                print("*", end="")
            else:
                print(" ", end="")

        print()

def main():
    skull()
main()
