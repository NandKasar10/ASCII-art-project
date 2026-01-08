

# for getting rows no. when 
# i=0
# for char in first_line.split():
#     i=i+1
# print(i)


# for getting columns no.
# i=0
# for line in ascii_art.splitlines():
#     i=i+1
# print(i)



rows = 84 
act_cols = 100  

for r in range(rows):
    line = ""
    
    if r == 0 :
        cols = 0;
        for i in range(6):
            line += "@"
            cols += 1;
        for i in range(8):
            cols += 1;
            line += "%"
        for i in range(6):
            cols += 1;
            line += "#"
        for i in range(2):
            cols += 1;
            line += "%"
        for i in range(5):
            cols += 1;
            line += "@"
        for i in range(2):
            cols += 1;
            line += "%"
        for i in range(43):
            cols += 1;
            line += "@"
        for i in range(4):
            cols += 1;
            line += "%"
        for i in range(4):
            cols += 1;
            line += "@"
        line += "%"
        cols += 1;
        for i in range(4):
            cols += 1;
            line += "#"
        for i in range(3):
            cols += 1;
            line += "%"
        for i in range(12):
            cols += 1;
            line += "@"
        if(cols == act_cols):
            line += " -> okay1"
    if r == 1 :
        cols = 0;
        for i in range(7):
            line += "@"
            cols += 1;
        for i in range(2):
            cols += 1;
            line += "%"
        for i in range(4):
            cols += 1;
            line += "#"
        for i in range(2):
            cols += 1;
            line += ":"
        for i in range(1):
            cols += 1;
            line += "+"
        for i in range(1):
            cols += 1;
            line += "-"
        for i in range(1):
            cols += 1;
            line += "*"
        for i in range(2):
            cols += 1;
            line += "#"
        for i in range(2):
            cols += 1;
            line += "%"
        for i in range(6):
            cols += 1;
            line += "@"
        for i in range(1):
            cols += 1;
            line += "%"
        for i in range(44):
            cols += 1;
            line += "@"
        for i in range(4):
            cols += 1;
            line += "%"
        for i in range(1):
            cols += 1;
            line += "@"
        for i in range(2):
            cols += 1;
            line += "%"
        for i in range(5):
            cols += 1;
            line += "#"
        for i in range(2):
            cols += 1;
            line += "%"
        for i in range(13):
            cols += 1;
            line += "@"
        if(cols == act_cols):
            line += " -> okay"
    if r == 2 :
        cols = 0;
        for i in range(1):
            line += "#"
            cols += 1;
        for i in range(1):
            cols += 1;
            line += "%"
        for i in range(5):
            cols += 1;
            line += "@"
        for i in range(1):
            cols += 1;
            line += "%"
        for i in range(1):
            cols += 1;
            line += "*"
        for i in range(3):
            cols += 1;
            line += "+"
        for i in range(1):
            cols += 1;
            line += "="
        for i in range(1):
            cols += 1;
            line += ":"
        for i in range(1):
            cols += 1;
            line += "."
        for i in range(1):
            cols += 1;
            line += ":"
        for i in range(1):
            cols += 1;
            line += "."
        for i in range(1):
            cols += 1;
            line += "="
        for i in range(1):
            cols += 1;
            line += "."
        for i in range(1):
            cols += 1;
            line += "="
        for i in range(1):
            cols += 1;
            line += "%"
        for i in range(53):
            cols += 1;
            line += "@"
        for i in range(5):
            cols += 1;
            line += "%"
        for i in range(7):
            cols += 1;
            line += "#"
        for i in range(3):
            cols += 1;
            line += "%"
        for i in range(11):
            cols += 1;
            line += "@"
        if(cols == act_cols):
            line += " -> okay"
    if r == 3 :
        cols = 0;
        for i in range(3):
            line += "*"
            cols += 1;
        for i in range(1):
            cols += 1;
            line += "#"
        for i in range(2):
            cols += 1;
            line += "%"
        for i in range(1):
            cols += 1;
            line += "#"
        for i in range(1):
            cols += 1;
            line += "*"
        for i in range(1):
            cols += 1;
            line += "+"
        for i in range(1):
            cols += 1;
            line += "="
        for i in range(4):
            cols += 1;
            line += "-"
        for i in range(1):
            cols += 1;
            line += ":"
        for i in range(2):
            cols += 1;
            line += "."
        for i in range(1):
            cols += 1;
            line += ":"
        for i in range(1):
            cols += 1;
            line += "."
        for i in range(1):
            cols += 1;
            line += "-"
        for i in range(1):
            cols += 1;
            line += "."
        for i in range(1):
            cols += 1;
            line += "="
        for i in range(1):
            cols += 1;
            line += "%"
        for i in range(1):
            cols += 1;
            line += "*"
        for i in range(1):
            cols += 1;
            line += "."
        for i in range(1):
            cols += 1;
            line += ":"
        for i in range(1):
            cols += 1;
            line += "%"
        for i in range(47):
            cols += 1;
            line += "@"
        for i in range(3):
            cols += 1;
            line += "%"
        for i in range(11):
            cols += 1;
            line += "#"
        for i in range(2):
            cols += 1;
            line += "%"
        for i in range(10):
            cols += 1;
            line += "@"
        if(cols == act_cols):
            line += " -> okay"
    if r == 4 :
        cols = 0;
        for i in range(4):
            line += "+"
            cols += 1;
        for i in range(3):
            cols += 1;
            line += "*"
        for i in range(1):
            cols += 1;
            line += "+"
        for i in range(1):
            cols += 1;
            line += "="
        for i in range(5):
            cols += 1;
            line += "-"
        for i in range(2):
            cols += 1;
            line += "="
        for i in range(1):
            cols += 1;
            line += ":"
        for i in range(1):
            cols += 1;
            line += "."
        for i in range(1):
            cols += 1;
            line += "-"
        for i in range(1):
            cols += 1;
            line += ":"
        for i in range(1):
            cols += 1;
            line += "+"
        for i in range(1):
            cols += 1;
            line += ":"
        for i in range(1):
            cols += 1;
            line += "."
        for i in range(1):
            cols += 1;
            line += "*"
        for i in range(1):
            cols += 1;
            line += "="
        for i in range(1):
            cols += 1;
            line += ":"
        for i in range(1):
            cols += 1;
            line += "."
        for i in range(1):
            cols += 1;
            line += "+"
        for i in range(1):
            cols += 1;
            line += "#"
        for i in range(1):
            cols += 1;
            line += "%"
        for i in range(43):
            cols += 1;
            line += "@"
        for i in range(4):
            cols += 1;
            line += "%"
        for i in range(6):
            cols += 1;
            line += "#"
        for i in range(2):
            cols += 1;
            line += "%"
        for i in range(3):
            cols += 1;
            line += "#"
        for i in range(3):
            cols += 1;
            line += "%"
        for i in range(9):
            cols += 1;
            line += "@"
        if(cols == act_cols):
            line += " -> okay"
    if r == 5 :
        cols = 0;
        for i in range(1):
            line += "*"
            cols += 1;
        for i in range(6):
            cols += 1;
            line += "+"
        for i in range(2):
            cols += 1;
            line += "="
        for i in range(3):
            cols += 1;
            line += "-"
        for i in range(2):
            cols += 1;
            line += "="
        for i in range(1):
            cols += 1;
            line += "+"
        for i in range(1):
            cols += 1;
            line += "*"
        for i in range(1):
            cols += 1;
            line += "+"
        for i in range(1):
            cols += 1;
            line += ":"
        for i in range(5):
            cols += 1;
            line += "."
        for i in range(1):
            cols += 1;
            line += ":"
        for i in range(1):
            cols += 1;
            line += "-"
        for i in range(1):
            cols += 1;
            line += ":"
        for i in range(2):
            cols += 1;
            line += "."
        for i in range(1):
            cols += 1;
            line += "+"
        for i in range(1):
            cols += 1;
            line += "#"
        for i in range(1):
            cols += 1;
            line += "%"
        for i in range(41):
            cols += 1;
            line += "@"
        for i in range(2):
            cols += 1;
            line += "%"
        for i in range(2):
            cols += 1;
            line += "#"
        for i in range(6):
            cols += 1;
            line += "%"
        for i in range(3):
            cols += 1;
            line += "@"
        for i in range(3):
            cols += 1;
            line += "%"
        for i in range(2):
            cols += 1;
            line += "#"
        for i in range(3):
            cols += 1;
            line += "%"
        for i in range(7):
            cols += 1;
            line += "@"
        
        if(cols == act_cols):
            line += " -> okay"
    if r == 6:   # change row number as needed
        cols = 0
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(4):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += " "
        for i in range(2):
            cols += 1; line += "."
        for i in range(2):
            cols += 1; line += ":"
        for i in range(3):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(39):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(8):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(4):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"
    if r == 7:   # change row number as needed
        cols = 0
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(5):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(5):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(9):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(38):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay"
    if r == 8:
        cols = 0
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(7):
            cols += 1; line += "*"
        for i in range(5):
            cols += 1; line += "#"
        for i in range(5):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(4):
            cols += 1; line += "."
        for i in range(2):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(38):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(5):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(5):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay"
    if r == 9:
        cols = 0
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "#"
        for i in range(5):
            cols += 1; line += "*"
        for i in range(5):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(5):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(16):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(13):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "*"
        for i in range(9):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay10"

    if r == 10:
        cols = 0
        for i in range(1):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(5):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(14):
            cols += 1; line += "@"
        for i in range(7):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(8):
            cols += 1; line += "%"
        for i in range(4):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(7):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(8):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay"

    if r == 11:
        cols = 0
        for i in range(6):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(4):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(28):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(7):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(8):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 12:
        cols = 0
        for i in range(7):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "-"
        for i in range(4):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(29):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(8):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(4):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(10):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 13:
        cols = 0
        for i in range(8):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(3):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(35):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(5):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(6):
            cols += 1; line += "%"
        for i in range(4):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay"
    
    if r == 14:
        cols = 0
        for i in range(3):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "*"
        for i in range(5):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(27):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(5):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(6):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(4):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay"

    if r == 15:
        cols = 0
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(5):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(38):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(6):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(5):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 16:
        cols = 0
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(7):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(39):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(5):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(7):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(5):
            cols += 1; line += "%"
        
        if(cols == act_cols):
            line += " -> okay"

    if r == 17:
        cols = 0
        for i in range(1):
            cols += 1; line += "%"
        for i in range(8):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(6):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(3):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += ":"
        for i in range(33):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(9):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"

        if(cols == act_cols):
            line += " -> okay"

    if r == 18:
        cols = 0
        for i in range(10):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(4):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(3):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(31):
            cols += 1; line += "@"
        for i in range(7):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"

        if(cols == act_cols):
            line += " -> okay"

    if r == 19:
        cols = 0
        for i in range(10):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(3):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(35):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(9):
            cols += 1; line += "@"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(8):
            cols += 1;line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"

        if(cols == act_cols):
            line += " -> okay20"

    if r == 20:
        cols = 0
        for i in range(1):
            cols += 1; line += "%"
        for i in range(8):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(3):
            cols += 1; line += "="
        for i in range(3):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(35):
            cols += 1; line += "@"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(12):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(10):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 21:
        cols = 0
        for i in range(3):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(4):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(5):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(47):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(9):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 22:
        cols = 0
        for i in range(3):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(47):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(8):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 23:
        cols = 0
        for i in range(1):
            cols += 1; line += "%"
        for i in range(8):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(45):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(8):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 24:
        cols = 0
        for i in range(1):
            cols += 1; line += "%"
        for i in range(7):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += "="
        for i in range(8):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(4):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(22):
            cols += 1; line += "@"
        for i in range(7):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(7):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 25:
        cols = 0
        for i in range(1):
            cols += 1; line += "%"
        for i in range(7):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += "="
        for i in range(7):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "."
        for i in range(3):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "%"
        for i in range(10):
            cols += 1; line += "@"
        for i in range(4):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(4):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(4):
            cols += 1; line += "#"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 26:
        cols = 0
        for i in range(1):
            cols += 1; line += "%"
        for i in range(7):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(4):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(4):
            cols += 1; line += "+"
        for i in range(5):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "="
        for i in range(6):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "*"
        for i in range(8):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(13):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(4):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 27:
        cols = 0
        for i in range(8):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "*"
        for i in range(6):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "*"
        for i in range(4):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "#"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "#"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(4):
            cols += 1; line += "#"
        for i in range(6):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"

        if(cols == act_cols):
            line += " -> okay"

    if r == 28:
        cols = 0
        for i in range(12):
            cols += 1; line += "@"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "="
        for i in range(5):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(2):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "-"
        for i in range(3):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(2):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(2):
            cols += 1; line += "-"
        for i in range(9):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(9):
            cols += 1; line += "%"
        for i in range(4):
            cols += 1; line += "#"
        for i in range(6):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"

        if(cols == act_cols):
            line += " -> okay"

    if r == 29:
        cols = 0
        for i in range(24):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(3):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(18):
            cols += 1; line += "@"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(10):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay30"

    if r == 30:
        cols = 0
        for i in range(24):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(39):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 31:
        cols = 0
        for i in range(24):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(3):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(3):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(39):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 32:
        cols = 0
        for i in range(25):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(5):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += ":"
        for i in range(4):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(3):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "*"
        for i in range(39):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 33:
        cols = 0
        for i in range(25):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(4):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(4):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(3):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(39):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 34:
        cols = 0
        for i in range(26):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(7):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "."
        for i in range(4):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "-"
        for i in range(3):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(38):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 35:
        cols = 0
        for i in range(26):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(6):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(5):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(37):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 36:
        cols = 0
        for i in range(27):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(5):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(7):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "="
        for i in range(36):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay"

    if r == 37:
        cols = 0
        for i in range(28):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(6):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(4):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(33):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"

        if(cols == act_cols):
            line += " -> okay"

    if r == 38:
        cols = 0
        for i in range(29):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(2):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(32):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"

        if(cols == act_cols):
            line += " -> okay"

    if r == 39:
        cols = 0
        for i in range(29):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(4):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(4):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(27):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += ":"

        if(cols == act_cols):
            line += " -> okay40"

    if r == 40:
        cols = 0
        for i in range(30):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "."
        for i in range(3):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "+"
        for i in range(22):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "-"
        for i in range(4):
            cols += 1; line += ":"

        if(cols == act_cols):
            line += " -> okay"

    if r == 41:
        cols = 0
        for i in range(30):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(5):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(6):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(18):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(6):
            cols += 1; line += ":"

        if(cols == act_cols):
            line += " -> okay"

    if r == 42:
        cols = 0
        for i in range(1):
            cols += 1; line += "%"
        for i in range(29):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "."
        for i in range(6):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "="
        for i in range(3):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(3):
            cols += 1; line += "="
        for i in range(4):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "-"
        for i in range(3):
            cols += 1; line += " "
        for i in range(5):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += " "
        for i in range(16):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(6):
            cols += 1; line += ":"

        if(cols == act_cols):
            line += " -> okay"

    if r == 43:
        cols = 0
        for i in range(1):
            cols += 1; line += "%"
        for i in range(29):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += ":"
        for i in range(3):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(8):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(9):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(2):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "="
        for i in range(3):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += " "
        for i in range(15):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "-"
        for i in range(5):
            cols += 1; line += ":"

        if(cols == act_cols):
            line += " -> okay"

    if r == 44:
        cols = 0
        for i in range(1):
            cols += 1; line += "%"
        for i in range(29):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(9):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "="
        for i in range(6):
            cols += 1; line += "-"
        for i in range(4):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(15):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "-"
        for i in range(4):
            cols += 1; line += ":"

        if(cols == act_cols):
            line += " -> okay"

    if r == 45:
        cols = 0
        for i in range(30):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(12):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += ":"
        for i in range(6):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(4):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(3):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(7):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += ":"
        for i in range(16):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += ":"

        if(cols == act_cols):
            line += " -> okay"

    if r == 46:
        cols = 0
        for i in range(30):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(16):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += ":"
        for i in range(3):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(4):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(4):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "%"
        for i in range(17):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"

        if(cols == act_cols):
            line += " -> okay"

    if r == 47:
        cols = 0
        for i in range(30):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(21):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += ":"
        for i in range(4):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(19):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"

        if(cols == act_cols):
            line += " -> okay"

    if r == 48:
        cols = 0
        for i in range(29):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "."
        for i in range(14):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "="
        for i in range(15):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(4):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(22):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay"

    if r == 49:
        cols = 0
        for i in range(29):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(33):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(5):
            cols += 1; line += "+"
        for i in range(24):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay50"

    if r == 50:
        cols = 0
        for i in range(30):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "="
        for i in range(34):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(24):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 51:
        cols = 0
        for i in range(32):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "."
        for i in range(33):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(23):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 52:
        cols = 0
        for i in range(33):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "."
        for i in range(32):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(3):
            cols += 1; line += ":"
        for i in range(23):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 53:
        cols = 0
        for i in range(33):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(28):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(3):
            cols += 1; line += ":"
        for i in range(23):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 54:
        cols = 0
        for i in range(34):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(3):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(15):
            cols += 1; line += " "
        for i in range(3):
            cols += 1; line += "."
        for i in range(8):
            cols += 1; line += " "
        for i in range(2):
            cols += 1; line += "@"
        for i in range(4):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += ":"
        for i in range(23):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 55:
        cols = 0
        for i in range(34):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += ":"
        for i in range(5):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(22):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "@"
        for i in range(4):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(22):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 56:
        cols = 0
        for i in range(34):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "."
        for i in range(2):
            cols += 1; line += ":"
        for i in range(5):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(17):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(4):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "#"
        for i in range(22):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 57:
        cols = 0
        for i in range(34):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "."
        for i in range(3):
            cols += 1; line += ":"
        for i in range(8):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(14):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "+"
        for i in range(4):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "-"
        for i in range(22):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 58:
        cols = 0
        for i in range(1):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(22):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "."
        for i in range(4):
            cols += 1; line += ":"
        for i in range(5):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(4):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(10):
            cols += 1; line += " "
        for i in range(5):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "*"
        for i in range(21):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 59:
        cols = 0
        for i in range(3):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(28):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "."
        for i in range(4):
            cols += 1; line += ":"
        for i in range(12):
            cols += 1; line += "-"
        for i in range(3):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += ":"
        for i in range(7):
            cols += 1; line += " "
        for i in range(5):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(6):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(7):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(6):
            cols += 1; line += "%"
        for i in range(7):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay60"

    if r == 60:
        cols = 0
        for i in range(34):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "."
        for i in range(4):
            cols += 1; line += ":"
        for i in range(17):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(3):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "="
        for i in range(14):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(4):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 61:
        cols = 0
        for i in range(4):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(29):
            cols += 1; line += "%"
        for i in range(4):
            cols += 1; line += "."
        for i in range(3):
            cols += 1; line += ":"
        for i in range(21):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "-"
        for i in range(4):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(5):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += ":"
        for i in range(17):
            cols += 1; line += "%"

        for i in range(3):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 62:
        cols = 0
        for i in range(33):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(31):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "*"
        for i in range(4):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(4):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += ":"
        for i in range(20):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay"

    if r == 63:
        cols = 0
        for i in range(33):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(31):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(19):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay"

    if r == 64:
        cols = 0
        for i in range(34):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "."
        for i in range(30):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "+"
        for i in range(4):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(4):
            cols += 1; line += "="
        for i in range(3):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "*"
        for i in range(19):
            cols += 1; line += "%"
        
        if(cols == act_cols):
            line += " -> okay"

    if r == 65:
        cols = 0
        for i in range(33):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "."
        for i in range(2):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "."
        for i in range(13):
            cols += 1; line += " "
        for i in range(2):
            cols += 1; line += ":"
        for i in range(4):
            cols += 1; line += " "
        for i in range(2):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "."
        for i in range(5):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "*"
        for i in range(19):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay"

    if r == 66:
        cols = 0
        for i in range(32):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(9):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(3):
            cols += 1; line += ":"
        for i in range(4):
            cols += 1; line += "-"
        for i in range(3):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(11):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(3):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(19):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay"

    if r == 67:
        cols = 0
        for i in range(32):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(15):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(16):
            cols += 1; line += " "
        for i in range(4):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "+"
        for i in range(19):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay"

    if r == 68:
        cols = 0
        for i in range(32):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(15):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(16):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(19):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay"

    if r == 69:
        cols = 0
        for i in range(13):
            cols += 1; line += ":"
        for i in range(19):
            cols += 1; line += "."
        for i in range(16):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "."
        for i in range(20):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += ":"
        for i in range(19):
            cols += 1; line += "."

        if(cols == act_cols):
            line += " -> okay70"

    if r == 70:
        cols = 0
        for i in range(48):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(23):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(19):
            cols += 1; line += " "
        if(cols == act_cols):
            line += " -> okay"

    if r == 71:
        cols = 0
        for i in range(48):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(23):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(19):
            cols += 1; line += " "
        if(cols == act_cols):
            line += " -> okay"

    if r == 72:
        cols = 0
        for i in range(48):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "."
        for i in range(22):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(6):
            cols += 1; line += " "
        for i in range(13):
            cols += 1; line += "."
        
        if(cols == act_cols):
            line += " -> okay"

    if r == 73:
        cols = 0
        for i in range(1):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(6):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(6):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(16):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(19):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 74:
        cols = 0
        for i in range(1):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(6):
            cols += 1; line += "@"
        for i in range(16):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(4):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(16):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(18):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 75:
        cols = 0
        for i in range(1):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "."
        for i in range(16):
            cols += 1; line += " "
        for i in range(3):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(18):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 76:
        cols = 0
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(6):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(4):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(17):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(20):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(4):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 77:
        cols = 0
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "="
        for i in range(17):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(20):
            cols += 1; line += " "
        for i in range(2):
            cols += 1; line += "="
        for i in range(5):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(7):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 78:
        cols = 0
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(5):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "."
        for i in range(16):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "="
        for i in range(19):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += " "
        for i in range(2):
            cols += 1; line += "="
        for i in range(3):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 79:
        cols = 0
        for i in range(1):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(17):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(21):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(11):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay80"

    if r == 80:
        cols = 0
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(21):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "."
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += "="
        for i in range(3):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "."
        for i in range(3):
            cols += 1; line += " "
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 81:
        cols = 0
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(10):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(4):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(4):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(2):
            cols += 1; line += ":"
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(4):
            cols += 1; line += "*"
        for i in range(15):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"

        if(cols == act_cols):
            line += " -> okay"

    if r == 82:
        cols = 0
        for i in range(31):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "%"
        for i in range(7):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(5):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(4):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += ":"
        for i in range(2):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(2):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(3):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(5):
            cols += 1; line += "@"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(10):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(5):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay"

    if r == 83:
        cols = 0
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(2):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "%"
        for i in range(3):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(2):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(2):
            cols += 1; line += "%"
        for i in range(8):
            cols += 1; line += "@"
        for i in range(1):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "+"
        for i in range(1):
            cols += 1; line += "="
        for i in range(5):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(5):
            cols += 1; line += "+"
        for i in range(4):
            cols += 1; line += "-"
        for i in range(1):
            cols += 1; line += "="
        for i in range(1):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(2):
            cols += 1; line += "+"
        for i in range(3):
            cols += 1; line += "*"
        for i in range(1):
            cols += 1; line += "="
        for i in range(3):
            cols += 1; line += "@"
        for i in range(2):
            cols += 1; line += "#"
        for i in range(1):
            cols += 1; line += "*"
        for i in range(16):
            cols += 1; line += "@"

        if(cols == act_cols):
            line += " -> okay84"

    print(line)


