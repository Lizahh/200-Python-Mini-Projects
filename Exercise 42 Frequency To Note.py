# -*- coding: utf-8 -*-
"""

In the previous question you converted from note name to frequency. In this question
you will write a program that reverses that process. Begin by reading a frequency
from the user. If the frequency is within one Hertz of a value listed in the table in
the previous question then report the name of the note. Otherwise report that the
frequency does not correspond to a known note. In this exercise you only need to
consider the notes listed in the table. There is no need to consider notes from other
octaves.
"""

# Begin by reading a frequency from the user.
user_input = float(input("Please enter a frequency: "))

# In this exercise you only need to consider the notes listed in the table. There is no need to consider notes from other octaves.
freq_c4 = 440.00
freq_d4 = 493.88
freq_e4 = 261.63
freq_f4 = 293.66
freq_g4 = 329.63
freq_a4 = 349.23
freq_b4 = 392.00
set_limit = 1

# If the frequency is within one Hertz of a value listed in the table in the previous question then report the name of the note
if user_input >= freq_c4 - set_limit and user_input <= freq_c4 + set_limit:
  note = "C4"
elif user_input >= freq_d4 - set_limit and user_input <= freq_d4 + set_limit:
  note = "D4"
elif user_input >= freq_e4 - set_limit and user_input <= freq_e4 + set_limit:
  note = "E4"
elif user_input >= freq_f4 - set_limit and user_input <= freq_f4 + set_limit:
  note = "F4"
elif user_input >= freq_g4 - set_limit and user_input <= freq_g4 + set_limit:
  note = "G4"
elif user_input >= freq_a4 - set_limit and user_input <= freq_a4 + set_limit:
  note = "A4"
elif user_input >= freq_b4 - set_limit and user_input <= freq_b4 + set_limit:
  note = "B4"
else:
  note = ""

# Otherwise report that the frequency does not correspond to a known note
if note == "":
  print("No note corresponds to this frequency")
else:
  print("Note related to {} frequency is {}".format(user_input,note))

