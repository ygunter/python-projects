#pythonstartup.py

#Use an OS call to clear the interpreter screen
class cls(object):
    def _repr_(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        return ''
    
    cls = cls()