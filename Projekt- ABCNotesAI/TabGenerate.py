from textgenrnn import textgenrnn

textgen.train_from_file('WhatIsBass.txt', num_epochs=1)
textgen.generate()