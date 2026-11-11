"""Draw the Box Breath icon as PNG files using only the standard library."""
import struct, sys, zlib
from pathlib import Path

BG, FILL, INK, DOT = (14, 42, 59), (29, 90, 99), (244, 249, 251), (127, 224, 199)

def rrect(x, y, x0, y0, x1, y1, r):
    cx = min(max(x, x0 + r), x1 - r); cy = min(max(y, y0 + r), y1 - r)
    return (x - cx) ** 2 + (y - cy) ** 2 <= r * r if (x < x0 + r or x > x1 - r) and (y < y0 + r or y > y1 - r) else x0 <= x <= x1 and y0 <= y <= y1

def color(u, v):  # u, v in 0..512 design units
    d2 = (u - 136) ** 2 + (v - 376) ** 2
    if d2 <= 34 ** 2: return DOT
    if d2 <= 44 ** 2: return INK
    if rrect(u, v, 127, 127, 385, 385, 45):
        return FILL if rrect(u, v, 145, 145, 367, 367, 27) else INK
    return BG

def png(size, path, ss=3):
    rows = bytearray()
    for y in range(size):
        rows.append(0)
        for x in range(size):
            acc = [0, 0, 0]
            for sy in range(ss):
                for sx in range(ss):
                    c = color((x + (sx + .5) / ss) * 512 / size, (y + (sy + .5) / ss) * 512 / size)
                    acc[0] += c[0]; acc[1] += c[1]; acc[2] += c[2]
            rows += bytes(a // (ss * ss) for a in acc)
    def chunk(t, d): return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    Path(path).write_bytes(b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(bytes(rows), 9)) + chunk(b'IEND', b''))

out = Path(sys.argv[1])
for s in (180, 192, 512, 1024):
    png(s, out / f'icon-{s}.png', ss=2 if s >= 512 else 3)
    print('wrote', s)
