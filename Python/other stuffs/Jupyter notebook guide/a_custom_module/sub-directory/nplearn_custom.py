credentials = {
    'main' : {
        'acc_name':'abc',
        'acc_pass':'efg',
        'container':'123'
        },
    'backup' : {
        'acc_name':'aaa',
        'acc_pass':'bbb',
        'container':'333'
        }
}

def add_number(num1,num2):
    """Add number 

    Args:
        num1 (integer): The first input number
        num2 (integer): The second input number

    Returns:
        integer: the number of the first number plus by the second number
    """
    result = num1 + num2
    print(f'You are about to add {num1} to {num2} which is {result}')
    return result

if __name__ == "__main__":
    print(credentials)