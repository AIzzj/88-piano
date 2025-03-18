from src.core.keyboard_handler import KeyboardHandler
from loguru import logger

if __name__ == '__main__':
    try:
        logger.info('Starting Piano App')
        handler = KeyboardHandler()
        handler.start_listening()
        input('Press Enter to exit...\n')
    except KeyboardInterrupt:
        logger.info('Application shutdown')