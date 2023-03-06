import json
import pandas as pd

def calculate_lat(row):
    if not pd.isnull(row["LAT"]):
        return row["LAT"]
    else:
        return row["Google Lat, Lon"].split(", ")[0]


def calculate_lon(row):
    if not pd.isnull(row["LON"]):
        return row["LON"]
    else:
        return row["Google Lat, Lon"].split(", ")[1]

def get_ospool_project_institutions() -> set:

    ospool_institutions = set()
    ospool_projects = None
    all_osgconnect_projects = None

    with open("ospool_projects.json", "r") as fp:
        ospool_projects = json.load(fp)

    with open("all_osgconnect_projects.json", "r") as fp:
        all_osgconnect_projects = json.load(fp)

    for name, value in all_osgconnect_projects.items():
        if name in ospool_projects:
            ospool_institutions.add(value['Organization'])

    return ospool_institutions