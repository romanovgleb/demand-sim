'''
- spawn 3 demand points
- have a store with two couriers
- serve 1 + 2 (batch) orders
- display stats
'''

'''
tests:

'''


import shapely
import geopandas as gpd

class Supply:
    def __init__(self, title, amount, location):
        # type = [foot, auto]
        self.title = title
        self.amount = amount
        self.location = location

class Demand:
    def __init__(self, gmv, priority, location):
        # type = ['stationary', 'transfer', 'pass-through']
        self.gmv = gmv
        self.priority = priority
        self.location = location

def generate_demand_events(source_gdf):
    demand_gdf = gpd.GeoDataFrame()
    


'priority queue'


st = Supply(title='sample store', amount=2, location=shapely.geometry.Point(0, 0))
print(st.title, st.amount, st.location, sep='\n')

# first - generate demand events, then move from one event to another

