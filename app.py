""" Outer library """
import sys

""" Inner library """
import module.process.management_language as management_language
import module.process.management_window as management_window
import module.process.error as error

""" Global """
_textListCopy = None

""" Main """
def main(args):
    if str.isdigit(args[2]) and str.isdigit(args[3]) and str.isdigit(args[4]):
        if int(args[4]) > 199:
            management_window.makeWindow(_textListCopy, 600, 600, args[2], args[3], int(args[4]))
        else:
            error.messageEnd("Error:Simulation count should be 200 or more")
    else:
        error.messageEnd("Error:Not type of integer")

""" Call main process """
if __name__ == "__main__":
    
    # Catch language option
    _textListCopy = management_language.checkLanguage(sys.argv)
    #Debug# print(_textListCopy)

    # Start system
    print(_textListCopy["StartSystem"])
    main(sys.argv)