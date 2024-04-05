import databento as db
from datetime import datetime

now = datetime.now()

def download_data():

    client = db.Historical("DATA_BENTO_API")
    data = client.timeseries.get_range(
        dataset="GLBX.MDP3",
        stype_in='continuous',
        symbols=["ES.v.0"],
        schema="ohlcv-1m",
        start="2017-05-21T00:00:00",
        end="2023-09-16T00:00:00",
    )

    data.to_csv('raw_dbento_es_1m.csv')

def list_schemas():
    client = db.Historical("DATA_BENTO_API")

    schemas = client.metadata.list_schemas(dataset="GLBX.MDP3")
    print(schemas)   

def get_data_cost():

    client = db.Historical("DATA_BENTO_API")

    cost = client.metadata.get_cost(
        dataset="GLBX.MDP3",
        stype_in='continuous',
        symbols=["ES.v.0"],
        schema="ohlcv-1m",
        start="2017-05-21T00:00:00",
        end="2023-9-16T00:00:00+00:00",
    )
    print(cost)

get_data_cost()

