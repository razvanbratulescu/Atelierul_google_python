def my_function():
    def my_second_function():
        global msg
        msg = "hello"
        return None
    my_second_function()
    msg = "Hello1"
    print(f"functia principala {msg}")
    return None

def functie2():
    print(msg, '>>>>')
    return None

my_function()
functie2()

print(globals())
print(locals())
