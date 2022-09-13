import os
import sys
import binascii
import zlib

OUTPUT = 'puzzle'


def bin2hex(data):
    return binascii.b2a_hex(data)


def hex2bin(data):
    return binascii.a2b_hex(data)


def dec2bin(data, l=1):
    l = l / 2
    if l == 4:
        return hex2bin("%08x" % int(data))
    else:
        return hex2bin("%02x" % int(data))


def bin2dec(data):
    return int(bin2hex(data), 16)


def crc32(chunkType, chunkData):
    return dec2bin(binascii.crc32(chunkType + chunkData), 8)


def genIHDR(w, h):
    width = dec2bin(w, 8)
    height = dec2bin(h, 8)
    bits = dec2bin(8)
    color_type = dec2bin(2)
    compr_method = filter_method = interlace_method = dec2bin(0)
    chunkData = width+height+bits+color_type + \
        compr_method+filter_method+interlace_method
    res = dec2bin(len(chunkData), 8)+b'IHDR' + \
        chunkData+crc32(b'IHDR', chunkData)
    print([res])
    return res


def genIDAT(data):
    _c = zlib.crc32(b'IDAT'+data)
    if _c < 0:
        _c = ~_c ^ 0xffffffff
    _crc = dec2bin(_c, 8)
    return dec2bin(len(data), 8) + b'IDAT' + data + _crc


def merge_png(width, height, names, output="tmp.png"):
    header = hex2bin("89504E470D0A1A0A")
    ihdr = genIHDR(width, height)
    idat = []
    for name in names:
        f=open("%s/%s" % (OUTPUT, name),'rb')
        data = f.read()
        idat.append(genIDAT(data))
        f.close()
    idat = b''.join(idat)
    iend = hex2bin("00000000" + "49454E44" + "AE426082")
    with open(output, 'wb') as f:
        f.write(header+ihdr+idat+iend)


if __name__ == '__main__':
    fs = ["blczioav.data", "ciaoxptf.data", "csizrgxn.data", "dwelszrk.data", "fhnkotmb.data", "fkjhepcs.data", "gpiuezjw.data", "hbctmwqj.data", "jlxphwfm.data", "jrbiznkl.data", "jtxsbevz.data", "kczwtlrd.data", "lstjobzi.data",
          "mrxtfkzj.data", "oaeqnubi.data", "pyusgabf.data", "rnydeiho.data", "tihzkoyu.data", "uilqywot.data", "uozjmdnl.data", "wgkapjbh.data", "xufbyndk.data", "xufnmacj.data", "ycqzmbrw.data", "yscijlzx.data", "yvxmeawg.data"]
    merge_png(400, 400, ['yvxmeawg.data',
                             'rnydeiho.data','uozjmdnl.data',
                             "fhnkotmb.data",'jlxphwfm.data',
                             'yscijlzx.data','ciaoxptf.data',
                             'blczioav.data','jtxsbevz.data',
                             'lstjobzi.data','pyusgabf.data',
                             'wgkapjbh.data','xufbyndk.data',
                             'csizrgxn.data','oaeqnubi.data',
                             'gpiuezjw.data','tihzkoyu.data',
                             'hbctmwqj.data','ycqzmbrw.data',
                             'fkjhepcs.data','kczwtlrd.data',
                             'dwelszrk.data','uilqywot.data',
                             'xufnmacj.data','jrbiznkl.data',
                             'mrxtfkzj.data'], "%s.png" % "flag")