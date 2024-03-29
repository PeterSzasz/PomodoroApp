# time handling for pomodoro

import time
import simpleaudio

class PomodoTimer():

    def minToMSec(self, min):
        return min * 60 * 1000
    
    def minToSec(self, min):
        return min * 60

    def __init__(self):
        super().__init__()
        self.paused = True
        self.elapsed_time = 0
        self.last_update = 0
        self.states = [ {'STOPPED':99.99},
                        {'RUN1':15},
                        {'BREAK1':5},
                        {'RUN2':15},
                        {'BREAK2':5},
                        {'RUN3':15},
                        {'LONGBREAK':25}
                      ]
        self.state = self.states[0]

        #audio objects
        self.start_sound = simpleaudio.WaveObject.from_wave_file('sound/start.wav')
        self.stop_sound = simpleaudio.WaveObject.from_wave_file('sound/stop.wav')
        self.break_sound = simpleaudio.WaveObject.from_wave_file('sound/break.wav')
        self.pause_sound = simpleaudio.WaveObject.from_wave_file('sound/pause.wav')

    def getElapsedTime(self):
        return self.elapsed_time

    def getEndTime(self):
        return self.minToSec(list(self.state.values())[0])

    def pause(self):
        self.paused = not self.paused
        self.pause_sound.play()

    def start(self, state = None):
        self.start_sound.play()
        self.last_update = time.time()
        self.paused = False
        if not state:
            self.state = self.states[1]
        else:
            self.state = state

    def stop(self):
        self.state = self.states[0]
        self.elapsed_time = 0
        self.paused = True
        self.stop_sound.play()

    def getNormalizedElapsed(self):
        '''elapsed time on a 0.0 to 1.0 scale'''
        return self.elapsed_time / self.minToSec(list(self.state.values())[0])

    def update(self):
        print(self.elapsed_time)
        if not self.paused:
            time_diff = time.time() - self.last_update
            self.elapsed_time += time_diff
            self.last_update = time.time()
        else:
            self.last_update = time.time()

        if self.elapsed_time >= self.minToSec(list(self.state.values())[0]):
            index = self.states.index(self.state)
            if index + 1 >= len(self.states):
                self.state = self.states[1]
            else:
                self.state = self.states[index + 1]
            self.elapsed_time = 0
            self.break_sound.play()


if __name__ == "__main__":
    pt = PomodoTimer()
    print('initialized')
    pt.start()
    print('started')
    pt.update()
    pt.update()
    pt.update()
    pt.update()
    pt.update()
    #while list(pt.state.keys())[0] != 'RUN2':
    while True:
        pt.update()
        print(str(pt.state))
        time.sleep(0.2)
    pt.update()
    pt.pause()
    print('paused')
    pt.update()
    pt.pause()
    print('paused')
    pt.update()
    pt.update()
    pt.stop()
    print('stopped')
