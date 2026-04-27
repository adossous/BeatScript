from mido import MidiFile, MidiTrack, Message, MetaMessage, bpm2tempo

BPM = 105     #tempo of Rolling In The Deep By Adele
VELOCITY = 100
STEPS = 16  # 4/4 throughout — always 16 sixteenth-note steps
 # drum patterns
verse_pattern = {
    "kick":       [1,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0],
    "snare":      [0,0,0,0, 1,0,0,0, 0,0,0,0, 1,0,0,0],
    "hihat":      [1,0,1,0, 1,0,1,0, 1,0,1,0, 1,0,1,0],
}

pre_chorus_pattern = {
    "kick":       [1,0,0,1, 0,0,1,0, 1,0,0,1, 0,0,0,0],
    "snare":      [0,0,0,0, 1,0,0,0, 0,0,0,0, 1,0,0,0],
    "hihat":      [1,0,1,0, 1,0,1,0, 1,0,1,0, 1,0,1,0],
}

chorus_pattern = {
    "crash":      [1,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
    "kick":       [1,0,0,1, 0,0,1,0, 1,0,0,1, 0,0,1,0],
    "snare":      [0,0,0,0, 1,0,0,0, 0,0,0,0, 1,0,0,0],
    "hihat":      [1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,0],
    "open_hihat": [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,1],
}

bridge_pattern = {
    "snare":      [0,0,0,0, 1,0,0,0, 0,0,0,0, 1,0,0,0],
}

breakdown_pattern = {
    "snare":      [1,0,0,0, 1,0,0,0, 1,0,0,0, 1,0,0,0],
}

outro_pattern = {
    "kick":       [1,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0],
    "snare":      [0,0,0,0, 1,0,0,0, 0,0,0,0, 1,0,0,0],
    "hihat":      [1,0,1,0, 1,0,1,0, 1,0,1,0, 1,0,0,0],
    "open_hihat": [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,1,0],
}
# Universal Midi note map
note_map = {
    "kick":       36,
    "snare":      38,
    "hihat":      42,
    "open_hihat": 46,
    "foot_hihat": 44,
    "crash":      49,
    "floor_tom":  43,
}
#song structure
# (start_bar, end_bar_exclusive, pattern)
sections = [
    (0,   4,  verse_pattern),
    (4,   6,  pre_chorus_pattern),
    (6,   10, chorus_pattern),
    (10,  14, verse_pattern),
    (14,  16, pre_chorus_pattern),
    (16,  20, chorus_pattern),
    (20,  22, bridge_pattern),
    (22,  24, breakdown_pattern),
    (24,  28, chorus_pattern),
    (28,  32, outro_pattern),
]

def get_pattern(bar):
    for start, end, pattern in sections:
        if start <= bar < end:
            return pattern
    return verse_pattern

#MIDI File setup
mid = MidiFile(type=0, ticks_per_beat=480)
track = MidiTrack()
mid.tracks.append(track)

tempo = bpm2tempo(BPM)
track.append(MetaMessage('set_tempo', tempo=tempo, time=0))
#timing match
ticks_per_step = mid.ticks_per_beat // 4   # 120 ticks per 16th note
note_duration  = ticks_per_step - 10       # notes ring for 110 ticks

TOTAL_BARS = 32

for bar in range(TOTAL_BARS):
    beat_pattern = get_pattern(bar)

    # Build event list for this bar: (abs_tick, 'on'/'off', note, vel)
    events = []
    for step in range(STEPS):
        for drum, pattern in beat_pattern.items():
            if pattern[step] == 1:
                abs_tick = step * ticks_per_step
                note = note_map[drum]
                events.append((abs_tick,                 'on',  note, VELOCITY))
                events.append((abs_tick + note_duration, 'off', note, 0))

    # Sorting drum events
    events.sort(key=lambda e: (e[0], 0 if e[1] == 'on' else 1))

    # Convert absolute ticks to delta ticks and write to track
    prev_tick = 0
    for abs_tick, kind, note, vel in events:
        delta = abs_tick - prev_tick
        if kind == 'on':
            track.append(Message('note_on',  channel=9, note=note, velocity=vel, time=delta))
        else:                                  #channel=9 is the standard midi drum channel
            track.append(Message('note_off', channel=9, note=note, velocity=0,   time=delta))
        prev_tick = abs_tick

    # Advance to end of bar
    bar_end = STEPS * ticks_per_step
    track.append(Message('note_off', channel=9, note=36, velocity=0,
                         time=bar_end - prev_tick))

mid.save("RollingInTheDeep.mid")
print("Beat saved as RollingInTheDeep.mid!")
print("Beat saved as ThatsWhatYouGet.mid!")
