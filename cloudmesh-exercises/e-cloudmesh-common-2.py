# fa19-516-156 E.Cloudmesh.Common.2
# Develop a program that demonstartes the use of dotdict.

from cloudmesh.common.dotdict import dotdict
data = {
"Book": "Azure"
}
data = dotdict(data)
var = data.Book
print(var)

#Use Logical condition if..else..
if data.Book is "Azure":
    print("Cloud Engineering using Azure")
else:
    print("Other Cloud Books")

