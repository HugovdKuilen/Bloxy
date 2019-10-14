from urllib2 import urlopen
import re

urlpath =urlopen('http://www.divms.uiowa.edu/~jni/courses/ProgrammignInCobol/presentation/')
string = urlpath.read().decode('utf-8')

pattern = re.compile('ch[0-9]*.ppt"') #the pattern actually creates duplicates in the list

filelist = pattern.findall(string)
print(filelist)

for filename in filelist:
    filename=filename[:-1]
    remotefile = urlopen('http://www.divms.uiowa.edu/~jni/courses/ProgrammignInCobol/presentation/' + filename)
    localfile = open(filename,'wb')
    localfile.write(remotefile.read())
    localfile.close()
    remotefile.close()
