# Hardware

You will need a supported AC and suitable ESPHome board. We'll describe both in this document.

## AC
The AC provides the signals via the CNS connector. We're not keeping a list of supported AC units here. It should work on at least the same AC units supported in other implementations like https://github.com/absalom-muc/MHI-AC-Ctrl/#prerequisites . It has been [reported](https://github.com/ginkage/MHI-AC-Ctrl-ESPHome/issues/196) (and [here](https://gathering.tweakers.net/forum/list_message/85326154) 🇳🇱) that this project also works on some models where other implementations have problems.

The CNS connector has 5 pins with a pitch of 2.5 mm. It is out of the [XH series from JST](http://www.jst-mfg.com/product/detail_e.php?series=277). The position of the connector is visible on the following photo of the AC indoor unit PCB.
![Indoor PCB](images/SRK-PCB.jpg)

The PCB of the remote control uses a pin connector out of [JST JQ series](https://jst.de/file/download/124/pitch-2-5-mm-btb-jq-pdf) also with a pitch of 2.5 mm. So the board can be directly plugged into the board of the AC.
 
It was not tested to directly plug the MHI-AC-Ctrl-ESP32-C3 into the AC unit. Instead, we recommend using an extender cable (called "4S balancer JST-XH extension cable" with one male and one female connector), e.g. https://www.aliexpress.com/item/1005003669930722.html. On the board, you can solder a cable, e.g. https://www.aliexpress.com/item/4000800420412.html. 

:warning: **Opening of the indoor unit should be done by a qualified professional because faulty handling may cause leakage of water, electric shock or fire!** :warning:. You can show that expert [this video](https://www.youtube.com/watch?v=PBVX02dmgYY) that describes how to open the unit.

## ESPHome boards

As described in the the [readme](README.md), this project officially supports the UAC and our DIY ESP32-C3 board. The AC provides 12V power and uses 5V levels for signals. 

### TinyTronics Universal Air Conditioning Controller
The [Universal Air Conditioning Controller](https://www.tinytronics.nl/en/development-boards/microcontroller-boards/with-wi-fi/universal-air-conditioning-controller-esp32-s3) + [JST cable](https://www.tinytronics.nl/en/cables-and-connectors/cables-and-adapters/jst-compatible/jst-xh-female-to-dupont-female-compatible-cable-5p-15cm) and soldering them together will be enough to get you going.

Note that board version < 1.3 is known for generating some rate of frame errors. Users [reported](https://github.com/ginkage/MHI-AC-Ctrl-ESPHome/issues/196) (and [here](https://gathering.tweakers.net/forum/list_message/85326154#85326154) 🇳🇱) it regardless works fine for them. This is because this project automatically retransmits commands when a frame error occurs. This issue has been fixed in version 1.3.

### DIY ESP32-C3 board

#### Schematic
![schematic](images/MHI-AC-Ctrl_Schematic.png)

#### PCB (KiCad)
<img src="images/PCB_top.PNG" width=450/>
<img src="images/PCB_bottom.PNG" width=450/>

You find the KiCad schematic and the layout in the [kicad folder](kicad). I used this KiCad project for the PCB order at [Aisler](https://aisler.net).


#### Bill of Materials
Part |Value            |Package                    |comment
---- | ----            |----                       |-----
C1   |22µ/25V          |E15-5 (axial)              |consider the polarity
C2, C3   |100n             |C025-024X044
U1   |[TSR_1-2450](https://www.aliexpress.com/item/1005004319529660.html)       |TSR-1                      |consider the polarity  <sup>1</sup>
U2  |[ESP-C3-32S(4M)-KIT](https://nl.aliexpress.com/item/1005002983050962.html)    |ESP-C3-32S(4M)-KIT              |consider the polarity
U3  |LEVEL-SHIFTER-4CH|LEVEL-SHIFTER-4CH          |consider the polarity
R1   | 12K        |                      | Optional <sup>2</sup>

The level shifter is required to convert the 5V signals from/to 3v3 the ESP uses. Skipping it could damage the ESP and might be too low for the AC. Note that the AC does not provide the SPI chip select signal. Old versions of the board had an internally generated loopback chip select signal looped back by connecting two GPIO pins. This is not used any more so it was removed from the board.

<sup>1</sup>According to the discussions [here](https://github.com/absalom-muc/MHI-AC-Ctrl/issues/102) and [here](https://github.com/absalom-muc/MHI-AC-Ctrl/issues/17) TSR 1-2450 can be replaced by TSR 1-2450E. That component converts the +12V to +5V. 

<sup>2</sup>The documentation of AI-Thinker says this one should be connected, though the USB-Serial chip already pulls this pin.

#### Assembled PCB
The following photos show the assembled PCB

<img src="images/Assembled-Board-top1.jpg" width=300/>
<img src="images/before-mount.jpg" width=300/>
<img src="images/Board-plugged.jpg" width=300/>
