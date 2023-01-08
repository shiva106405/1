import time

from cadtest3 import vtPnt,vtInt,vtFloat,vtObject,vtVariant

import win32com.client

wincad = win32com.client.Dispatch("AutoCAD.Application")
doc1 = wincad.ActiveDocument
mp1 = doc1.ModelSpace

str_counter=0
mt1_insertpt1=vtFloat([0,0,0])
for str_counter in range(48):
    mt1=mp1.AddMtext(mt1_insertpt1,1000,str_counter)
    wincad.Update()
    time.sleep(0.04)
    mt1.Delete()



