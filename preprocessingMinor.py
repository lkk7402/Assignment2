import pandas as pd
import os
import pandas as pd


df = pd.read_csv('INTERSECTIONS_CRASH_MINOR_REDUCED.csv')


#get the Intersection data
MultipleIntersection = df[df['Road geometry'] == 'Multiple intersection                    ']
TIntersection = df[df['Road geometry'] == 'T intersection                      ']
CrossIntersection = df[df['Road geometry'] == 'Cross intersection                     ']
YIntersection = df[df['Road geometry'] == 'Y intersection                      ']

#print to csv file
MultipleIntersection.to_csv("CRASH_MINOR_MULTIPLE_INTERSECTION.csv", index=False)
TIntersection.to_csv("CRASH_MINOR_T_INTERSECTION.csv", index=False)
CrossIntersection.to_csv("CRASH_MINOR_Cross_INTERSECTION.csv", index=False)
YIntersection.to_csv("CRASH_MINOR_Y_INTERSECTION.csv", index=False)
