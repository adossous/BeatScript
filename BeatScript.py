from mido import MidiFile, MidiTrack, Message, MetaMessage, bpm2tempo

BPM = 131           # tempo of That's What You Get by Paramore
STEPS = 12
BARS = 12
VELOCITY = 110
# key = instrument name, value = list of 12 steps
# 1 = hit, 0 = silence
intro_pattern = {
    "kick":       [1,0,0, 0,1,0, 0,0,1, 0,0,0],
    "snare":      [0,0,0, 1,0,0, 0,0,0, 1,0,0],
    "hihat":      [1,0,1, 1,0,1, 1,0,1, 1,0,1],
    "open_hihat": [0,0,0, 0,0,0, 0,0,0, 0,0,1],
}

verse_pattern = {
    "kick":       [1,0,0, 1,0,0, 0,0,1, 0,0,0],
    "snare":      [0,0,0, 0,0,0, 0,0,0, 1,0,0],
    "hihat":      [1,1,1, 1,1,1, 1,1,1, 1,1,1],
    "foot_hihat": [1,0,0, 0,0,0, 1,0,0, 0,0,0],
}

chorus_pattern = {
    "kick":       [1,0,0, 1,0,0, 1,0,0, 0,0,0],
    "snare":      [0,0,0, 1,0,0, 0,0,0, 1,0,0],
    "hihat":      [1,1,1, 1,1,1, 1,1,1, 1,1,0],
    "open_hihat": [0,0,0, 0,0,0, 0,0,0, 0,0,1],
    "crash": [1,0,0, 0,0,0, 0,0,0, 0,0,0],
    "floor_tom": [0,0,0, 0,0,0, 0,0,0, 0,0,1],
}

note_map = {                                        #MIDI Note Map
    "kick":  36,                                   # Translates drum names into MIDI note numbers
    "snare": 38,                                   # These universal across every DAW
    "hihat": 42,
    "open_hihat": 46,
    "foot_hihat": 44,
    "crash": 49,
    "floor_tom": 43
}
# Returns the correct pattern based on which bar we are on
# bars 0-1 = intro, bars 2-4 = verse, bars 5-11 = chorus
def get_pattern(bar):
    if bar < 2:
        return intro_pattern
    elif bar < 5:
        return verse_pattern
    else:
        return chorus_pattern
# Create the MIDI file and a single track
mid = MidiFile(type=0, ticks_per_beat=480)
track = MidiTrack()
mid.tracks.append(track)
# Convert BPM into microseconds per beat (this is the format MIDI uses internally)
tempo = bpm2tempo(BPM)
track.append(MetaMessage('set_tempo', tempo=tempo, time=0))

ticks_per_step = mid.ticks_per_beat // 4

for bar in range(BARS):
    beat_pattern = get_pattern(bar)
    for step in range(STEPS):
        hits = []

        for drum, pattern in beat_pattern.items():
            if pattern[step] == 1:
                hits.append(drum)

        for i, drum in enumerate(hits):
            time = ticks_per_step if i == 0 else 0
            track.append(Message('note_on', channel=9, note=note_map[drum],
                                 velocity=VELOCITY, time=time))

        for i, drum in enumerate(hits):
            time = 10 if i == 0 else 0
            track.append(Message('note_off', channel=9, note=note_map[drum],
                                 velocity=0, time=time))

        if not hits:
            track.append(Message('note_on', channel=9, note=36,
                                 velocity=0, time=ticks_per_step))

mid.save("ThatsWhatYouGet.mid")
print("Beat saved as ThatsWhatYouGet.mid!")