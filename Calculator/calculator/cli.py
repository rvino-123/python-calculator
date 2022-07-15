from calculate import Calculator
import commands
import sys

OPTIONS = {
    "QUIT": ["q", "Q", "quit"],
    "HELP": ["h", "H", "help"]
    # FUTURE IMPLEMENTATIONS WILL ALLOW TO USE THE PREVIOUS ANSWER FOR NEXT CALCULATION
}


calculator = Calculator()


def runCLI():
    while True:
        command = input("calculator> ")
        if bool([e for e in OPTIONS["HELP"] if (e in command)]):
            commands.help()
            continue
        if bool([e for e in OPTIONS["QUIT"] if (e in command)]):
            commands.quit()
        result = calculator.calculate(command)
        print(result)


print(sys.path)
runCLI()
