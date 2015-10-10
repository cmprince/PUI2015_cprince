# HW3 Problem 3 (Citibike)
The notebooks in this repo explore whether or not tourists are more likely
to take Citibikes across the East River bridges than city residents. To
do this, I also needed to write a script (also included here) to generate
a file containing the station ID numbers and the boroughs in which they are
located. This script is not executed as part of the notebook because of the
time it takes to execute (a few hundred API calls to a reverse geolocation
service) and the fickleness of the script (it failed twice due to timing out
before I successfully got a complete list), but it can be run with with the
`geopy` package installed. The main work is in the file 
Citibike-Bridges-cmp670.ipynb; the analysis is rerun for September 2015 (and
possibly other months) is in Citibike-Bridges-cmp670-rerun.ipynb.

The notebooks themselves require `os`,`csv`,`pylab`,`pandas`,`numpy`,`zipfile`,`IPython.display` and `scipy.stats`. The Citibike data for August 2015 (at
https://s3.amazonaws.com/tripdata/201508-citibike-tripdata.zip) 
should be accessible from a directory (or link) named 
$PUI2015/citibikes/data. The second notebook also requires the data from September to be in the same directory.

I worked alone on this project--and now that I've done it I wish I'd put more
effort into finding a team!
