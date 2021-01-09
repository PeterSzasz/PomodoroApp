# time handling for pomodoro

import time

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
        self.states = [{'STOPPED':0}, {'RUN1':4}, {'BREAK1':2}, {'RUN2':4}, {'BREAK2':2}, {'LONGBREAK':4}]
        self.state = self.states[0]

    def pause(self):
        self.paused = not self.paused

    def start(self, state = None):
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

    def update(self):
        print(self.elapsed_time)
        if not self.paused:
            time_diff = time.time() - self.last_update
            self.elapsed_time += time_diff
            self.last_update = time.time()
        else:
            self.last_update = time.time()

        #if self.elapsed_time >= self.minToSec(list(self.state.values())[0]):
        if self.elapsed_time >= list(self.state.values())[0]:
            index = self.states.index(self.state)
            if index + 1 >= len(self.states):
                self.state = self.states[1]
            else:
                self.state = self.states[index + 1]
            self.elapsed_time = 0
            print("next state: " + str(self.state))

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
