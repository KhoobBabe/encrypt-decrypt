#dictionary contaning the keys
encrypt_key = {'a': 'i', 'e': 'o', 'i': 'u', 'o': 'a', 'u': 'e',
               'b': 'm', 'd': 't', 'g': 'b', 'm': 'd', 't': 'g',
               '1': '5', '3': '7', '5': '9', '7': '1', '9': '3'}

#function to do encryption
def encrypt_text():
    orig_text = input("original text: ")
    
    #input converted into a list
    y = list(orig_text)
    a = ''
    for i in y:
        if i in encrypt_key:
            #gets the replacement of the element from dictionary
            z = encrypt_key.get(i)
            j = str(z)
            a += j
        if i not in encrypt_key:
            #to keep the same element if it is not in the dictionary
            j = str(i)
            a += j
    print("encrypted text: ", a)
    print()
    
    #the text is sorted in ascending order
    z = sorted(y)
    print("Rule\tFrequency")
    
    #counts the frequency of the elements of the text
    freq = {x:z.count(x) for x in z}

    #compare the element and the key in dictionary to develop the table
    for i in freq:
        for j in encrypt_key:
            if i == j:
                print(j, "→", encrypt_key.get(i), "\t", freq[i])
    print()
    
        
#function to do decryption
def decrypt_text():
    orig_text = input("original text: ")
    y = list(orig_text)

    #the keys of encrypt_key are changed into values and the values into keys
    decrypt_key = {v: k for k, v in encrypt_key.items()}

    #the decryption is done using the same method as encryption
    a= ''
    for i in y:
        if i in decrypt_key:
            z = decrypt_key.get(i)
            j = str(z)
            a += j
        if i not in decrypt_key:
            j = str(i)
            a += j
    
    print("decrypted text: ", a)
    print()
    
    z = sorted(y)
    print("Rule\tFrequency")
    freq = {x:z.count(x) for x in z}
    for i in freq:
        for j in decrypt_key:
            if i == j:
                print(j, "→", decrypt_key.get(i), "\t", freq[i])
    print()

   
#code starts from here
#options are given to the user
print("select the option:-")
print("a. encrypt")
print("b. decrypt")
print("c. close program")
print()

opt = ''
#a while loop so it can prompt the user to do multiple inputs
while opt != 0:
    opt = input("enter the task you want to perform: ")
    if opt == "a":
        encrypt_text()
    elif opt == "b":
        decrypt_text()
    elif opt == "c":
        print("program closed")
        break
    else:
        print("please select from the above options\t")
    
