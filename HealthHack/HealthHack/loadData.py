from os import listdir
from django.conf import settings

# returns a dictionary of all the load data
def loadData():
	return {"cssData": cssData(), "pageNames" : pageNames()}
# finds the names of all css files and returns them as a list
def cssData():
	return listdir("HealthHack/static/css")

def camelCase(str):
    str = str[0].upper() + str[1:]
    return str

def pageNames():
	out = []
	# gets the name of all the html pages except the home page
	for name in listdir("HealthHack/templates/pages"):
	       out.append(camelCase(name.split(".")[0]))
	return out
