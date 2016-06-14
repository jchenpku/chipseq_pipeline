#!/usr/bin/env python2

import os


def get_files_by_file_size(dirname, reverse=False):
    """ Return list of file paths in directory sorted by file size """

    # Get list of files
    filepaths = []
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        if os.path.isfile(filename):
            filepaths.append(filename)

    # Re-populate list with filename, size tuples
    for i in xrange(len(filepaths)):
        filepaths[i] = (filepaths[i], os.path.getsize(filepaths[i]))

    # Sort list by file size
    # If reverse=True sort from largest to smallest
    # If reverse=False sort from smallest to largest
    filepaths.sort(key=lambda filename: filename[1], reverse=reverse)

    # Re-populate list with just filenames
    for i in xrange(len(filepaths)):
        filepaths[i] = filepaths[i][0]

    return filepaths

#ctl_to_subsample = ["CONTROL.K562.unpaired.fastq.gz", "CONTROL.GM12878.unpaired.fastq.gz", "CONTROL.HepG2.unpaired.fastq.gz", "CONTROL.SK-N-SH.unpaired.fastq.gz", "CONTROL.HeLa-S3.unpaired.fastq.gz", "CONTROL.H1-hESC.unpaired.fastq.gz", "CONTROL.MCF-7.unpaired.fastq.gz", "CONTROL.A549.unpaired.fastq.gz", "CONTROL.liver.BSID_ENCBS401URL.unpaired.fastq.gz", "CONTROL.Panc1.unpaired.fastq.gz", "CONTROL.HCT116.unpaired.fastq.gz", "CONTROL.liver.BSID_ENCBS046RNA.unpaired.fastq.gz", "CONTROL.PC-3.unpaired.fastq.gz", "CONTROL.B_cell.unpaired.fastq.gz", "CONTROL.fibroblast_of_lung.unpaired.fastq.gz", "CONTROL.endothelial_cell_of_umbilical_vein.unpaired.fastq.gz"]
ctl_to_subsample = ["CONTROL.K562.unpaired.fastq.gz", "CONTROL.GM12878.unpaired.fastq.gz", "CONTROL.HepG2.unpaired.fastq.gz", "CONTROL.SK-N-SH.unpaired.fastq.gz", "CONTROL.HeLa-S3.unpaired.fastq.gz", "CONTROL.H1-hESC.unpaired.fastq.gz", "CONTROL.MCF-7.unpaired.fastq.gz", "CONTROL.A549.unpaired.fastq.gz", "CONTROL.liver.BSID_ENCBS401URL.unpaired.fastq.gz", "CONTROL.Panc1.unpaired.fastq.gz", "CONTROL.HCT116.unpaired.fastq.gz", "CONTROL.liver.BSID_ENCBS046RNA.unpaired.fastq.gz", "CONTROL.PC-3.unpaired.fastq.gz", "CONTROL.B_cell.unpaired.fastq.gz", "CONTROL.fibroblast_of_lung.unpaired.fastq.gz", "CONTROL.endothelial_cell_of_umbilical_vein.unpaired.fastq.gz", "CONTROL.astrocyte.unpaired.fastq.gz", "CONTROL.NT2_D1.unpaired.fastq.gz", "CONTROL.myotube.unpaired.fastq.gz", "CONTROL.induced_pluripotent_stem_cell.unpaired.fastq.gz", "CONTROL.GM12892.unpaired.fastq.gz", "CONTROL.HL-60.unpaired.fastq.gz", "CONTROL.foreskin_fibroblast.unpaired.fastq.gz", "CONTROL.IMR-90.unpaired.fastq.gz", "CONTROL.T47D.unpaired.fastq.gz"]

lst = get_files_by_file_size( os.getcwd(), True )

ctl = []
for i in lst:
    if "CONTROL." in i:
        ctl.append( os.path.basename(i) )

cnt = 1
for j in ctl:
    if ".R1." in j or ".R2." in j:
        continue
    prefix = j.rsplit(".unpaired",1)[0]
    filesize = os.path.getsize(j)
    print "#" + str(cnt) + " size:" + str( filesize )
    nth = filesize/2000000000
    if nth == 0:
        nth = 1
    subsample = ""
    if os.path.basename(j) in ctl_to_subsample:
        subsample = " -subsample 40000000 -mem 40G "
    print "NTH="+str(nth)+"; SUFFIX="+prefix
    print "FASTQ1=$DATA/DREAM_challenge/"+j
    print "WORK=$RUN/DREAM_challenge_ctl/$SUFFIX; mkdir -p $WORK; cd $WORK;"
    print "bds_scr ${SUFFIX//\//_} $CODE/bds_atac/chipseq/chipseq.bds -species hg19 -nth $NTH -fastq1 $FASTQ1 -final_stage tag" + subsample
    print
    cnt = cnt + 1