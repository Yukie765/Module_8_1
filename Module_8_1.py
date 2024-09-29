def add_everything_up(a,b):
    try:
        return round(a+b,3)
    except TypeError as ex:
       if isinstance(a,int) or isinstance(a,float):
            a_str = str(a)
            return a_str+b
       if isinstance(b,int) or isinstance(b,float):
            b_str = str(b)
            return a+b_str

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
