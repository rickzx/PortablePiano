class Note(object):
    def __init__(self, note,pitch, time, duration):
        self.note = note
        self.time = time
        self.duration = duration
        self.x = 400
        self.putBars(note)
        self.pitch = pitch
        
    def putBars(self, note):
        if (note == "c3" or note == "c#3"):
            self.y = 228+18
           
        elif (note == "d3" or note == "d#3"):
            self.y = 228
            
        elif (note == "e3"):
            self.y = 210
           
        elif (note == "f3" or note == "f#3"):
            self.y = 191
            
        elif (note == "g3" or note == "g#3"):
            self.y = 191-18
            
        elif (note == "a3" or note == "a#3"):
            self.y = 155
            
        elif (note == "b3"):
            self.y = 155-18
           
        elif (note == "c4" or note == "c#4"):
            
            self.y = 123
            
        elif (note == "d4" or note == "d#4"):
           
            self.y = 123-18
            
        elif (note == "e4"):
           
            self.y = 87
           
        elif (note == "f4" or note == "f#4"):
            
            self.y = 87-18
            
        elif (note == "g4" or note == "g#4"):
            
            self.y = 87-36
            
        elif (note == "a4" or note == "a#4"):
           
            self.y = 87-36
            
        elif (note == "b4"):
           
            self.y = 87-36 
           