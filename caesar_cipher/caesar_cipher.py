import re
import nltk
nltk.download('words')

def encrypt(str,key,state="encrypt"):
    """
    str- String that will be encrypted using ASCII Code
    key-: Number of shifting
    encrypted_msg _ returned encrypted message
    """


    if state == "encrypt": # Remove the special characters just for encryption
        str=text_only(str)

    encrypted_msg=''
    
    if key <0:
        key = abs(key)%26
        key=-key
    elif key > 26:
        key%=26

    

    for char in str:
        letter=ord(char)+key
        # print(letter,chr(letter))
        encrypted_msg+=chr(letter)
        # print(encrypted_msg)
    return encrypted_msg

def text_only(str):
    # a=re.sub('[^A-Za-z0-9]+', '', str)
    # a=re.sub('[?|$|.|!|:]','',str)
    # a=re.sub(r"[^a-zA-Z0-9|(\s)(\n)]","",str)
    a=re.sub(r"[^a-zA-Z|(\s)(\n)]","",str)

    return a
def decrypt(str,key):
    return encrypt(str,-key,"dec")




original_words_list = nltk.corpus.words.words()
# print(words_list[30000:30100])
words_list = [word.lower() for word in original_words_list]





def most_likely(sentences):
    """
    function to expect the message
    input -{sentences}encrypted message(s)
    output-{arr3} list of possible messeges
    """
    try:
        sentences=sentences.split()
        for word in sentences:
            arr=[decrypt(word,i) for i in range(1,27)]
    
        # print(sentences)


        arr2=[]
        arr3=[]
        
        
        for sp in arr:
            sp=sp.split()
            # print(sp)
            for i in sp :
                if i in words_list:
                    arr2.append(sp)
                    break
                # print(i)
        for i in arr2:
            print("Tjis is I : ",i)
            a=' '.join([str(elem) for elem in i])
            arr3.append(a)
    except:
        return "invalid input"
    # most_possible=most_possible_func(arr3)
    # return f"Array of possible sentences is/are : {arr3}"
    return arr3

 





# def most_possible_func(str):
#     _max = 0
#     _max_sentence = ''

#     for sentence in str:
#         try:
#             sen=sentence.split()
#             for i in sen:
                
#                 if i in words_list:
#                     _max+=1


#         if count_words(sentence) > _max:
#             _max_sentence = sentence
#             _max = count_words(sentence)
#     return _max_sentence
    


if __name__ == "__main__":
    # print(encrypt("mohammed",1))
    print(encrypt("Why you 401 5are here",5))
    print(decrypt('\m~%~tz%956%:fwj%mjwj',5))
    # print(most_likely('dktf"jkdjk"oqjcoogf'))

    # print(most_likely('Gcv"vjg"dktf"dfsg"oqjcoogf'))
    # print(most_likely('\m~%~tz%fwj%mjwj'))
    # print(most_likely(""))
    
    

    

    
    # print(reg('moh:dgdf555s jkhl'))