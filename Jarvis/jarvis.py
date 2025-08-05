import sounddevice as sd
import wavio
import speech_recognition as sr

def takecommand() -> str:
    """Takes voice input using sounddevice and recognizes it."""
    fs = 44100  # Sample rate
    seconds = 5  # Duration of recording
    print("Listening... Speak now!")

    try:
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()
        wavio.write("input.wav", recording, fs, sampwidth=2)
        print("Recording saved.")

        # Use recognizer to convert speech to text
        r = sr.Recognizer()
        with sr.AudioFile("input.wav") as source:
            audio = r.record(source)
            print("Recognizing...")

            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            return query.lower()

    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return None
    except Exception as e:
        speak(f"An error occurred: {e}")
        print(f"Error: {e}")
        return None
