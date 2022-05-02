This folder contains the "Traveler Attributes" Metrics for the Origin-Destination trips between the zones of the named analysis.

The "Traveler Attributes" include Trip Purpose, Household Income, Education of Head of Household, Race, and Family Status. For O-D Analyses, these attributes apply to trips that start at the Origin Zones and end at the Destination Zones.

Information about demographics is based on the 2010 US Census and 2017 data from Manifold SuperDemographics (for Canada).

DEFINITIONS
===========
Trip Purpose: This represents whether travelers are making Home-Based Work, Home-Based Other or Non-Home Based trips.

Household Income: This represents what household income bracket travelers are in. 

Education of Head of Household: This represents the highest education level of the head of the household for travelers.

Race: This represents the self-identified race of travelers. 

Family Status: This represents the household family status of travelers. 

TERMS
=====
Origin zone: Trips analyzed that started in or initially passed through any of the origin zones.

Destination zone: Trips analyzed that ended in or passed through any of the destination zones after starting in or passing through an origin zone.

Pass-Through: A zone setting indicating how to analyze how trips interact with the zone. Zones marked as pass-through use trips that pass through the zone but do not start or stop in it. Zones not marked as pass-through use trips that start or stop in the zone.

Zone Direction: A pass-through zone can have applied direction which limits the trips analyzed for the zone: only trips that pass through the zone within -20/+20 degrees of the direction will be analyzed for the zone. Values are provided in degrees from 0 to 359, where 0 is due north, 90 is east, 180 is due south, etc. A value of "Null" refers to zones with no applied direction therefore all trips that pass through the zone will be used.


OUTPUT UNIT TERMS
=================
StreetLight Volume: The estimated trip counts as calculated by StreetLight Data's machine learning algorithm.

StreetLight Index: The relative trip activity. The StreetLight Index does not indicate the actual number of trips or vehicles. Trip Index values for different modes of travel (All Vehicles, Trucks, Bicycle, Pedestrian, etc.)  weight classes (such as Trucks Heavy-Duty/Medium-Duty), and countries are based on different sample populations and therefore cannot be compared with each other. 

StreetLight Calibrated Index: The estimated number of trips or vehicles derived from the StreetLight Index. Calibration is performed with either StreetLight AADT or user-provided counts.

StreetLight Sample Trip Counts: The total StreetLight sample trip counts for the zone (or set of zones) for all days in the entire data period.

*Note that, while most output units are represented as an average day per its day type definition, Trip Counts are not converted to an average day but rather represent the total Trip Counts. For example, a Trip Count value of 100 for an O-D pair, on an average weekday in March 2017, represents the sum of all trips used from the StreetLight data set for all the weekdays in March 2017.

*More information of the output unit methodology can be found in StreetLight Data's Support Center (https://support.streetlightdata.com).


FILES
=====
od_traveler_*.csv
=================
This file contains the Trip Purpose and Demographics for the O-D Analysis.

The fields are:
- Mode of Travel: Mode of travel analyzed.
- Origin zone ID: Numeric ID for the origin zone as provided by the user.
- Origin zone Name: Name for the origin zone.
- Origin zone Is Pass-Through: Indicates if the origin zone is pass-through or not as described above under Terms. Is either marked as “Yes” or “No."
- Origin zone Direction (degrees): This refers to the direction in which trips pass through the origin zone as described above under Terms.
- Origin zone is Bi-Direction: Indicates if the zones are bi-directional. Is either marked as “Yes” or “No."
- Destination zone ID: Numeric ID for the destination zone as provided by the user.
- Destination zone Name: Name for the destination zone.
- Destination zone Is Pass-Through: Indicates if the destination zone is pass-through or not as described above under Terms. Is either marked as “Yes” or “No."
- Destination zone Direction (degrees): This refers to the direction in which trips pass through the destination zone as described above in the Terms.
- Destination zone is Bi-Direction: Indicates if the zones are bi-directional. Is either marked as “Yes” or “No."
- Day Type: All Days (traffic from Monday through Sunday), and other day type traffic segmentation as defined by user.
- Day Part: Segments of the day defined by the user in intervals of hours to analyze traffic (All Day is always included as entire 24 hours). The day parts reflect the local time at the origin zone.
- O-D Traffic: The volume of trips from the origin zone to the destination zone, measured using one of the output units described above under the Output Unit Terms.

For analysis run with Location-Based Services data source, the Trip Purpose fields are:
- Purpose HBW (percent): Percent of travel that is home-based work (i.e. home-to-work or work-to-home).
- Purpose HBO (percent): Percent of travel that is home-based other (i.e. from or to home, but not home-based work).
- Purpose NHB (percent): Percent of travel that is not home-based (i.e. not from or to home).

For analysis run with Navigation-GPS data source, the Simple Trip Purpose fields are:
- Purpose RESI to RESI (percent): Percent of travel from a residential area to another residential area for all trips starting at the origin zone and ending at the destination zone.
- Purpose RESI to COMM (percent): Percent of travel from a residential area to a commercial area for all trips starting at the origin zone and ending at the destination zone.
- Purpose RESI to OTHER (percent): Percent of travel from a residential area to a known non-residential / non-commercial area (such as a church) for all trips starting at the origin zone and ending at the destination zone.
- Purpose COMM to RESI (percent): Percent of travel from a commercial area to a residential area for all trips starting at the origin zone and ending at the destination zone.
- Purpose COMM to COMM (percent): Percent of travel from a commercial area to another commercial area for all trips starting at the origin zone and ending at the destination zone.
- Purpose COMM to OTHER (percent): Percent of travel from a commercial area to a known non-residential / non-commercial area for all trips starting at the origin zone and ending at the destination zone.
- Purpose OTHER to RESI (percent): Percent of travel from a known non-residential / non-commercial area to a residential area for all trips starting at the origin zone and ending at the destination zone.
- Purpose OTHER to COMM (percent): Percent of travel from a known non-residential / non-commercial area to a commercial area for all trips starting at the origin zone and ending at the destination zone.
- Purpose OTHER to OTHER (percent): Percent of travel from a known non-residential / non-commercial area  to another non-residential / non-commercial area for all trips starting at the origin zone and ending at the destination zone.
- Purpose UNKNOWN (percent):  Percent of travel for which the purpose is unknown for all trips starting at the origin zone and ending at the destination zone.

For US analysis, the Demographics fields are:
- Income Less than 20K (percent): Percent of travelers that have a household income of less than $20,000, for all trips starting at the origin zone and ending at the destination zone.
- Income 20K to 35K (percent): Percent of travelers that have a household income of $20,000 to $35,000, for all trips starting at the origin zone and ending at the destination zone.
- Income 35K to 50K (percent): Percent of travelers that have a household income of $35,000 to $50,000, for all trips starting at the origin zone and ending at the destination zone.
- Income 50K to 75K (percent): Percent of travelers that have a household income of $50,000 to $75,000, for all trips starting at the origin zone and ending at the destination zone.
- Income 75K to 100K (percent): Percent of travelers that have a household income of $75,000 to $100,000, for all trips starting at the origin zone and ending at the destination zone.
- Income 100K to 125K (percent): Percent of travelers that have a household income of $100,000 to $125,000, for all trips starting at the origin zone and ending at the destination zone.
- Income 125K to 150K (percent): Percent of travelers that have a household income of $125,000 to $150,000, for all trips starting at the origin zone and ending at the destination zone.
- Income 150K to 200K (percent): Percent of travelers that have a household income of $150,000 to $200,000, for all trips starting at the origin zone and ending at the destination zone.
- Income More than 200K (percent): Percent of travelers that have a household income of more than $200,000, for all trips starting at the origin zone and ending at the destination zone.
- No High School Diploma (percent): Percent of travelers over the age of 25 of which the highest level of education is below high school completion (diploma not awarded), for all trips starting at the origin zone and ending at the destination zone.
- High School Diploma (percent): Percent of travelers over the age of 25 of which the highest level of education is completion of high school, for all trips starting at the origin zone and ending at the destination zone.
- Some College (percent): Percent of travelers over the age of 25 of which the highest level of education is some college (but bachelor's degree not awarded), including associate's degree, for all trips starting at the origin zone and ending at the destination zone.
- Bachelors Degree (percent): Percent of travelers over the age of 25 of which the highest level of education is the completion of a bachelor's college, for all trips starting at the origin zone and ending at the destination zone.
- Graduate Degree (percent): Percent of travelers over the age of 25 of which the highest level of education is beyond completion of college, for all trips starting at the origin zone and ending at the destination zone.
- White (percent): Percent of travelers that self-identify as White, for all trips starting at the origin zone and ending at the destination zone.
- Black (percent): Percent of travelers that self-identify as Black or African American, for all trips starting at the origin zone and ending at the destination zone.
- Indian (percent): Percent of travelers that self-identify as American Indian or Alaska Native, for all trips starting at the origin zone and ending at the destination zone.
- Asian (percent): Percent of travelers that self-identify as Asian, for all trips starting at the origin zone and ending at the destination zone.
- Islander (percent): Percent of travelers that self-identify as Native Hawaiian or Other Pacific Islander, for all trips starting at the origin zone and ending at the destination zone.
- Other Race (percent): Percent of travelers that self-identify as Some Other Race, for all trips starting at the origin zone and ending at the destination zone.
- Multiple Races (percent): Percent of travelers that self-identify as Two or More Races, for all trips starting at the origin zone and ending at the destination zone.
- Hispanic (percent): Percent of travelers that self-identify as of Hispanic or Latino Origin, for all trips starting at the origin zone and ending at the destination zone.
- With Kids (percent): Percent of travelers that live in households with children, for all trips starting at the origin zone and ending at the destination zone.
- With No Kids (percent): Percent of travelers that live in households with no children, for all trips starting at the origin zone and ending at the destination zone.
- With Kids under 6 years (percent): Percent of travelers that live in households with children under the age of 6, for all trips starting at the origin zone and ending at the destination zone.
- With Kids between 6-17 years (percent): Percent of travelers that live in households with children between the ages of 6 and 17, for all trips starting at the origin zone and ending at the destination zone.

For Canada projects, the demographics fields are:
- Income Less than 10K (percent): Percent of travelers that have a household income of less than C$10,000, for all trips starting at the origin zone and ending at the destination zone.
- Income 10K to 20K (percent): Percent of travelers that have a household income of C$10,000 to C$20,000, for all trips starting at the origin zone and ending at the destination zone.
- Income 20K to 30K (percent): Percent of travelers that have a household income of C$20,000 to C$30,000, for all trips starting at the origin zone and ending at the destination zone.
- Income 30K to 40K (percent): Percent of travelers that have a household income of C$30,000 to C$40,000, for all trips starting at the origin zone and ending at the destination zone.
- Income 40K to 50K (percent): Percent of travelers that have a household income of C$40,000 to C$50,000, for all trips starting at the origin zone and ending at the destination zone.
- Income 50K to 60K (percent): Percent of travelers that have a household income of C$50,000 to C$60,000, for all trips starting at the origin zone and ending at the destination zone.
- Income 60K to 80K (percent): Percent of travelers that have a household income of C$60,000 to C$80,000, for all trips starting at the origin zone and ending at the destination zone.
- Income 80K to 100K (percent): Percent of travelers that have a household income of C$80,000 to C$100,000, for all trips starting at the origin zone and ending at the destination zone.
- Income More than 100K (percent): Percent of travelers that have a household income of more than C$100,000, for all trips starting at the origin zone and ending at the destination zone.
- No High School Diploma (percent): Percent of travelers over the age of 25 of which the highest level of education is below high school completion (diploma not awarded), for all trips starting at the origin zone and ending at the destination zone.
- High School Diploma (percent): Percent of travelers over the age of 25 of which the highest level of education is completion of high school, for all trips starting at the origin zone and ending at the destination zone.
- Some College (percent): Percent of travelers over the age of 25 of which the highest level of education is some college (but bachelor's degree not awarded), including associate's degree, for all trips starting at the origin zone and ending at the destination zone.
- Bachelors Degree (percent): Percent of travelers over the age of 25 of which the highest level of education is the completion of a bachelor's college, for all trips starting at the origin zone and ending at the destination zone.
- Graduate Degree (percent): Percent of travelers over the age of 25 of which the highest level of education is beyond completion of college, for all trips starting at the origin zone and ending at the destination zone.
- White (percent): Percent of travelers that self-identify as White, for all trips starting at the origin zone and ending at the destination zone.
- Black (percent): Percent of travelers that self-identify as Black or African American, for all trips starting at the origin zone and ending at the destination zone.
- Asian (percent): Percent of travelers that self-identify as Asian, for all trips starting at the origin zone and ending at the destination zone.
- Other Race (percent): Percent of travelers that self-identify as Some Other Race, for all trips starting at the origin zone and ending at the destination zone.
- Multiple Races (percent): Percent of travelers that self-identify as Two or More Races, for all trips starting at the origin zone and ending at the destination zone.
- Hispanic (percent): Percent of travelers that self-identify as of Hispanic or Latino Origin, for all trips starting at the origin zone and ending at the destination zone.
- With Kids (percent): Percent of travelers that live in households with children, for all trips starting at the origin zone and ending at the destination zone.
- With No Kids (percent): Percent of travelers that live in households with no children, for all trips starting at the origin zone and ending at the destination zone.

za_traveler_*.csv
=================
This file contains the Trip Purpose and Demographics for travel at the Zones.

The fields are:
- Mode of Travel: Mode of travel analyzed.
- Zone Type: Indicates if the zone is an origin or destination zone for this analysis.
- Zone ID: Numeric ID for the zone as provided by the user.
- Zone Name: Name for the zone.
- Zone Is Pass-Through: Indicates if the zone is marked as pass-through or not as described above under Terms. Is either marked as “Yes” or “No."
- Zone Direction (degrees): This refers to the direction in which trips pass through the zone as described above in the Terms.
- Zone is Bi-Direction: Indicates if the zones are bi-directional. Is either marked as "Yes" or "No".
- Day Type: All Days (traffic from Monday through Sunday), and other day type traffic segmentation as defined by user.
- Day Part: Segments of the day defined by the user in intervals of hours to analyze traffic (All Day is always included as entire 24 hours). The day parts reflect the local time at the origin zone.
- Zone Traffic: The volume of trips starting in or ending in the zone, or trips that pass-through the zone-- based on whether the zone is or is not pass-through as described above under Terms. Zone traffic is measured in its chosen output unit as described above under Output Unit Terms.

For analysis run with Location-Based Services data source, the Trip Purpose fields are:
- Purpose HBW (percent): Percent of travel that is home-based work (i.e. home-to-work or work-to-home).
- Purpose HBO (percent): Percent of travel that is home-based other (i.e. from or to home, but not home-based work).
- Purpose NHB (percent): Percent of travel that is not home-based (i.e. not from or to home).

For analysis run with Navigation-GPS data source, the Simple Trip Purpose fields are:
- Purpose RESI to RESI (percent): Percent of travel from a residential area to another residential area for all trips based on the zone intersection type value.
- Purpose RESI to COMM (percent): Percent of travel from a residential area to a commercial area for all trips based on the zone intersection type value.
- Purpose RESI to OTHER (percent): Percent of travel from a residential area to a known non-residential / non-commercial area (such as a church) for all trips based on the zone intersection type value.
- Purpose COMM to RESI (percent): Percent of travel from a commercial area to a residential area for all trips based on the zone intersection type value.
- Purpose COMM to COMM (percent): Percent of travel from a commercial area to another commercial area for all trips based on the zone intersection type value.
- Purpose COMM to OTHER (percent): Percent of travel from a commercial area to a known non-residential / non-commercial area for all trips based on the zone intersection type value.
- Purpose OTHER to RESI (percent): Percent of travel from a known non-residential / non-commercial area to a residential area for all trips based on the zone intersection type value.
- Purpose OTHER to COMM (percent): Percent of travel from a known non-residential / non-commercial area to a commercial area for all trips based on the zone intersection type value.
- Purpose OTHER to OTHER (percent): Percent of travel from a known non-residential / non-commercial area  to another non-residential / non-commercial area for all trips based on the zone intersection type value.
- Purpose UNKNOWN (percent):  Percent of travel for which the purpose is unknown for all trips based on the zone intersection type value.

For US analysis, the Demographics fields are:
- Income Less than 20K (percent): Percent of travelers that have a household income of less than $20,000, for all trips based on the zone intersection type value.
- Income 20K to 35K (percent): Percent of travelers that have a household income of $20,000 to $35,000, for all trips based on the zone intersection type value.
- Income 35K to 50K (percent): Percent of travelers that have a household income of $35,000 to $50,000, for all trips based on the zone intersection type value.
- Income 50K to 75K (percent): Percent of travelers that have a household income of $50,000 to $75,000, for all trips based on the zone intersection type value.
- Income 75K to 100K (percent): Percent of travelers that have a household income of $75,000 to $100,000, for all trips based on the zone intersection type value.
- Income 100K to 125K (percent): Percent of travelers that have a household income of $100,000 to $125,000, for all trips based on the zone intersection type value.
- Income 125K to 150K (percent): Percent of travelers that have a household income of $125,000 to $150,000, for all trips based on the zone intersection type value.
- Income 150K to 200K (percent): Percent of travelers that have a household income of $150,000 to $200,000, for all trips based on the zone intersection type value.
- Income More than 200K (percent): Percent of travelers that have a household income of more than $200,000, for all trips based on the zone intersection type value.
- No High School Diploma (percent): Percent of travelers over the age of 25 of which the highest level of education is below high school completion (diploma not awarded), for all trips based on the zone intersection type value.
- High School Diploma (percent): Percent of travelers over the age of 25 of which the highest level of education is completion of high school, for all trips based on the zone intersection type value.
- Some College (percent): Percent of travelers over the age of 25 of which the highest level of education is some college (but bachelor's degree not awarded), including associate's degree, for all trips based on the zone intersection type value.
- Bachelors Degree (percent): Percent of travelers over the age of 25 of which the highest level of education is the completion of a bachelor's college, for all trips based on the zone intersection type value.
- Graduate Degree (percent): Percent of travelers over the age of 25 of which the highest level of education is beyond completion of college, for all trips based on the zone intersection type value.
- White (percent): Percent of travelers that self-identify as White, for all trips based on the zone intersection type value.
- Black (percent): Percent of travelers that self-identify as Black or African American, for all trips based on the zone intersection type value.
- Indian (percent): Percent of travelers that self-identify as American Indian or Alaska Native, for all trips based on the zone intersection type value.
- Asian (percent): Percent of travelers that self-identify as Asian, for all trips based on the zone intersection type value.
- Islander (percent): Percent of travelers that self-identify as Native Hawaiian or Other Pacific Islander, for all trips based on the zone intersection type value.
- Other Race (percent): Percent of travelers that self-identify as Some Other Race, for all trips based on the zone intersection type value.
- Multiple Races (percent): Percent of travelers that self-identify as Two or More Races, for all trips based on the zone intersection type value.
- Hispanic (percent): Percent of travelers that self-identify as of Hispanic or Latino Origin, for all trips based on the zone intersection type value.
- With Kids (percent): Percent of travelers that live in households with children, for all trips based on the zone intersection type value.
- With No Kids (percent): Percent of travelers that live in households with no children, for all trips based on the zone intersection type value.
- With Kids under 6 years (percent): Percent of travelers that live in households with children under the age of 6, for all trips based on the zone intersection type value.
- With Kids between 6-17 years (percent): Percent of travelers that live in households with children between the ages of 6 and 17, for all trips based on the zone intersection type value.

For Canada projects, the demographics fields are:
- Income Less than 10K (percent): Percent of travelers that have a household income of less than C$10,000, for all trips based on the zone intersection type value.
- Income 10K to 20K (percent): Percent of travelers that have a household income of C$10,000 to C$20,000, for all trips based on the zone intersection type value.
- Income 20K to 30K (percent): Percent of travelers that have a household income of C$20,000 to C$30,000, for all trips based on the zone intersection type value.
- Income 30K to 40K (percent): Percent of travelers that have a household income of C$30,000 to C$40,000, for all trips based on the zone intersection type value.
- Income 40K to 50K (percent): Percent of travelers that have a household income of C$40,000 to C$50,000, for all trips based on the zone intersection type value.
- Income 50K to 60K (percent): Percent of travelers that have a household income of C$50,000 to C$60,000, for all trips based on the zone intersection type value.
- Income 60K to 80K (percent): Percent of travelers that have a household income of C$60,000 to C$80,000, for all trips based on the zone intersection type value.
- Income 80K to 100K (percent): Percent of travelers that have a household income of C$80,000 to C$100,000, for all trips based on the zone intersection type value.
- Income More than 100K (percent): Percent of travelers that have a household income of more than C$100,000, for all trips based on the zone intersection type value.
- No High School Diploma (percent): Percent of travelers over the age of 25 of which the highest level of education is below high school completion (diploma not awarded), for all trips based on the zone intersection type value.
- High School Diploma (percent): Percent of travelers over the age of 25 of which the highest level of education is completion of high school, for all trips based on the zone intersection type value.
- Some College (percent): Percent of travelers over the age of 25 of which the highest level of education is some college (but bachelor's degree not awarded), including associate's degree, for all trips based on the zone intersection type value.
- Bachelors Degree (percent): Percent of travelers over the age of 25 of which the highest level of education is the completion of a bachelor's college, for all trips based on the zone intersection type value.
- Graduate Degree (percent): Percent of travelers over the age of 25 of which the highest level of education is beyond completion of college, for all trips based on the zone intersection type value.
- White (percent): Percent of travelers that self-identify as White, for all trips based on the zone intersection type value.
- Black (percent): Percent of travelers that self-identify as Black or African American, for all trips based on the zone intersection type value.
- Asian (percent): Percent of travelers that self-identify as Asian, for all trips based on the zone intersection type value.
- Other Race (percent): Percent of travelers that self-identify as Some Other Race, for all trips based on the zone intersection type value.
- Multiple Races (percent): Percent of travelers that self-identify as Two or More Races, for all trips based on the zone intersection type value.
- Hispanic (percent): Percent of travelers that self-identify as of Hispanic or Latino Origin, for all trips based on the zone intersection type value.
- With Kids (percent): Percent of travelers that live in households with children, for all trips based on the zone intersection type value.
- With No Kids (percent): Percent of travelers that live in households with no children, for all trips based on the zone intersection type value.


NOTES
=====
OD Pairs with No Values
=======================
If the output unit values for an OD pair for a specific time period (e.g. Average Weekday, Early AM) are below StreetLight's significance threshold, no results will be shown in the od_*.csv file.

Day Part Calculations
=====================
The Day Part calculations are done in relation to the zones used in the analysis.
The O-D Trip Count values Day Parts are calculated in relation to the origin zone. The Day Part is determined when trips either start in the origin zone or pass by the centroid of the origin zone, if the origin zone is designated as pass-through.
The origin zone values Day Parts are also calculated in relation to the origin zone.
The destination zone values Day Parts are calculated in relation to the destination zone. The Day Part is determined when trips either end in the destination zone or pass by the centroid of the destination zone, if the destination zone is designated as pass-through.


Copyright © 2011 - 2021, StreetLight Data, Inc. All rights reserved.
