# fa19-516-156 E.Cloudmesh.Common.3
# Develop a program that demonstartes the use of FlatDict.

from cloudmesh.common.FlatDict import FlatDict
import flatdict

values = {'City': {'Houston': {'Offices': 4,
                               'Cars': 20,
                               'Employees': 25},
                   'Newyork': {'Offices': 10,
                               'Cars': 25,
                               'Employees': 45}
                   }
          }

flat = flatdict.FlatDict(values)

## Print all city details flatdict
print(flat['City'])

## Print each city details.
print(flat['City:Houston'])
print(flat['City:Newyork'])
