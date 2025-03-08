class bird:
    def __init__(self):
        print("Bird is ready")
    def whoisthis(self):
        print('bird')
    def swim(self):
        print('swim faster')
class pg(bird):
    def __init__(self):
        super().__init__()
        print('pegunin is ready')
    def whoisthis(self):
        print('pegunin')
    def run(self):
        print('run faster')
peggy= pg()
peggy.whoisthis()
peggy.swim()
peggy.run()