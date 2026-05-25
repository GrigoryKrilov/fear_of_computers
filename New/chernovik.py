def decorator_simp (func):
    def wrapper():
        print("0")
        
        print("2")
    return wrapper
@ decorator_simp
def education():
    print("1")
education()
