# Proposal

## What will (likely) be the title of your project?

Midi 

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

A python program beat generator that lets you create a music beat.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

My project will function as a drum beat generator which operates through Python programming to transform user-created percussion patterns into MIDI files that professional music production software such as Logic Pro can use. The software works by representing drum patterns as Python dictionaries, where each key is an instrument name such as kick, snare, or hi-hat, and each value is a list of 16 steps containing either a 1 for a hit or a 0 for silence, mimicking the exact grid system used by real drum machines. The program features multiple sections, a verse and a chorus, each with their own distinct pattern that is selected dynamically using a function as the beat progresses through 8 bars. The mido library converts BPM values into MIDI ticks to handle timing, which enables the exported file to maintain correct playback speed across all digital audio workstations. The project will be executed by running the Python script from the terminal, which generates a .mid file that can be dragged directly into Logic Pro and played back through a drum instrument plugin. 
## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?
N/A


## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

N/A

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

That I successfully generate a MIDI file using Python and get it to play back in Logic Pro as a drum beat.

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

That I successfully generate a MIDI file from Python code that includes multiple drum instruments like kick, snare, and hi-hat playing together as a cohesive beat at the correct tempo.
### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

That I successfully generate a multi-section MIDI drum beat from Python code that attempts to replicate the drum line of a real song, with different patterns for different sections of the song, and that it plays back accurately in Logic Pro through a drum instrument plugin.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

My first step will be researching how MIDI files are structured and what Python libraries are available to create them. The mido library will be my main focus because my initial research shows that this library provides beginner-friendly documentation for MIDI file creation and export functions. I need to learn how to install third-party libraries through pip because this process has not been fully explained to us during class sessions. I need to learn how MIDI transmits musical data which includes understanding how note numbers and velocity and timing functions operate because this concept is completely new to me except for my knowledge of Python. I need to study how drum machines use grids of on and off steps to show beats because this information will help me create that same pattern in Python through dictionary and list data structures. I need to learn how to import a MIDI file into a project on Logic Pro and assign it to a drum instrument because this task requires me to explore the software independently. I expect my main challenge to involve timing mathematics because I must convert BPM into the MIDI internal tick-based system which requires extensive research and testing. The project requires me to learn a new library and study a new file format while using my Python coding skills to create a real-world artistic product which exceeds our classroom instruction.
