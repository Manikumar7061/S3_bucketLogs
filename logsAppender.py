import subprocess
import os
import fileinput
import re
from time import strptime

def logSorter(l,t_fmt,t_fmt2,t_fmt3):
    key=""
    try:
        key=strptime(re.search(r'^\[?\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d+Z',l).group(0).replace('[',''), t_fmt)  #"?" -- optional    
    except:
            try:
                key=strptime(re.search(r'^\[?\w{3}, \d{2} \w+ \d{4} \d{2}:\d{2}:\d{2}',l).group(0), t_fmt2)
            except:
                try:
                    key=strptime(re.sub("^\(\w{4}:\d{4}", '',(re.search(r'^\(\w{4}:\d+?\[?-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d+Z',l).group(0))), "%Y-%m-%dT%H:%M:%S.%fZ")  #"?" -- optional 
                except:
                    try:
                        key=strptime(re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+',l).group(0), t_fmt3)
                    except:
                        pass
    return key


def sortingAppending(file):
    
    lines = open(file,"r+")

    t_fmt = "%Y-%m-%dT%H:%M:%S.%fZ" # format of time stamps
    t_fmt2 = "%a, %d %b %Y %H:%M:%S"
    t_fmt3 = "%Y-%m-%d %H:%M:%S,%f"
    temp_list =[]
    try:    
        for l in lines:
            if logSorter(l,t_fmt,t_fmt2,t_fmt3)!='':
                temp_list.append(l)
            else:        
                res = ' '.join([temp_list[-1],l])
                temp_list.pop()
                temp_list.append(res)
        lines.truncate(0);
        lines.seek(0);
        for l in sorted(temp_list, key=lambda line: logSorter(line,t_fmt,t_fmt2,t_fmt3)):
            lines.write(l)
    except:
        print("no date patterns in it")
        return
 


os.chdir(os.getcwdb().decode("utf8")+"/.serverLogs")

serverFiles = os.listdir();

serverFiles_0=[]
serverFiles_1=[]

for i in range(len(serverFiles)):
    print(serverFiles[i])
    os.chdir(os.getcwdb().decode("utf8")+"/"+serverFiles[i])
    globals()['serverFiles_%s' % i] = os.listdir();
    os.chdir("..")

serverLogsDirectoryPath = os.getcwdb().decode("utf8")
print(serverLogsDirectoryPath)

os.chdir("..")  #home dir

cmd = "mkdir -p finalServerLogs"
subprocess.call(cmd, shell=True)

print(serverFiles)

for j in range(len(serverFiles_1)):
    cmd = "cat "+serverLogsDirectoryPath+"/logFiles_1/"+serverFiles_1[j]+" "+serverLogsDirectoryPath+"/logFiles_3/"+serverFiles_1[j]+" >finalServerLogs/" +serverFiles_1[j]
    subprocess.call(cmd, shell=True)
    
    
    sortingAppending("finalServerLogs/"+serverFiles_1[j])
    cmd2 = "gedit finalServerLogs/"+serverFiles_1[j]+" &"
    subprocess.call(cmd2, shell=True)

cmd3 = "rm -r .serverLogs"
subprocess.call(cmd3, shell=True)
