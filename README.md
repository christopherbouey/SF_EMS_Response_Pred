### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [Data Overview](#data-overview)
- [Analysis Summary](#analysis-summary)
- [Null Hypothesis](#null-hypothesis)
- [Takeaway](#takeaway)

---

## Description

San Francisco is well known for its publicized homeless community. This community tends to suffer from physical and mental illnesses more than the general population, presumably leading to a higher rate of EMS calls for people afflicted by homelessness. I wanted to investigate the relationship between the areas of San Francisco that contain the largest populations of homeless communities, and the response rate of EMS in those areas compared to others. 

## Data Overview

All EMS calls through SFFD available through [sfgov.org](https://data.sfgov.org/Public-Safety/Fire-Department-Calls-for-Service/nuek-vuh3)
- Investigated the time deltas between: 
    1. The call being received and a unit being dispatched 
    2. The unit being dispatch and the unit responding 
    3. The unit response and the unit arriving on scene
    4. The total time between call received and on scene arrival.

Data for homeless population available online through [Department of Homelessness and Supportive Housing](https://hsh.sfgov.org/about/research-and-reports/san-francisco-homeless-point-in-time-count-reports/)
- Located two districts with elevated population and linked with neighborhoods used in EMS data

[Back To The Top](#read-me-template)

---

## Analysis Summary

#### Cleaned Data
-Selected only 'Medical Incidents' and 'Alarms' to investigate as they would be most influenced and made up the vast majority of EMS calls (~80%)

-Ended with 3.12 M rows of useable EMS calls spanning April 2000 to present (July 2020)

-Separated data into two categories: One for high-homeless areas and one for low-homeless areas
 
- Used these categories for EDA

#### EDA
![Call Received to Dispatch Contacted](/Call_to_Disp.png)

![Dispatch Contacted to Unit Responding](/Disp_to_Resp.png)

![Unit Responds to Unit Arriving on Scene](/Resp_to_Scene.png)

![Total Time from Call to On Scene Arrival](/Call_to_Scene.png)

##### ^All time measurements seemed to match up similarly, so used the total time (call to scene)

[Back To The Top](#read-me-template)

---

## Null Hypothesis
### First
**Null Hypothesis:** Areas with high homeless population have same response rate as areas with low homeless population.

**Alternative Hypothesis:** Areas with high homeless population have different response rate as areas with low homeless population.

**P-Value** of 0.02 for rejection

### Second
I wanted to investigate my data a bit further, so I decided to break up the data into calls that were life-threatening and calls that were not life threatening. I did not perform EDA on this data but used it in another hypothesis test.

**Null Hypothesis:** Calls marked as life-threatening have same response rate as calls marked as non-life threatening.

**Alternative Hypothesis:** Calls marked as life-threatening have different response rate as calls marked as non-life threatening.

**P-Value** of 0.02 for rejection


[Back To The Top](#read-me-template)

---

## Results
### First
High Pop Avg: 530 seconds

Low Pop Avg: 516 seconds

P-Value: 0.0 (very very low)

**Reject Null Hypothesis**

![Homeless Hist](/High_to_Low_Homeless_Hist.png)

### Second
Life Threatening Avg: 508 seconds

Non-Life Threatening Avg: 528 seconds

P-Value: 4 e-214

**Reject Null Hypothesis**

![Homeless Hist](/Life_Threat_to_Non_Hist.png)

## Takeaway
The data suggests with very high confidence that the areas with low homeless populations in San Francisco have a slightly faster EMS response time, and that calls marked as life-threatening have a faster response time. The high confidence is not surprising as this dataset included all EMS calls in San Francisco, so was the population data. There is not suggestion of causation in this analysis.

[Back To The Top](#read-me-template)

