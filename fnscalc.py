print("flipnote length calculator version 0.0.1 \n developed by NoodleGuy64 with the help of bigminiboss on replit.com \n this program is licensed under the CC-BY-SA 4.0 license by Creative Commons.")
frames = input("How many frames is the flipnote (no larger than 999)?\n")
if float(frames) == "":
  print("Do not enter string text.")
if float(frames) > 999:
	print("Invalid.")
if float(frames) < 1:
	print("Invalid.")
fps = float(input("Choose a flipnote speed from 1-8\n"))
if float(fps) > 8:
  print("Choose a number between 1 and 8\n")
if float(fps) < 1:
  print("Choose a number between 1 and 8\n")

# conversion of flipnote speed to frames per second
if fps == 1:
  fps = 0.5
if fps == 2:
  fps = 1
if fps == 3:
  fps = 2
if fps == 4:
  fps = 4
if fps == 5:
  fps = 6
if fps == 6:
  fps = 12
if fps  == 7:
  fps = 20
if fps == 8:
  fps = 30
flipnoteLength = float(frames) / float(fps)

if float(flipnoteLength) > 60:
	flipnoteLength = flipnoteLength / 60
	print("Flipnote is", flipnoteLength, "minutes long.")
else:
	print("Flipnote is", flipnoteLength, "seconds long.")
