class anagram():
    def __init__(self):
        self.dictionary = {} #an actual dictionary, not just a dict()
        self.results = {}

    def handler(self,word): #make a key
        return "".join(sorted(word))
    
    def tester(self,word): #lookup a key, use to map
        hw = self.handler(word)
        result = self.dictionary.get(hw,[])
        #result = self.dictionary.get(self.handler(word),[])
        #result = self.dictionary.get(self.handler(word),[]) #now program won't fail to compile no key found
        result2 = []
        result2.append([r for r in result if r != word])
        if result2: #each input mapped seperately, fn handles only one word at a time
            self.results[word] = result2
        else:
            self.results[word] = []
            


if __name__ == '__main__': #so imports work
    # User input...
    #inputs = raw_input('Input words seperated by commas to look up anagrams for.').split(',')
    # ... or list input!
    inputs = ['silence','angered','married','elvis','foobar','somethingwithnoanagram']
    wl = open('wordlist.txt','r')
    A = anagram()

    for w in wl: #construct dictionary object in python
        hw = A.handler(w.strip()) #this is my key, strip for possible whitespace in wordlist file
        if hw not in A.dictionary:
            A.dictionary[hw] = [w.strip()] #list object for appending
        else:
            A.dictionary[hw].append(w.strip())
    
    m = map(A.tester,inputs)  #maybe use this map later for results?

    for key, value in A.results.iteritems(): #print results
        print key, value
