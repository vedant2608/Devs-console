try:

    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 190)
    intro = '''
    Hey there, I am Dev.
    I am here, to Give you the short intro of me.
    I am the assistant created as a project. Currently I am working only for windows. But very soon I will be available for linux too.
    If you stuck in somewhere you can run the help.py to get the help. I am a command line utility assistant build with python. 
    To run the assistant firstly please do read the readme.md file from the repository
    Start the assistant either by symbolic link or by running assistant.bat
    Hope you will have a good experience. 
    Any suggestions are welcome.
    '''
    print(f"\n\n{intro}")
    engine.say(intro)
    engine.runAndWait()
    engine.say("Starting Dev's console...")
    engine.runAndWait()
except Exception as e:
    intro = '''
    Hello, I am Dev.
    I am here, to Give you the short intro of me.
    I am the assistant created as a project by vedant. Currently I am working only for windows. But very soon I will be available for linux too.
    I am a command line utility assistant build with python. 
    To run the assistant firstly please do read the readme.md file from the repository
    Start the assistant either by symbolic link or by running assistant.bat
    Hope you will have a good experience. 
    Any suggestions are welcome.
    '''
    print(f"\n\n{intro}")
