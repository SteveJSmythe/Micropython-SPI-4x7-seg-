# Micropython-SPI-4x7-seg-
Micropython code for driving DSP-7S04 HW SPI 4 x 7-seg display (BBC micro:bit)
Connecting things up
This is very straightforward. The display has five pins. Apart from VCC and GND (it's 3.3v-friendly), there is DIN (data in), CS (chip select) and CLK (clock). As it is an SPI device, the default connections on the micro:bit are CLK=P13 and DIN=P14 (although these are just the defaults - you can use any pins). In addition, you'll need to connect CS to any micro:bit pin (I used P0).
