# import test.txt

def counts_words(file):
    open_file = open(file)      #opens file
    word_count = {} #dictionary with words and their count
    for line in open_file:
        line = line.lower()
        str_lines = line.rstrip('\n')   #removes trailing \n
        str_no_end_pun = str_lines.strip('.')
        str_no_end_pun = str_lines.strip(',') #removes trailing .
        str_no_end_pun = str_no_end_pun.rstrip('?') #removes trailing ?
        list_words = str_no_end_pun.split(' ') #split words where there are spaces
        for word in list_words:
            word_count[word] = word_count.get(word, 0) + 1   
    return word_count

word_count = counts_words('test.txt')
print(word_count)