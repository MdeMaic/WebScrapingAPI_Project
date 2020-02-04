from SRC.parser import parser
from SRC.createdfsregion import createRegion, filterRegion, printReport
from SRC.createdfstop import createTop
from SRC.initialclean import cleanMerge

if __name__ == "__main__":
    top, region, filt, repo = parser()
    
    if top == region == filt == repo == False:
        print("Hola! Elige un flag: -top, -region, -filt, -repo")

    if top:
        clean = cleanMerge()
        now = createTop()
    
    if region:
        clean = cleanMerge()
        reg = createRegion()
    
    if filt:
        print("\nFilter subregion between 0.49 and 0.92 HDI values")
        minim =input("Insert a min value: ")
        maxim =input("Insert a max value: ")
        if float(minim) >= 0.93 or float(maxim) <= 0.48:
            print("FAIL | Error de parametrización")
        else:
            if minim > maxim:
                print("FAIL | min > max")
            else:
                flt = filterRegion(minim,maxim)
    
    if repo:
        report = printReport()     

