This folder contains the "Trip Attributes" metrics for the Zone Activity zones within the named analysis.

The "Trip Attributes" include Travel Time, Trip Length, Trip Speed and Trip Circuity. For Zone Activity analyses, these attributes apply to the entire trip. For each attribute, the average value and a distribution are provided. Distribution bins are customizable.


DEFINITIONS
===========
Travel Time: This is the trip time in seconds for the full lenght of trips starting at an origin zone and ending at a destination zone. While the travel time is calculated in seconds, the distribution bins are in minutes.

Trip Length: This is the trip length delivered in the chosen unit of measurement (miles or kilometers) starting at an origin zone and ending at a destination zone. It is dependent on the Trip Type (Unlocked or Locked to Route). Locked to Route trips are generally longer than Unlocked trips.

Trip Speed: This is the average speed delivered in the chosen unit of measurement (mph or kph) for the full length of trips starting at an origin zone and ending at a destination zone. It is dependent on the Trip Type (Unlocked or Locked to Route). Locked to Route trips generally have a slower average speed than Unlocked trips because they are longer.

Trip Circuity: This is the average ratio of the length of the trip to the crows' flight (or direct) distance between the end points of the trips starting at an origin zone and ending at a destination zone.


TERMS
=====
Pass-Through: A zone setting indicating how to analyze how trips interact with the zone. Zones marked as pass-through use trips that pass through the zone but do not start or stop in it. Zones not marked as pass-through use trips that start or stop in the zone.

Zone Direction: A pass-through zone can have applied direction which limits the trips analyzed for the zone: only trips that pass through the zone within -20/+20 degrees of the direction will be analyzed for the zone. Values are provided in degrees from 0 to 359, where 0 is due north, 90 is east, 180 is due south, etc. A value of "Null" refers to zones with no applied direction therefore all trips that pass through the zone will be used.

Vehicle Weight: The weight of the vehicles analyzed. Weight values can either be “Medium” or “Heavy”. This column is present only if the commercial analysis is segmented by weight class.


OUTPUT UNIT TERMS
=================
StreetLight Volume: The estimated trip counts as calculated by StreetLight Data's machine learning algorithm.

StreetLight Index: The relative trip activity. The StreetLight Index does not indicate the actual number of trips or vehicles. Trip Index values for different modes of travel (All Vehicles, Trucks, Bicycle, Pedestrian, etc.)  weight classes (such as Trucks Heavy-Duty/Medium-Duty), and countries are based on different sample populations and therefore cannot be compared with each other.

StreetLight Calibrated Index: The estimated number of trips or vehicles derived from StreetLight Index calibrated with StreetLight AADT or user-input counts.

StreetLight Sample Trip Counts: StreetLight sample trip counts for the zone (or set of zones) for all days in the entire data period.

*Note that, while most output units are represented as an average day per its day type definition, Trip Counts are not converted to an average day. For example, a Trip Count value of 100 for O-D pair A and B for average weekday in March 2017 means that the sum of all trips used from StreetLight data set from all the weekdays in March 2017 is 100.

*More information of the output unit methodology can be found in StreetLight Data's Support Center (https://support.streetlightdata.com).


FILES
=====
za_trip_*.csv
=============
This file contains "Trip Attributes" for the zones.

The fields are:
- Mode of Travel: Mode of travel analyzed.
- Intersection Type: Type of trips analyzed--dependent on whether the zone Is Pass-Through. If Zone Is Pass-Through is "Yes", then Intersection Type = "Trip Pass-Through". If Zone Is Pass-Through is "No", then there is a row each for Intersection Type = "Trip Start" and "Trip End".
- Zone ID: Numeric ID for the zone as provided by the user.
- Zone Name: Name for the zone.
- Zone Is Pass-Through: Indicates if the zone is pass-through or not as described above in the Terms.
- Zone Direction (degrees): This refers to the direction in which trips pass through the zone as described above in the Terms.
- Zone is Bi-Direction: Indicates if the zones are bi-directional. Values are "Yes" or "No".
- Day Type: All Days (traffic from Monday through Sunday), and other day type traffic segmentation as defined by user.
- Day Part: Segments of the day defined by the user in intervals of hours to analyze traffic (All Day is always included as entire 24 hours).
- Zone Traffic: The volume of trips starting in, passing through, or ending in the zone based on the zone Mode of Travel, Interue.
- Avg Travel Time (sec): The average trip time in seconds for low network factor* trips starting in, passing through, or ending in the zone based on the zone type.
- Avg All Travel Time (sec): The average trip time in seconds for all trips starting in, passing through, or ending in the zone based on the zone type.
- Avg Trip Length (mi or km): The average trip length in miles for low network factor* trips starting in, passing through, or ending in the zone based on the zone type.
- Avg All Trip Length (mi or km): The average trip length in miles for all trips starting in, passing through, or ending in the zone based on the zone type.
- Avg Trip Speed (mph or kph): The average trip speed in mph for low network factor* trips starting in, passing through, or ending in the zone based on the zone type.
- Avg All Trip Speed (mph or kph): The average trip speed in mph for all trips starting in, passing through, or ending in the zone based on the zone type.
- Avg All Circuity: The average circuity for all trips starting in, passing through, or ending in the zone based on the zone type.
- Travel Time X-Y min (percent): The percent of all trips starting in, passing through, or ending in the zones based on the zone type for which the trip time is in the bin from X to Y minutes.**
- Trip Length X-Y mi or km (percent): The percent of all trips starting in, passing through, or ending in the zones based on the zone type for which the trip length is in the bin from X to Y miles.**
- Trip Speed X-Y mph or kph (percent): The percent of all trips starting in, passing through, or ending in the zones based on the zone type for which the average speed is in the bin from X to Y mph.**
- Trip Circuity X-Y (percent): The percent of all trips starting in, passing through, or ending in the zones based on the zone type for which the trip circuity is in the bin from X to Y.**

*Network factor is defined as unlocked trip length / distance (trip point in origin zone, trip point in destination zone). Low network is less than 4. This is different from circuity in that it is always calculated using the unlocked (or connect the points) trip length, not the Locked to Route trip length.
**Each distribution bin is inclusive of the start value X and exclusive of the end value Y. For example, the bin (5-10) contains values greater than or equal to 5.0 and less than 10.0.


NOTES
=====
ZA with No Values
=================
If the output unit values for a zone for a specific time period (e.g. Average Weekday, Early AM) are below StreetLight's significance threshold, no results will be shown in the za_*.csv file.

Day Part Calculations
=====================
The Day Part calculations are done in relation to the zones used in the analysis. The Day Part is determined by when trips either Start in the zone or pass by the centroid of the zone, if the zone is designated as pass-through.

Trip Type
=========
The file Analysis.txt specifies the type of trips used in the analysis: Locked to Route Trips or Unlocked Trips. Unlocked Trips may not consistently align with roads depending upon the device ping rate, the speed of the vehicle, and how curvy the roads are. Locked to Route Trips address this by aligning to the road segments of the most likely path taken for the set of points that comprise the Unlocked Trip.


Copyright © 2011 - 2021, StreetLight Data, Inc. All rights reserved.
