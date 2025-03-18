import pygame
import numpy as np
from loguru import logger

class SoundEngine:
    NOTE_FREQUENCIES = {
        'C4': 261.63, 'C#4': 277.18, 'D4': 293.66, 'D#4': 311.13,
        'E4': 329.63, 'F4': 349.23, 'F#4': 369.99, 'G4': 392.00,
        'G#4': 415.30, 'A4': 440.00, 'A#4': 466.16, 'B4': 493.88
    }

    def __init__(self):
        pygame.mixer.init(frequency=44100, channels=2)
        self.sounds = {}
        self._create_waveforms()
        logger.success('Sound engine initialized')

    def _create_waveforms(self):
        sample_rate = 44100
        duration = 1  # 持续1秒（实际播放时控制）
        
        for note, freq in self.NOTE_FREQUENCIES.items():
            t = np.linspace(0, duration, int(sample_rate * duration), False)
            wave = 0.5 * np.sin(2 * np.pi * freq * t)
            stereo_wave = np.column_stack([wave, wave])
            sound = pygame.sndarray.make_sound((stereo_wave * 32767).astype(np.int16))
            self.sounds[note] = sound

    def play_note(self, note: str):
        if sound := self.sounds.get(note):
            sound.play(loops=-1)  # 循环播放直到停止
            logger.debug(f'Playing {note}')

    def stop_note(self, note: str):
        if sound := self.sounds.get(note):
            sound.stop()
            logger.debug(f'Stopped {note}')