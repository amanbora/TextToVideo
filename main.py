import sys  
import os
import sel
import utils
import emotion
import nlp
import image
import music
import video
import exe

def main(filepath):  
        emotions = []
	if not os.path.isfile(filepath):
            print("File path does not exist. Exiting...".format(filepath))
	    sys.exit()
        # make it txt
	exe.run("xargs -n5 < " + filepath + " > temp.txt")
	filepath = "temp.txt"	
	with open(filepath) as fp:
            ln_count = 0;
            blob = []
            for line in fp:
                ln_count += 1
                if ln_count % 10 == 0:
                    emotions.append(emotion.get(blob))
                    blob = []
                else:
                    blob.append(unicode(line, "utf-8"))
		input = nlp.preprocess(line)
		input = utils.unique(input)
                print(input)
                sel.getImage(' '.join(input))
                image.join(line, ln_count)
        if len(blob) != 0:
            emotions.append(emotion.get(blob))
	print(emotions)
        mood = emotion.process(emotions)
        print(mood)
        song = music.getSong(mood)
        song = "./music/" + mood + "/" + song
        video.generate(song, "Awesomevideo", "mp4")
