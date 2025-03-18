from pynput import keyboard
from loguru import logger
from .sound_engine import SoundEngine

class KeyboardHandler:
    from .config import Config

class KeyboardHandler:
    current_octave = CONFIG.BASE_OCTAVE


    def __init__(self):
        self.sound_engine = SoundEngine()
        self.listener = None
        logger.info('Keyboard handler initialized')

    def _on_press(self, key):
        try:
            if char := getattr(key, 'char', None):
                if note_base := CONFIG.KEY_MAPPING.get(char.lower()):
                    note = f"{note_base}{self.current_octave}"
                    self.sound_engine.play_note(note)
            elif octave_change := CONFIG.OCTAVE_KEYS.get(char):
                self.current_octave = max(0, min(8, self.current_octave + octave_change))
        except Exception as e:
            logger.error(f'Key press error: {e}')

    def _on_release(self, key):
        try:
            if char := getattr(key, 'char', None):
                if note_base := CONFIG.KEY_MAPPING.get(char.lower()):
                    note = f"{note_base}{self.current_octave}"
                    self.sound_engine.stop_note(note)
        except Exception as e:
            logger.error(f'Key release error: {e}')

    def start_listening(self):
        self.listener = keyboard.Listener(
            on_press=self._on_press,
            on_release=self._on_release
        )
        self.listener.start()
        logger.success('Keyboard listening started')