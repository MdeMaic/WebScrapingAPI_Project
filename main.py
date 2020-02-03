from SRC.parser import parser
from SRC.createdfsregion import createRegion
from SRC.createdfstop import createTop
from SRC.initialclean import cleanMerge

if __name__ == "__main__":
    top, region = parser()
    
    clean = cleanMerge()

    if top:
        now = createTop()
    
        

