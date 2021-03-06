#!python
# filename: testforpost.py
# function: test for the esutils.py
#           
# Author: Mingqing Liao
# E-mail: liaomq1900127@163.com
# FGMS @ Harbin Institute of Technology(HIT)

import elastic3rd.post.post as espost

'''
    Here the test is Si
'''
V0 = 163.193194972   #The volume of undeformed structure
Flag_Fig = 1
Flag_Ord = 4
EEnergy = "EEnergy.txt"
INPUT = "INPUT"

#Post for a given symmetry, no specific the strain mode
(C2, C3) = espost.post(V0, Flag_Fig, Flag_Ord, EEnergy, INPUT)
print(C2)
print(C3)

#Post for some specific the strain mode
STRAINMODE = "STRAINMODE"
(C2, C3) = espost.post_mode(V0, Flag_Fig, Flag_Ord, EEnergy, INPUT, STRAINMODE)
print(C2)
print(C3)