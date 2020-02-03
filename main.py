from SRC.parser import parser
from SRC.createdfsregion import createRegion, filterRegion
from SRC.createdfstop import createTop
from SRC.initialclean import cleanMerge

if __name__ == "__main__":
    top, region, filt = parser()
    
    if top == region == filt == False:
        print("Elige un flag: -top, -region, -filt")

    if top:
        clean = cleanMerge()
        now = createTop()
    
    if region:
        clean = cleanMerge()
        reg = createRegion()
    
    if filt:
        print("filter subregion between 0.49 and 0.92 HDI values")
        minim =input("Insert a min value: ")
        maxim =input("Insert a max value: ")
        if float(minim) >= 0.93 or float(maxim) <= 0.48:
            print("Error de parametrización")
        else:
            if minim > maxim:
                print("Error | min > max")
            else:
                flt = filterRegion(minim,maxim)
    
        

