"""
class objects are shared across instances of this class,
while this has no bearing on a string, it would have
altered the way a list worked.
"""

class A():
    name_list = ['Peter']
    def add(self, name):
        self.name_list.append(name)

a1 = A()
a2 = A()

# expected output
print a1.name_list
print a2.name_list

# modify the shared object
a1.add('Not Peter')  

# unexpected output
print a1.name_list
print a2.name_list

# both a1 and a2 point at the same "class" object name_list
# when init is called each gets a fresh "instance" object
# this appears to be the only real difference I can find...
