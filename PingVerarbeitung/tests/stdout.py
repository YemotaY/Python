import glob
import os
cwd = os.getcwd()
search_wd = os.path.join(cwd,"tests")
res = []
def show_executable() -> list:
    show_execs = glob.glob(glob.escape(search_wd) + "/*.py")
    for i in range(0,len(show_execs)):
        if(str(show_execs[i]).find(".py") != -1):
            res.append(str(show_execs[i]).split("\\")[-1])
        else:
            print("\n Error listing executables")
            return "E"
    print("\n Everything went flawlessly.")
    return res
res = show_executable()
print("\n Result : " + str(res))
        