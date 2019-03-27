import comtypes.client as cc
import comtypes

cc.GetModule("sample1.dll")

import comtypes.gen.SAMPLE1Lib as SAMPLE1Lib

test = cc.CreateObject(SAMPLE1Lib.CGreet, None, None, SAMPLE1Lib.ICGreet)

print (test.COPY("__init__.py", "C:\\Users\\Denys_Bohdan\\AppData\\Local\\Programs\\Git\\ci-server-course-work\\fe", "C:\\Users\\Denys_Bohdan\\AppData\\Local\\Programs\\Git\\ci-server-course-work\\be\\modules\\clis"))