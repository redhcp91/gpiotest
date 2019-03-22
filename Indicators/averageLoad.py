
from gpiozero import LEDBarGraph, LoadAverage
from signal import pause

la = LoadAverage(min_load_average=0, max_load_average=2)
graph = LEDBarGraph(4, 17, 27, 22, pwm=True)

graph.source = la

pause()
