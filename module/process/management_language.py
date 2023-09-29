""" Inner library """
import module.data.language as language_data
import module.process.error as error

""" Data """
languageType = "en"

""" Processes """
def checkLanguage(args):
    if len(args) == 5:
        
        if args[1] in language_data.textList.keys():
            _languageType = args[1]
            print(language_data.textList[_languageType]["SetLanguage"])

            return language_data.textList[_languageType]
        
        else:
            error.messageEnd("Error:Not exist such language.")

    elif len(args) > 5:
        error.messageEnd("Error:Too many argument")

    else:
        error.messageEnd("Error:Too few argument")