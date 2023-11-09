#!/usr/bin/python3
import math

def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    if not isinstance(radius, (int, float)):
        raise TypeError('Radius must be a number')
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    
    area = math.pi * radius**2
    return area

def format_area(area):
    """Format the area into a nice string with 2 decimal places."""
    formatted_area = '{:.2f}'.format(area)
    return formatted_area


if __name__ == '__main__':
    radius = 5.5
    area = calculate_area(radius)
    print(format_area(area))