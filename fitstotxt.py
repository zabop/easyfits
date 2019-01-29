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

    foutname=EACH.split('/')[-1]+'.txt'
    fout=open(foutname,'w')

    for index, column_name in enumerate(data.names):
        if index==0:
            fout.write('#'+column_name)
        else:
            fout.write(' '+column_name)
    fout.write('\n')

    data = [data[each] for each in data.names]

    for rownum in range(len(data[0])):
        for colnum in range(len(data)):
            if colnum==0:
                fout.write(str(data[colnum][rownum]))
            else:
                fout.write(' '+str(data[colnum][rownum]))
        fout.write('\n')

    fout.close()