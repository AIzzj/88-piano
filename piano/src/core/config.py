from dataclasses import dataclass, field

@dataclass
@dataclass
class Config:
    NOTE_NAMES: list = field(default_factory=lambda: ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'])
    KEY_MAPPING: dict = field(default_factory=lambda: {
        'a': 'C', 'w': 'C#',
        's': 'D', 'e': 'D#',
        'd': 'E',
        'f': 'F', 'r': 'F#',
        'g': 'G',
        'h': 'G#',
        'j': 'A',
        'k': 'A#',
        'l': 'B'
    })
    OCTAVE_KEYS: dict = field(default_factory=lambda: {'1': -1, '2': 0, '3': 1})
    BASE_OCTAVE: int = 4

CONFIG = Config()