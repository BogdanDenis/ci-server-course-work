import random
import string
from comtypes.client import CreateObject
from pythoncom import CoInitializeEx
from pythoncom import CoUninitialize

def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

def generateReport(data):
    CoInitializeEx(0)

    xl = CreateObject("Excel.Application")
    xlBook = xl.Workbooks.Add()

    from comtypes.gen.Excel import xlRangeValueDefault

    def setHeadings():
        xl.Range["A1", "H1"].Value[xlRangeValueDefault] = (
            "Commit Id",
            "Commit Message",
            "Commit Author",
            "status",
            "startTime",
            "endTime",
            "duration",
            "output")

    def fillRows(builds):
        for index, build in enumerate(builds):
            xl.Range("A{index}".format(index=index+2), "H{index}".format(index=index+2)).Value[xlRangeValueDefault] = (
                build["commitId"],
                build["commitMessage"],
                build["commitAuthor"],
                build["status"],
                build["startTime"]['$date'],
                build["endTime"]['$date'],
                build["duration"],
                build["output"]
            )
    
    setHeadings()
    fillRows(data["builds"])

    fileName = "{name}.xlsx".format(name=randomString(10))

    xlBook.SaveAs(Filename=fileName)
    xlBook.Close(SaveChanges=1)

    CoUninitialize()

    return fileName
