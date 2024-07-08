# Network Architecture and Management VoIP Project

## Overview
This project is an implementation of an Interactive Voice Response (IVR) system based on Voice over IP (VoIP) technology, using an Asterisk Private Branch Exchange (PBX). The system will support both voice and video calls.

## Objectives
- **Develop an IVR system**: Create a functional IVR system using Asterisk PBX that can handle multiple voice and video calls.
- **Interactive menu options**: Implement an IVR menu with options to get the current day of the week, play a Mastermind game, and retrieve the latest Totoloto key drawn.

## Architecture
The project utilizes the following architecture:
- **Asterisk PBX**: Running on a Linux machine, serving as the core component for call handling and IVR functionalities.
- **SIP Softphones**: Will be using Linphone app to make audio/video calls.

## IVR Menu Options
The IVR system includes a menu with the following options:
1. **Get the current day of the week (Press 1)**: Informs the caller of the current day and spells it out using the NATO phonetic alphabet.
2. **Play Mastermind (Press 2)**: A game where the user guesses a random two-digit number within eight tries, receiving feedback on the correctness of each guess.
3. **Get the last Totoloto key drawn (Press 3)**: Retrieves and announces the latest Totoloto key via web scraping.
4. **Hang up (Press 0)**: Ends the call.

## Configuration Files
- **`extensions.conf`**: Defines extension number contexts and their associations to telephones.
- **`sip.conf`**: Configures users/extensions to use.
- **`toto.py`**: Scraps the totoloto webpage for the last key draw and uses Asterisk's AGI to say the numbers.

## Implementation Details
Google TTS was used for most of the text to speech used.

Run Asterisk on your linux machine.

After modifying extensions.conf execute:
```sh
dialplan reload
```
To use the python script:
```sh
sudo chmod +x /home/mint/toto.py
```

Call 80859 extension to use the IVR.
