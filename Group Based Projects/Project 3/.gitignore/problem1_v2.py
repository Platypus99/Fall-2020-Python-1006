# Group Exercises 3

# Teammates: Luke Zerrer, Lance Wong

from collections import defaultdict
import string
def count_ngrams(file_name, n): 
    """
    This function reads an input file and returns a dictionary of n-gram counts.  
    file_name is a string, n is an integer. 
    The result dictionary maps n-grams to their frequency (i.e. the count of 
    how often that n-gram appears). Each n-gram key is a tuple and the count is
    an int.
    """
    # The defaultdict class may be useful here. Check the python 
    # documentation for more information: 
    # https://docs.python.org/3/library/collections.html#collections.defaultdict


    
    # actor_to_movie_set= {}
    li_all_words = []
    f = open(file_name, 'r')
    for line in f: 
        line = line.strip()
        line = line.lower()
        fields = line.split(" ")
        if fields == ['']:
            continue
        new_word_to_add_to_big_list = ""
        for word in fields:
          all_weird_char = string.punctuation
          for ch in word:
            if ord(ch) == 32 or ord(ch) == 45:
              new_word_to_add_to_big_list = new_word_to_add_to_big_list + ch

            elif ch not in all_weird_char:
               new_word_to_add_to_big_list = new_word_to_add_to_big_list + ch
            



          li_all_words.append(new_word_to_add_to_big_list)
          new_word_to_add_to_big_list = "" 
         
    ngram_dict = {}
    set_unique_ngrams = set()
    for words in range(len(li_all_words)):
      li_ngram_sized = li_all_words[words:words+n]
      ngram_dict_key = (tuple(li_ngram_sized))
      if ngram_dict_key in set_unique_ngrams:
           ngram_dict[ngram_dict_key] = ngram_dict[ngram_dict_key] + 1 
      else:
          ngram_dict[ngram_dict_key] = 1
          set_unique_ngrams.add(ngram_dict_key)


    return ngram_dict
    # pass # Replace this


def single_occurences(ngram_count_dict): 
    """
    This functions takes in a dictionary (in the format produces by 
    count_ngrams) and returns a list of all ngrans with only 1 occurence.
    That is, this function should return a list of all n-grams with a count
    of 1. 
    """
    li_count_1 = []
    for key in ngram_count_dict.keys()  :
        if ngram_count_dict[key] == 1:
            li_count_1.append(key)
            
    return li_count_1
    # return []# Replace this

def most_frequent(ngram_count_dict, num): 
    """
    This function takes in two parameters: 
        ngram_count_dict is a dictionary of ngram counts. 
        num denotes the number of n-grams to return.       
    This function returns a list of the num n-grams with the highest
    occurence in the file. For example if num=10, the method should 
    return the 10 most frequent ngrams in a list. 
    """
    # Hint: For this you will need to sort the information in the dict 
    # Python does not support any way of sorting dicts 
    # You will have to convert the dict into a list of (frequency, n-gram)
    # tuples, sort the list based on frequency, and return a list of the num
    # n-grams with the highest frequency. 
    # NOTE: you should NOT return the frequencies, just a list of the n-grams



    # Now print a sorted list of letters and frequencies
    ngrams_and_freqs = []
    li_n_highest_freq = []
    for k,v in ngram_count_dict.items():
        ngrams_and_freqs.append((v,k))
    ngrams_and_freqs.sort(reverse = True)
    # print(ngrams_and_freqs)  
    for things in range(num):
        high_freq_ngrams = ngrams_and_freqs[things][1]
        li_n_highest_freq.append(high_freq_ngrams)
    return li_n_highest_freq
        
  

# return [] # Replace this

def main():
    filename = "alice.txt"
    n = 2
    most_frequent_k = 5

    ngram_counts = count_ngrams(filename, n)

    print('{}-grams that occur only once:'.format(n))
    print(single_occurences(ngram_counts))

    print('{} most frequent {}-grams:'.format(most_frequent_k, n))
    print(most_frequent(ngram_counts, most_frequent_k))

if __name__ == "__main__":
    main()
