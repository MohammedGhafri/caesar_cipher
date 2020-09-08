import re
import nltk
nltk.download('words')

def encrypt(str,key):
    """
    str- String that will be encrypted using ASCII Code
    key-: Number of shifting
    encrypted_msg _ returned encrypted message
    """
    
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
    return encrypt(str,-key)




original_words_list = nltk.corpus.words.words()
# print(words_list[30000:30100])
words_list = [word.lower() for word in original_words_list]


def count_words(sentence):

    # sentence=[decrypt(sentence,i) for i in range(1,27)]
    # print(sentence)

    # sentence_words = [str.split() for str in sentence]
    en_word_count = 0

    for word in sentence:
        for word_s in word:
            if word.lower() in words_list:
                en_word_count += 1

    return en_word_count

def most_likely(sentences):
    _max = 0
    _max_sentence = ''
    sentence=[decrypt(sentences,i) for i in range(1,27)]
    print(sentence)

    for sentence in sentence:
        if count_words(sentence) > _max:
            print(count_words(sentence))
            _max_sentence = sentence
            _max = count_words(sentence)
    return _max_sentence







    


if __name__ == "__main__":
    # print(encrypt("mohammed",1))
    print(encrypt("mohamm21:?/ed",28))
    print(decrypt('oqjcoogf',2))
    print(most_likely('oqjcoogf'))
    # print(reg('moh:dgdf555s jkhl'))