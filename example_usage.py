from client import CFGTokenMaskGenerator

allowed = CFGTokenMaskGenerator.get_allowed_next("START")
print("Allowed initial tokens:", allowed)
next_st = CFGTokenMaskGenerator.transition("START", "{")
print("Next state after '{':", next_st)
