command = "(al)G(al)()()G"
def interpret(command):
    return command.replace("()", "o").replace("(al)", "al")

print(interpret(command))