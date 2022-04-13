x = 'print('
print(f'x = {x};')
# x = 'print(';

x = 'print('
print(f'x = {x};', x)
# x = 'print('; print(

x = "print(f'x = {x};', x)"
print(f'x = {x};', x)
# x = "print(f'x = {x};', x)"; print(f'x = {x};', x)
