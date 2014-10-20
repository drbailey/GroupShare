__author__ = 'drew bailey'

'''
This is a very simple look at writing cards that I started when I was learning
objects a while ago.
This is not finished (war doesn't work), but is an example of simple object
types.
'''

class Deck():
    def __init__(self,player_number=2):
        self.cards = {}
        self.suits = [u"\u2660",u"\u2666",u"\u2665",u"\u2663"]
        self.crange = range(2,14)
        self.ace = 1
        self.aceval = 14
        if self.ace == 0:
            self.aceval = 1
        elif self.ace == -1: 
            self.aceval = 0
        self.order = []
        self.player_number = player_number
        self.players = {}
		
    def generate(self):
        for suit in self.suits:
            self.cards[unicode('A')+unicode(suit)] = self.aceval
            for value in self.crange:
                if value < 11:
                    self.cards[unicode(value)+unicode(suit)] = value
                elif value < 12:
                    self.cards[unicode('J')+unicode(suit)] = value
                elif value < 13:
                    self.cards[unicode('Q')+unicode(suit)] = value
                elif value < 14:
                    self.cards[unicode('K')+unicode(suit)] = value
                    
    def shuffle(self):
        import random
        for x in self.cards:
            self.order.append(x)
        random.shuffle(self.order)

    def abstract_shuffle(self,alist):
        import random
        random.shuffle(alist)
        return alist
        
    def deal(self): #limit to even number of cards
        i=1
        for x in range(self.player_number):
            self.players[x+1] = []
        for x in self.order:
            for p in self.players:
                if i==p:
                    self.players[i].append(x)
            if i < self.player_number:
                i+=1
            else:
                i=1

class War(Deck):
    def __init__(self):
        Deck.__init__(self)
        self.something = 0

    def fight(self):
        import time
##        print 3
##        time.sleep(1)
##        print 2
##        time.sleep(1)
##        print 1
##        time.sleep(1)
        print "FIGHT!"
        i=0
        while i<10:
            table,value,winner,winnings=[],0,0,[]
            for p in self.players:
                if self.players[p]:
                    table.append((p,self.players[p][0],self.cards[self.players[p][0]]))
            for entry in table:
                print entry[0],entry[1]
                if entry[2] == value:
                    print "there was a war."
                    #war(table)
                elif entry[2] > value:
                    value = entry[2]
                    winner = entry[0]
                    winnings.append(entry[1])
            for p in self.players:
                if p == winner:
                    self.players[winner].extend(winnings)
                    print "Player ",p," wins ",','.join(winnings)
                del(self.players[p][0])
            #self.status_check()
            c = self.breaker()
            if c==True:
                break
            
    def breaker(self):
        for p in self.players:
            if not self.players[p]:
                print "Player ",p," lost!"
                return True
    
    def war(table):
        print "WAR!"

    def _status_check(self):
        for y in w.players:
            print "player ",y
            print ','.join(w.players[y])
        
if __name__ == '__main__':
    w = War()
    w.generate()
    w.shuffle()
    w.deal()

    w._status_check()
    #w.fight()

