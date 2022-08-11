from calculate import Calculator
import commands

OPTIONS = {
    "QUIT": ["q", "Q", "quit"],
    "HELP": ["h", "H", "help"]
    # FUTURE IMPLEMENTATIONS WILL ALLOW TO USE THE PREVIOUS ANSWER FOR NEXT CALCULATION
}

# instantiate Caculator
calculator = Calculator()


def runCLI():
    """Accepts user input and returns the calculated result or runs a command function if it detects them"""
    try:
        while True:
            command = input("calculator> ")
            if bool([e for e in OPTIONS["HELP"] if (e in command)]):
                commands.help()
                continue
            if bool([e for e in OPTIONS["QUIT"] if (e in command)]):
                commands.quit()
            result = calculator.calculate(command)
            print(result)

    except AttributeError as err:
        print("ERROR: You entered an invalid character")
        commands.quit()

    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")

    except KeyboardInterrupt:
        commands.quit()
