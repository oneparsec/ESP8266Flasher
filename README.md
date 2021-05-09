# ESP8266Flasher
ESP8266 flash program based on PyQt5 and esptool

You can download this program from releases or build from source

## Build from source

You need git and python.

```git clone https://github.com/OneParsec/ESP8266Flasher``` Download source code

```cd ESP8266Flasher``` 

```pip install pyinstaller``` Install build instrument

```pyinstaller --onefile --noconsole --icon=icon.ico main.py``` Start build

## Table of ESP8266 flashing program
| Programs                   | Support Windows | Support Linux | Support MacOS   | GUI(Graphic interface) | More settings(like baud rate, flash size, etc.)                    | 
| ---------------------------|:---------------:| -------------:|:---------------:| ----------------------:| ------------------------------------------------------------------:|
| ESP8266 Flasher            | +               | +             | +               | +                      | +(baud rate,flash size,erase flash,flash mode)                     |
| N2D                        | +               | -             | -               | +                      | +(baud rate, flash mode)                                           |
| NodeMCU ESP8266 Programmer | +               | -             | -               | +                      | +(baud rate,flash speed,flash size,erase flash,flash mode)         |
| esptool                    | +               | +             | +               | -                      | +(baud rate,flash speed,flash size,erase flash,flash mode and more)|
| esptool-gui                | +               | +             | +               | +                      | +(baud rate)                                                       |
