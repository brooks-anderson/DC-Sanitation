# -*- coding: utf-8 -*-
"""
This script builds and updates GeoDataFrames and .shp files of 311 request from 
opendata.dc.gov.

311 Request DataFrames:
    * pest_request
    * trash_collection
    * recycle_collection
    * illegal_dumping
    * public_can collection
    * sanitation_enforce

311 Request columns:
    SERVICECODEDESCRIPTION - Type of 311 Request
    SERVICECALLCOUNT - number of calls for incident
    ADDDATE - date call was placed
    RESOLUTIONDATE - date incident was resolved
    STREETADDRESS - not currently used
    ZIPCODE - not currently used
    WARD - Ward where incident occurred
    XCOORD - ???
    YCOORD - ???
    LATITUDE
    LONGITUDE
"""