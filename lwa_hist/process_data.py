import glob
import numpy
import matplotlib
matplotlib.use('Agg')
import pylab
from os.path import basename,splitext

bins=numpy.arange(-2048,2048,1)

for file in glob.glob('data/*.npy'):
    currenthist=numpy.load(file)
    pylab.clf()
    pylab.plot(bins,currenthist,marker='.',linestyle='None')
    pylab.savefig('plots/'+ splitext(basename(file))[0] + '.pdf',format='pdf')
    
    #display a log plot
    pylab.clf()
    pylab.plot(bins,currenthist,marker='.',linestyle='None')
    pylab.yscale('log')
    pylab.savefig('plots/'+ splitext(basename(file))[0] + '_log.pdf',format='pdf')


