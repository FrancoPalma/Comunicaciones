import time
import math

# Build the dictionary.
dict_size = 256
dictionary = dict((chr(i), i) for i in range(dict_size))

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char
        return encoding


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        # If the character is numerical...
        if char.isdigit():
            # ...append it to our count
            count += char
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            decode += char * int(count)
            count = ''
    return decode

aux = 1
#f = open("/Github/Comunicaciones/ResultadosRLECP.txt", "w")
f = open("ResultadosRLECP.txt", "w")
while(aux <= 30):
    file = open("ArchivosCP/archivo"+str(aux)+".txt", "r")
    x = ""
    for i in file:
        x += i
    file.close()
    start_time = time.time()
    time.sleep(0.1)
    compressed = rle_encode(x)
    decompressed = rle_decode(compressed)
    f.write("ArchivoCP"+str(aux)+".\n")
    f.write(compressed)
    f.write("\n")

    num_simbolos = []
    for c in compressed:
        if c in dictionary:
            num_simbolos.append(dictionary[c])

    bits = 0;           #total de bits
    for i in num_simbolos:
        bits_simbolo = math.log2(i);
        if(bits_simbolo%1 != 0):
            bits_simbolo = bits_simbolo // 1;
            bits_simbolo +=1;
            bits += bits_simbolo;
        else:
            bits += bits_simbolo

    f.write("El peso en bites comprimidos es: "+str(bits)+".\n")
    f.write("\n")

    f.write(str(num_simbolos))
    f.write("\n")
    f.write(decompressed)
    f.write("\n")

    num_simbolos = []
    for c in decompressed:
        if c in dictionary:
            num_simbolos.append(dictionary[c])

    bits = 0;           #total de bits
    for i in num_simbolos:
        bits_simbolo = math.log2(i);
        if(bits_simbolo%1 != 0):
            bits_simbolo = bits_simbolo // 1;
            bits_simbolo +=1;
            bits += bits_simbolo;
        else:
            bits += bits_simbolo

    f.write("El peso en bites descomprimidos es: "+str(bits)+".\n")
    f.write("\n")

    f.write(str((time.time()-start_time)-0.1))
    f.write("\n\n")
    aux += 1
f.close()

#f = open("/Github/Comunicaciones/ResultadosRLESP.txt", "w")
f = open("ResultadosRLESP.txt", "w")
aux = 1
while(aux <= 30):
    file = open("ArchivosSP/archivo"+str(aux)+".txt", "r")
    x = ""
    for i in file:
        x += i
    file.close()
    start_time = time.time()
    time.sleep(0.01)
    compressed = rle_encode(x)
    decompressed = rle_decode(compressed)
    f.write("ArchivoSP"+str(aux)+".\n")
    f.write(compressed)
    f.write("\n")

    num_simbolos = []
    for c in compressed:
        if c in dictionary:
            num_simbolos.append(dictionary[c])

    bits = 0;           #total de bits
    for i in num_simbolos:
        bits_simbolo = math.log2(i);
        if(bits_simbolo%1 != 0):
            bits_simbolo = bits_simbolo // 1;
            bits_simbolo +=1;
            bits += bits_simbolo;
        else:
            bits += bits_simbolo

    f.write("El peso en bites comprimidos es: "+str(bits)+".\n")
    f.write("\n")

    f.write(decompressed)
    f.write("\n")

    num_simbolos = []
    for c in decompressed:
        if c in dictionary:
            num_simbolos.append(dictionary[c])

    bits = 0;           #total de bits
    for i in num_simbolos:
        bits_simbolo = math.log2(i);
        if(bits_simbolo%1 != 0):
            bits_simbolo = bits_simbolo // 1;
            bits_simbolo +=1;
            bits += bits_simbolo;
        else:
            bits += bits_simbolo

    f.write("El peso en bites descomprimidos es: "+str(bits)+".\n")
    f.write("\n")
    f.write(str((time.time()-start_time)-0.01))
    f.write("\n\n")
    aux += 1
f.close()
