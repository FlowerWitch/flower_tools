import argparse
import zlib

g="\033[1;32m"
r="\033[1;31m"
ret="\033[1;0m"

def get_parser():
    parser = argparse.ArgumentParser(description='Power by ❀flower❀')
    parser.add_argument("-t",dest="target",help="Input Target png",required=True)
    parser.add_argument("-o", dest="output_filename", help='default: output.png ; If with -o, output upon completion.',default="output.png")
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
        print(f"{r}CRC Not equal!\n[*]Start Brute Force {ret}")
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
                print(f"{g}[√]Found !\nwidth :{w} , height : {h}{ret}")
                if args.output_filename :
                    with open(args.output_filename,"wb") as w_png:
                        w_png.write(bin_data[:12]+tmp_data+int(r_crc,16).to_bytes(4)+bin_data[33:])
                    print(f"save filename: ./{args.output_filename}")
                return
    print(f"{r}GG")

def file_check(bin_data):
    png_head = "89504E470D0A1A0A0000000D49484452"
    input_head = bin_data[:16].hex()
    if not (input_head.upper() == png_head):
        print("Error Not PNG file headinfo !")
        exit(0)

def main(png_name):
    r = open(png_name, "rb")
    bin_data = r.read()
    file_check(bin_data)
    fort,r_crc = crc_cmp(bin_data)
    if not fort:
        crc_brute(bin_data,r_crc)

if '__main__' == __name__:
    args = get_parser()
    main(args.target)
