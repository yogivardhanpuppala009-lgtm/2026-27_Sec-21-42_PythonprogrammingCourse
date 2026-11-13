def total_and_average(num1, num2, num3):
    total = num1 + num2 + num3
    average = total / 3
    return total, average

m1, m2, m3 = 100, 70, 90
total, average = total_and_average(m1, m2, m3)
print("Total:", total)
print("Average:", average)