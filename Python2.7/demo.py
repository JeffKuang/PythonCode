# coding: GB2312  
import os, re  
  
# execute command, and return the output  
def execCmd(cmd):  
    r = os.popen(cmd)  
    text = r.read()  
    r.close()  
    return text  
  
# write "data" to file-filename  
def writeFile(filename, data):  
    f = open(filename, "w")  
    f.write(data)  
    f.close()  
  
# ��ȡ�����MAC��ַ��IP��ַ  
if __name__ == '__main__':  
    cmd = "ipconfig /all"  
    result = execCmd(cmd)
    #print result
    #pat1 = "Physical Address[\. ]+: ([\w-]+)"  
    pat1 = "�����ַ[\. ]+: ([\w-]+)"  
    #pat2 = "IP Address[\. ]+: ([\.\d]+)"  
    pat2 = "IPv4 ��ַ[\. ]+: ([\.\d]+)"  
    MAC = re.findall(pat1, result)[0]       # �ҵ�MAC  
    IP = re.findall(pat2, result)[0]        # �ҵ�IP  
    print("MAC=%s, IP=%s" %(MAC, IP))

    cmd = "python ex12.py"
    result = os.system(cmd)
    check = "How old are you?"
    print result
