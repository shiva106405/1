import mpmath
import pythoncom
import win32com.client
wincad=win32com.client.Dispatch("AutoCAD.Application")
doc1=wincad.ActiveDocument
mp1=doc1.ModelSpace

def vtPnt(x,y,z=0):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY|pythoncom.VT_R8,(x,y,z))
def vtObject(obj):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY|pythoncom.VT_DISPATCH,obj)
def vtFloat(list):
    return  win32com.client.VARIANT(pythoncom.VT_ARRAY|pythoncom.VT_R8,list)
def vtInt(list):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY|pythoncom.VT_I2,list)
def vtVariant(list):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY|pythoncom.VT_VARIANT,list)
pt1=vtFloat([100,100,100])
pt2=vtFloat([200,200,200])
retval=mp1.Addline(pt1,pt2)
