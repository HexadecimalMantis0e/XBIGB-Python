import os
import struct
import argparse

# handle chunks
def parsechunk(chunk, outfile):
    print "Dumping " + outfile + "...\n"
    f1 = open(outfile, "wb")
    filebytes = f.read(chunk)
    f1.write(filebytes)
    f1.close()
        
        
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

f = open(args.filename,"r+b")
magic = f.read(0x04)
if magic != "BIGB":
    raise ValueError("Incorrect header")

start = struct.unpack('i', f.read(4))[0]

start += 0x0c

# Gather chunk info
f.seek(0x78, os.SEEK_SET)
dumpUC00 = struct.unpack('i', f.read(4))[0]
f.seek(0x7c, os.SEEK_SET)
dumpUC01 = struct.unpack('i', f.read(4))[0]
f.seek(0x80, os.SEEK_SET)
dump00 = struct.unpack('i', f.read(4))[0]
f.seek(0x84, os.SEEK_SET)
dump01 = struct.unpack('i', f.read(4))[0]
f.seek(0x88, os.SEEK_SET)
dump02 = struct.unpack('i', f.read(4))[0]

f.seek(start, os.SEEK_SET)
parsechunk(dump00,"dump00.bin")
parsechunk(dump01,"dump01.bin")
parsechunk(dump02,"dump02.bin")

if dumpUC00 != 0x00:
    byte = 0x00

    while byte == 0x00:
        byte = struct.unpack("b",f.read(1))[0]

    f.seek(-0x01, os.SEEK_CUR)
    parsechunk(dumpUC00,"dumpUC00.bin")

    
if dumpUC01 != 0x00:
    byte = 0x00

    while byte == 0x00:
        byte = struct.unpack("b",f.read(1))[0]

    f.seek(-0x01, os.SEEK_CUR)
    parsechunk(dumpUC01,"dumpUC01.bin")
    
f.close()
