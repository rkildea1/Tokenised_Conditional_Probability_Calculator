
f = open('moby_dick.txt', 'r+')

def rwrds(f):
    words1 = f.read()
    single_words_list = words1.split()
    #first create the bigram
    q3_words_list = words1.split() #words1 defined above
    print('\nUnigrams list:\n',q3_words_list) # print the word list (unigrams)
    def bigram(file,n=2,i=0):
        while len(file[i:i+n]) == n:
            yield file[i:i+n]
            i += 1
    bigrams_lists = list(bigram(q3_words_list, n=2)) #this is my bigram list. list inside a list
    print('\nBigrams list:\n',bigrams_lists)
    
    ##count of each item appearing##
    f.seek(0) #reset back to top of file
    single_words_list = words1.split()
    l = single_words_list
    single_item_count_list = []
    for i in l:
        counter = single_words_list.count(i)
        new_li = i,counter
        single_item_count_list.append(new_li)
    print('\nUnigram Dict with Count of appearance:\n',single_item_count_list)
    
    #probability of each unigram appearing (#
    print('\nUnigram, Count and Probability of appearing:')
    for item in single_item_count_list:
        x = item[1]
        print(item, x/len(single_item_count_list)) 
    unigram_prob_list= [] #create the refined list (to take out count)
    for item in single_item_count_list:
        x = item[1]
        uniprob = (x/len(single_item_count_list))
        y = item[0]
        uniprob1 = (y, uniprob)
        unigram_prob_list.append(uniprob1)
#     print('\nProbability of each unigram appearance:\n',unigram_prob_list)

    ## count of each bigram appearing ##
    l = bigrams_lists
    bigrams_count = []
    for i in l:
        counter = bigrams_lists.count(i)
        new_li = i,counter
        bigrams_count.append(new_li)
#     print('\nCount of each bigram appearance:\n',bigrams_count)
    

    Bigram_prob_list= []
    for item in bigrams_count:
        x = item[1]
        prob1 = (item[0], x/len(bigrams_count))
        Bigram_prob_list.append(prob1)
#     print('\nProbability of each bigram appearance:\n',Bigram_prob_list)
    print()
    
    #so, CND PRB = (the odds of [Bigram] appearing) / (the odds of [Unigram] appearing)
    a = unigram_prob_list
    b = Bigram_prob_list

    cndt_bigram_list = []
    for x, y in zip(unigram_prob_list, Bigram_prob_list):
        #print('\nCombined:',y,'and',x)
        cndt_prob = (x[1]/y[1])
        f_cndt_prob = (y[0], cndt_prob)
        sentencized = ("The Conditional Probability of",y[0][1],"appearing when", x[0], "preceeds it is",cndt_prob)
        #print('Conditional Prob is equal to:',(y[1]/x[1]))
        cndt_bigram_list.append(sentencized)
#     print('print the first example of the list')
    for i in cndt_bigram_list:
        print(i)
    
    

    
rwrds(f)
