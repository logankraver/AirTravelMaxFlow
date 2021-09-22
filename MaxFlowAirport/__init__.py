"""
Algorithm for finding the max flow of passengers from starting airport to a destination given a 24 hour period and connecting airports

The max flow algorithm employs a graph of nodes and edges. The nodes represent both the airport and the hour 
(e.g. LAX10 represents 10 AM in the LAX airport). The edges represent the flights between airports and time 
of transit (e.g. LAX7CLT15 = flight leaving LAX at 7 AM, arrives in CLT at 3 PM) and the passing of time within
the airport (e.g. SFO78 = time passing in the SFO airport from 7 - 8 AM). The algorithm employs the PuLP library
and linear programming to find the best optimization for the max flow network by using constraint equations to 
find the best combination of edge variables to maximize the objective function.

Starting Airport = Los Angeles
Connecting Airports = Atlanta, Charlotte, Chicago, Dallas, Denver, Detroit, Houston, Miami, Orlando, Phoenix, Salt Lake City, San Francisco, Seattle, Washington
Destination = New York

Flight Data: https://www.google.com/flights?hl=en#flt=LAX.JFK.2020-06-19;c:USD;e:1;ca:-DCA,-TPA,-PDX,-FLL,-BOS,-MSP,-SJC,-SMF,-TUS;a:AA,DL,UA,WN,AS;sd:1;t:f;tt:o

Author: logan Kraver
Date: 6/10/2020
"""


import pulp as p
import csv


airportFlow = p.LpProblem('airportProblem', p.LpMaximize)


#LAX edge variables
edgeLAX12 = p.LpVariable("EdgeLAX1,2",lowBound=0,upBound = 9999)
edgeLAX23 = p.LpVariable("EdgeLAX2,3",lowBound=0,upBound = 9999)
edgeLAX34 = p.LpVariable("EdgeLAX3,4",lowBound=0,upBound = 9999)
edgeLAX45 = p.LpVariable("EdgeLAX4,5",lowBound=0,upBound = 9999)
edgeLAX56 = p.LpVariable("EdgeLAX5,6",lowBound=0,upBound = 9999)
edgeLAX67 = p.LpVariable("EdgeLAX6,7",lowBound=0,upBound = 9999)
edgeLAX78 = p.LpVariable("EdgeLAX7,8",lowBound=0,upBound = 9999)
edgeLAX89 = p.LpVariable("EdgeLAX8,9",lowBound=0,upBound = 9999)
edgeLAX910 = p.LpVariable("EdgeLAX9,10",lowBound=0,upBound = 9999)
edgeLAX1011 = p.LpVariable("EdgeLAX10,11",lowBound=0,upBound = 9999)
edgeLAX1112 = p.LpVariable("EdgeLAX11,12",lowBound=0,upBound = 9999)
edgeLAX1213 = p.LpVariable("EdgeLAX12,13",lowBound=0,upBound = 9999)
edgeLAX1314 = p.LpVariable("EdgeLAX13,14",lowBound=0,upBound = 9999)
edgeLAX1415 = p.LpVariable("EdgeLAX14,15",lowBound=0,upBound = 9999)
edgeLAX1516 = p.LpVariable("EdgeLAX15,16",lowBound=0,upBound = 9999)
edgeLAX1617 = p.LpVariable("EdgeLAX16,17",lowBound=0,upBound = 9999)
edgeLAX1718 = p.LpVariable("EdgeLAX17,18",lowBound=0,upBound = 9999)
edgeLAX1819 = p.LpVariable("EdgeLAX18,19",lowBound=0,upBound = 9999)
edgeLAX1920 = p.LpVariable("EdgeLAX19,20",lowBound=0,upBound = 9999)
edgeLAX2021 = p.LpVariable("EdgeLAX20,21",lowBound=0,upBound = 9999)
edgeLAX2122 = p.LpVariable("EdgeLAX21,22",lowBound=0,upBound = 9999)
edgeLAX2223 = p.LpVariable("EdgeLAX22,23",lowBound=0,upBound = 9999)
edgeLAX2324 = p.LpVariable("EdgeLAX23,24",lowBound=0,upBound = 9999)


#SFO edge variables
edgeSFO12 = p.LpVariable("EdgeSFO1,2",lowBound=0,upBound = 0)
edgeSFO23 = p.LpVariable("EdgeSFO2,3",lowBound=0,upBound = 9999)
edgeSFO34 = p.LpVariable("EdgeSFO3,4",lowBound=0,upBound = 9999)
edgeSFO45 = p.LpVariable("EdgeSFO4,5",lowBound=0,upBound = 9999)
edgeSFO56 = p.LpVariable("EdgeSFO5,6",lowBound=0,upBound = 9999)
edgeSFO67 = p.LpVariable("EdgeSFO6,7",lowBound=0,upBound = 9999)
edgeSFO78 = p.LpVariable("EdgeSFO7,8",lowBound=0,upBound = 9999)
edgeSFO89 = p.LpVariable("EdgeSFO8,9",lowBound=0,upBound = 9999)
edgeSFO910 = p.LpVariable("EdgeSFO9,10",lowBound=0,upBound = 9999)
edgeSFO1011 = p.LpVariable("EdgeSFO10,11",lowBound=0,upBound = 9999)
edgeSFO1112 = p.LpVariable("EdgeSFO11,12",lowBound=0,upBound = 9999)
edgeSFO1213 = p.LpVariable("EdgeSFO12,13",lowBound=0,upBound = 9999)
edgeSFO1314 = p.LpVariable("EdgeSFO13,14",lowBound=0,upBound = 9999)
edgeSFO1415 = p.LpVariable("EdgeSFO14,15",lowBound=0,upBound = 9999)
edgeSFO1516 = p.LpVariable("EdgeSFO15,16",lowBound=0,upBound = 9999)
edgeSFO1617 = p.LpVariable("EdgeSFO16,17",lowBound=0,upBound = 9999)
edgeSFO1718 = p.LpVariable("EdgeSFO17,18",lowBound=0,upBound = 9999)
edgeSFO1819 = p.LpVariable("EdgeSFO18,19",lowBound=0,upBound = 9999)
edgeSFO1920 = p.LpVariable("EdgeSFO19,20",lowBound=0,upBound = 9999)
edgeSFO2021 = p.LpVariable("EdgeSFO20,21",lowBound=0,upBound = 9999)
edgeSFO2122 = p.LpVariable("EdgeSFO21,22",lowBound=0,upBound = 9999)
edgeSFO2223 = p.LpVariable("EdgeSFO22,23",lowBound=0,upBound = 9999)
edgeSFO2324 = p.LpVariable("EdgeSFO23,24",lowBound=0,upBound = 9999)


#PHX edge variables
edgePHX12 = p.LpVariable("EdgePHX1,2",lowBound=0,upBound = 0)
edgePHX23 = p.LpVariable("EdgePHX2,3",lowBound=0,upBound = 9999)
edgePHX34 = p.LpVariable("EdgePHX3,4",lowBound=0,upBound = 9999)
edgePHX45 = p.LpVariable("EdgePHX4,5",lowBound=0,upBound = 9999)
edgePHX56 = p.LpVariable("EdgePHX5,6",lowBound=0,upBound = 9999)
edgePHX67 = p.LpVariable("EdgePHX6,7",lowBound=0,upBound = 9999)
edgePHX78 = p.LpVariable("EdgePHX7,8",lowBound=0,upBound = 9999)
edgePHX89 = p.LpVariable("EdgePHX8,9",lowBound=0,upBound = 9999)
edgePHX910 = p.LpVariable("EdgePHX9,10",lowBound=0,upBound = 9999)
edgePHX1011 = p.LpVariable("EdgePHX10,11",lowBound=0,upBound = 9999)
edgePHX1112 = p.LpVariable("EdgePHX11,12",lowBound=0,upBound = 9999)
edgePHX1213 = p.LpVariable("EdgePHX12,13",lowBound=0,upBound = 9999)
edgePHX1314 = p.LpVariable("EdgePHX13,14",lowBound=0,upBound = 9999)
edgePHX1415 = p.LpVariable("EdgePHX14,15",lowBound=0,upBound = 9999)
edgePHX1516 = p.LpVariable("EdgePHX15,16",lowBound=0,upBound = 9999)
edgePHX1617 = p.LpVariable("EdgePHX16,17",lowBound=0,upBound = 9999)
edgePHX1718 = p.LpVariable("EdgePHX17,18",lowBound=0,upBound = 9999)
edgePHX1819 = p.LpVariable("EdgePHX18,19",lowBound=0,upBound = 9999)
edgePHX1920 = p.LpVariable("EdgePHX19,20",lowBound=0,upBound = 9999)
edgePHX2021 = p.LpVariable("EdgePHX20,21",lowBound=0,upBound = 9999)
edgePHX2122 = p.LpVariable("EdgePHX21,22",lowBound=0,upBound = 9999)
edgePHX2223 = p.LpVariable("EdgePHX22,23",lowBound=0,upBound = 9999)
edgePHX2324 = p.LpVariable("EdgePHX23,24",lowBound=0,upBound = 9999)

#SLC edge variables
edgeSLC12 = p.LpVariable("EdgeSLC1,2",lowBound=0,upBound = 0)
edgeSLC23 = p.LpVariable("EdgeSLC2,3",lowBound=0,upBound = 9999)
edgeSLC34 = p.LpVariable("EdgeSLC3,4",lowBound=0,upBound = 9999)
edgeSLC45 = p.LpVariable("EdgeSLC4,5",lowBound=0,upBound = 9999)
edgeSLC56 = p.LpVariable("EdgeSLC5,6",lowBound=0,upBound = 9999)
edgeSLC67 = p.LpVariable("EdgeSLC6,7",lowBound=0,upBound = 9999)
edgeSLC78 = p.LpVariable("EdgeSLC7,8",lowBound=0,upBound = 9999)
edgeSLC89 = p.LpVariable("EdgeSLC8,9",lowBound=0,upBound = 9999)
edgeSLC910 = p.LpVariable("EdgeSLC9,10",lowBound=0,upBound = 9999)
edgeSLC1011 = p.LpVariable("EdgeSLC10,11",lowBound=0,upBound = 9999)
edgeSLC1112 = p.LpVariable("EdgeSLC11,12",lowBound=0,upBound = 9999)
edgeSLC1213 = p.LpVariable("EdgeSLC12,13",lowBound=0,upBound = 9999)
edgeSLC1314 = p.LpVariable("EdgeSLC13,14",lowBound=0,upBound = 9999)
edgeSLC1415 = p.LpVariable("EdgeSLC14,15",lowBound=0,upBound = 9999)
edgeSLC1516 = p.LpVariable("EdgeSLC15,16",lowBound=0,upBound = 9999)
edgeSLC1617 = p.LpVariable("EdgeSLC16,17",lowBound=0,upBound = 9999)
edgeSLC1718 = p.LpVariable("EdgeSLC17,18",lowBound=0,upBound = 9999)
edgeSLC1819 = p.LpVariable("EdgeSLC18,19",lowBound=0,upBound = 9999)
edgeSLC1920 = p.LpVariable("EdgeSLC19,20",lowBound=0,upBound = 9999)
edgeSLC2021 = p.LpVariable("EdgeSLC20,21",lowBound=0,upBound = 9999)
edgeSLC2122 = p.LpVariable("EdgeSLC21,22",lowBound=0,upBound = 9999)
edgeSLC2223 = p.LpVariable("EdgeSLC22,23",lowBound=0,upBound = 9999)
edgeSLC2324 = p.LpVariable("EdgeSLC23,24",lowBound=0,upBound = 9999)

#DFW edge variables
edgeDFW12 = p.LpVariable("EdgeDFW1,2",lowBound=0,upBound = 0)
edgeDFW23 = p.LpVariable("EdgeDFW2,3",lowBound=0,upBound = 9999)
edgeDFW34 = p.LpVariable("EdgeDFW3,4",lowBound=0,upBound = 9999)
edgeDFW45 = p.LpVariable("EdgeDFW4,5",lowBound=0,upBound = 9999)
edgeDFW56 = p.LpVariable("EdgeDFW5,6",lowBound=0,upBound = 9999)
edgeDFW67 = p.LpVariable("EdgeDFW6,7",lowBound=0,upBound = 9999)
edgeDFW78 = p.LpVariable("EdgeDFW7,8",lowBound=0,upBound = 9999)
edgeDFW89 = p.LpVariable("EdgeDFW8,9",lowBound=0,upBound = 9999)
edgeDFW910 = p.LpVariable("EdgeDFW9,10",lowBound=0,upBound = 9999)
edgeDFW1011 = p.LpVariable("EdgeDFW10,11",lowBound=0,upBound = 9999)
edgeDFW1112 = p.LpVariable("EdgeDFW11,12",lowBound=0,upBound = 9999)
edgeDFW1213 = p.LpVariable("EdgeDFW12,13",lowBound=0,upBound = 9999)
edgeDFW1314 = p.LpVariable("EdgeDFW13,14",lowBound=0,upBound = 9999)
edgeDFW1415 = p.LpVariable("EdgeDFW14,15",lowBound=0,upBound = 9999)
edgeDFW1516 = p.LpVariable("EdgeDFW15,16",lowBound=0,upBound = 9999)
edgeDFW1617 = p.LpVariable("EdgeDFW16,17",lowBound=0,upBound = 9999)
edgeDFW1718 = p.LpVariable("EdgeDFW17,18",lowBound=0,upBound = 9999)
edgeDFW1819 = p.LpVariable("EdgeDFW18,19",lowBound=0,upBound = 9999)
edgeDFW1920 = p.LpVariable("EdgeDFW19,20",lowBound=0,upBound = 9999)
edgeDFW2021 = p.LpVariable("EdgeDFW20,21",lowBound=0,upBound = 9999)
edgeDFW2122 = p.LpVariable("EdgeDFW21,22",lowBound=0,upBound = 9999)
edgeDFW2223 = p.LpVariable("EdgeDFW22,23",lowBound=0,upBound = 9999)
edgeDFW2324 = p.LpVariable("EdgeDFW23,24",lowBound=0,upBound = 9999)

#IAH edge variables
edgeIAH12 = p.LpVariable("EdgeIAH1,2",lowBound=0,upBound = 0)
edgeIAH23 = p.LpVariable("EdgeIAH2,3",lowBound=0,upBound = 9999)
edgeIAH34 = p.LpVariable("EdgeIAH3,4",lowBound=0,upBound = 9999)
edgeIAH45 = p.LpVariable("EdgeIAH4,5",lowBound=0,upBound = 9999)
edgeIAH56 = p.LpVariable("EdgeIAH5,6",lowBound=0,upBound = 9999)
edgeIAH67 = p.LpVariable("EdgeIAH6,7",lowBound=0,upBound = 9999)
edgeIAH78 = p.LpVariable("EdgeIAH7,8",lowBound=0,upBound = 9999)
edgeIAH89 = p.LpVariable("EdgeIAH8,9",lowBound=0,upBound = 9999)
edgeIAH910 = p.LpVariable("EdgeIAH9,10",lowBound=0,upBound = 9999)
edgeIAH1011 = p.LpVariable("EdgeIAH10,11",lowBound=0,upBound = 9999)
edgeIAH1112 = p.LpVariable("EdgeIAH11,12",lowBound=0,upBound = 9999)
edgeIAH1213 = p.LpVariable("EdgeIAH12,13",lowBound=0,upBound = 9999)
edgeIAH1314 = p.LpVariable("EdgeIAH13,14",lowBound=0,upBound = 9999)
edgeIAH1415 = p.LpVariable("EdgeIAH14,15",lowBound=0,upBound = 9999)
edgeIAH1516 = p.LpVariable("EdgeIAH15,16",lowBound=0,upBound = 9999)
edgeIAH1617 = p.LpVariable("EdgeIAH16,17",lowBound=0,upBound = 9999)
edgeIAH1718 = p.LpVariable("EdgeIAH17,18",lowBound=0,upBound = 9999)
edgeIAH1819 = p.LpVariable("EdgeIAH18,19",lowBound=0,upBound = 9999)
edgeIAH1920 = p.LpVariable("EdgeIAH19,20",lowBound=0,upBound = 9999)
edgeIAH2021 = p.LpVariable("EdgeIAH20,21",lowBound=0,upBound = 9999)
edgeIAH2122 = p.LpVariable("EdgeIAH21,22",lowBound=0,upBound = 9999)
edgeIAH2223 = p.LpVariable("EdgeIAH22,23",lowBound=0,upBound = 9999)
edgeIAH2324 = p.LpVariable("EdgeIAH23,24",lowBound=0,upBound = 9999)

#DTW edge variables
edgeDTW12 = p.LpVariable("EdgeDTW1,2",lowBound=0,upBound = 0)
edgeDTW23 = p.LpVariable("EdgeDTW2,3",lowBound=0,upBound = 9999)
edgeDTW34 = p.LpVariable("EdgeDTW3,4",lowBound=0,upBound = 9999)
edgeDTW45 = p.LpVariable("EdgeDTW4,5",lowBound=0,upBound = 9999)
edgeDTW56 = p.LpVariable("EdgeDTW5,6",lowBound=0,upBound = 9999)
edgeDTW67 = p.LpVariable("EdgeDTW6,7",lowBound=0,upBound = 9999)
edgeDTW78 = p.LpVariable("EdgeDTW7,8",lowBound=0,upBound = 9999)
edgeDTW89 = p.LpVariable("EdgeDTW8,9",lowBound=0,upBound = 9999)
edgeDTW910 = p.LpVariable("EdgeDTW9,10",lowBound=0,upBound = 9999)
edgeDTW1011 = p.LpVariable("EdgeDTW10,11",lowBound=0,upBound = 9999)
edgeDTW1112 = p.LpVariable("EdgeDTW11,12",lowBound=0,upBound = 9999)
edgeDTW1213 = p.LpVariable("EdgeDTW12,13",lowBound=0,upBound = 9999)
edgeDTW1314 = p.LpVariable("EdgeDTW13,14",lowBound=0,upBound = 9999)
edgeDTW1415 = p.LpVariable("EdgeDTW14,15",lowBound=0,upBound = 9999)
edgeDTW1516 = p.LpVariable("EdgeDTW15,16",lowBound=0,upBound = 9999)
edgeDTW1617 = p.LpVariable("EdgeDTW16,17",lowBound=0,upBound = 9999)
edgeDTW1718 = p.LpVariable("EdgeDTW17,18",lowBound=0,upBound = 9999)
edgeDTW1819 = p.LpVariable("EdgeDTW18,19",lowBound=0,upBound = 9999)
edgeDTW1920 = p.LpVariable("EdgeDTW19,20",lowBound=0,upBound = 9999)
edgeDTW2021 = p.LpVariable("EdgeDTW20,21",lowBound=0,upBound = 9999)
edgeDTW2122 = p.LpVariable("EdgeDTW21,22",lowBound=0,upBound = 9999)
edgeDTW2223 = p.LpVariable("EdgeDTW22,23",lowBound=0,upBound = 9999)
edgeDTW2324 = p.LpVariable("EdgeDTW23,24",lowBound=0,upBound = 9999)

#ORD edge variables
edgeORD12 = p.LpVariable("EdgeORD1,2",lowBound=0,upBound = 0)
edgeORD23 = p.LpVariable("EdgeORD2,3",lowBound=0,upBound = 9999)
edgeORD34 = p.LpVariable("EdgeORD3,4",lowBound=0,upBound = 9999)
edgeORD45 = p.LpVariable("EdgeORD4,5",lowBound=0,upBound = 9999)
edgeORD56 = p.LpVariable("EdgeORD5,6",lowBound=0,upBound = 9999)
edgeORD67 = p.LpVariable("EdgeORD6,7",lowBound=0,upBound = 9999)
edgeORD78 = p.LpVariable("EdgeORD7,8",lowBound=0,upBound = 9999)
edgeORD89 = p.LpVariable("EdgeORD8,9",lowBound=0,upBound = 9999)
edgeORD910 = p.LpVariable("EdgeORD9,10",lowBound=0,upBound = 9999)
edgeORD1011 = p.LpVariable("EdgeORD10,11",lowBound=0,upBound = 9999)
edgeORD1112 = p.LpVariable("EdgeORD11,12",lowBound=0,upBound = 9999)
edgeORD1213 = p.LpVariable("EdgeORD12,13",lowBound=0,upBound = 9999)
edgeORD1314 = p.LpVariable("EdgeORD13,14",lowBound=0,upBound = 9999)
edgeORD1415 = p.LpVariable("EdgeORD14,15",lowBound=0,upBound = 9999)
edgeORD1516 = p.LpVariable("EdgeORD15,16",lowBound=0,upBound = 9999)
edgeORD1617 = p.LpVariable("EdgeORD16,17",lowBound=0,upBound = 9999)
edgeORD1718 = p.LpVariable("EdgeORD17,18",lowBound=0,upBound = 9999)
edgeORD1819 = p.LpVariable("EdgeORD18,19",lowBound=0,upBound = 9999)
edgeORD1920 = p.LpVariable("EdgeORD19,20",lowBound=0,upBound = 9999)
edgeORD2021 = p.LpVariable("EdgeORD20,21",lowBound=0,upBound = 9999)
edgeORD2122 = p.LpVariable("EdgeORD21,22",lowBound=0,upBound = 9999)
edgeORD2223 = p.LpVariable("EdgeORD22,23",lowBound=0,upBound = 9999)
edgeORD2324 = p.LpVariable("EdgeORD23,24",lowBound=0,upBound = 9999)

#MIA edge variables
edgeMIA12 = p.LpVariable("EdgeMIA1,2",lowBound=0,upBound = 0)
edgeMIA23 = p.LpVariable("EdgeMIA2,3",lowBound=0,upBound = 9999)
edgeMIA34 = p.LpVariable("EdgeMIA3,4",lowBound=0,upBound = 9999)
edgeMIA45 = p.LpVariable("EdgeMIA4,5",lowBound=0,upBound = 9999)
edgeMIA56 = p.LpVariable("EdgeMIA5,6",lowBound=0,upBound = 9999)
edgeMIA67 = p.LpVariable("EdgeMIA6,7",lowBound=0,upBound = 9999)
edgeMIA78 = p.LpVariable("EdgeMIA7,8",lowBound=0,upBound = 9999)
edgeMIA89 = p.LpVariable("EdgeMIA8,9",lowBound=0,upBound = 9999)
edgeMIA910 = p.LpVariable("EdgeMIA9,10",lowBound=0,upBound = 9999)
edgeMIA1011 = p.LpVariable("EdgeMIA10,11",lowBound=0,upBound = 9999)
edgeMIA1112 = p.LpVariable("EdgeMIA11,12",lowBound=0,upBound = 9999)
edgeMIA1213 = p.LpVariable("EdgeMIA12,13",lowBound=0,upBound = 9999)
edgeMIA1314 = p.LpVariable("EdgeMIA13,14",lowBound=0,upBound = 9999)
edgeMIA1415 = p.LpVariable("EdgeMIA14,15",lowBound=0,upBound = 9999)
edgeMIA1516 = p.LpVariable("EdgeMIA15,16",lowBound=0,upBound = 9999)
edgeMIA1617 = p.LpVariable("EdgeMIA16,17",lowBound=0,upBound = 9999)
edgeMIA1718 = p.LpVariable("EdgeMIA17,18",lowBound=0,upBound = 9999)
edgeMIA1819 = p.LpVariable("EdgeMIA18,19",lowBound=0,upBound = 9999)
edgeMIA1920 = p.LpVariable("EdgeMIA19,20",lowBound=0,upBound = 9999)
edgeMIA2021 = p.LpVariable("EdgeMIA20,21",lowBound=0,upBound = 9999)
edgeMIA2122 = p.LpVariable("EdgeMIA21,22",lowBound=0,upBound = 9999)
edgeMIA2223 = p.LpVariable("EdgeMIA22,23",lowBound=0,upBound = 9999)
edgeMIA2324 = p.LpVariable("EdgeMIA23,24",lowBound=0,upBound = 9999)

#ATL edge variables
edgeATL12 = p.LpVariable("EdgeATL1,2",lowBound=0,upBound = 0)
edgeATL23 = p.LpVariable("EdgeATL2,3",lowBound=0,upBound = 9999)
edgeATL34 = p.LpVariable("EdgeATL3,4",lowBound=0,upBound = 9999)
edgeATL45 = p.LpVariable("EdgeATL4,5",lowBound=0,upBound = 9999)
edgeATL56 = p.LpVariable("EdgeATL5,6",lowBound=0,upBound = 9999)
edgeATL67 = p.LpVariable("EdgeATL6,7",lowBound=0,upBound = 9999)
edgeATL78 = p.LpVariable("EdgeATL7,8",lowBound=0,upBound = 9999)
edgeATL89 = p.LpVariable("EdgeATL8,9",lowBound=0,upBound = 9999)
edgeATL910 = p.LpVariable("EdgeATL9,10",lowBound=0,upBound = 9999)
edgeATL1011 = p.LpVariable("EdgeATL10,11",lowBound=0,upBound = 9999)
edgeATL1112 = p.LpVariable("EdgeATL11,12",lowBound=0,upBound = 9999)
edgeATL1213 = p.LpVariable("EdgeATL12,13",lowBound=0,upBound = 9999)
edgeATL1314 = p.LpVariable("EdgeATL13,14",lowBound=0,upBound = 9999)
edgeATL1415 = p.LpVariable("EdgeATL14,15",lowBound=0,upBound = 9999)
edgeATL1516 = p.LpVariable("EdgeATL15,16",lowBound=0,upBound = 9999)
edgeATL1617 = p.LpVariable("EdgeATL16,17",lowBound=0,upBound = 9999)
edgeATL1718 = p.LpVariable("EdgeATL17,18",lowBound=0,upBound = 9999)
edgeATL1819 = p.LpVariable("EdgeATL18,19",lowBound=0,upBound = 9999)
edgeATL1920 = p.LpVariable("EdgeATL19,20",lowBound=0,upBound = 9999)
edgeATL2021 = p.LpVariable("EdgeATL20,21",lowBound=0,upBound = 9999)
edgeATL2122 = p.LpVariable("EdgeATL21,22",lowBound=0,upBound = 9999)
edgeATL2223 = p.LpVariable("EdgeATL22,23",lowBound=0,upBound = 9999)
edgeATL2324 = p.LpVariable("EdgeATL23,24",lowBound=0,upBound = 9999)

#CLT edge variables
edgeCLT12 = p.LpVariable("EdgeCLT1,2",lowBound=0,upBound = 0)
edgeCLT23 = p.LpVariable("EdgeCLT2,3",lowBound=0,upBound = 9999)
edgeCLT34 = p.LpVariable("EdgeCLT3,4",lowBound=0,upBound = 9999)
edgeCLT45 = p.LpVariable("EdgeCLT4,5",lowBound=0,upBound = 9999)
edgeCLT56 = p.LpVariable("EdgeCLT5,6",lowBound=0,upBound = 9999)
edgeCLT67 = p.LpVariable("EdgeCLT6,7",lowBound=0,upBound = 9999)
edgeCLT78 = p.LpVariable("EdgeCLT7,8",lowBound=0,upBound = 9999)
edgeCLT89 = p.LpVariable("EdgeCLT8,9",lowBound=0,upBound = 9999)
edgeCLT910 = p.LpVariable("EdgeCLT9,10",lowBound=0,upBound = 9999)
edgeCLT1011 = p.LpVariable("EdgeCLT10,11",lowBound=0,upBound = 9999)
edgeCLT1112 = p.LpVariable("EdgeCLT11,12",lowBound=0,upBound = 9999)
edgeCLT1213 = p.LpVariable("EdgeCLT12,13",lowBound=0,upBound = 9999)
edgeCLT1314 = p.LpVariable("EdgeCLT13,14",lowBound=0,upBound = 9999)
edgeCLT1415 = p.LpVariable("EdgeCLT14,15",lowBound=0,upBound = 9999)
edgeCLT1516 = p.LpVariable("EdgeCLT15,16",lowBound=0,upBound = 9999)
edgeCLT1617 = p.LpVariable("EdgeCLT16,17",lowBound=0,upBound = 9999)
edgeCLT1718 = p.LpVariable("EdgeCLT17,18",lowBound=0,upBound = 9999)
edgeCLT1819 = p.LpVariable("EdgeCLT18,19",lowBound=0,upBound = 9999)
edgeCLT1920 = p.LpVariable("EdgeCLT19,20",lowBound=0,upBound = 9999)
edgeCLT2021 = p.LpVariable("EdgeCLT20,21",lowBound=0,upBound = 9999)
edgeCLT2122 = p.LpVariable("EdgeCLT21,22",lowBound=0,upBound = 9999)
edgeCLT2223 = p.LpVariable("EdgeCLT22,23",lowBound=0,upBound = 9999)
edgeCLT2324 = p.LpVariable("EdgeCLT23,24",lowBound=0,upBound = 9999)

#JFK edge variables
edgeJFK12 = p.LpVariable("EdgeJFK1,2",lowBound=0,upBound = 0)
edgeJFK23 = p.LpVariable("EdgeJFK2,3",lowBound=0,upBound = 9999)
edgeJFK34 = p.LpVariable("EdgeJFK3,4",lowBound=0,upBound = 9999)
edgeJFK45 = p.LpVariable("EdgeJFK4,5",lowBound=0,upBound = 9999)
edgeJFK56 = p.LpVariable("EdgeJFK5,6",lowBound=0,upBound = 9999)
edgeJFK67 = p.LpVariable("EdgeJFK6,7",lowBound=0,upBound = 9999)
edgeJFK78 = p.LpVariable("EdgeJFK7,8",lowBound=0,upBound = 9999)
edgeJFK89 = p.LpVariable("EdgeJFK8,9",lowBound=0,upBound = 9999)
edgeJFK910 = p.LpVariable("EdgeJFK9,10",lowBound=0,upBound = 9999)
edgeJFK1011 = p.LpVariable("EdgeJFK10,11",lowBound=0,upBound = 9999)
edgeJFK1112 = p.LpVariable("EdgeJFK11,12",lowBound=0,upBound = 9999)
edgeJFK1213 = p.LpVariable("EdgeJFK12,13",lowBound=0,upBound = 9999)
edgeJFK1314 = p.LpVariable("EdgeJFK13,14",lowBound=0,upBound = 9999)
edgeJFK1415 = p.LpVariable("EdgeJFK14,15",lowBound=0,upBound = 9999)
edgeJFK1516 = p.LpVariable("EdgeJFK15,16",lowBound=0,upBound = 9999)
edgeJFK1617 = p.LpVariable("EdgeJFK16,17",lowBound=0,upBound = 9999)
edgeJFK1718 = p.LpVariable("EdgeJFK17,18",lowBound=0,upBound = 9999)
edgeJFK1819 = p.LpVariable("EdgeJFK18,19",lowBound=0,upBound = 9999)
edgeJFK1920 = p.LpVariable("EdgeJFK19,20",lowBound=0,upBound = 9999)
edgeJFK2021 = p.LpVariable("EdgeJFK20,21",lowBound=0,upBound = 9999)
edgeJFK2122 = p.LpVariable("EdgeJFK21,22",lowBound=0,upBound = 9999)
edgeJFK2223 = p.LpVariable("EdgeJFK22,23",lowBound=0,upBound = 9999)
edgeJFK2324 = p.LpVariable("EdgeJFK23,24",lowBound=0,upBound = 9999)


#Flights between all airports
#LAX -> JFK
edgeLAX15JFK23 = p.LpVariable("EdgeLAX15,JFK23",lowBound=0,upBound = 375)
edgeLAX7JFK15 = p.LpVariable("EdgeLAX7,JFK15",lowBound=0,upBound = 375)
edgeLAX8JFK16 = p.LpVariable("EdgeLAX8,JFK16",lowBound=0,upBound = 240) 
edgeLAX12JFK21 = p.LpVariable("EdgeLAX12,JFK21",lowBound=0,upBound = 375)
edgeLAX13JFK22 = p.LpVariable("EdgeLAX13,JFK22",lowBound=0,upBound = 240)


#LAX -> SFO
edgeLAX8SFO9 = p.LpVariable("EdgeLAX8SFO9",lowBound=0,upBound = 100)
edgeLAX8SFO10 = p.LpVariable("EdgeLAX8SFO10",lowBound=0,upBound = 100)


#LAX -> SLC
edgeLAX14SLC17 = p.LpVariable("EdgeLAX14,SLC17",lowBound=0,upBound = 215)
edgeLAX10SLC13 = p.LpVariable("EdgeLAX10,SLC13",lowBound=0,upBound = 215)
edgeLAX8SLC11 = p.LpVariable("EdgeLAX8,SLC11",lowBound=0,upBound = 215)
edgeLAX6SLC9 = p.LpVariable("EdgeLAX6,SLC9",lowBound=0,upBound = 240)


#LAX -> PHX
edgeLAX7PHX9 = p.LpVariable("EdgeLAX7,PHX9",lowBound=0,upBound = 160)
edgeLAX12PHX14 = p.LpVariable("EdgeLAX12,PHX14",lowBound=0,upBound = 240)
edgeLAX17PHX18 = p.LpVariable("EdgeLAX17,PHX18",lowBound=0,upBound = 160)


#LAX -> IAH
edgeLAX1IAH6 = p.LpVariable("EdgeLAX2,IAH6",lowBound=0,upBound = 215)


#IAH -> ATL
edgeIAH10ATL13 = p.LpVariable("EdgeIAH10ATL13",lowBound=0,upBound = 100)
edgeIAH14ATL17 = p.LpVariable("EdgeIAH14ATL17",lowBound=0,upBound = 134)


#LAX -> DFW
edgeLAX9DFW14 = p.LpVariable("EdgeLAX9,DFW14",lowBound=0,upBound = 240)
edgeLAX7DFW12 = p.LpVariable("EdgeLAX7,DFW12",lowBound=0,upBound = 240)


#DFW -> MIA
edgeDFW15MIA19 = p.LpVariable("EdgeDFW15,MIA19",lowBound=0,upBound = 160)


#LAX -> DTW
edgeLAX12DTW19 = p.LpVariable("EdgeLAX12,DTW19",lowBound=0,upBound = 215)
edgeLAX7DTW14 = p.LpVariable("EdgeLAX7DTW14",lowBound=0,upBound = 295)


#DTW -> ATL
edgeDTW16ATL18 = p.LpVariable("EdgeDTW16,ATL18",lowBound=0,upBound = 215)
edgeDTW15ATL17 = p.LpVariable("EdgeDTW15,ATL17",lowBound=0,upBound = 240)


#LAX -> ORD
edgeLAX1ORD7 = p.LpVariable("EdgeLAX1,ORD7",lowBound=0,upBound = 215)


#LAX -> MIA
edgeLAX11MIA19 = p.LpVariable("EdgeLAX11,MIA19",lowBound=0,upBound = 215)
edgeLAX14MIA22 = p.LpVariable("EdgeLAX14,MIA22",lowBound=0,upBound = 215)


#LAX -> ATL
edgeLAX11ATL18 = p.LpVariable("EdgeLAX11,ATL18",lowBound=0,upBound = 240)
edgeLAX13ATL20 = p.LpVariable("EdgeLAX13,ATL20",lowBound=0,upBound = 240)
edgeLAX9ATL16 = p.LpVariable("EdgeLAX9,ATL16",lowBound=0,upBound = 400)
edgeLAX15ATL22 = p.LpVariable("EdgeLAX15,ATL22",lowBound=0,upBound = 240)


#LAX -> CLT
edgeLAX1CLT8 = p.LpVariable("EdgeLAX1,CLT8",lowBound=0,upBound = 240)
edgeLAX7CLT15 = p.LpVariable("EdgeLAX7,CLT15",lowBound=0,upBound = 240)


#SFO -> JFK
edgeSFO13JFK21 = p.LpVariable("EdgeSFO13,JFK21",lowBound=0,upBound = 295)


#SLC -> JFK
edgeSLC17JFK23 = p.LpVariable("EdgeSLC17,JFK23",lowBound=0,upBound = 375)
edgeSLC12JFK20 = p.LpVariable("EdgeSLC12,JFK20",lowBound=0,upBound = 295)


#SLC -> ATL
edgeSLC11ATL17 = p.LpVariable("EdgeSLC11,ATL17",lowBound=0,upBound = 375)
edgeSLC10ATL16 = p.LpVariable("EdgeSLC10,ATL16",lowBound=0,upBound = 295)


#SLC -> DTW
edgeSLC14DTW20 = p.LpVariable("EdgeSLC14DTW20",lowBound=0,upBound = 240)


#PHX -> JFK
edgePHX10JFK18 = p.LpVariable("EdgePHX10,JFK18",lowBound=0,upBound = 215)
edgePHX16JFK23 = p.LpVariable("EdgePHX16,JFK23",lowBound=0,upBound = 215)


#DTW -> JFK
edgeDTW21JFK23 = p.LpVariable("EdgeDTW21,JFK23",lowBound=0,upBound = 240)


#ORD -> ATL
edgeORD9ATL12 = p.LpVariable("EdgeORD9,ATL12",lowBound=0,upBound = 100)


#MIA -> JFK
edgeMIA20JFK23 = p.LpVariable("EdgeMIA20JFK23",lowBound=0,upBound = 215)


#ATL -> JFK
edgeATL19JFK21 = p.LpVariable("EdgeATL19,JFK21",lowBound=0,upBound = 215)
edgeATL21JFK23 = p.LpVariable("EdgeATL21,JFK23",lowBound=0,upBound = 240)
edgeATL14JFK16 = p.LpVariable("EdgeATL14,JFK16",lowBound=0,upBound = 375)
edge2ATL21JFK23 = p.LpVariable("Edge2ATL21,JFK23",lowBound=0,upBound = 215)


#CLT -> JFK
edgeCLT9JFK11 = p.LpVariable("EdgeCLT9,JFK11",lowBound=0,upBound = 215)
edgeCLT16JFK18 = p.LpVariable("EdgeCLT16,JFK18",lowBound=0,upBound = 240)
edgeCLT13JFK15 = p.LpVariable("EdgeCLT13,JFK15",lowBound=0,upBound = 215)


#Objective function
airportFlow += edgeJFK2324


#LAX Constraints
airportFlow += edgeLAX12 - edgeLAX23 == 0
airportFlow += edgeLAX23 - edgeLAX34 - edgeLAX1CLT8 - edgeLAX1IAH6 - edgeLAX1ORD7 == 0
airportFlow += edgeLAX34 - edgeLAX45 == 0
airportFlow += edgeLAX45 - edgeLAX56 == 0
airportFlow += edgeLAX56 - edgeLAX67 - edgeLAX6SLC9 == 0
airportFlow += edgeLAX67 - edgeLAX78 - edgeLAX7JFK15 - edgeLAX7PHX9 - edgeLAX7DTW14 - edgeLAX7CLT15 - edgeLAX7DFW12 == 0
airportFlow += edgeLAX78 - edgeLAX89 - edgeLAX8JFK16 - edgeLAX8SLC11 - edgeLAX8SFO9 - edgeLAX8SFO10 == 0
airportFlow += edgeLAX89 - edgeLAX910 - edgeLAX9ATL16 - edgeLAX9DFW14 == 0
airportFlow += edgeLAX910 - edgeLAX1011 - edgeLAX10SLC13 == 0
airportFlow += edgeLAX1011 - edgeLAX1112 - edgeLAX11ATL18 - edgeLAX11MIA19 == 0
airportFlow += edgeLAX1112 - edgeLAX1213 - edgeLAX12JFK21 - edgeLAX12PHX14 - edgeLAX12DTW19 == 0
airportFlow += edgeLAX1213 - edgeLAX1314 - edgeLAX13JFK22 - edgeLAX13ATL20 == 0
airportFlow += edgeLAX1314 - edgeLAX1415 - edgeLAX14SLC17 - edgeLAX14MIA22 == 0
airportFlow += edgeLAX1415 - edgeLAX1516 - edgeLAX15JFK23 - edgeLAX15ATL22 == 0
airportFlow += edgeLAX1516 - edgeLAX1617 == 0
airportFlow += edgeLAX1617 - edgeLAX1718 - edgeLAX17PHX18 == 0
airportFlow += edgeLAX1718 - edgeLAX1819 == 0
airportFlow += edgeLAX1819 - edgeLAX1920 == 0
airportFlow += edgeLAX1920 - edgeLAX2021 == 0
airportFlow += edgeLAX2021 - edgeLAX2122 == 0
airportFlow += edgeLAX2122 - edgeLAX2223 == 0
airportFlow += edgeLAX2223 - edgeLAX2324 == 0


#SFO Constraints
airportFlow += edgeSFO12 - edgeSFO23 == 0
airportFlow += edgeSFO23 - edgeSFO34 == 0
airportFlow += edgeSFO34 - edgeSFO45 == 0
airportFlow += edgeSFO45 - edgeSFO56 == 0
airportFlow += edgeSFO56 - edgeSFO67 == 0
airportFlow += edgeSFO67 - edgeSFO78 == 0
airportFlow += edgeSFO78 - edgeSFO89 == 0
airportFlow += edgeLAX8SFO9 + edgeSFO89 - edgeSFO910 == 0
airportFlow += edgeLAX8SFO10 + edgeSFO910 - edgeSFO1011 == 0
airportFlow += edgeSFO1011 - edgeSFO1112 == 0
airportFlow += edgeSFO1112 - edgeSFO1213 == 0
airportFlow += edgeSFO1213 - edgeSFO1314 - edgeSFO13JFK21 == 0
airportFlow += edgeSFO1314 - edgeSFO1415 == 0
airportFlow += edgeSFO1415 - edgeSFO1516 == 0
airportFlow += edgeSFO1516 - edgeSFO1617 == 0
airportFlow += edgeSFO1617 - edgeSFO1718 == 0
airportFlow += edgeSFO1718 - edgeSFO1819 == 0
airportFlow += edgeSFO1819 - edgeSFO1920 == 0
airportFlow += edgeSFO1920 - edgeSFO2021 == 0
airportFlow += edgeSFO2021 - edgeSFO2122 == 0
airportFlow += edgeSFO2122 - edgeSFO2223 == 0
airportFlow += edgeSFO2223 - edgeSFO2324 == 0


#PHX Constraints
airportFlow += edgePHX12 - edgePHX23 == 0
airportFlow += edgePHX23 - edgePHX34 == 0
airportFlow += edgePHX34 - edgePHX45 == 0
airportFlow += edgePHX45 - edgePHX56 == 0
airportFlow += edgePHX56 - edgePHX67 == 0
airportFlow += edgePHX67 - edgePHX78 == 0
airportFlow += edgePHX78 - edgePHX89 == 0
airportFlow += edgeLAX7PHX9 + edgePHX89 - edgePHX910 == 0
airportFlow += edgePHX910 - edgePHX1011 - edgePHX10JFK18 == 0
airportFlow += edgePHX1011 - edgePHX1112 == 0
airportFlow += edgePHX1112 - edgePHX1213 == 0
airportFlow += edgePHX1213 - edgePHX1314 == 0
airportFlow += edgeLAX12PHX14 + edgePHX1314 - edgePHX1415 == 0
airportFlow += edgePHX1415 - edgePHX1516 == 0
airportFlow += edgePHX1516 - edgePHX1617 - edgePHX16JFK23 == 0
airportFlow += edgePHX1617 - edgePHX1718 == 0
airportFlow += edgeLAX17PHX18 + edgePHX1718 - edgePHX1819 == 0
airportFlow += edgePHX1819 - edgePHX1920 == 0
airportFlow += edgePHX1920 - edgePHX2021 == 0
airportFlow += edgePHX2021 - edgePHX2122 == 0
airportFlow += edgePHX2122 - edgePHX2223 == 0
airportFlow += edgePHX2223 - edgePHX2324 == 0


#SLC Constraints
airportFlow += edgeSLC12 - edgeSLC23 == 0
airportFlow += edgeSLC23 - edgeSLC34 == 0
airportFlow += edgeSLC34 - edgeSLC45 == 0
airportFlow += edgeSLC45 - edgeSLC56 == 0
airportFlow += edgeSLC56 - edgeSLC67 == 0
airportFlow += edgeSLC67 - edgeSLC78 == 0
airportFlow += edgeSLC78 - edgeSLC89 == 0
airportFlow += edgeLAX6SLC9 + edgeSLC89 - edgeSLC910 == 0
airportFlow += edgeSLC910 - edgeSLC1011 - edgeSLC10ATL16 == 0
airportFlow += edgeLAX8SLC11 + edgeSLC1011 - edgeSLC1112 - edgeSLC11ATL17 == 0
airportFlow += edgeSLC1112 - edgeSLC1213 - edgeSLC12JFK20 == 0
airportFlow += edgeLAX10SLC13 + edgeSLC1213 - edgeSLC1314 == 0
airportFlow += edgeSLC1314 - edgeSLC1415 - edgeSLC14DTW20 == 0
airportFlow += edgeSLC1415 - edgeSLC1516 == 0
airportFlow += edgeSLC1516 - edgeSLC1617 == 0
airportFlow += edgeLAX14SLC17 + edgeSLC1617 - edgeSLC1718 - edgeSLC17JFK23 == 0
airportFlow += edgeSLC1718 - edgeSLC1819 == 0
airportFlow += edgeSLC1819 - edgeSLC1920 == 0
airportFlow += edgeSLC1920 - edgeSLC2021 == 0
airportFlow += edgeSLC2021 - edgeSLC2122 == 0
airportFlow += edgeSLC2122 - edgeSLC2223 == 0
airportFlow += edgeSLC2223 - edgeSLC2324 == 0


#DFW Constraints
airportFlow += edgeDFW12 - edgeDFW23 == 0
airportFlow += edgeDFW23 - edgeDFW34 == 0
airportFlow += edgeDFW34 - edgeDFW45 == 0
airportFlow += edgeDFW45 - edgeDFW56 == 0
airportFlow += edgeDFW56 - edgeDFW67 == 0
airportFlow += edgeDFW67 - edgeDFW78 == 0
airportFlow += edgeDFW78 - edgeDFW89 == 0
airportFlow += edgeDFW89 - edgeDFW910 == 0
airportFlow += edgeDFW910 - edgeDFW1011 == 0
airportFlow += edgeDFW1011 - edgeDFW1112 == 0
airportFlow += edgeLAX7DFW12 + edgeDFW1112 - edgeDFW1213 == 0
airportFlow += edgeDFW1213 - edgeDFW1314 == 0
airportFlow += edgeLAX9DFW14 + edgeDFW1314 - edgeDFW1415 == 0
airportFlow += edgeDFW1415 - edgeDFW1516 - edgeDFW15MIA19 == 0
airportFlow += edgeDFW1516 - edgeDFW1617 == 0
airportFlow += edgeDFW1617 - edgeDFW1718 == 0
airportFlow += edgeDFW1718 - edgeDFW1819 == 0
airportFlow += edgeDFW1819 - edgeDFW1920 == 0
airportFlow += edgeDFW1920 - edgeDFW2021 == 0
airportFlow += edgeDFW2021 - edgeDFW2122 == 0
airportFlow += edgeDFW2122 - edgeDFW2223 == 0
airportFlow += edgeDFW2223 - edgeDFW2324 == 0


#IAH Constraints
airportFlow += edgeIAH12 - edgeIAH23 == 0
airportFlow += edgeIAH23 - edgeIAH34 == 0
airportFlow += edgeIAH34 - edgeIAH45 == 0
airportFlow += edgeIAH45 - edgeIAH56 == 0
airportFlow += edgeLAX1IAH6 + edgeIAH56 - edgeIAH67 == 0
airportFlow += edgeIAH67 - edgeIAH78 == 0
airportFlow += edgeIAH78 - edgeIAH89 == 0
airportFlow += edgeIAH89 - edgeIAH910 == 0
airportFlow += edgeIAH910 - edgeIAH1011 - edgeIAH10ATL13 == 0
airportFlow += edgeIAH1011 - edgeIAH1112 == 0
airportFlow += edgeIAH1112 - edgeIAH1213 == 0
airportFlow += edgeIAH1213 - edgeIAH1314 == 0
airportFlow += edgeIAH1314 - edgeIAH1415 == 0
airportFlow += edgeIAH1415 - edgeIAH1516 == 0
airportFlow += edgeIAH1516 - edgeIAH1617 == 0
airportFlow += edgeIAH1617 - edgeIAH1718 == 0
airportFlow += edgeIAH1718 - edgeIAH1819 == 0
airportFlow += edgeIAH1819 - edgeIAH1920 == 0
airportFlow += edgeIAH1920 - edgeIAH2021 == 0
airportFlow += edgeIAH2021 - edgeIAH2122 == 0
airportFlow += edgeIAH2122 - edgeIAH2223 == 0
airportFlow += edgeIAH2223 - edgeIAH2324 == 0


#DTW Constraints
airportFlow += edgeDTW12 - edgeDTW23 == 0
airportFlow += edgeDTW23 - edgeDTW34 == 0
airportFlow += edgeDTW34 - edgeDTW45 == 0
airportFlow += edgeDTW45 - edgeDTW56 == 0
airportFlow += edgeDTW56 - edgeDTW67 == 0
airportFlow += edgeDTW67 - edgeDTW78 == 0
airportFlow += edgeDTW78 - edgeDTW89 == 0
airportFlow += edgeDTW89 - edgeDTW910 == 0
airportFlow += edgeDTW910 - edgeDTW1011 == 0
airportFlow += edgeDTW1011 - edgeDTW1112 == 0
airportFlow += edgeDTW1112 - edgeDTW1213 == 0
airportFlow += edgeDTW1213 - edgeDTW1314 == 0
airportFlow += edgeLAX7DTW14 + edgeDTW1314 - edgeDTW1415 == 0
airportFlow += edgeDTW1415 - edgeDTW1516 - edgeDTW15ATL17 == 0
airportFlow += edgeDTW1516 - edgeDTW1617 - edgeDTW16ATL18 == 0
airportFlow += edgeDTW1617 - edgeDTW1718 == 0
airportFlow += edgeDTW1718 - edgeDTW1819 == 0
airportFlow += edgeLAX12DTW19 + edgeDTW1819 - edgeDTW1920 == 0
airportFlow += edgeSLC14DTW20 + edgeDTW1920 - edgeDTW2021 == 0
airportFlow += edgeDTW2021 - edgeDTW2122 - edgeDTW21JFK23 == 0
airportFlow += edgeDTW2122 - edgeDTW2223 == 0
airportFlow += edgeDTW2223 - edgeDTW2324 == 0


#ORD Constraints
airportFlow += edgeORD12 - edgeORD23 == 0
airportFlow += edgeORD23 - edgeORD34 == 0
airportFlow += edgeORD34 - edgeORD45 == 0
airportFlow += edgeORD45 - edgeORD56 == 0
airportFlow += edgeORD56 - edgeORD67 == 0
airportFlow += edgeLAX1ORD7 + edgeORD67 - edgeORD78 == 0
airportFlow += edgeORD78 - edgeORD89 == 0
airportFlow += edgeORD89 - edgeORD910 - edgeORD9ATL12 == 0
airportFlow += edgeORD910 - edgeORD1011 == 0
airportFlow += edgeORD1011 - edgeORD1112 == 0
airportFlow += edgeORD1112 - edgeORD1213 == 0
airportFlow += edgeORD1213 - edgeORD1314 == 0
airportFlow += edgeORD1314 - edgeORD1415 == 0
airportFlow += edgeORD1415 - edgeORD1516 == 0
airportFlow += edgeORD1516 - edgeORD1617 == 0
airportFlow += edgeORD1617 - edgeORD1718 == 0
airportFlow += edgeORD1718 - edgeORD1819 == 0
airportFlow += edgeORD1819 - edgeORD1920 == 0
airportFlow += edgeORD1920 - edgeORD2021 == 0
airportFlow += edgeORD2021 - edgeORD2122 == 0
airportFlow += edgeORD2122 - edgeORD2223 == 0
airportFlow += edgeORD2223 - edgeORD2324 == 0


#MIA Constraints
airportFlow += edgeMIA12 - edgeMIA23 == 0
airportFlow += edgeMIA23 - edgeMIA34 == 0
airportFlow += edgeMIA34 - edgeMIA45 == 0
airportFlow += edgeMIA45 - edgeMIA56 == 0
airportFlow += edgeMIA56 - edgeMIA67 == 0
airportFlow += edgeMIA67 - edgeMIA78 == 0
airportFlow += edgeMIA78 - edgeMIA89 == 0
airportFlow += edgeMIA89 - edgeMIA910 == 0
airportFlow += edgeMIA910 - edgeMIA1011 == 0
airportFlow += edgeMIA1011 - edgeMIA1112 == 0
airportFlow += edgeMIA1112 - edgeMIA1213 == 0
airportFlow += edgeMIA1213 - edgeMIA1314 == 0
airportFlow += edgeMIA1314 - edgeMIA1415 == 0
airportFlow += edgeMIA1415 - edgeMIA1516 == 0
airportFlow += edgeMIA1516 - edgeMIA1617 == 0
airportFlow += edgeMIA1617 - edgeMIA1718 == 0
airportFlow += edgeMIA1718 - edgeMIA1819 == 0
airportFlow += edgeDFW15MIA19 + edgeLAX11MIA19 + edgeMIA1819 - edgeMIA1920 == 0
airportFlow += edgeMIA1920 - edgeMIA2021 - edgeMIA20JFK23 == 0
airportFlow += edgeMIA2021 - edgeMIA2122 == 0
airportFlow += edgeLAX14MIA22 + edgeMIA2122 - edgeMIA2223 == 0
airportFlow += edgeMIA2223 - edgeMIA2324 == 0


#ATL Constraints
airportFlow += edgeATL12 - edgeATL23 == 0
airportFlow += edgeATL23 - edgeATL34 == 0
airportFlow += edgeATL34 - edgeATL45 == 0
airportFlow += edgeATL45 - edgeATL56 == 0
airportFlow += edgeATL56 - edgeATL67 == 0
airportFlow += edgeATL67 - edgeATL78 == 0
airportFlow += edgeATL78 - edgeATL89 == 0
airportFlow += edgeATL89 - edgeATL910 == 0
airportFlow += edgeATL910 - edgeATL1011 == 0
airportFlow += edgeATL1011 - edgeATL1112 == 0
airportFlow += edgeORD9ATL12 + edgeATL1112 - edgeATL1213 == 0
airportFlow += edgeIAH10ATL13 + edgeATL1213 - edgeATL1314 == 0
airportFlow += edgeATL1314 - edgeATL1415 - edgeATL14JFK16 == 0
airportFlow += edgeATL1415 - edgeATL1516 == 0
airportFlow += edgeSLC10ATL16 + edgeLAX9ATL16 + edgeATL1516 - edgeATL1617 == 0
airportFlow += edgeDTW15ATL17 + edgeSLC11ATL17 + edgeATL1617 - edgeATL1718 == 0
airportFlow += edgeDTW16ATL18 + edgeLAX11ATL18 + edgeATL1718 - edgeATL1819 == 0
airportFlow += edgeATL1819 - edgeATL1920 - edgeATL19JFK21 == 0
airportFlow += edgeLAX13ATL20 + edgeATL1920 - edgeATL2021 == 0
airportFlow += edgeATL2021 - edgeATL2122 - edgeATL21JFK23 - edge2ATL21JFK23 == 0
airportFlow += edgeLAX15ATL22 + edgeATL2122 - edgeATL2223 == 0
airportFlow += edgeATL2223 - edgeATL2324 == 0


#CLT Constraints
airportFlow += edgeCLT12 - edgeCLT23 == 0
airportFlow += edgeCLT23 - edgeCLT34 == 0
airportFlow += edgeCLT34 - edgeCLT45 == 0
airportFlow += edgeCLT45 - edgeCLT56 == 0
airportFlow += edgeCLT56 - edgeCLT67 == 0
airportFlow += edgeCLT67 - edgeCLT78 == 0
airportFlow += edgeLAX1CLT8 + edgeCLT78 - edgeCLT89 == 0
airportFlow += edgeCLT89 - edgeCLT910 - edgeCLT9JFK11 == 0
airportFlow += edgeCLT910 - edgeCLT1011 == 0
airportFlow += edgeCLT1011 - edgeCLT1112 == 0
airportFlow += edgeCLT1112 - edgeCLT1213 == 0
airportFlow += edgeCLT1213 - edgeCLT1314 - edgeCLT13JFK15 == 0
airportFlow += edgeCLT1314 - edgeCLT1415 == 0
airportFlow += edgeLAX7CLT15 + edgeCLT1415 - edgeCLT1516 == 0
airportFlow += edgeCLT1516 - edgeCLT1617 - edgeCLT16JFK18 == 0
airportFlow += edgeCLT1617 - edgeCLT1718 == 0
airportFlow += edgeCLT1718 - edgeCLT1819 == 0
airportFlow += edgeCLT1819 - edgeCLT1920 == 0
airportFlow += edgeCLT1920 - edgeCLT2021 == 0
airportFlow += edgeCLT2021 - edgeCLT2122 == 0
airportFlow += edgeCLT2122 - edgeCLT2223 == 0
airportFlow += edgeCLT2223 - edgeCLT2324 == 0


#JFK Constraints
airportFlow += edgeJFK12 - edgeJFK23 == 0
airportFlow += edgeJFK23 - edgeJFK34 == 0
airportFlow += edgeJFK34 - edgeJFK45 == 0
airportFlow += edgeJFK45 - edgeJFK56 == 0
airportFlow += edgeJFK56 - edgeJFK67 == 0
airportFlow += edgeJFK67 - edgeJFK78 == 0
airportFlow += edgeJFK78 - edgeJFK89 == 0
airportFlow += edgeJFK89 - edgeJFK910 == 0
airportFlow += edgeJFK910 - edgeJFK1011 == 0
airportFlow += edgeCLT9JFK11 + edgeJFK1011 - edgeJFK1112 == 0
airportFlow += edgeJFK1112 - edgeJFK1213 == 0
airportFlow += edgeJFK1213 - edgeJFK1314 == 0
airportFlow += edgeJFK1314 - edgeJFK1415 == 0
airportFlow += edgeCLT13JFK15 + edgeLAX7JFK15 + edgeJFK1415 - edgeJFK1516 == 0
airportFlow += edgeATL14JFK16 + edgeLAX8JFK16 + edgeJFK1516 - edgeJFK1617 == 0
airportFlow += edgeJFK1617 - edgeJFK1718 == 0
airportFlow += edgeCLT16JFK18 + edgePHX10JFK18 + edgeJFK1718 - edgeJFK1819 == 0
airportFlow += edgeJFK1819 - edgeJFK1920 == 0
airportFlow += edgeSLC12JFK20 + edgeJFK1920 - edgeJFK2021 == 0
airportFlow += edgeSFO13JFK21 + edgeATL19JFK21 + edgeLAX12JFK21 + edgeJFK2021 - edgeJFK2122 == 0
airportFlow += edgeLAX13JFK22 + edgeJFK2122 - edgeJFK2223 == 0
airportFlow += edgeMIA20JFK23 + edgeDTW21JFK23 + edgePHX16JFK23 + edge2ATL21JFK23 + edgeATL21JFK23 + edgeSLC17JFK23 + edgeLAX15JFK23 + edgeJFK2223 - edgeJFK2324 == 0


#Misc Constraints
airportFlow += edgeLAX12 - edgeJFK2324 == 0


#print max flow
status = airportFlow.solve()
print(p.value(airportFlow.objective))

