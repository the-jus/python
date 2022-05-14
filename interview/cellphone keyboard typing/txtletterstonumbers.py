def textToKey (string) :
    keypad = {
    '1' : ['.', ',', '?', '!', ':'],
    '2' : ['A', 'B', 'C'],
    '3' : ['D', 'E', 'F'],
    '4' : ['G', 'H', 'I'],
    '5' : ['J', 'K', 'L'],
    '6' : ['M', 'N', 'O'],
    '7' : ['P', 'Q', 'R', 'S'],
    '8' : ['T', 'U', 'V'],
    '9' : ['W', 'X', 'Y', 'Z'],
    '0' : [' ']
    }

    txt = string.upper()

    result = ""
    keys = list(keypad.items())

    for i in range(len(txt)):
        for j in range(len(keys)):
            for k in range(len(keys[j][1])):
                if txt[i] == keys[j][1][k]:
                    result+=((k+1)*keys[j][0])

    return result

k="Hello world"
print(textToKey(k))