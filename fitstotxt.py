from astropy.io import fits
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument("filestoprocess", help="provide the files to process")
args = parser.parse_args()
print("Provided input:")
print(args.filestoprocess)

foundfiles = glob.glob(args.filestoprocess)
if len(foundfiles)!=0:
    for each in foundfiles: print(each)
else:
    print('No file found matching your input')

for EACH in foundfiles:

    hdul = fits.open(EACH)
    data=hdul[1].data
    TIME=data['TIME']
    FLUX_RAW=data['FLUX_RAW']

    foutname=EACH.split('/')[-1]+'.txt'
    fout=open(foutname,'w')
    fout.write('TIME FLUX_RAW')
    for index, each in enumerate(TIME):
        fout.write(str(each)+" "+str(FLUX_RAW[index])+'\n')
    fout.close()