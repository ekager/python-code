def CaesarEncrypt(k, str2):
    i = 0
    if (k>26 or k<0):
        print "Please give a valid key 0-25"
    else:
        str3=""
        while (i<len(str2)):
            b = ord(str2[i])
            if (64<b<91):
                c = ((b-65+k)%26)
                str3 += str(chr(c+65))
            elif (96<b<123):
                c = ((b-97+k)%26)
                str3 += str(chr(c+97))
            else:
                str3 += str(str2[i])
            i=i+1
        print str3

#Using encryption
CaesarEncrypt(7, 'Hello!')

#Decryption function
def CaesarDecrypt(k, str2):
    i = 0
    if (k>26 or k<0):
        print "Please give a valid key 0-25"
    else:
        str3=""
        while (i<len(str2)):
            b = ord(str2[i])
            if (64<b<91):
                c = ((b-65-k)%26)
                str3 += str(chr(c+65))
            elif (96<b<123):
                c = ((b-97-k)%26)
                str3 += str(chr(c+97))
            else:
                str3 += str(str2[i])
            i=i+1
        return str3

#Using decryption
CaesarDecrypt(7, 'Olssv!')

#Encryption
CaesarEncrypt(6, "Get me a vanilla ice cream, make it a double.")

CaesarEncrypt(15, "I don't much care for Leonard Cohen.")

CaesarEncrypt(16, "I like root beer floats.")

#CaesarAttack goes through and tests all keys, printing all possibilities
def CaesarAttack(ciphertext,str2=""):
    j = 0
    str4="".join(str2.split())
    print str4
    while j < 26:
        i = 0
        str3=""
        while (i<len(ciphertext)):
            b = ord(ciphertext[i])
            if (64<b<91):
                c = ((b-65-j)%26)
                str3 += str(chr(c+65))
            elif (96<b<123):
                c = ((b-97-j)%26)
                str3 += str(chr(c+97))
            else:
                str3 += str(ciphertext[i])
            i=i+1
        if (str4 in str3):
            print "Key:",j,str3,"\n"
        j=j+1

#Testing

CaesarAttack('wziv kyv jyfk nyve kyv tpdsrcj tirjy.', 'cymbal')

CaesarAttack('gryy gurz gb tb gb nzoebfr puncry.', 'chapel')

CaesarAttack('baeeq klwosjl osk s esf ozg cfwo lgg emuz.')

CaesarDecrypt(12, 'nduzs ftq buzq oazqe.')

CaesarDecrypt(3, "fdhvdu qhhgv wr orvh zhljkw.")

CaesarDecrypt(20, "ufgihxm uly numnys.")


#More Efficient Attack Function
def CaesarAttack2(ciphertext, str2="", str3="", i=0):
    while (i<25):
        str3 = CaesarDecrypt(i, ciphertext)
        if (str2 in str3):
            print "key " + str(i)+ " " + str3
        i=i+1

CaesarAttack2('gryy gurz gb tb gb nzoebfr puncry.', 'chapel')