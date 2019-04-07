from mongoengine import connect

connect('ciserver', host='mongodb', port=27017)
