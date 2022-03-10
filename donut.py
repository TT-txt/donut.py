from math import cos, sin
import sys

def main():
    A, B = 0, 0
    print("\x1b[2J")
    try:
        while True:
            z = [0] * 1760
            b = [chr(32)] * 1760
            j = 0
            char = [c for c in ".,-~:;=!*#$@"]
            while j < 6.28:
                i = 0
                while i < 6.28:
                    sini, cosj, sinA, sinj, cosA, cosj2= sin(i), cos(j), sin(A), sin(j), cos(A), cos(2+j) 
                    mess = 1/(sini*cosj2*sinA+sinj*cosA+5)
                    cosi, cosB, sinB = cos(i), cos(B), sin(B)
                    t = sini*cosj2*cosA-sinj*sinA
                    x = int(40+30*mess*(cosi*cosj2*cosB-t*sinB))
                    y = int(12+15*mess*(cosi*cosj2*sinB +t*cosB))
                    o = int(x+80*y)
                    N = int(8*((sinj*sinA-sini*cosj*cosA)*cosB-sini*cosj*sinA-sinj*cosA-cosi *cosj*sinB))
                    if 22 > y and y > 0 and x > 0 and 80 > x and mess > z[o]:
                        z[o] = mess
                        b[o] = char[N if N > 0 else 0]
                    i+=0.02
                j+=0.07
            print("\x1b[2J")
            for k in range(0, 1761):
                if k % 80:
                    sys.stdout.write(b[k])
                else:
                    sys.stdout.write(chr(10))
            A+=0.04
            B+=0.02
    except KeyboardInterrupt:
        quit()

if __name__ == "__main__":
    main()
