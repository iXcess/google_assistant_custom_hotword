








import snowboydecoder
import sys
import signal
from light import Light

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.6)
print('Listening... Press Ctrl+C to exit')

led = Light(23)
detector.start(detected_callback=led.blink,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)

detector.terminate()
