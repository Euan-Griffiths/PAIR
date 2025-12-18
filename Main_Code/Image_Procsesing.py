from astropy.io import fits
from matplotlib import pyplot as plt
import numpy as np

class Main():
    def __init__(self):
        self.imageLink = r"FITS_IMAGES\ESA\502nmos.fits" #
        self.cmap = "CMRmap"
        self.lowerbound = 0
        self.upperbound = 70
    
    def main(self):
        try:
            with fits.open(self.imageLink) as self.hdul:
                self.data = self.hdul[0].data
                self.header = self.hdul[0].header
        except FileNotFoundError:
            
        
        plt.imshow(self.data,cmap=self.cmap,vmin=self.lowerbound,vmax=self.upperbound)
        plt.colorbar()
        self.render()
        
            
    def render(self):
        plt.show()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            return
        
    
    
    
if __name__ == "__main__":
    main = Main()
    main.main()