import argparse
import zlib

g="\033[1;32m"
r="\033[1;31m"
ret="\033[1;0m"


def get_parser():
    parser = argparse.ArgumentParser(description='Power by ❀flower❀')
    parser.add_argument("-t",dest="target",help="Input Target png",required=True)
    return parser.parse_args()

def crc_cmp(bin_data):
    r_crc = bin_data[29:33].hex()
    fake_crc=zlib.crc32(bin_data[12:29]).to_bytes(4).hex()

    print("Real PNG CRC: \t"+r_crc)
    print("PNG CRC: \t"+fake_crc)
    print('-' * 10)
    if fake_crc == r_crc:
        print("equal")
        return True
    else:
        print(f"{r}Not equal! {ret}")
        return False,r_crc

def crc_brute (bin_data,r_crc):
    IHDR = bin_data[12:16]
    other_file_byte = bin_data[24:29]
    for w in range(1,6000):
        for h in range(1,6000):
            tmp_data = IHDR+w.to_bytes(4)+h.to_bytes(4)+other_file_byte
            tmp_crc = zlib.crc32(tmp_data).to_bytes(4).hex()
            # print(tmp_data)
            if tmp_crc == r_crc:
                print('-'*10)
                print(f"{g}Found !\nwidth :{w} | height : {h}")
                return

def main(png_name):
    r = open(png_name, "rb")
    bin_data = r.read()
    fort,r_crc = crc_cmp(bin_data)
    if not fort:
        crc_brute(bin_data,r_crc)


if '__main__' == __name__:
    args = get_parser()
    main(args.target)
