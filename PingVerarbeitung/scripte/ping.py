# -*- coding: utf-8 -*-

import sys
stdout_encoding = sys.stdout.encoding
import os
import glob
import subprocess
from datetime import datetime
import re

class execute_CMD():
    def __init__(self,lv_adress="www.google.de",lv_command="ping", lv_args = "") -> None:
        
        #preparations of empty variables
        self.process = None
        self.err = None
        self.out = None
        self.res = None
        self.run_error = False
        
        #for result saving
        self.environment = os.path.dirname(os.path.realpath(__file__))
        self.log_environment = str(os.path.dirname(os.path.realpath(__file__))).replace("scripte","Logs")
        self.script_environment = str(os.path.dirname(os.path.realpath(__file__))).replace("scripte","scripte")
        self.success = True
        self.adress = lv_adress
        self.command = lv_command
        self.args = lv_args
        self.int_log = []

    
    def runtime(self) -> list:
        self.do_command()
        self.save_res()
        return self.res

    def do_command(self) -> list:
        #Does the request over cmd via subprocess.popen which returns raw byte-like "res" list
        try:
            print("Starting to "+str(self.command)+" "+ str(self.adress))
            self.res = subprocess.run([self.command, self.adress], stdout=subprocess.PIPE, shell=True)
            print("Self.process : " + str(self.process))

            if(self.err!=None):
                print("Error :" + self.err)
                self.success = False
            else:
                 self.intLog("We have some result")
                 self.beautify_response()
        except Exception as E:
           print("Error in do_ping function \n" + str(E))
           self.intLog("Error in do_ping function \n" + str(E))

    def show_executable(self) -> list:
        self.intLog("show_executable started")
        res = []
        if(self.environment!=""):
            show_execs = glob.glob(glob.escape(self.script_environment) + "/*.py")
            for i in range(0,len(show_execs)):
                if(str(show_execs[i]).find(".py") != -1):
                    res.append(str(show_execs[i]).split("\\")[-1])
                else:
                    print("Error listing executables")
                    return "E"
            return res
        else:
            print("self.Environment empty")
            return "E"
        
    def beautify_response(self) -> list:
        import codecs
        #Convert list of byteobjects -> str and fix encoding errors
        lv_res = []
        try:
            if(self.res!=None):
                #byte -> str conversion
                for i in range(0,len(self.res)):
                    #print(self.res[i].decode("unicode_escape"))
                    lv_res.append(self.res[i].decode('unicode_escape').rstrip())
                self.res = lv_res
                del lv_res
        except Exception as E:
            print("Error in beautify_response function \n"+str(E))
            self.intLog("Error in beautify_response function \n"+str(E))

    def save_res(self)-> bool:
        now = datetime.now()
        lv_fname = str(self.command) +"-"+ str(self.adress) + now.strftime("%H.%M") +".txt"
        try:
            print(os.path.join(self.log_environment,lv_fname))
            with open(os.path.join(self.log_environment,lv_fname),"w",encoding="utf-8") as file:
                file.write("Results:")
                for i in range(0,len(self.res)):
                    file.write(self.res[i])
                print("File saved under " + self.environment + lv_fname)
                self.intLog("File saved under " + self.environment + lv_fname)
        except Exception as E:
            print(E)
            self.intLog(E)
    
    def show(self) -> None:
        try:
            for i in range(0,len(self.res)):
                if(self.res[i]==""):
                    del self.res[i]
                else:
                    print(self.res[i])
        except Exception as E:
            print("Error in show function \n"+str(E))
            self.intLog("Error in show function \n"+str(E))
            pass

    def intLog(self,message)->None:
        now = datetime.now()
        self.int_log.append(now.strftime("%H.%M.%S") + str(message))

    def extract_ping(self)->list:
        lv_res_str = ""
        #bundling in one str
        for i in range(0,len(self.res)):
            lv_res_str = lv_res_str + str(self.res[i])
        
        ips = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",lv_res_str)
        resp_times = re.findall(r"\d\dms",lv_res_str)
        ttl = re.findall(r"TTL=\d\d\d",lv_res_str)
        breakpoint

    def extract_tracert(self):
        raise NotImplementedError


"""
adress = r"www.google.de"
command = "ping"
arg = ""
#The call can retain following paramters: an adress, a command and optional args to command
ping = PingToArray(adress,command,arg)

if(ping.success):
    print()
    print("Everything done, bye bye")
else:
    print()
    print("Some error during runtime occured")


"""