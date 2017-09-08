alphabet = 'abcdefghijklmnopqrstuvwxyz'
text =" g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
trans_text = ""
for alp in text:
    if alp in alphabet:
        if alphabet.index(alp) == alphabet.index("y"):
            alp = "a"
        elif alphabet.index(alp) == alphabet.index("z"):
            alp = "b"
        else:
            alp = alphabet[alphabet.index(alp)+2]
        trans_text += alp
    else:
        trans_text += alp

print(trans_text)
        
