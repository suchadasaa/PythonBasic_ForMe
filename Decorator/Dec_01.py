# template
'''
def capsule(function):
    def new_function():
        function()


    return new_function
'''

def capsule(function):
    def new_function():
        print('เกราะหัว เกราะแขน เกราะอก')
        function()
        print('เกราะขา')


    return new_function

@capsule
def megaman():
    print('Megaman')

megaman()

@capsule
def zero():
    print('zero')

zero()