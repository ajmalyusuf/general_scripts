import sys
import re
import os
import os.path
import copy
import errno    
from shutil import copy, copyfile, copy2

filenameRegEx = [
	'.*-hdfs-namenode-.*\.log.*',
	'.*-hdfs-secondarynamenode-.*\.log.*',
	'.*-hdfs-datanode-.*\.log.*',
	'.*-hdfs-journalnode-.*\.log.*',
	'.*-yarn-resourcemanager-.*\.log.*',
	'.*-yarn-nodemanager-.*\.log.*'
	]

acceptedTopLevelDirs = ['hadoop', 'hadoop-yarn']

def makeDir(path):
    try:
	print '===> Creating...', path
        os.makedirs(path)
	print '===> Creaeted...', path
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def isAcceptable(filename):
    for exp in filenameRegEx:
	regex = re.compile(exp)
	if regex.match(filename):
	    return True
    return False

def getFileSize(filename):
	try:
		return os.path.getsize(filename)
	except FileNotFoundError:
		return 0

#######################
#--- Program Start ---#
#######################

if len(sys.argv) < 3:
	print 'Usage:'
	print sys.argv[0] + ' <source_dir> <destination_dir>'
	sys.exit(1)

currWDir = os.getcwd()
if sys.argv[1][0] == '/':
	#sourceBaseDir = os.path.join(sys.argv[1], '')
	sourceBaseDir = sys.argv[1]
else:
	sourceBaseDir = os.path.join(currWDir, sys.argv[1])

if sys.argv[2][0] == '/':
	#destBaseDir = os.path.join(sys.argv[2], '')
	destBaseDir = sys.argv[2]
else:
	destBaseDir = os.path.join(currWDir, sys.argv[2])

topLevel = True
os.chdir(sourceBaseDir)
for dirpath, dirnames, filenames in os.walk('.'):
    if topLevel:
        dirnamesDeepCopy = []
	for val in dirnames:
	    dirnamesDeepCopy.append(val)
	for dir in dirnamesDeepCopy:
	    if not dir in acceptedTopLevelDirs:
		dirnames.remove(dir)
	topLevel = False

    sourceDir = os.path.join(sourceBaseDir, dirpath)
    #sourceDir = dirpath
    destDir = os.path.join(destBaseDir, dirpath)
    print sourceDir
    print destBaseDir

    #for filename in [f for f in filenames if f.endswith(".jpg") or f.endswith(".JPG") or f.endswith(".jpeg")]:

    firstTime = True
    for filename in filenames:
	if isAcceptable(filename):
		sourceFile = os.path.join(sourceDir,filename)
		destFile = os.path.join(destDir,filename)
		try:
			if firstTime:
				makeDir(destDir)
				firstTime = False
			print '--> Copying : ', sourceFile
			print '<-- To : ', destFile
			copy2(sourceFile, destFile)

			fileSize = getFileSize(sourceFile)
			print 'Size ::: ', fileSize
		except:
			print 'Error : |' + sourceFile + '|'
			raise
