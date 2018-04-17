from pydub import AudioSegment
import wave
import contextlib

def addToSong():
    fname = 'mySong.wav'
    with contextlib.closing(wave.open(fname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        currentSongLength = frames / float(rate)

    fname = 'recoredSong.wav'
    with contextlib.closing(wave.open(fname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        trackLength = frames / float(rate)

    sound1 = AudioSegment.from_file("mySong.wav")
    ####CHANGE TO localizedSong.wav when covfefe is working
    sound2 = AudioSegment.from_file("recoredSong.wav")

    if(currentSongLength > trackLength):
        combined = sound2.overlay(sound1)
    else:
        combined = sound1.overlay(sound2)

    combined.export("mySong.wav", format='wav')
