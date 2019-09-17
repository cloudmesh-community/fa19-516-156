# fa19-516-156 E.Cloudmesh.Common.4
# Develop a program that demonstartes the use of cloudmesh.common.Shell.

from cloudmesh.common.Shell import Shell

##Check Python Version
result = Shell.check_python()
print(result)

## Check Valid Shell command
result = Shell.command_exists("print")
print(result)

result = Shell.command_exists("output")
print(result)


result = Shell.terminal_type()
print(result)

