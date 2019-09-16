# fa19-516-156 E.Cloudmesh.Common.1
# Objective: Develop a program that demonstartes the use of banner, HEADING, and VERBOSE
from cloudmesh.common.console import Console
from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE

banner("Cloud Programming")

mesg = "console test"

# test Console
Console.ok(mesg)
Console.msg(mesg)


class Example(object):

    def doit(self):
        HEADING()
        Print(" Heading")


m = {"key": "value"}
VERBOSE(m)
