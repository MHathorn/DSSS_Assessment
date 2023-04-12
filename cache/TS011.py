"""
TS011 - Households by deprivation dimensions

Code autogenerated by UKCensusAPI
(https://github.com/virgesmith/UKCensusAPI)
"""

# This code requires an API key, see the README.md for details

# Query url:
# https://www.nomisweb.co.uk/api/v01/dataset/NM_2031_1.data.tsv?C2021_DEP_6=0...5&MEASURES=20100&date=latest&geography=&select=GEOGRAPHY_CODE%2CC2021_DEP_6%2COBS_VALUE

import ukcensusapi.Nomisweb as CensusApi

api = CensusApi.Nomisweb("cache")
table = "TS011"
table_internal = "NM_2031_1"
query_params = {}
query_params["date"] = "latest"
query_params["select"] = "GEOGRAPHY_CODE,C2021_DEP_6,OBS_VALUE"
query_params["C2021_DEP_6"] = "0...5"
query_params["MEASURES"] = "20100"
query_params["geography"] = ""
TS011 = api.get_data(table, query_params)
