
class LimitError(BaseException):
    pass



def very_dangerous_function():
    """evil things happen here, easily breaks your code"""
    ### ToDo: add crazy stuff here

    raise LimitError("es klappt leider nicht")




try:
    very_dangerous_function()

except LimitError:
    print("hurra es klappt")
