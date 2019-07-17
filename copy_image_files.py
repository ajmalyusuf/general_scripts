import sys
import os
import os.path
import errno    
from shutil import copy, copyfile, copy2
import imagehash
from PIL import Image, ExifTags

#extnList = ['gif', 'jpg', 'jpeg', 'bmp', 'nef', 'tga', 'hdr', 'ico', 'png', 'psd']
#extnList = ['jpg', 'jpeg', 'nef', 'png', 'psd']
extnList = ['mpeg', 'mpg']
excludeDirs = ['.Trashes', 'RECYCLER', '$RECYCLE.BIN', 'Photo Booth Library', 'Photos Library.photoslibrary']

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def isImage(filename):
	indx = filename.rfind('.')
	if indx >= 0 and filename[indx+1:].lower() in extnList:
		return True
	return False

def get_file_size(file_name):
	try:
		return os.path.getsize(file_name)
	except FileNotFoundError:
		return 0


def get_image_size(img):
	return "{} x {}".format(*img.size)


def get_capture_time(img):
	try:
		exif = {
			ExifTags.TAGS[k]: v
			for k, v in img._getexif().items()
			if k in ExifTags.TAGS
		}
		return exif["DateTimeOriginal"]
	except:
		return "Time unknown"

#--- Program Start ---#

if len(sys.argv) < 3:
	print 'Usage:'
	print sys.argv[0] + ' <source_dir> <destination_dir>'
	sys.exit(1)

sourceBaseDir = sys.argv[1]
destBaseDir = sys.argv[2]

for dirpath, dirnames, filenames in os.walk("."):
    for excludeDir in excludeDirs:
	if excludeDir in dirnames:
		dirnames.remove(excludeDir)

    sourceDir = os.path.join(sourceBaseDir, dirpath)
    destDir = os.path.join(destBaseDir, dirpath)

    #for filename in [f for f in filenames if f.endswith(".jpg") or f.endswith(".JPG") or f.endswith(".jpeg")]:

    firstTime = True
    for filename in filenames:
	if isImage(filename):
		sourceFile = os.path.join(sourceDir,filename)
		destFile = os.path.join(destDir,filename)
		try:
			if firstTime:
				#mkdir_p(destDir)
				firstTime = False
			#copy2(sourceFile, destFile)
			img = Image.open(sourceFile)
			print '>>> ' + sourceFile
			print str(imagehash.phash(img))

			file_size = get_file_size(sourceFile)
			image_size = get_image_size(img)
			capture_time = get_capture_time(img)
			print file_size, image_size, capture_time
			print '<<<'
		except:
			print 'Error : |' + sourceFile + '|'
			raise
