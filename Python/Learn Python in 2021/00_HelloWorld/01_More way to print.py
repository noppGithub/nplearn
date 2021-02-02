day = 'Sunday'
year = 2021
# pros: compatability with old version of python

# using % formatting, this is not good when you have several input variables
print('Today is a %s of %s' % (day,year))
# output: Today is Sunday

# using .format()
print('Today is a {} of {}'.format(day,year))

# using .format() with variable names
print('Today is a {date_name} of {year}, and last {date_name} is also in {year} as well'.format(date_name=day,year=year))

# using fstring, you need at least Python 3.6
# remember to use double quote is better when you have to work with dictionary
print(f'Today is a {day} of {year}')

# fstring: single quote vs double quote
my_dict = {'day':'Sunday','year':2021}

# print(f'Today is a {my_dict['day']} of {my_dict['year']}')
print(f"Today is a {my_dict['day']} of {my_dict['year']}")

# fstring: multiple line
my_message = (
    f"Today is a {day} "
    f"of {year}"
)
print(my_message)

# fstring with \
my_message = f"""Today is a {day} \
of {year}
"""
print(my_message)

# fstring without \
my_message = f"""Today is a {day} 
of {year}
"""
print(my_message)

