from easygui import *
import sys
while 1:
    msgbox("e-bazzar")

    msg ="choose your shopping category"
    title = "shopping items"
    choices = ["electronics", "sports", "footwear", "clothes"]
    choice = choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Survey Result")
    if choice=="electronics"
       msg="electronics store"
       choices=   
    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)
