# Google Assistant Custom Wakeword
This documentation utilises snowboy's trained and locally stored ASR(Automatic Speech Recogniton) on raspberry pi as <strong>custom wakeword</strong> for the <strong>AIY HAT Google Assistant</strong>. It uses the <strong>button trigger method</strong> on raspberry pi GPIO pin 23.

<h3>What is snowboy?</h3>

Introduction
Snowboy is an highly customizable hotword detection engine that is embedded real-time and is always listening (even when off-line) compatible with Raspberry Pi, (Ubuntu) Linux, and Mac OS X.

A hotword (also known as wake word or trigger word) is a keyword or phrase that the computer constantly listens for as a signal to trigger other actions.

Some examples of hotword include “Alexa” on Amazon Echo, “OK Google” on some Android devices and “Hey Siri” on iPhones. These hotwords are used to initiate a full-fledged speech interaction interface. However, hotwords can be used in other ways too like performing simple command & control actions.

In one hacky solution, one can run a full ASR (Automatic Speech Recognition) to perform hotword detection. In this scenario, the device would watch for specific trigger words in the ASR transcriptions. However, ASR consumes a lot of device and bandwidth resources. In addition, it does not protect your privacy when one uses a cloud-based solution. Luckily, Snowboy was created to solve these problems!

Snowboy is:

1. Highly customizable allowing you to freely define your own magic hotword such as (but not limited to) “open sesame”, “garage door open”, or “hello dreamhouse”. If you can think it, you can hotword it!
2. Always listening but protects your privacy because Snowboy does not connect to the Internet or stream your voice anywhere.
3. Light-weight and embedded allowing you to runs it on Raspberry Pi’s consuming less than 10% CPU on the smallest Pi’s (single-core 700M Hz ARMv6).
4. Apache licensed!

Ref website: http://docs.kitt.ai/snowboy/

I assume you have a working Google Assistant from the AIY project. If not, please visit https://github.com/google/aiyprojects-raspbian/blob/master/HACKING.md for installation.

<h4>Steps</h4> 

1. <code>sudo apt-get install python-pyaudio python3-pyaudio sox</code> 

2. <code>pip install pyaudio</code> , if you do not have pip installed, refer https://pip.pypa.io/en/stable/installing/

3. Test record your audio with <code>rec temp.wav</code> and then play it with <code>aplay temp.wav</code> and make sure there is sound output.

4. <code>wget https://s3-us-west-2.amazonaws.com/snowboy/snowboy-releases/rpi-arm-raspbian-8.0-1.1.1.tar.bz2</code>

5. <code>tar zxvf <the downloaded file></code>
  
6. Create a custom hotword of your choice in snowboy and download the .pmdl file into the same directory.

7. <code>git clone https://github.com/iXcess/google_assistant_custom_hotword</code>

8. Move the .asoundrc file to home directory and the trigger_ga.py to the same directory as the .pmdl file.

9. Use a male-to-male jumper wire to connect raspberry pi GPIO pin 23 to GND.

10. Run the python script with <code>python2 trigger_ga.py <your .pmdl file here></code>. Then run <code>python3 /home/pi/voice-recognizer-raspi/src/main.py</code>.

11. Test it out with your custom wake word.
  
<h4>Misc</h4>

This method works because we have editted the .asoundrc to let both google assistant and snowboy to use the same audio output with dsnoop. Please keep in mind that snowboy is written in python 2 while google assistant is written in python 3.



