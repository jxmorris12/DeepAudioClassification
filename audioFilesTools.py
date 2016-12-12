# -*- coding: utf-8 -*-
import eyed3

#Remove logs
eyed3.log.setLevel("ERROR")

loaded_files = {}

# Cache audio file data
def loadFile(filename):
  if filename not in loaded_files:
    loaded_files[filename] eyed3.load(filename)
  return loaded_files[filename]

def isMono(filename):
	audiofile = loadFile(filename)
	return audiofile.info.mode == 'Mono'

def getGenre(filename):
	audiofile = loadFile(filename)
	#No genre
	if not audiofile.tag.genre:
		return None
	else:
		return audiofile.tag.genre.name.encode('utf-8')



	