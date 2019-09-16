# fa19-516-156 E.Cloudmesh.Common.1
# Objective: Develop a program that demonstartes the use of banner, HEADING, and VERBOSE
from cloudmesh.common.console import Console
from cloudmesh.common.util import banner, HEADING
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.variables import Variables

banner("Cloud Programming")

mesg = "console test"

# test Console
Console.ok(mesg)
Console.msg(mesg)

## Print the Heading, with ###
HEADING("Heading")

##VERBOSE
variables = Variables()

variables['debug'] = True
variables['trace'] = True
variables['verbose'] = 10

m = dict(key1="value1", key2="value2", key3="value3")
VERBOSE(m)
