import pandas as pd
import os
import pandas as pd


df = pd.read_csv('ALLROADS_CRASH_SEVERE REDUCED.csv')


#get the Intersection data
MultipleIntersection = df[df['Road geometry'] == 'Multiple intersection                    ']
TIntersection = df[df['Road geometry'] == 'T intersection                      ']
CrossIntersection = df[df['Road geometry'] == 'Cross intersection                     ']
YIntersection = df[df['Road geometry'] == 'Y intersection                      ']


MultipleIntersection.to_csv("ALLROADS_CRASH_SEVERE_MULTIPLE_INTERSECTION.csv", index=False)
TIntersection.to_csv("ALLROADS_CRASH_SEVERE_T_INTERSECTION.csv", index=False)
CrossIntersection.to_csv("ALLROADS_CRASH_SEVERE_Cross_INTERSECTION.csv", index=False)
YIntersection.to_csv("ALLROADS_CRASH_SEVERE_Y_INTERSECTION.csv", index=False)
