""" Windows Sounds! """

__author__ = 'drew bailey'

### bach suit #1 (cello range A_4 = 440 Hz) first two bars alarm ###
import winsound
import itertools
import time

k = 2000.  # a "konstant" hahahaha (easy to remember?) length of a whole note

# can make a scale with formulas for octaves... but for now...
notes = [(196.00,16),(293.66,16),(493.88,16),(440.,16),
         (493.88,16),(293.66,16),(493.88,16),(293.66,16),
         (196.00,16),(293.66,16),(493.88,16),(440.,16),
         (493.88,16),(293.66,16),(493.88,16),(293.66,16),
         (196.00,16),(329.63,16),(523.25,16),(493.88,16),
         (523.25,16),(329.63,16),(523.25,16),(329.63,16),
         (196.00,16),(329.63,16),(523.25,16),(493.88,16),
         (523.25,16),(329.63,16),(523.25,16),(329.63,16)]
#notes2 = []
for n in notes:
    f,d = n[0],n[1]
    winsound.Beep(int(f),int(k/d))
    time.sleep(.1)
    
