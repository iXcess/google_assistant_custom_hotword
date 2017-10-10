# google_assistant_custom_hotword
This documentation utilises snowboy's trained and locally stored ASR(Automatic Speech Recogniton) on raspberry pi as custom wakeword for the AIY HAT Google Assistant. It uses the button trigger method on raspberry pi GPIO pin 23.

<h1>What is snowboy?</h1>

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


