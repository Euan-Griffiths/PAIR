from astropy.io import fits
from matplotlib import pyplot as plt

hdul = fits.open(r".\imaging_pipeline.60755.433778935185\14A-000.MJD60755.41922898148._1331+305_3C286__ph.C_band.cont.regcal.I.alpha.error.fits")
info = hdul[0].header
data = hdul[0].data
with open("./astropy/test.txt","w") as f:
    f.write(str(info))
with open("./astropy/data.txt","w") as f:
    f.write(str(data))
print(data.shape)
#plt.imshow(data, cmap="gray") Problem for checking dimensions look at visulise docs

print(f"Data Shape (NAXIS,NAXIS1): {data.shape}")


hdul.close()