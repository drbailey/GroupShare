#CS 145 Spring 2014 Programming Assignment 1 -  Doubly Linked List
#Filename: garrett_gregory_assignment_1.py
#Author: Garrett Gregory
#Date: 14 June 2014
#Description: This programming assignment contains a doubly linked list class that links together nodes containing three fields of student
#   information. The main() function gives the user controls to modify their linked list using both private and public class functions.
"""
Linked lists are generally not super useful by themselves,
though they can reduce time complexity of certain queuing algorithms.
- Drew
"""
__author__ = "Garrett Gregory"
"""  """
class StudentNode:
    def __init__(self, sID, sName=None, sMajor=None, nextPtr=None, prevPtr=None):
        self._sID = sID
        self._sName = sName
        self._sMajor = sMajor
        self.next = nextPtr
        self.prev = prevPtr

    def __str__(self):
        '''prints out the information contained by the node'''
        return '\nStudent ID: '+str(self._sID)+'\nStudent Name: '+str(self._sName)+'\nMajor: '+str(self._sMajor)
        
class SortedLinkList:
    def __init__(self):
        self.head=None
        self.tail=None
        self._size=0
        
    def __len__(self):
        '''traverses the linked list and returns the number of nodes counted'''
        start=self.head
        length=0
        while start!=None:
            length+=1
            start=start.next
        return length

    # private methods-----------------------------------------------------------

    def _addFirst(self, node):
        '''adds a node to the beginning of the linked list'''
        if self.head == None: #empty list
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def _addLast(self, node):
        '''adds a node to the end of the linked list'''
        self.tail.next = node #does not need to work on empty list
        node.prev = self.tail
        self.tail = node

    def _find(self, sID):
        '''returns a pointer to node with specified sID'''
        spot = self.head
        while spot!=None: #empty list will skip and return False
            if spot._sID == sID:
                return spot
            else:
                spot=spot.next #check compare next node
        return False

    def _isEmpty():
        '''returns True if the list is empty'''
        if self._size == 0:
            return True
        else:
            return False

    # public methods------------------------------------------------------------

    def index(self, sID):
        '''returns the position index of the node containing a sID (1,2,3,4,5...)'''
        start=self.head
        ind=1
        while start!=None: #will return False if empty list
            if start._sID == sID:
                return ind
            else:
                start=start.next  #check next node, add one to index count
                ind+=1
        return False

    def insert(self, sID, sName=None, sMajor=None):
        '''creates and adds a new node using appropriate private methods'''
        self._size+=1
        node=StudentNode(sID, sName, sMajor)
        
        if self.head == None or int(sID) < int(self.head._sID): #empty list or lower sID
            self._addFirst(node)
        elif int(sID) > int(self.tail._sID): #higher sID
            self._addLast(node)
        else: #sID fits somewhere in between start and end of linked list
            spot=self.head
            while spot!=None:
                if int(spot.next._sID) < int(node._sID): #finds proper node location
                    spot=spot.next
                else:
                    node.next = spot.next #links nodes prev and next to new node
                    spot.next.prev = node
                    spot.next = node
                    node.prev = spot
                    return
                    
        
    def remove(self, sID):
        '''removes a node containing the provided sID from the linked list'''
        point = self.head
        while point!=None:
            if point._sID == sID:
                self._size-=1 #removal confirmed, list size reduced by 1
                if point.prev == None and point.next == None: #only one node in list
                    self.head = None
                elif point.prev == None: #node is the head
                    self.head = point.next
                    self.head.prev = None
                    return
                elif point.next == None: #node is the tail
                    self.tail = point.prev
                    self.tail.next = None
                    return
                else: #node is between head and tail
                    point.prev.next = point.next
                    point.next.prev = point.prev
                    return
            point = point.next
        return False

    def pop(self):
        '''removes the last node in the linked list'''
        if self.tail.prev == None: #node is head
            self.tail = None
            self.head = None
        else:                      #multiple nodes in list
            self.tail = self.tail.prev
            self.tail.next = None
            self._size-=1

    def printList(self):
        '''prints the linked list in order of head to tail'''
        start=self.head
        while start!=None:
            print(start,'\n\n-----------------')
            start=start.next

    def printListReverse(self):
        '''prints the linked list in reverse order (tail to head)'''
        start=self.tail
        while start!=None:
            print(start,'\n\n-----------------')
            start=start.prev

    def reverse(self):
        '''returns a reversed version of the linked list'''
        point = self.head
        tempoint = None
        while point!=None:
            tempoint = point.next
            point.next = point.prev   #swap next and prev for current point
            point.prev = tempoint
            if point.next != None:    #check for end of list
                point.next.prev = point
            point = point.prev        #THIS LINE OF CODE.... >:O        moves to next node which is now point.prev
        tempoint = self.head
        self.head = self.tail         #swap head and tail to finalize
        self.tail = tempoint





def main():
    '''main controller function that prompts the user with a set of options to make changes to their linked list'''
    linkList = SortedLinkList()

    while True:
        option = input('\nEnter one of the following options (letter/number only)...  a: add a node, d: delete a node, p: pop node from end, i: get node index, c: get node count, r: reverse list order, 1: print list, 2: print list in reverse, e: exit\n\n')
        if option == 'a': #insert new node
            sID = input('9-digit Student ID: ')
            while type(sID) != str or len(str(sID)) != 9 or sID.isdigit()==False or linkList._find(sID) != False: #check if sID in proper format
                sID = input('Student ID must be a numerical string 9 digits long. Try again: ')
            name = input('Student Name: ')
            major = input('Major: ')
            linkList.insert(sID,name,major)
            print('---Complete---')
        elif option == 'd': #remove a node
            sID = input('Student ID to delete: ')
            if linkList.index(sID)==False:
                print('Student ID not found')
            else:
                linkList.remove(sID)
                print('---Complete---')
        elif option == 'p': #pop a node
            linkList.pop()
            print('---Complete---')
        elif option == 'i': #check node index
            sID = input('9-digit Student ID: ')
            if linkList.index(sID)==False:
                print('Student ID not found')
            else:
                print('The node index is '+str(linkList.index(sID)))
        elif option == 'c': #get node count
            print('The total number of nodes is '+str(len(linkList)))
        elif option == 'r': #reverse linked list order
            linkList.reverse()
            print('---Complete---')
        elif option == '1': #print linked list
            linkList.printList()
        elif option == '2': #print linked list in reverse
            linkList.printListReverse()
        elif option == 'e': #exit script
            return

main()
    
            
            




##a=SortedLinkList()
##a.insert('555555555','gar','yo')
##a.insert('444444444','bar','no')     #test nodes
##a.insert('333333333','far','go')
##a.insert('999999999','lar','ko')
##a.insert('567777777','mar','bo')
        
