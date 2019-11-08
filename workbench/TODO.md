  VENUS:
1. test "serio" con relay reed per routing;
2. test "serio" con consumi in corrente e conseguente scelta se accettare alimentazione 8-15v ed inserire uno stabilizzatore a 5v, oppure accettare solo 5v
	e se il consumo lo richiede pensare ad una ventolina di raffreddamento;
3. progettare sch e pcb:
	rear-panel-board-bottom con connettori 4xAudio Jack, 2xUSB, 1xDC Power, power led, inverted polarity led, power switch
	rear-panel-board-top con connettori 2xMIDI, 1xPS2
4. progettare pcb mainboard con connettore RPi, connettore switchbank, logica routing, logica midi in/out, stabilizzatore 5v;



TODO
----
	- Unbundle one-by-one the functionalities from the original samplerbox.py, study them and recode into separate software modules.

	musicalBOX "Venus":
	- Plan hardware for future features (MIDI In-Out circuit, Remote Controller Port)
    - Add RPi-Output/External-Input In-Out Line Routing
	- Refactory Switch-Matrix

	musicalBOX "Mars":
	- Add Serial-MIDI

	musicalBOX "Jupiter":
	- Add MIDI-Out Messages on Program selection

	musicalBOX "Saturn":
	- Add Program with multiple Presets
	
	
The goals is my personal learning of python programming and my understanding of the technologies needed to plays audio samples on RaspberryPi.



TODO
----
    - Functionalities definition and specifics.

    - Unbundle one-by-one the functionalities from the original samplerbox.py, study them and recode into separate software modules.

    Hardware:
	- Front/Rear Panel design.
	- Front Panel circuits schematic and pcb.
	- Rear Panel circuits schematic.
	- Audio Routing logic circuits schematic.
	- Main board (with Rear Panel, Audio Routing logic and RPi) schematic and pcb.

    Software:
    - Python project setup from original Samplerbox.
    - Switch/Led-Bank module.
    - Program configuration module.
    - Audio module.
    - Midi module.


	

------------------------------------------------------------------------------
REAR PANEL
------------------------------------------------------------------------------
Power: Power-Switch, Power-Jack
USB-Port: USB-1, USB-2
MIDI-Port: MIDI-In, MIDI-Out
Output: Out-1, Out-2, Out-3
Input: Aux
Remote: PS2-RemoteFootSwitch

------------------------------------------------------------------------------
FRONT PANEL
------------------------------------------------------------------------------
Programs: 2x8 Program Switch-Selector
Routing: 3 LineOut Mutually-Inclusive-Switch-Selector (Output: 1,2,3), 2 Source Mutually-Exclusive-Switch-Selector (Source: INTernal,EXTernal)
Controls: ProgramStore Switch

    - Red LED on audio/midi/configuration/samples problems.
    - Green LED for Power-On and Program setting indicators.
    - Blu LED for Program storing activity.
------------------------------------------------------------------------------
DEFINITIONS
------------------------------------------------------------------------------
Program: 1 Preset, 1 LineIn, n LineOut, 1 NextProgram

program.position: [0-15]
program.name: <alpha-numeric>
program.source: [0,1]
program.preset: [0-15] se input=[0], [nnn] midi program change se input=[1]
program.output: [1,2,3]

programs.cfg
[
    {
        "position": N
      , "name": "Program N"
      , "source": 0
      , "preset": 14
      , "output": [1,2]
    },
    ...
]
------------------------------------------------------------------------------



Modalità di programmazione di un program
----------------------------------------
1. selezione del program position: 0-15;
2. selezione del source: INTernal, EXTernal (Line, Aux);
	se source=INTernal (Line):
	3.1 selezione del preset: 0-15, utilizzando i 2x8 preset-switch-bank;
	se source=EXTernal (Aux):
	3.2 selezione del preset "remoto" mediante selezione del bank: + (switch0), - (switch8) e del program: + (switch1), - (switch9)
3. selezione del Output: 1-3;
4. store.


todo
----
- circuito main-board con connettori, midi-in/usb sovrapposti e routing via relays:
	midi in-out;
	power jack + switch;
	IN/OUT + routing;
	USB + PS2;
- modulo python driver switchbank;
- modulo python driver signal-routing;
- changelog modifiche samplerbox.py originale;
