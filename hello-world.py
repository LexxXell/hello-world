#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# By Alexey aka LexxXell lexxxell007@gmail.com

'''
Callback functionf name end whis _clbk
'''

# HelloWorld variable
hello_world = "Hello World!"

# error types list
error_types = [
            "* ",
            "DEBUG: ",
            "ERROR: ",
            "CRITICAL ERROR: ",
        ]
#END error types list

# classes

#loger
class loger:
    '''
    Simple loger
    Class take on args:
        - log file name (fale_name: str) if missing - no log in file
        - callback function for displayed (output_callback)
        - error list (optional) (error_list: list)
            example:
            error_list = [
                        "ERROR: ",
                        "CRITICAL: ",
                    ]

    Method write tqke on:
        - log text (text: str)
        - error type (error_type: int)
    '''
    # def (class loger)

    # def __init__
    def __init__(self,
                 file_name: str,
                 output_callback,
                 error_list: list,
            ):
        super(loger, self).__init__()
        self.__file_name__ = file_name
        self.__output_callback__ = output_callback
        self.__error_list__ = error_list
    #END def __init__

    # def write
    #  Method to output to file or/and displayed log
    def write(
            self,
            text: str,
            error_type: int,
            ):

        #  Check error_type value
        if error_type < 0 or error_type >= len(self.__error_list__):
            error_type = 0

        #  Add error type to text
        text = self.__error_list__[error_type] + text

        #  If file_name is available write log in file
        if self.__file_name__:
            with open(self.__file_name__, "a") as f:
                f.write(f"\n{text}")

        #  If output function is available to transfer text to it
        if self.__output_callback__:
            self.__output_callback__(text)
    #END def write

    #END def (class loger)
#END loger

#END classes

# def

# output_clbk
'''
Funtion take on data as string and displayed it via "print()"
'''
def output_clbk(
            text: str,
        ):
    print(text)  #  Singl print() in whole code!!!
#END output_clbk

# input_clbk
'''
Funtion take on data as string and displayed it via "print()"
'''
def input_clbk(
            invite: str,
        ):
    return input(invite)  #  Singl print() in whole code!!!
#END input_clbk

# enum_items_clbk
'''
Function take on data as list and arguments as dict. Arguments contains:
    - starting position of enumeration ("start": int)
    - end position of enumeration ("stop": int)
    - step of enumeration ("step": int)
Function returns the converted data as list.
'''
def enum_items(
            data: list,
            args: dict,
        ):
    tmp = []
    for i in range(
                int(args["start"]),
                int(args["stop"]),
                int(args["step"]),
            ):
        tmp.append(data[i])
    return tmp
#END enum_items_clbk

# input_enum_args
def input_args(
            args: dict,
            min_arg_value: int,
            max_arg_value: int,
            output_callback,
            input_callback,
            check_callback,
            invite_text: str,
            log_callback,
        ):
    output_callback(invite_text)
    for arg in args:
        while True:
            try:
                arg_value = int(input_callback(f"{arg} = "))
                check = True
            except:
                check = False
                log_callback("Invalid values entered", 2)
            if check and check_args(
                                arg_name = arg,
                                arg_value = arg_value,
                                min_value = min_arg_value,
                                max_value = max_arg_value,
                            ):
                args[arg] = arg_value
                break
            else: log_callback("Input fail. Please repeat.", 1)
    return args
#END input_enum_args

# check_args
def check_args(
            arg_name: str,
            arg_value: int,
            min_value: int,
            max_value: int,
        ):
    if arg_name == "start" or arg_name == "stop":
        if min_value <= arg_value <= max_value:
            return True
    elif arg_name == "step":
        if not(arg_value == 0):
            return True
    return False
#END check_args

#END def

# MainFrame
if __name__ == "__main__":

    log = loger(
            file_name = None,
            output_callback = output_clbk,
            error_list = error_types,
        )

    args = input_args(
                args = {
                            "start": None,
                            "stop": None,
                            "step": None,
                        },
                min_arg_value = 0,
                max_arg_value = len(hello_world),
                output_callback = output_clbk,
                input_callback = input_clbk,
                check_callback = check_args,
                invite_text = "Input vriables for enumeration:",
                log_callback = log.write,
        )

    tmp = enum_items(
                        data = hello_world,
                        args = args,
                    )

    output_clbk("".join(tmp))
