
import pandas as pd

"""
This script imports the combined raw bathymetric and lidar data, shifts the origin of the data to make it easier to work with and then exports it as an xyz file format importable into Meshlab.
"""

#Raw coordinates
data=pd.read_csv(r"C:\Users\Jason\Desktop\OpenFOAMRiverModeling\Step1-Geometry\rawBathyTopoData.csv", sep="\t",header=(0))

data=data[['Xnew','Ynew','Z_lit_vrai']]
data.columns=['x','y','z']

#Subtract the minimum latitude and longitude so the numbers are easier to work with
data['x_shifted']=data.x-data.x.min()
data['y_shifted']=data.y-data.y.min()
data.z.min()
#print out the minimum latitude and longitude for future reference
print("The minimum latitude coordinate is:  %s" %data.x.min())
print("The minimum longitude coordinate is:  %s" %data.y.min())

#Export the shifted origin data to a file in 'xyz' format that can be read into Meshlab
data.to_csv('newOriginBathyTopoData.xyz', sep=' ',header=False,index=False,columns=['x_shifted','y_shifted','z'])
