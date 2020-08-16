from collections import OrderedDict

CONGIF = {
    "creds":
        {
            "aws_id": "dummy",
            "aws_key": "dummy"
        },
    "func":
        {
            "name_prefix": "mytest",
            "region": "us-east-1",
            "role_1": "dummy",
<<<<<<< HEAD
            "role_2": "dummy"
=======
            "role_2": "dummy",
            "role_3": "dummy",

>>>>>>> origin/fileupload_measurement
        }
}


# The default path for function code

CODE_PATH = {
    'python2.7': './code/python',
    'python3.6': './code/python',
    'python3.7': './code/python',
    #'nodejs12.x': './code/nodejs',
    #'java8': './code/java',
}


"""
The template request
sleep: set a value X here. The function will sleep for X seconds before return
stat: if let the measurement function will run the basic_stat subroutine
run: pass a cmd to the measurement function. if set the measurement function
	will run the specified string as an external command.
io: pass the parameters for the IO tests
net: pass the parameters for the network throughput tests
cpu: pass the parameters for the CPU tests
cpuu: pass the parameters for the CPU utilization tests
"""
PARA_TEMP = OrderedDict()
PARA_TEMP["sleep"] = 0		# change it to 0 for quick tests
PARA_TEMP["stat"] = dict(argv=1)
PARA_TEMP["run"] = dict(cmd=str)
PARA_TEMP["io"] = dict(rd=int, size=str, cnt=int)
PARA_TEMP["net"] = dict(port_offset=int, server_ip=str)
PARA_TEMP["cpu"] = dict(n=int)
PARA_TEMP["cpuu"] = dict(n=int)
