def main():
    codes = {"A" : "=", "a" : "z", "B" : "*", "b" : "y", "C" : "x", "c" : "-", "D" : "1", "d" : "9", "E" : "0", "e" : "3", "F" : "7", "f" : "2", "G" : "4", "g" : "5", "H" : "?", "h" : "!", "I" : "<", "i" : ">", "J" : "@", "j" : "#", "K" : "%", "k" : "^", "L" : "&", "l" : "6", "M" : "8", "m" : "~", "N" : "`", "n" : "+", "O" : "q", "o" : "Q", "P" : "w", "p" : "W", "Q" : "u", "q" : "U", "R" : "k", "r" : "K", "S" : "o", "s" : "O", "T" : "j", "t" : "J", "U" : "b", "u" : "B", "V" : "c", "v" : "C", "W" : "s", "w" : "S", "X" : "d", "x" : "D", "Y" : "a", "y" : "A", "Z" : "f", "z" : "F"}
    list_of_keys = list(codes)
    infile = open('Encryption\info_security.txt', "r")
    outfile = open("encryptionHW.txt", "w")
    for line in infile:
        for c in line:
            for key in list_of_keys:
                if c == key:
                    c = codes[key]
                    outfile.write(c)
    outfile.close()
    infile.close

main()
    

