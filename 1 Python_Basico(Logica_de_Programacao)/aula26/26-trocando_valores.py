"""
x = 10
y = 'Will'

z = x
x = y
y = z

print(f'x={x} e y={y}')
"""

x = 10
y = 'Will'

x, y = y, x

print(f'x={x} e y={y}')
