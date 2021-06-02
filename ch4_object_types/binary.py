import struct

packed = struct.pack('>i4sh', 7, b'spam', 8)

print(packed)
