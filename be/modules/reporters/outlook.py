import random
import string
from comtypes.client import CreateObject
from pythoncom import CoInitializeEx
from pythoncom import CoUninitialize

def _sendMail(to, subject, body):
    CoInitializeEx(0)

    outlook = CreateObject("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = subject
    mail.Body = body

    mail.Send()

    CoUninitialize()

def notifyViaEmail(data):
    to = data["to"]
    build = data["build"]
    projectKey = data["projectKey"]

    message = "Build of '{project}' has finished with status '{status}'. Output:\n{output}".format(
        project=projectKey,
        status=build["status"],
        output=build["output"]
    )

    _sendMail(to, "Build result notification", message)
