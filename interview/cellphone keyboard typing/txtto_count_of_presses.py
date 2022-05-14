def presses(phrase):
    keypad_dict = {
        1: ['A','D','G','J','M','P','T','W','*','#',' ','1'],
        2: ['B','E','H','K','N','Q','U','X','0'],
        3: ['C','F','I','L','O','R','V','Y'],
        4: ['S','Z','2','3','4','5','6','8'],
        5: ['7','9']
    }
    press_count = 0
    for p in phrase:
        for key, value in keypad_dict.items():
            if p.upper() in value:
                press_count += key
    return press_count

phrase = "Where is the food"
print(presses(phrase))