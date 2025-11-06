import math

# Information about units used for calculation
print("Note that all measurements are to be provided in centimeters.") 

# Calculate for the square
length_square = float(input("What is the length of a side of the square? "))
area_square = length_square ** 2
print(f"The area of the square is: {area_square} cm squared or {area_square / 10000:.4f} m squared.")

# Calculate for the rectangle
length_rectangle = float(input("What is the length of the rectangle? "))
width_rectangle = float(input("What is the width of the rectangle? "))
area_rectangle = length_rectangle * width_rectangle
print(f"The area of the rectangle is: {area_rectangle} cm squared or {area_rectangle / 10000:.4f} m squared.")

# Calculate for the circle
radius_circle = float(input("What is the radius of the circle? "))
length_circle = 2 * math.pi * radius_circle
print(f"The length of the circle is: {length_circle:.4f} cm.")
area_circle = math.pi * radius_circle ** 2
print(f"The area of the circle is: {area_circle:.4f} cm squared or {area_circle / 10000:.4f} m squared.") 