import speech_recognition as sr

def transcribe_wavefile(filename, language='en'):
    '''
    Use sr.Recognizer.AudioFile(filename) as the source,
    recognize from that source,
    and return the recognized text.
    
    @params:
    filename (str) - the filename from which to read the audio
    language (str) - the language of the audio (optional; default is English)
    
    @returns:
    text (str) - the recognized speech
    '''
    #raise RuntimeError("FAIL!!  You need to change this function so it works!")
    r = sr.Recognizer()
    
    with sr.AudioFile(filename) as source:
        audio = r.record(source)
        text = r.recoggnize_google(audio,languang=languang)

    return text

   
    
