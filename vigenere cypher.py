import string

def textstrip(filename):
    '''This takes the file and converts it to a string with all the spaces and other
    special characters removed. What remains is only the lower case letters,
    retain only the lowercase letters!
    '''
    #I will open the file in read mode and read it.
    f=open(filename,"r")
    r=f.read()
    s=''
    #This string will store only the lowercase letters from the file.
    for i in r:
        if i in string.ascii_lowercase:
            #string.ascii_lowercase is a string containing all the lowercase
            s+=i
    #I will close the file and return the string.
    f.close()
    return s

def letter_distribution(s):
    '''Consider the string s which comprises of only lowercase letters. Count
    the number of occurrences of each letter and return a dictionary'''
    d={}
    #Initializing the dictionary.
    for i in string.ascii_lowercase:
        #Assigning the value 0 to each key where the keys are the lowercase letters.
        d[i]=0
    #Now using the for loop to count the number of occurrences of each letter.
    for i in s:
        d[i]+=1
    #Returning the dictionary.
    return d

def substitution_encrypt(s,d):
    '''encrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    e=''
    #e will store the encrypted string.
    for i in s:
        #dictionary d will be used to encrypt the string.
        #i is the letter in the string s and d[i] is the encrypted letter.
        e+=d[i]
    #returning the encrypted string.
    return e

def substitution_decrypt(s,d):
    '''decrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    decrypt=''
    dk=list(d.keys())
    #these are the keys of the dictionary d and the actual letters which should be there.
    dv=list(d.values())
    #these are the values of the dictionary d and the encrypted letters.
    d1={}
    #this dictionary will be used to decrypt the string.
    for i in range(26):
        #this for loop will create the dictionary d1 with the keys and values interchanged.
        d1[dv[i]]=dk[i]
    for i in s:
        #this for loop will decrypt the string.
        decrypt+=d1[i]
    #returning the final string.
    return decrypt

def cryptanalyse_substitution(s):
    '''Given that the string s is given to us and it is known that it was
    encrypted using some substitution cipher, predict the d'''
    rank='etaoinsrhrhdlucmfywgpbvkxqjz'
    #this is the rank of the letters in the english language.
    #this means that the most frequent letter is e, then t and so on.
    d=letter_distribution(s)
    #this is the dictionary of the letter distribution of the string s.
    dic={}
    #this dictionary will store the the letters and their substitutions.
    for i in range(26):
        m=d['z']
        #I have initialized m to be the frequency of z.
        a='z'
        #I have initialized a to be z.
        for j in d:
            if d[i]>m:
                m=d[i]
                #m is the frequency of the most frequent letter.
                a=i
                #a is the most frequent letter.
        dic[rank(i)]=a
        #The most frequent letter of the encrypted string is the most frequent letter of the english language.
        d.pop(a)
        #I have removed the most frequent letter from the dictionary d.
        #Now I will repeat the process for the second most frequent letter and so on.
        rank=rank[1:]
        #I will also keep removing the first letter from the rank.
    return dic

def vigenere_encrypt(s,password):
    '''Encrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    e=''
    #e will store the encrypted string.
    lower=string.ascii_lowercase
    s=list(s)
    #I have converted the string s to a list so that I can assign values to it.
    for i in range(len(s)):
        #this for loop will encrypt the string.
        #i%len(password) will ensure that the password gets repeated after it has been used once.
        #I will replace the letter in the string s with the encrypted letter.
        s[i]=lower[(lower.index(s[i])+lower.index(password[(i%len(password))]))%26]
    #now I will convert the list s to a string and return it.
    return ''.join(s)

def vigenere_decrypt(s,password):
    '''Decrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    d=''
    #d will store the decrypted string.
    lower=list(string.ascii_lowercase)
    s=list(s)
    for i in range(len(s)):
        #this for loop will decrypt the string.
        #using the same logic as in the encryption, I will replace the letter in the string s with the decrypted letter.
        s[i]=lower[(lower.index(s[i])-lower.index(password[(i%len(password))]))%26]
    #now I will convert the list s to a string and return it.
    return ''.join(s)

def rotate_compare(s,r):
    '''This rotates the string s by r places and compares s(0) with s(r) and
    returns the proportion of collisions'''
    sr=''
    #sr will store the rotated string.
    for i in range(len(s)):
        #this for loop will rotate the string.
        sr+=s[(i+r)%len(s)]
    count=0
    #count will store the number of collisions between the original string and the rotated string.
    for i in range(len(s)):
        if s[i]==sr[i]:
            #if the letters are the same, then count will increase by 1.
            count+=1
    #I will return the proportion of collisions.
    return count/len(s)

def cryptanalyse_vigenere_afterlength(s,k):
    '''Given the string s which is known to be vigenere encrypted with a
    password of length k, find out what is the password'''
    #First I will find out the number of partitions which will be there.
    #The number of partitions will be least integer greater than or equal to len(s)/k.
    if len(s)%k==0:
        partitions=len(s)//k
    else: partitions=(len(s)//k)+1
    password=''
    #password will store the password.
    lower=string.ascii_lowercase
    for i in range(k):
        s1=''
        #This will store the string partition.
        j=0
        #This will be used to store the partition values.
        while (i+j*k)<len(s):
            s1+=s[i+j*k]
            #for example, in case of the first partition, the letters will be s[0],s[5],s[10] and so on if k=5.
            j+=1
        #Now I will find out the letter distribution of the partition.
        d1=letter_distribution(s1)
        m=d1['a']
        #I have initialized m to be the frequency of a.
        a='a'
        #a will store the letter which has the highest frequency and is substituted for e.
        for i in d1:
            if d1[i]>m:
                m=d1[i]
                a=i
        #Now I will find out the letter which is substituted for e.
        #4 is the index of e in the string lower.
        password+=lower[lower.index(a)-4]
    return password

def cryptanalyse_vigenere_findlength(s):
    '''Given just the tring s, find out the length of the password using which
    some text has resuted in the string s. We just need to return the number
    k'''
    for i in range(1,len(s)):
        #this for loop will find out the length of the password.
        #I will rotate the string by i places and compare the original string with the rotated string.
        #If the proportion of collisions is greater than 0.062, then this is the length of the password.
        #when two random english strings are compared, the proportion of collisions is greater than 0.062.
        if rotate_compare(s,i)>0.062:
            return i

def cryptanalyse_vigenere(s):
    '''Given the string s cryptanalyse vigenere, output the password as well as
    the plaintext'''
    #First I will find out the length of the password.
    k=cryptanalyse_vigenere_findlength(s)
    #Now I will find out the password.
    password=cryptanalyse_vigenere_afterlength(s,k)
    #Now I will decrypt the string using the password.
    plaintext=vigenere_decrypt(s,password)
    #As the string is very long, I will only print the first 500 characters.
    plaintext=plaintext[:500]
    #I will return the password and the plaintext.
    return password,plaintext
                                                      
s=textstrip('english_random.txt')
#Using english_random.txt to test the functions.
s=vigenere_encrypt(s,'coding')
print("I have encrypted the string using password 'coding'.")
print("Now I will decrypt the string using cryptanalyse_vigenere without knowing the password.")
import time
start=time.time()
#I will find out the time taken to decrypt the string.
print(cryptanalyse_vigenere(s))
end=time.time()
print(end-start)


