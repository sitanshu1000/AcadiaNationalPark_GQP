This folder contains the "Traveler Attributes" metrics for the Zone Activity zones within the named analysis.

The "Traveler Attributes" include Trip Purpose, Household Income, Education of Head of Household, Race, and Family Status. For Zone Activity analyses, these attributes apply to the entire trip.

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
za_traveler_*.csv
=================
This file contains the Trip Purpose and Demographics for travel at the zones. Note that Trip Purpose columns are not available for Zone Activity with Home and Work Locations projects.

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
- Zone Traffic: The volume of trips starting in, passing through, or ending in the zone based on the zone Mode of Travel, Intersection Type, and Output Type (as descibed above in the Output Unit Terms).

For analysis run with Location-Based Services data source, the Trip Purpose fields are:
- Purpose HBW (percent): Percent of travel that is home-based work (i.e. home-to-work or work-to-home).
- Purpose HBO (percent): Percent of travel that is home-based other (i.e. from or to home, but not home-based work).
- Purpose NHB (percent): Percent of travel that is not home-based (i.e. not from or to home).

For analysis run with Navigation-GPS data source, the Simple Trip Purpose fields are:
- Purpose RESI to RESI (percent): Percent of travel from a residential area to another residential area.
- Purpose RESI to COMM (percent): Percent of travel from a residential area to a commercial area.
- Purpose RESI to OTHER (percent): Percent of travel from a residential area to a known non-residential / non-commercial area.
- Purpose COMM to RESI (percent): Percent of travel from a commercial area to a residential area.
- Purpose COMM to COMM (percent): Percent of travel from a commercial area to another commercial area.
- Purpose COMM to OTHER (percent): Percent of travel from a commercial area to a known non-residential / non-commercial area.
- Purpose OTHER to RESI (percent): Percent of travel from a known non-residential / non-commercial area to a residential area.
- Purpose OTHER to COMM (percent): Percent of travel from a known non-residential / non-commercial area to a commercial area.
- Purpose OTHER to OTHER (percent): Percent of travel from a known non-residential / non-commercial area  to another non-residential / non-commercial area.
- Purpose UNKNOWN (percent):  Percent of travel for which the purpose is unknown.

For US analysis, the Demographics fields are:
- Income Less than 20K (percent): Percent of travelers that have a household income of less than $20,000.
- Income 20K to 35K (percent): Percent of travelers that have a household income of $20,000 to $35,000.
- Income 35K to 50K (percent): Percent of travelers that have a household income of $35,000 to $50,000.
- Income 50K to 75K (percent): Percent of travelers that have a household income of $50,000 to $75,000.
- Income 75K to 100K (percent): Percent of travelers that have a household income of $75,000 to $100,000.
- Income 100K to 125K (percent): Percent of travelers that have a household income of $100,000 to $125,000.
- Income 125K to 150K (percent): Percent of travelers that have a household income of $125,000 to $150,000.
- Income 150K to 200K (percent): Percent of travelers that have a household income of $150,000 to $200,000.
- Income More than 200K (percent): Percent of travelers that have a household income of more than $200,000.
- No High School Diploma (percent): Percent of travelers over the age of 25 of which the highest level of education is below high school completion (diploma not awarded).
- High School Diploma (percent): Percent of travelers over the age of 25 of which the highest level of education is completion of high school.
- Some College (percent): Percent of travelers over the age of 25 of which the highest level of education is some college (but bachelor's degree not awarded), including associate's degree.
- Bachelors Degree (percent): Percent of travelers over the age of 25 of which the highest level of education is the completion of a bachelor's college.
- Graduate Degree (percent): Percent of travelers over the age of 25 of which the highest level of education is beyond completion of college.
- White (percent): Percent of travelers that self-identify as White.
- Black (percent): Percent of travelers that self-identify as Black or African American.
- Indian (percent): Percent of travelers that self-identify as American Indian or Alaska Native.
- Asian (percent): Percent of travelers that self-identify as Asian.
- Islander (percent): Percent of travelers that self-identify as Native Hawaiian or Other Pacific Islander.
- Other Race (percent): Percent of travelers that self-identify as Some Other Race.
- Multiple Races (percent): Percent of travelers that self-identify as Two or More Races.
- Hispanic (percent): Percent of travelers that self-identify as of Hispanic or Latino Origin.
- With Kids (percent): Percent of travelers that live in households with children.
- With No Kids (percent): Percent of travelers that live in households with no children.
- With Kids under 6 years (percent): Percent of travelers that live in households with children under the age of 6.
- With Kids between 6-17 years (percent): Percent of travelers that live in households with children between the ages of 6 and 17.

For Canada projects, the demographics fields are:
- Income Less than 10K (percent): Percent of travelers that have a household income of less than C$10,000.
- Income 10K to 20K (percent): Percent of travelers that have a household income of C$10,000 to C$20,000.
- Income 20K to 30K (percent): Percent of travelers that have a household income of C$20,000 to C$30,000.
- Income 30K to 40K (percent): Percent of travelers that have a household income of C$30,000 to C$40,000.
- Income 40K to 50K (percent): Percent of travelers that have a household income of C$40,000 to C$50,000.
- Income 50K to 60K (percent): Percent of travelers that have a household income of C$50,000 to C$60,000.
- Income 60K to 80K (percent): Percent of travelers that have a household income of C$60,000 to C$80,000.
- Income 80K to 100K (percent): Percent of travelers that have a household income of C$80,000 to C$100,000.
- Income More than 100K (percent): Percent of travelers that have a household income of more than C$100,000.
- No High School Diploma (percent): Percent of travelers over the age of 25 of which the highest level of education is below high school completion (diploma not awarded).
- High School Diploma (percent): Percent of travelers over the age of 25 of which the highest level of education is completion of high school.
- Some College (percent): Percent of travelers over the age of 25 of which the highest level of education is some college (but bachelor's degree not awarded), including associate's degree.
- Bachelors Degree (percent): Percent of travelers over the age of 25 of which the highest level of education is the completion of a bachelor's college.
- Graduate Degree (percent): Percent of travelers over the age of 25 of which the highest level of education is beyond completion of college.
- White (percent): Percent of travelers that self-identify as White.
- Black (percent): Percent of travelers that self-identify as Black or African American.
- Asian (percent): Percent of travelers that self-identify as Asian.
- Other Race (percent): Percent of travelers that self-identify as Some Other Race.
- Multiple Races (percent): Percent of travelers that self-identify as Two or More Races.
- Hispanic (percent): Percent of travelers that self-identify as of Hispanic or Latino Origin.
- With Kids (percent): Percent of travelers that live in households with children.
- With No Kids (percent): Percent of travelers that live in households with no children.


NOTES
=====
ZA with No Values
=================
If the output unit values for a zone for a specific time period (e.g. Average Weekday, Early AM) are below StreetLight's significance threshold, no results will be shown in the za_*.csv file.

Day Part Calculations
=====================
The Day Part calculations are done in relation to the zones used in the analysis. The Day Part is determined by when trips either Start in the zone or pass by the centroid of the zone, if the zone is designated as pass-through.


Copyright © 2011 - 2021, StreetLight Data, Inc. All rights reserved.
