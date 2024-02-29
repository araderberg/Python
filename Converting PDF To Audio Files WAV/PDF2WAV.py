###Program Name: PDF2WAV.py
###Programmer: Aaliyah Raderberg
###Class: Converting PDF To Audio Files (Python)

##save each page's speech to a WAV file with the appropriate filename.
##Then, it combines all audio segments into a single audio file and exports it as cv_audio.wav.
##Adjust the settings of pyttsx3 according to your preferences.

import pyttsx3
from PyPDF2 import PdfReader
from pydub import AudioSegment

def pdf_to_audio(pdf_path, output_audio_path):
    pdf_reader = PdfReader(pdf_path)
    speaker = pyttsx3.init()

    # Configure the speaker
    speaker.setProperty('voice', 'english')  # Example: 'english'
    speaker.setProperty('rate', 150)  # Example: 150 words per minute
    speaker.setProperty('volume', 1.0)  # Example: 1.0 full volume
    
    audio_segments = []

    for page_num in range(len(pdf_reader.pages)):
        text = pdf_reader.pages[page_num].extract_text()
        cleaned_text = text.strip().replace('\n', ' ')
        print(cleaned_text)
        output_filename = f'{page_num}.wav'
        speaker.save_to_file(cleaned_text, output_filename)  # Save each page's speech to a WAV file
        speaker.runAndWait()
        
        audio_segments.append(AudioSegment.from_wav(output_filename))  # Load the generated WAV file

    combined_audio = sum(audio_segments)  # Combine all audio segments
    combined_audio.export(output_audio_path, format="wav")  # Export the combined audio as a WAV file

    speaker.stop()

pdf_to_audio('Django_.pdf', 'pdf_audio.wav')
