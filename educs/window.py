import pygame

class Window(pygame.window.Window):

    def __init__(self, batch, *args, **kwargs):
        self._batch = batch
        super().__init__(*args, **kwargs)

    @property
    def batch(self):
        return self._batch

    @batch.setter
    def batch(self, b):
        self._batch = b