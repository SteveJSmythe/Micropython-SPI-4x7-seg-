from microbit import *
spi.init(baudrate=1000000,bits=8,mode=0, sclk=pin13, mosi=pin15, miso=pin14) #setup SPI
# initialisation code

pin0.write_digital(0)
spi.write(b'\x0f\x00')#enable normal mode (disable test mode)
pin0.write_digital(1) #latch data
sleep(300)

# zero-out all registers
for cmd in range(16):
    pin0.write_digital(0)
    packet = cmd << 8
    # e.g., if cmd is 0101, 0101 << 8 becomes 010100000000
    spi.write(bytearray(packet))
    pin0.write_digital(1)

# set some essential parameters
pin0.write_digital(0)
spi.write(bytearray([0x09,0x00])) #enable no decode
pin0.write_digital(1)

pin0.write_digital(0)
spi.write(bytearray([0x0b,0x07])) #enable 8 cols
pin0.write_digital(1)

pin0.write_digital(0)
spi.write(bytearray([0x0c,0x01])) # enable shutdown register
pin0.write_digital(1)


# set intensity
pin0.write_digital(0)
spi.write(b'\x0a\x0f')# set intensity to 15 (max)
pin0.write_digital(1) #latch data

# dictionary of bit patterns
# n.b. decimal point can be added to any character by adding 128 to its decimal value
DIGITS = {
    ' ': 0,
    '-': 1,
    '_': 8,
    '\'': 2,
    '0': 126,
    '1': 48,
    '2': 109,
    '3': 121,
    '4': 51,
    '5': 91,
    '6': 95,
    '7': 112,
    '8': 127,
    '9': 123,
    'a': 125,
    'b': 31,
    'c': 13,
    'd': 61,
    'e': 111,
    'f': 71,
    'g': 123,
    'h': 23,
    'i': 16,
    'j' : 24,
    # 'k' Can't represent
    'l': 6,
    # 'm' Can't represent
    'n': 21,
    'o': 29,
    'p': 103,
    'q': 115,
    'r': 5,
    's': 91,
    't': 15,
    'u': 28,
    'v': 28,
    # 'w' Can't represent
    # 'x' Can't represent
    'y': 59,
    'z': 109,
    'A': 119,
    'B': 127,
    'C': 78,
    'D': 126,
    'E': 79,
    'F': 71,
    'G': 94,
    'H': 55,
    'I': 48,
    'J': 56,
    # 'K' Can't represent
    'L': 14,
    # 'M' Can't represent
    'N': 118,
    'O': 126,
    'P': 103,
    'Q': 115,
    'R': 70,
    'S': 91,
    'T': 15,
    'U': 62,
    'V': 62,
    # 'W' Can't represent
    # 'X' Can't represent
    'Y': 59,
    'Z': 109,
    ',': 128,
    '.': 128,
    '!': 176,
}

def write_segs(col,char): # turn on the relevant segments
    pin0.write_digital(0)
    spi.write(bytearray([col,char]))
    pin0.write_digital(1) #latch data

def letter(charx): # Look up character in DIGITS dictionary & return
    value = DIGITS.get(str(charx))
    return value

def blank_cols(): # blank out all columns
 for col in range(8):
  pin0.write_digital(0)
  spi.write(bytearray([col+1,0x00])) # range is 0-7, cols are 1-8!
  pin0.write_digital(1)
 
def write_str(disp_str): #
 len_str=len(disp_str) # find length of string
 if len_str>8:
  len_str=8 #truncate if too long for display
 c=len_str #start column
 for x in range(len_str):
  n=disp_str[x]
  write_segs(c,letter(n))
  c-=1 #Next (i.e. previous) COLUMN
  
################################################################ now send some stuff to the display!
while True:
    blank_cols() # blank all columns
    write_str('Hello  ') # write another string
    sleep(2000)
    write_str('there  ') #write a string
    sleep(2000)
    for displ_count in range(1,500): #count up from 0 to 500
        write_str("{0:0=8d}".format(displ_count)) #turn into 8-digit str with leading spaces#  
