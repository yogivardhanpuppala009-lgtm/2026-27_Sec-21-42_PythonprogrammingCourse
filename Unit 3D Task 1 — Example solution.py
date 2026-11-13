def rectangle_area_perimeter(length, width):
    area = length * width 
    perimeter =2 * (length + width)
    return area, perimeter 

length =900
width   =300 
area, perimeter = rectangle_area_perimeter(length, width)
print("Area:", area)
print("Perimeter:", perimeter)