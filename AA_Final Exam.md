# Examining the Impact of Pell Grant Distribution on Graduation Rates: A Comparative Study of HBCUs and Non-HBCUs

# Abstract

This study investigates the association between institutional characteristics—namely
control (public vs. private), level (2-year vs. 4-year), and HBCU (Historically Black
Colleges and Universities) status—and graduation rates among Pell Grant recipients
in the United States. Multiple linear regression analyses were conducted using institution-level data to quantify the relationship between these factors and the graduation outcomes of Pell-eligible students

The results indicate that HBCU status is significantly associated with lower graduation 
rates for Pell recipients (β = -0.147, p < 0.001), suggesting a 14.7 percentage point 
decrease relative to non-HBCUs. Conversely, enrollment in private not-for-profit institutions 
is associated with higher graduation rates (β = 0.118, p < 0.001), corresponding to an 
11.8 percentage point increase. Additionally, students attending 4-year institutions 
demonstrate a 5.9 percentage point advantage over those at 2-year colleges (β = 0.059, p < 0.001).

These findings reveal persistent disparities in educational attainment among Pell Grant 
recipients, emphasizing the influence of institutional characteristics on student success.
The study underscores the need for equity-driven policies and institutional reforms 
that address structural differences and promote improved outcomes for underrepresented 
student populations.


## **Introduction**

Financial aid has long been recognized as a critical tool in promoting access and success in higher education, particularly for students from underserved and economically disadvantaged backgrounds. Among the various need-based aid programs in the United States, the **Federal Pell Grant** remains the cornerstone of federal financial assistance, targeting low-income students to support their pursuit of postsecondary credentials. In the 2021–2022 academic year, over six million students received Pell Grants, the majority of whom identified as first-generation college students, students of color, or members of historically marginalized groups (U.S. Department of Education, 2022).

Extensive research has documented the positive effects of Pell Grants on **college access**, **enrollment**, and **persistence** (e.g., Bettinger, 2015; Dynarski, 2003; Castleman & Long, 2016). However, the relationship between Pell Grant receipt and **institutional-level outcomes**, particularly graduation rates, remains underexamined. While individual-level studies have shown that Pell recipients face unique challenges—such as financial insecurity, limited academic preparation, and systemic barriers—the extent to which these challenges manifest in aggregate institutional outcomes is less well understood.

This study explores the connection between institutional characteristics and Pell recipient graduation rates, with a particular emphasis on **Historically Black Colleges and Universities (HBCUs)**. HBCUs serve a disproportionately high number of Pell-eligible students and have historically played a vital role in advancing educational equity and social mobility. Yet, these institutions continue to face chronic underfunding, resource inequities, and structural constraints that may affect student outcomes (Gasman et al., 2010; Nichols & Evans-Bell, 2017).

Using national postsecondary data, this paper investigates how graduation rates within 150% of normal program time among Pell recipients vary across institutional contexts. Specifically, it examines the roles of **HBCU status**, **institutional control** (public vs. private), and **institutional level** (2-year vs. 4-year) in shaping these outcomes. By integrating these structural factors, this research aims to provide a more nuanced understanding of how financial aid policy interacts with institutional environments—offering implications for the design and targeting of support mechanisms intended to close equity gaps in higher education.


## **Research Questions**
1. What is the relationship between the proportion of students receiving Pell Grants and graduation rates within 150% of normal program time, and how does this relationship differ across two-year and four-year institutions?

2. In what ways do patterns of Pell Grant distribution relate to graduation outcomes at Historically Black Colleges and Universities (HBCUs) versus Predominantly White Institutions (PWIs), particularly in the context of racial equity in higher education?


## **Problem Statement**
Federal financial aid, especially Pell Grants, plays a significant role in supporting students from low-income backgrounds in U.S. higher education. However, the impact of Pell Grants on graduation rates within 150% of normal time remains unclear, particularly when comparing institutions with differing characteristics, such as 2-year vs. 4-year institutions and public vs. private nonprofit institutions. Additionally, the unique challenges faced by Historically Black Colleges and Universities (HBCUs) in relation to Pell Grant distribution and graduation rates warrant further investigation. This analysis hypothesizes that the percentage of students receiving Pell Grants positively influences graduation rates, with variations across institutional types and particularly within HBCUs.

## **Data Description**

### Data Sources

The data used in this study were obtained from the **Integrated Postsecondary Education Data System (IPEDS)**, a program administered by the **U.S. Department of Education** that provides comprehensive data on postsecondary institutions in the United States. The analysis draws on the following IPEDS surveys from the **2022–2023 academic year**:

- **Graduation Rates (GR) Survey** – Reports institutional-level graduation rates within 150% of normal time for first-time, full-time undergraduate students.
- **Student Financial Aid (SFA) Survey** – Provides data on the percentage of undergraduate students receiving Pell Grants and other federal financial aid.
- **Institutional Characteristics (IC) Survey** – Includes data on institutional attributes such as control (public, private nonprofit, private for-profit), level (2-year vs. 4-year), and HBCU designati n.

### Dataset Overview

The dataset is aggregated at the institutional level, enabling an analysis of patterns and trends across U.S. colleges and universities. Individual-level student data are not available; instead, this study analyzes averages and rates reported by institutions to identify relationships between financial aid distribution and graduation outcomes.

### Key Variables

#### Dependent Variable
- **pell_grad_rate**: Graduation rate within 150% of normal time for first-time, full-time Pell Grant recipients.

#### Independent Variables
- **pell_percent**: Percentage of undergraduate students receiving Pell Grants (continuous).
- **IC_LEVEL**: Institutional level (2-year or 4-year).
- **CONTROL**: Type of institutional control (Public, Private Nonprofit
- **HBCU**: Indicates whether an institution is designated as a Historically Black College or University.

### Data Column Descriptions
The dataset includes the following columns, providing a comprehensive view of institutional characteristics and graduation outcomes for both Pell Grant and non-Pell Grant recipients:

- **INS_ID**: Unique institution identifier  
- **INI_NAME**: Institution name  
- **CITY**: City location of the institution  
- **STATE**: State location  
- **HBCU**: HBCU status  
- **DMV**: Regional indicator for institutions in D.C., Maryland, or Virginia (if applicable)  
- **PWI**: Indicator for Predominantly White Institutions (if applicable)  
- **IC_LEVEL**: Institution level  
- **CONTROL**: Institutional control  
- **total_cohort**: Total number of first-time, full-time undergraduates in the cohort  
- **pell_cohort**: Number of Pell Grant recipients in the cohort  
- **pell_percent**: Percentage of students receiving Pell Grants  
- **pell_complete_150**: Number of Pell recipients graduating within 150% of normal time  
- **pell_grad_rate**: Graduation rate for Pell recipients  
- **no_aid_cohort**: Number of students not receiving Pell Grants  
- **no_aid_complete_150**: Number of non-Pell recipients graduating within 150% of normal time  
- **no_aid_grad_rate**: Graduation rate for non-Pell recipients  
- **total_complete_150**: Total number of students graduating within 150% of normal time  
- **Grad_rate**: Overall institutional graduation rate


## **Data Import, Exploration, and Cleaning**
In this section, we outline the steps taken to import, explore, and clean the dataset for analysis. This process includes loading the data, inspecting its structure, handling missing values, and transforming variables as needed to ensure accurate analysis.

### **Loadindg the Dataset**


```python
 # Import the libraries
import pandas as pd
import numpy as np
import matplotlib as mb
import seaborn as sn
import os
current_directory = os.getcwd()
# Read the dataset
PELL_GR_DATA = pd.read_csv('/home/81e8adb4-b981-4fde-9a1a-464275ba01ce/IC_data/DATA_GRAD_PELL_MERGED.csv', encoding='ISO-8859-1')

```

### **Examining the Data**


```python
# Checking first elements of the DataFrame with .head( ) method
PELL_GR_DATA .head ()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>INS_ ID</th>
      <th>INI_NAME</th>
      <th>CITY</th>
      <th>STATE</th>
      <th>HBCU</th>
      <th>DMV</th>
      <th>PWI</th>
      <th>IC_LEVEL</th>
      <th>CONTROL</th>
      <th>total_cohort</th>
      <th>pell_cohort</th>
      <th>pell_percent</th>
      <th>pell_complete_150</th>
      <th>pell_grad_rate</th>
      <th>no_aid_cohort</th>
      <th>no_aid_complete_150</th>
      <th>no_aid_grad_rate</th>
      <th>total_complete_150</th>
      <th>Grad_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>180203.0</td>
      <td>Aaniiih Nakoda College</td>
      <td>Harlem</td>
      <td>MT</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Four or more years</td>
      <td>Public</td>
      <td>34.0</td>
      <td>29.0</td>
      <td>85%</td>
      <td>11.0</td>
      <td>38%</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0%</td>
      <td>11.0</td>
      <td>32%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>222178.0</td>
      <td>Abilene Christian University</td>
      <td>Abilene</td>
      <td>TX</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Four or more years</td>
      <td>Private not-for-profit</td>
      <td>940.0</td>
      <td>280.0</td>
      <td>30%</td>
      <td>130.0</td>
      <td>46%</td>
      <td>444.0</td>
      <td>309.0</td>
      <td>70%</td>
      <td>566.0</td>
      <td>60%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>222178.0</td>
      <td>Abilene Christian University</td>
      <td>Abilene</td>
      <td>TX</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>Four or more years</td>
      <td>Private not-for-profit</td>
      <td>940.0</td>
      <td>280.0</td>
      <td>30%</td>
      <td>130.0</td>
      <td>46%</td>
      <td>444.0</td>
      <td>309.0</td>
      <td>70%</td>
      <td>566.0</td>
      <td>60%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>138558.0</td>
      <td>Abraham Baldwin Agricultural College</td>
      <td>Tifton</td>
      <td>GA</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>Four or more years</td>
      <td>Public</td>
      <td>477.0</td>
      <td>219.0</td>
      <td>46%</td>
      <td>67.0</td>
      <td>31%</td>
      <td>209.0</td>
      <td>80.0</td>
      <td>38%</td>
      <td>166.0</td>
      <td>35%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>138558.0</td>
      <td>Abraham Baldwin Agricultural College</td>
      <td>Tifton</td>
      <td>GA</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>Four or more years</td>
      <td>Public</td>
      <td>488.0</td>
      <td>276.0</td>
      <td>57%</td>
      <td>45.0</td>
      <td>16%</td>
      <td>176.0</td>
      <td>65.0</td>
      <td>37%</td>
      <td>115.0</td>
      <td>24%</td>
    </tr>
  </tbody>
</table>
</div>




```python
PELL_GR_DATA.info() # checking the basic information about the dataset
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 6137 entries, 0 to 6136
    Data columns (total 19 columns):
     #   Column               Non-Null Count  Dtype  
    ---  ------               --------------  -----  
     0   INS_ ID              6136 non-null   float64
     1   INI_NAME             6136 non-null   object 
     2   CITY                 6136 non-null   object 
     3   STATE                6136 non-null   object 
     4   HBCU                 6136 non-null   float64
     5   DMV                  6136 non-null   float64
     6   PWI                  6136 non-null   float64
     7   IC_LEVEL             6136 non-null   object 
     8   CONTROL              6136 non-null   object 
     9   total_cohort         6136 non-null   float64
     10  pell_cohort          6136 non-null   float64
     11  pell_percent         6135 non-null   object 
     12  pell_complete_150    6136 non-null   float64
     13  pell_grad_rate       5939 non-null   object 
     14  no_aid_cohort        6136 non-null   float64
     15  no_aid_complete_150  6136 non-null   float64
     16  no_aid_grad_rate     5908 non-null   object 
     17  total_complete_150   6136 non-null   float64
     18  Grad_rate            6135 non-null   object 
    dtypes: float64(10), object(9)
    memory usage: 911.1+ KB



```python
PELL_GR_DATA.isnull().sum() # Missing values count
```




    INS_ ID                  1
    INI_NAME                 1
    CITY                     1
    STATE                    1
    HBCU                     1
    DMV                      1
    PWI                      1
    IC_LEVEL                 1
    CONTROL                  1
    total_cohort             1
    pell_cohort              1
    pell_percent             2
    pell_complete_150        1
    pell_grad_rate         198
    no_aid_cohort            1
    no_aid_complete_150      1
    no_aid_grad_rate       229
    total_complete_150       1
    Grad_rate                2
    dtype: int64




```python
PELL_GR_DATA.describe(include='all') # Statistical summary with all data types
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>INS_ ID</th>
      <th>INI_NAME</th>
      <th>CITY</th>
      <th>STATE</th>
      <th>HBCU</th>
      <th>DMV</th>
      <th>PWI</th>
      <th>IC_LEVEL</th>
      <th>CONTROL</th>
      <th>total_cohort</th>
      <th>pell_cohort</th>
      <th>pell_percent</th>
      <th>pell_complete_150</th>
      <th>pell_grad_rate</th>
      <th>no_aid_cohort</th>
      <th>no_aid_complete_150</th>
      <th>no_aid_grad_rate</th>
      <th>total_complete_150</th>
      <th>Grad_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>6136.000000</td>
      <td>6136</td>
      <td>6136</td>
      <td>6136</td>
      <td>6136.000000</td>
      <td>6136.000000</td>
      <td>6136.000000</td>
      <td>6136</td>
      <td>6136</td>
      <td>6136.000000</td>
      <td>6136.000000</td>
      <td>6135</td>
      <td>6136.000000</td>
      <td>5939</td>
      <td>6136.000000</td>
      <td>6136.000000</td>
      <td>5908</td>
      <td>6136.000000</td>
      <td>6135</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>2797</td>
      <td>1580</td>
      <td>51</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>97</td>
      <td>NaN</td>
      <td>101</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>98</td>
      <td>NaN</td>
      <td>97</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>Columbia College</td>
      <td>New York</td>
      <td>NY</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Four or more years</td>
      <td>Public</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0%</td>
      <td>NaN</td>
      <td>0%</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0%</td>
      <td>NaN</td>
      <td>33%</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>10</td>
      <td>68</td>
      <td>490</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4645</td>
      <td>3161</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>196</td>
      <td>NaN</td>
      <td>185</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>260</td>
      <td>NaN</td>
      <td>144</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>203452.020046</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.023631</td>
      <td>0.036343</td>
      <td>0.519557</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>650.960724</td>
      <td>245.845339</td>
      <td>NaN</td>
      <td>108.207790</td>
      <td>NaN</td>
      <td>304.453064</td>
      <td>190.450130</td>
      <td>NaN</td>
      <td>361.927803</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>86650.068880</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.151909</td>
      <td>0.187157</td>
      <td>0.499658</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1057.888341</td>
      <td>379.275120</td>
      <td>NaN</td>
      <td>202.195639</td>
      <td>NaN</td>
      <td>598.279013</td>
      <td>480.295771</td>
      <td>NaN</td>
      <td>771.907073</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>100654.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>154371.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>93.000000</td>
      <td>42.750000</td>
      <td>NaN</td>
      <td>14.000000</td>
      <td>NaN</td>
      <td>24.000000</td>
      <td>10.000000</td>
      <td>NaN</td>
      <td>34.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>189556.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>300.500000</td>
      <td>122.000000</td>
      <td>NaN</td>
      <td>49.000000</td>
      <td>NaN</td>
      <td>107.000000</td>
      <td>48.000000</td>
      <td>NaN</td>
      <td>123.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>217477.250000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>715.000000</td>
      <td>281.000000</td>
      <td>NaN</td>
      <td>111.000000</td>
      <td>NaN</td>
      <td>310.250000</td>
      <td>153.000000</td>
      <td>NaN</td>
      <td>336.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>498906.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>11163.000000</td>
      <td>9783.000000</td>
      <td>NaN</td>
      <td>5178.000000</td>
      <td>NaN</td>
      <td>6546.000000</td>
      <td>5711.000000</td>
      <td>NaN</td>
      <td>8458.000000</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
PELL_GR_DATA.columns.tolist()
```




    ['INS_ ID',
     'INI_NAME',
     'CITY',
     'STATE',
     'HBCU',
     'DMV',
     'PWI',
     'IC_LEVEL',
     'CONTROL',
     'total_cohort',
     'pell_cohort',
     'pell_percent',
     'pell_complete_150',
     'pell_grad_rate',
     'no_aid_cohort',
     'no_aid_complete_150',
     'no_aid_grad_rate',
     'total_complete_150',
     'Grad_rate']




```python
PELL_GR_DATA.dtypes # Data types of columns
```




    INS_ ID                float64
    INI_NAME                object
    CITY                    object
    STATE                   object
    HBCU                   float64
    DMV                    float64
    PWI                    float64
    IC_LEVEL                object
    CONTROL                 object
    total_cohort           float64
    pell_cohort            float64
    pell_percent            object
    pell_complete_150      float64
    pell_grad_rate          object
    no_aid_cohort          float64
    no_aid_complete_150    float64
    no_aid_grad_rate        object
    total_complete_150     float64
    Grad_rate               object
    dtype: object




```python
PELL_GR_DATA.shape[0] # number of rows
```




    6137




```python
PELL_GR_DATA.shape[1] # number of Columns
```




    19




```python
print(f"Rows: {PELL_GR_DATA.shape[0]}, Columns: {PELL_GR_DATA.shape[1]}")
```

    Rows: 6137, Columns: 19


*The dataset contains 6,137 rows and 19 columns, indicating that it includes information for 6,137 institutions with 19 different variables. These variables encompass both institutional characteristics (e.g., HBCU status, institutional control) and student outcomes (e.g., Pell Grant recipients, graduation rates). This shape allows for a comprehensive analysis of the relationship between Pell Grant distribution and graduation rates across various institutional types.*

### **Data Cleaning**
#### **Converting percentage-based variables to decimal format for analysis**


```python
PELL_GR_DATA['Grad_rate'] = pd.to_numeric(PELL_GR_DATA['Grad_rate'].astype(str).str.rstrip('%'), errors='coerce') / 100

```


```python
PELL_GR_DATA['pell_percent'] = pd.to_numeric(PELL_GR_DATA['pell_percent'].astype(str).str.rstrip('%'), errors='coerce') / 100

```


```python
PELL_GR_DATA['pell_grad_rate'] = pd.to_numeric(PELL_GR_DATA['pell_grad_rate'].astype(str).str.rstrip('%'), errors='coerce') / 100

```


```python
PELL_GR_DATA['no_aid_grad_rate'] = pd.to_numeric(PELL_GR_DATA['no_aid_grad_rate'].astype(str).str.rstrip('%'), errors='coerce') / 100

```


```python
PELL_GR_DATA.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>INS_ ID</th>
      <th>HBCU</th>
      <th>DMV</th>
      <th>PWI</th>
      <th>total_cohort</th>
      <th>pell_cohort</th>
      <th>pell_percent</th>
      <th>pell_complete_150</th>
      <th>pell_grad_rate</th>
      <th>no_aid_cohort</th>
      <th>no_aid_complete_150</th>
      <th>no_aid_grad_rate</th>
      <th>total_complete_150</th>
      <th>Grad_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>6136.000000</td>
      <td>6136.000000</td>
      <td>6136.000000</td>
      <td>6136.000000</td>
      <td>6136.000000</td>
      <td>6136.000000</td>
      <td>6135.000000</td>
      <td>6136.000000</td>
      <td>5939.000000</td>
      <td>6136.000000</td>
      <td>6136.000000</td>
      <td>5908.000000</td>
      <td>6136.000000</td>
      <td>6135.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>203452.020046</td>
      <td>0.023631</td>
      <td>0.036343</td>
      <td>0.519557</td>
      <td>650.960724</td>
      <td>245.845339</td>
      <td>0.446665</td>
      <td>108.207790</td>
      <td>0.431837</td>
      <td>304.453064</td>
      <td>190.450130</td>
      <td>0.513152</td>
      <td>361.927803</td>
      <td>0.473206</td>
    </tr>
    <tr>
      <th>std</th>
      <td>86650.068880</td>
      <td>0.151909</td>
      <td>0.187157</td>
      <td>0.499658</td>
      <td>1057.888341</td>
      <td>379.275120</td>
      <td>0.202332</td>
      <td>202.195639</td>
      <td>0.221012</td>
      <td>598.279013</td>
      <td>480.295771</td>
      <td>0.240533</td>
      <td>771.907073</td>
      <td>0.218148</td>
    </tr>
    <tr>
      <th>min</th>
      <td>100654.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>154371.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>93.000000</td>
      <td>42.750000</td>
      <td>0.320000</td>
      <td>14.000000</td>
      <td>0.280000</td>
      <td>24.000000</td>
      <td>10.000000</td>
      <td>0.340000</td>
      <td>34.000000</td>
      <td>0.310000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>189556.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>300.500000</td>
      <td>122.000000</td>
      <td>0.440000</td>
      <td>49.000000</td>
      <td>0.400000</td>
      <td>107.000000</td>
      <td>48.000000</td>
      <td>0.520000</td>
      <td>123.000000</td>
      <td>0.460000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>217477.250000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>715.000000</td>
      <td>281.000000</td>
      <td>0.560000</td>
      <td>111.000000</td>
      <td>0.550000</td>
      <td>310.250000</td>
      <td>153.000000</td>
      <td>0.690000</td>
      <td>336.000000</td>
      <td>0.610000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>498906.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>11163.000000</td>
      <td>9783.000000</td>
      <td>1.000000</td>
      <td>5178.000000</td>
      <td>1.000000</td>
      <td>6546.000000</td>
      <td>5711.000000</td>
      <td>1.000000</td>
      <td>8458.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



#### **Removing rows with missing values to ensure complete data for analysis**


```python
PELL_GR_CLEANED=PELL_GR_DATA.dropna() # Dropping missing values
```


```python
# Generates summary statistics for all numeric columns in the cleaned DataFrame
PELL_GR_CLEANED.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>INS_ ID</th>
      <th>HBCU</th>
      <th>DMV</th>
      <th>PWI</th>
      <th>total_cohort</th>
      <th>pell_cohort</th>
      <th>pell_percent</th>
      <th>pell_complete_150</th>
      <th>pell_grad_rate</th>
      <th>no_aid_cohort</th>
      <th>no_aid_complete_150</th>
      <th>no_aid_grad_rate</th>
      <th>total_complete_150</th>
      <th>Grad_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5736.000000</td>
      <td>5736.000000</td>
      <td>5736.000000</td>
      <td>5736.000000</td>
      <td>5736.000000</td>
      <td>5736.000000</td>
      <td>5736.000000</td>
      <td>5736.000000</td>
      <td>5736.000000</td>
      <td>5736.000000</td>
      <td>5736.000000</td>
      <td>5736.000000</td>
      <td>5736.000000</td>
      <td>5736.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>199430.381276</td>
      <td>0.023361</td>
      <td>0.036437</td>
      <td>0.519003</td>
      <td>692.368550</td>
      <td>261.416841</td>
      <td>0.447896</td>
      <td>115.286960</td>
      <td>0.431789</td>
      <td>324.140690</td>
      <td>202.455021</td>
      <td>0.513162</td>
      <td>385.018480</td>
      <td>0.471804</td>
    </tr>
    <tr>
      <th>std</th>
      <td>80898.150165</td>
      <td>0.151061</td>
      <td>0.187390</td>
      <td>0.499682</td>
      <td>1080.735503</td>
      <td>386.762391</td>
      <td>0.172261</td>
      <td>207.175902</td>
      <td>0.213558</td>
      <td>612.751392</td>
      <td>493.350818</td>
      <td>0.234786</td>
      <td>792.405427</td>
      <td>0.202327</td>
    </tr>
    <tr>
      <th>min</th>
      <td>100654.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>0.030000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>153922.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>125.000000</td>
      <td>57.000000</td>
      <td>0.330000</td>
      <td>20.000000</td>
      <td>0.280000</td>
      <td>35.000000</td>
      <td>15.000000</td>
      <td>0.340000</td>
      <td>48.000000</td>
      <td>0.320000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>188225.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>332.000000</td>
      <td>134.000000</td>
      <td>0.440000</td>
      <td>53.000000</td>
      <td>0.400000</td>
      <td>121.000000</td>
      <td>57.000000</td>
      <td>0.520000</td>
      <td>139.500000</td>
      <td>0.460000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>215704.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>759.000000</td>
      <td>303.000000</td>
      <td>0.560000</td>
      <td>120.000000</td>
      <td>0.550000</td>
      <td>332.000000</td>
      <td>165.250000</td>
      <td>0.690000</td>
      <td>362.000000</td>
      <td>0.610000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>498571.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>11163.000000</td>
      <td>9783.000000</td>
      <td>0.970000</td>
      <td>5178.000000</td>
      <td>1.000000</td>
      <td>6546.000000</td>
      <td>5711.000000</td>
      <td>1.000000</td>
      <td>8458.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
PELL_GR_CLEANED.isnull().sum()  # Determine the number of missing values
```




    INS_ ID                0
    INI_NAME               0
    CITY                   0
    STATE                  0
    HBCU                   0
    DMV                    0
    PWI                    0
    IC_LEVEL               0
    CONTROL                0
    total_cohort           0
    pell_cohort            0
    pell_percent           0
    pell_complete_150      0
    pell_grad_rate         0
    no_aid_cohort          0
    no_aid_complete_150    0
    no_aid_grad_rate       0
    total_complete_150     0
    Grad_rate              0
    dtype: int64




```python
# Checking first elements of the DataFrame PELL_GR_CLEANED with .head() method
PELL_GR_CLEANED.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>INS_ ID</th>
      <th>INI_NAME</th>
      <th>CITY</th>
      <th>STATE</th>
      <th>HBCU</th>
      <th>DMV</th>
      <th>PWI</th>
      <th>IC_LEVEL</th>
      <th>CONTROL</th>
      <th>total_cohort</th>
      <th>pell_cohort</th>
      <th>pell_percent</th>
      <th>pell_complete_150</th>
      <th>pell_grad_rate</th>
      <th>no_aid_cohort</th>
      <th>no_aid_complete_150</th>
      <th>no_aid_grad_rate</th>
      <th>total_complete_150</th>
      <th>Grad_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>180203.0</td>
      <td>Aaniiih Nakoda College</td>
      <td>Harlem</td>
      <td>MT</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Four or more years</td>
      <td>Public</td>
      <td>34.0</td>
      <td>29.0</td>
      <td>0.85</td>
      <td>11.0</td>
      <td>0.38</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>11.0</td>
      <td>0.32</td>
    </tr>
    <tr>
      <th>1</th>
      <td>222178.0</td>
      <td>Abilene Christian University</td>
      <td>Abilene</td>
      <td>TX</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Four or more years</td>
      <td>Private not-for-profit</td>
      <td>940.0</td>
      <td>280.0</td>
      <td>0.30</td>
      <td>130.0</td>
      <td>0.46</td>
      <td>444.0</td>
      <td>309.0</td>
      <td>0.70</td>
      <td>566.0</td>
      <td>0.60</td>
    </tr>
    <tr>
      <th>2</th>
      <td>222178.0</td>
      <td>Abilene Christian University</td>
      <td>Abilene</td>
      <td>TX</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>Four or more years</td>
      <td>Private not-for-profit</td>
      <td>940.0</td>
      <td>280.0</td>
      <td>0.30</td>
      <td>130.0</td>
      <td>0.46</td>
      <td>444.0</td>
      <td>309.0</td>
      <td>0.70</td>
      <td>566.0</td>
      <td>0.60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>138558.0</td>
      <td>Abraham Baldwin Agricultural College</td>
      <td>Tifton</td>
      <td>GA</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>Four or more years</td>
      <td>Public</td>
      <td>477.0</td>
      <td>219.0</td>
      <td>0.46</td>
      <td>67.0</td>
      <td>0.31</td>
      <td>209.0</td>
      <td>80.0</td>
      <td>0.38</td>
      <td>166.0</td>
      <td>0.35</td>
    </tr>
    <tr>
      <th>4</th>
      <td>138558.0</td>
      <td>Abraham Baldwin Agricultural College</td>
      <td>Tifton</td>
      <td>GA</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>Four or more years</td>
      <td>Public</td>
      <td>488.0</td>
      <td>276.0</td>
      <td>0.57</td>
      <td>45.0</td>
      <td>0.16</td>
      <td>176.0</td>
      <td>65.0</td>
      <td>0.37</td>
      <td>115.0</td>
      <td>0.24</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Checking last elements of the DataFrame  PELL_GR_CLEANED with .tail() method
PELL_GR_CLEANED.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>INS_ ID</th>
      <th>INI_NAME</th>
      <th>CITY</th>
      <th>STATE</th>
      <th>HBCU</th>
      <th>DMV</th>
      <th>PWI</th>
      <th>IC_LEVEL</th>
      <th>CONTROL</th>
      <th>total_cohort</th>
      <th>pell_cohort</th>
      <th>pell_percent</th>
      <th>pell_complete_150</th>
      <th>pell_grad_rate</th>
      <th>no_aid_cohort</th>
      <th>no_aid_complete_150</th>
      <th>no_aid_grad_rate</th>
      <th>total_complete_150</th>
      <th>Grad_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6131</th>
      <td>206695.0</td>
      <td>Youngstown State University</td>
      <td>Youngstown</td>
      <td>OH</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>Four or more years</td>
      <td>Public</td>
      <td>2124.0</td>
      <td>896.0</td>
      <td>0.42</td>
      <td>391.0</td>
      <td>0.44</td>
      <td>883.0</td>
      <td>573.0</td>
      <td>0.65</td>
      <td>1135.0</td>
      <td>0.53</td>
    </tr>
    <tr>
      <th>6132</th>
      <td>206695.0</td>
      <td>Youngstown State University</td>
      <td>Youngstown</td>
      <td>OH</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Four or more years</td>
      <td>Public</td>
      <td>40.0</td>
      <td>26.0</td>
      <td>0.65</td>
      <td>8.0</td>
      <td>0.31</td>
      <td>11.0</td>
      <td>2.0</td>
      <td>0.18</td>
      <td>10.0</td>
      <td>0.25</td>
    </tr>
    <tr>
      <th>6133</th>
      <td>206695.0</td>
      <td>Youngstown State University</td>
      <td>Youngstown</td>
      <td>OH</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>Four or more years</td>
      <td>Public</td>
      <td>40.0</td>
      <td>26.0</td>
      <td>0.65</td>
      <td>8.0</td>
      <td>0.31</td>
      <td>11.0</td>
      <td>2.0</td>
      <td>0.18</td>
      <td>10.0</td>
      <td>0.25</td>
    </tr>
    <tr>
      <th>6134</th>
      <td>126119.0</td>
      <td>Yuba College</td>
      <td>Marysville</td>
      <td>CA</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>At least 2 but less than 4 years</td>
      <td>Public</td>
      <td>307.0</td>
      <td>164.0</td>
      <td>0.53</td>
      <td>54.0</td>
      <td>0.33</td>
      <td>143.0</td>
      <td>45.0</td>
      <td>0.31</td>
      <td>99.0</td>
      <td>0.32</td>
    </tr>
    <tr>
      <th>6135</th>
      <td>204255.0</td>
      <td>Zane State College</td>
      <td>Zanesville</td>
      <td>OH</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>Four or more years</td>
      <td>Public</td>
      <td>202.0</td>
      <td>97.0</td>
      <td>0.48</td>
      <td>39.0</td>
      <td>0.40</td>
      <td>84.0</td>
      <td>57.0</td>
      <td>0.68</td>
      <td>107.0</td>
      <td>0.53</td>
    </tr>
  </tbody>
</table>
</div>




```python
# State the shape of the data frame PELL_GR_CLEANED
PELL_GR_CLEANED.shape  # Returns (rows, columns)

```




    (5736, 19)



##### ***The cleaned dataset contains 5736 rows and 19 columns, after removing rows with missing values***


```python
# How many rows does the data frame PELL_GR_CLEANED have?
PELL_GR_CLEANED.shape[0]
```




    5736




```python
# How many columns does the data frame ELL_GR_CLEANED have?
PELL_GR_CLEANED.shape[1]
```




    19




```python
# What is the total number of data points expected in the data set (rows x columns)?
PELL_GR_CLEANED.shape[0] * PELL_GR_CLEANED.shape[1]
```




    108984



##### ***The dataset contains 108,984 total data points, calculated by multiplying the 5736 rows by 19 columns.***


```python
# Checking for missing values
PELL_GR_CLEANED.isnull().sum()
```




    INS_ ID                0
    INI_NAME               0
    CITY                   0
    STATE                  0
    HBCU                   0
    DMV                    0
    PWI                    0
    IC_LEVEL               0
    CONTROL                0
    total_cohort           0
    pell_cohort            0
    pell_percent           0
    pell_complete_150      0
    pell_grad_rate         0
    no_aid_cohort          0
    no_aid_complete_150    0
    no_aid_grad_rate       0
    total_complete_150     0
    Grad_rate              0
    dtype: int64




```python
# Check the data types with .info() method
PELL_GR_CLEANED.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 5736 entries, 0 to 6135
    Data columns (total 19 columns):
     #   Column               Non-Null Count  Dtype  
    ---  ------               --------------  -----  
     0   INS_ ID              5736 non-null   float64
     1   INI_NAME             5736 non-null   object 
     2   CITY                 5736 non-null   object 
     3   STATE                5736 non-null   object 
     4   HBCU                 5736 non-null   float64
     5   DMV                  5736 non-null   float64
     6   PWI                  5736 non-null   float64
     7   IC_LEVEL             5736 non-null   object 
     8   CONTROL              5736 non-null   object 
     9   total_cohort         5736 non-null   float64
     10  pell_cohort          5736 non-null   float64
     11  pell_percent         5736 non-null   float64
     12  pell_complete_150    5736 non-null   float64
     13  pell_grad_rate       5736 non-null   float64
     14  no_aid_cohort        5736 non-null   float64
     15  no_aid_complete_150  5736 non-null   float64
     16  no_aid_grad_rate     5736 non-null   float64
     17  total_complete_150   5736 non-null   float64
     18  Grad_rate            5736 non-null   float64
    dtypes: float64(14), object(5)
    memory usage: 896.2+ KB


## **Methodology**

This section describes the data acquisition, preparation, and analytical procedures used to examine the relationship between Pell Grant distribution and institutional graduation outcomes in U.S. higher education.

### **Data Source and Loading**

The dataset utilized in this study was loaded and processed in a Python environment using the `pandas` library. It includes institutional-level data on graduation outcomes for first-time, full-time undergraduate students, disaggregated by Pell Grant recipient status. Preliminary steps involved inspecting the structure and integrity of the data using standard exploratory commands such as `.head()`, `.tail()`, `.shape`, `.info()`, and `.isnull().sum()`.

### **Data Cleaning and Preparation**

To ensure analytical rigor, several preprocessing steps were applied:

- **Data Type Conversion**: Variables were converted to appropriate data types (e.g., integer, float, categorical) based on their semantic meaning and statistical utility.
  
- **Handling Missing Values**: Given that the percentage of missing values was low, rows containing null entries were excluded using listwise deletion to preserve internal validity without the complexity of imputation techniques.

- **Standardization of Percentages**: Graduation and Pell participation rates were initially stored as string percentages (e.g., "75%") and were standardized by stripping the percentage symbol and converting values to decimal form (e.g., 0.75) to facilitate accurate computation in regression modeling.

### **Data Reduction and Validation**

Following preprocessing, the dataset was reduced from its original size to 5,736 complete cases across 19 variables, yielding a total of 108,984 data points. This cleaned dataset provided the foundation for all subsequent statistical analyses.


## **Exploratory Data Analysis (EDA) & Visualization**

This section uses a combination of visualizations and descriptive statistics to explore patterns in the dataset. Bar plots were used to compare average graduation rates across institutional categories (e.g., control type, HBCU status, institution level). Box plots provided additional insight into the distribution and variability of graduation outcomes. A correlation matrix was generated to assess linear relationships between continuous variables, including Pell Grant recipient rates and graduation rates. Furthermore, `groupby()` with `.mean()` was applied to calculate average graduation outcomes within each institutional subgroup, helping to uncover trends relevant to the study's research questions.


## **Correlation Matrix**


```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Copy dataset for safety
PELL_GR = PELL_GR_CLEANED.copy()

# Selecting only numeric columns for correlation
corr_matrix = PELL_GR.select_dtypes(include=['number']).corr()

# Set up the figure size
plt.figure(figsize=(10, 6))

# Create a heatmap
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

# Add title
plt.title('Correlation Matrix of Key Variables')

# Show the plot
plt.show()

```


    
![png](AA_Final%20Exam_43_0.png)
    



```python
# Use groupby + mean to see how each category relates to the dependent variable
PELL_GR_CLEANED.groupby('HBCU')['pell_grad_rate'].mean()
```




    HBCU
    0.0    0.435116
    1.0    0.292687
    Name: pell_grad_rate, dtype: float64




```python
PELL_GR_CLEANED.groupby('IC_LEVEL')['pell_grad_rate'].mean()
```




    IC_LEVEL
    At least 2 but less than 4 years    0.343174
    Four or more years                  0.462101
    Name: pell_grad_rate, dtype: float64




```python
PELL_GR_CLEANED.groupby('CONTROL')['pell_grad_rate'].mean()
```




    CONTROL
    Private not-for-profit    0.508694
    Public                    0.366440
    Name: pell_grad_rate, dtype: float64




```python
# Group by HBCU and show average pell graduation rate as percent
print("Average Pell Graduation Rate by HBCU:")
print((PELL_GR_CLEANED.groupby('HBCU')['pell_grad_rate'].mean() * 100).round(2))
print()

# Group by IC_LEVEL and show average as percent
print("Average Pell Graduation Rate by IC_LEVEL:")
print((PELL_GR_CLEANED.groupby('IC_LEVEL')['pell_grad_rate'].mean() * 100).round(2))
print()

# Group by CONTROL and show average as percent
print("Average Pell Graduation Rate by CONTROL:")
print((PELL_GR_CLEANED.groupby('CONTROL')['pell_grad_rate'].mean() * 100).round(2))

```

    Average Pell Graduation Rate by HBCU:
    HBCU
    0.0    43.51
    1.0    29.27
    Name: pell_grad_rate, dtype: float64
    
    Average Pell Graduation Rate by IC_LEVEL:
    IC_LEVEL
    At least 2 but less than 4 years    34.32
    Four or more years                  46.21
    Name: pell_grad_rate, dtype: float64
    
    Average Pell Graduation Rate by CONTROL:
    CONTROL
    Private not-for-profit    50.87
    Public                    36.64
    Name: pell_grad_rate, dtype: float64


### **Visualization of Pell Grant Graduation Rates Across Institution Types**

This code creates a grouped bar plot comparing Pell Grant graduation rates across different institution control types (Public vs Private) and institution levels (2-year vs 4-year). It uses the `seaborn` library for the bar plot and `matplotlib` for customization. The plot visually highlights how Pell Grant graduation rates vary across categories.

**Key Insights**:
- **Institution Control**: Public vs Private
- **Institution Level**: 2-year vs 4-year



```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a grouped bar plot comparing Pell Grant graduation rates across categories
PELL_GR_CLEANED.loc[:,"IC_LEVEL"]=PELL_GR_CLEANED["IC_LEVEL"].replace({"Four or more years":"4-year","At least 2 but less than 4 years":"2-year"})
plt.figure(figsize=(10,6))
sns.barplot(
    data=PELL_GR_CLEANED,
    x='CONTROL',
    y='pell_grad_rate',
    hue='IC_LEVEL',
    palette=['darkblue', 'darkred']
)
plt.title('Chart 1: Graduation Rates for Pell Grant Recipients: Comparison of Public vs Private, 2-year vs 4-year Institutions')
plt.xlabel('Institution Control')
plt.ylabel('Pell Grant Graduation Rate (%)')
plt.legend(title='Institution Level')
plt.show()

```


    
![png](AA_Final%20Exam_49_0.png)
    


### **Visualizing Graduation Rates of Pell Recipients by HBCU Status**


```python
import seaborn as sns
import matplotlib.pyplot as plt

# Replace 0 with "NON_HBCU" and 1 with "HBCU" 
PELL_GR_CLEANED.loc[:, "HBCU"] = PELL_GR_CLEANED["HBCU"].replace({0: "NON_HBCU", 1: "HBCU"})

# Define custom colors for CONTROL
palette = ['darkblue', 'darkred']

# Create a faceted bar plot
g = sns.catplot(
    data=PELL_GR_CLEANED,
    x="HBCU",
    y="pell_grad_rate",
    hue="CONTROL",
    col="IC_LEVEL",
    kind="bar",
    palette=palette,
    height=6,
    aspect=1
)

# Customize titles and labels
g.fig.subplots_adjust(top=0.85)
g.fig.suptitle("Chart 2:Graduation Rates of Pell Recipients by HBCU Status, Institution Control, and Level")
g.set_axis_labels("HBCU Status", "Pell Grant Graduation Rate (%)")
g._legend.set_title("Institution Control")

plt.show()

```


    
![png](AA_Final%20Exam_51_0.png)
    



```python

# Use matching string keys in the palette
palette = {"NON_HBCU": "darkred", "HBCU": "darkblue"}

# Re-attempt the plot
plt.figure(figsize=(12, 6))
sns.boxplot(data=PELL_GR_CLEANED, x="CONTROL", y="pell_grad_rate", hue="HBCU", palette=palette)
plt.title("Chart 3: Pell Graduation Rate by Institutional Control and HBCU Status")
plt.xlabel("Institutional Control (Public, Private Nonprofit, Private For-Profit)")
plt.ylabel("Pell Graduation Rate")
plt.legend(title="HBCU Status")
plt.show()

```


    
![png](AA_Final%20Exam_52_0.png)
    


## **Explanatory Analysis**

### Graduation Outcomes by Institutional Control and Level

Analysis of institutional-level data reveals pronounced disparities in Pell Grant recipient graduation rates when disaggregated by control (public vs. private) and level (2-year vs. 4-year). Among 4-year institutions, **private not-for-profit colleges exhibit the highest median graduation rate for Pell recipients (51%)**, surpassing their public 4-year counterparts (40%). A similar pattern emerges among 2-year institutions, where **private not-for-profits again outperform public institutions** (63% vs. 33%).

These patterns suggest that **private not-for-profit institutions may offer environments more conducive to student success** among Pell recipients, potentially due to factors such as smaller student-to-faculty ratios, greater financial support, or more robust academic advising infrastructures. Moreover, the data reveal that institutional level itself is an important determinant: 4-year institutions tend to yield higher graduation rates than 2-year colleges within the same control category, except in the case of private not-for-profits, where 2-year institutions slightly outperform their 4-year peers.

> **Interpretation**: These results underscore the influence of institutional resources and infrastructure on low-income student outcomes. The consistent advantage seen among private not-for-profits highlights systemic differences in how institutions support Pell Grant recipients.

### The Role of HBCU Designation in Graduation Outcomes

When institutional control and level are considered alongside **HBCU status**, new dimensions of disparity emerge. Among 4-year institutions, **non-HBCU private not-for-profits again lead in graduation outcomes (~51%)**, while **HBCUs—both public and private—lag behind at approximately 32%**. In the 2-year sector, the divergence is even more pronounced: **non-HBCU private not-for-profits maintain high Pell graduation rates (63%)**, whereas **HBCU public institutions exhibit significantly lower rates (approximately 20%)**.

These gaps signal that **HBCUs, while vital in expanding access to higher education for historically underserved populations, may face structural and financial challenges** that inhibit graduation outcomes for Pell recipients. This may include limited access to federal funding, higher rates of student financial need, and under-resourced student support services.

> **Interpretation**: The persistent underperformance of HBCUs in graduation rates, even after accounting for institutional type and control, suggests that targeted investment in these institutions is essential to achieving equitable outcomes.

### Distributional Insights: Variability in Graduation Outcomes

A box plot comparing graduation rates across institution types and HBCU status offers further insights. **Non-HBCUs exhibit higher median graduation rates and broader variability**, especially in the private sector, where some institutions achieve Pell recipient graduation rates near 100%. In contrast, **HBCUs show lower medians and narrower interquartile ranges**, suggesting both consistently lower performance and less variability in outcomes.

> **Interpretation**: This distributional compression among HBCUs may reflect a systemic cap imposed by resource limitations. The broader range seen in non-HBCU institutions—particularly private ones—may point to differentiated institutional strategies or capacities to support Pell recipients.

## Synthesis and Policy Implications

Collectively, these findings demonstrate that:

1. **Institutional control and level are significant predictors of Pell Grant recipient graduation rates**, with private not-for-profit institutions consistently yielding better outcomes.
2. **HBCU designation is associated with lower graduation rates**, even after controlling for structural characteristics, highlighting persistent inequities.
3. The intersection of financial aid, institutional characteristics, and racialized institutional identity underscores the **need for targeted, equity-focused policy interventions**.

These insights contribute to ongoing scholarship in the fields of **higher education policy, educational equity, and socioeconomic mobility**, and should inform both funding decisions and institutional practices aimed at improving graduation outcomes for low-income and historically marginalized student populations.


## Linear Regression Analysis of Institutional Factors Affecting Pell Grant Graduation Rates


```python
import pandas as pd
import statsmodels.api as sm

# Replace string categories with numeric values for HBCU, CONTROL, and IC_LEVEL
PELL_GR_CLEANED.loc[:, 'HBCU'] = PELL_GR_CLEANED['HBCU'].replace({
    'HBCU': 1,
    'NON_HBCU': 0
})

PELL_GR_CLEANED.loc[:, 'CONTROL'] = PELL_GR_CLEANED['CONTROL'].replace({
    'Public': 1,
    'Private not-for-profit': 2
})

# IC_LEVEL mapping: '2-year' -> 1, '4-year' -> 2
PELL_GR_CLEANED.loc[:, 'IC_LEVEL'] = PELL_GR_CLEANED['IC_LEVEL'].replace({
    '2-year': 1,
    '4-year': 2
})

# Check for any non-numeric values in the independent variables
print(PELL_GR_CLEANED[['HBCU', 'CONTROL', 'IC_LEVEL']].dtypes)  # Ensure they are integers or floats

# Optionally, check unique values to see if any non-numeric values still exist
print(PELL_GR_CLEANED[['HBCU', 'CONTROL', 'IC_LEVEL']].apply(pd.Series.nunique))

# Define independent (X) and dependent (y) variables
X = PELL_GR_CLEANED[['HBCU', 'CONTROL', 'IC_LEVEL']].astype(float)

# Check for missing or invalid values in X
if X.isnull().any().any():
    print("Missing values found in independent variables, please clean them.")
else:
    print("No missing values in independent variables.")

y = PELL_GR_CLEANED['pell_grad_rate'].astype(float)

# Add constant for intercept
X = sm.add_constant(X)

# Run the regression model
pell_simple_model = sm.OLS(y, X).fit()

# Show the regression table
print(pell_simple_model.summary2().tables[1])

```

    HBCU         int64
    CONTROL      int64
    IC_LEVEL    object
    dtype: object
    HBCU        2
    CONTROL     2
    IC_LEVEL    2
    dtype: int64
    No missing values in independent variables.
                 Coef.  Std.Err.          t         P>|t|    [0.025    0.975]
    const     0.160650  0.011301  14.215790  4.240458e-45  0.138496  0.182804
    HBCU     -0.146973  0.017453  -8.420979  4.669191e-17 -0.181188 -0.112758
    CONTROL   0.117593  0.005973  19.688676  1.476243e-83  0.105885  0.129302
    IC_LEVEL  0.058998  0.006840   8.625299  8.173293e-18  0.045589  0.072407


### Model Interpretation

The regression results you provided show the relationship between the variables `HBCU`, `CONTROL`, and `IC_LEVEL` with respect to the dependent variable, which is `pell_grad_rate`. Below is the interpretation of the output:

#### Model Summary:
| **Variable** | **Coefficient (Coef.)** | **Standard Error (Std.Err.)** | **t-statistic (t)** | **p-value (P>|t|)** | **95% Confidence Interval** |
|--------------|------------------------|-------------------------------|---------------------|---------------------|----------------------------|
| **const**    | 0.160650               | 0.011301                      | 14.216              | 4.24e-45            | [0.138496, 0.182804]       |
| **HBCU**     | -0.146973              | 0.017453                      | -8.421              | 4.67e-17            | [-0.181188, -0.112758]     |
| **CONTROL**  | 0.117593               | 0.005973                      | 19.689              | 1.48e-83            | [0.105885, 0.129302]       |
| **IC_LEVEL** | 0.058998               | 0.006840                      | 8.625               | 8.17e-18            | [0.045589, 0.072407]       |

---

### Key Findings:

1. **Intercept (const)**:
   - **Coefficient**: 0.160650
   - This indicates that when all the independent variables (`HBCU`, `CONTROL`, and `IC_LEVEL`) are zero, the expected value of `pell_grad_rate` is 0.160650. While this may not have a direct real-world interpretation in context (since `HBCU`, `CONTROL`, and `IC_LEVEL` are categorical), the constant helps establish the baseline for the model.

2. **HBCU**:
   - **Coefficient**: -0.146973
   - A negative coefficient for `HBCU` suggests that being a Historically Black College or University (HBCU) is associated with a decrease in the graduation rate for Pell Grant recipients, holding other variables constant. Specifically, the graduation rate for HBCUs is about 0.147 lower than for non-HBCUs.
   - **t-statistic**: -8.421 (which is statistically significant, given the large magnitude of the t-statistic).
   - **p-value**: 4.67e-17, which is very small, indicating strong statistical significance.
   - **Confidence Interval**: The 95% confidence interval for this coefficient ranges from -0.181188 to -0.112758, meaning that we are 95% confident that the true effect of being an HBCU on the graduation rate is between these values.

3. **CONTROL**:
   - **Coefficient**: 0.117593
   - The positive coefficient for `CONTROL` suggests that private not-for-profit institutions (represented by a value of 2 in the model) are associated with a higher Pell Grant graduation rate compared to public institutions, by approximately 0.118, controlling for other factors.
   - **t-statistic**: 19.689, which is very high, indicating a strong relationship between `CONTROL` and graduation rates.
   - **p-value**: 1.48e-83, which is extremely small, confirming the variable’s statistical significance.
   - **Confidence Interval**: The 95% confidence interval for the `CONTROL` coefficient is [0.105885, 0.129302], indicating a positive and significant effect.

4. **IC_LEVEL**:
   - **Coefficient**: 0.058998
   - The positive coefficient for `IC_LEVEL` suggests that the level of institution (2-year vs. 4-year) has a positive effect on Pell Grant graduation rates. Specifically, moving from a 2-year to a 4-year institution is associated with an increase of approximately 0.059 in the graduation rate, holding other variables constant.
   - **t-statistic**: 8.625, which is statistically significant.
   - **p-value**: 8.17e-18, which is very small, indicating the variable is highly significant.
   - **Confidence Interval**: The 95% confidence interval for `IC_LEVEL` is [0.045589, 0.072407], suggesting that the true effect lies within this range.

---

### Conclusion:
- **HBCU** is associated with a significant negative impact on Pell Grant graduation rates, indicating that students at HBCUs, on average, have lower graduation rates compared to students at non-HBCUs.
- **CONTROL** (institution type) has a positive effect on graduation rates, with private not-for-profit institutions outperforming public institutions.
- **IC_LEVEL** indicates that students at 4-year institutions have a higher graduation rate than those at 2-year institutions.

All independent variables are statistically significant with very small p-values, confirming their impact on the dependent variable, `pell_grad_rate`.


## **Synthesis, Policy Implications, and Conclusion**

The findings from this analysis reveal critical insights into the structural factors influencing graduation outcomes among Pell Grant recipients in U.S. higher education. Specifically:

1. **Institutional control and level emerge as significant predictors of Pell Grant recipient graduation rates**. Private not-for-profit institutions consistently demonstrate higher completion rates compared to their public counterparts, underscoring the role of institutional resources and support structures in promoting student success.

2. **HBCU designation is associated with significantly lower graduation rates** for Pell recipients, even after controlling for institutional control and level. This persistent disparity highlights the compounded effects of historical underfunding and systemic inequities faced by Historically Black Colleges and Universities. These findings call for renewed federal and state investment to strengthen capacity at HBCUs and support their predominantly underserved student populations.

3. The intersection of financial aid, institutional type, and racialized institutional identity underscores the **urgent need for equity-centered policy reforms**. Addressing these disparities requires a multifaceted approach that not only expands access to aid but also ensures that institutional environments are resourced and structured to foster equitable outcomes.

### **Conclusion**

The regression analysis confirms that:

- **HBCU status** is significantly and negatively associated with Pell Grant recipient graduation rates, indicating systemic challenges that continue to hinder student success in these institutions.
- **Institutional control (CONTROL)** exerts a positive influence on outcomes, with private not-for-profit institutions outperforming public ones in terms of Pell recipient graduation rates.
- **Institutional level (IC_LEVEL)** also plays a meaningful role, with students at 4-year institutions more likely to complete their programs than those at 2-year colleges.

All independent variables were found to be statistically significant, reinforcing the robustness of these relationships.

These insights contribute meaningfully to the broader literature on **higher education policy, educational equity, and socioeconomic mobility**, and should guide both policy development and institutional strategies aimed at improving postsecondary outcomes for Pell Grant recipients and other historically marginalized student populations.


## **Next Steps**

Building upon the current findings, several avenues for future research and analysis are recommended:

1. **Multivariate Regression Modeling**:  
   Conduct regression analyses to examine the predictive power of institutional characteristics (e.g., control, level, HBCU status) and Pell Grant distribution on graduation rates. This would allow for controlling multiple variables simultaneously and identifying the strongest predictors.

2. **Longitudinal Analysis**:  
   Incorporate multiple years of IPEDS data to assess whether the observed relationships persist over time. A time-series approach could help determine if certain institutions or sectors are improving in Pell Grant graduation outcomes.

3. **Institutional Resource Variables**:  
   Integrate data on institutional expenditures per student, student-to-faculty ratio, and academic support services. This could offer deeper insights into why certain types of institutions yield higher graduation rates among Pell recipients.

4. **Student Demographic Subgroups**:  
   Where possible, extend the analysis by disaggregating Pell recipient outcomes by race/ethnicity, gender, and first-generation status to assess how intersecting identities impact graduation outcomes.

5. **Predictive Modeling and Machine Learning**:  
   Explore supervised learning techniques (e.g., decision trees, random forests) to predict Pell recipient graduation likelihood based on institutional and financial aid variables. This could inform targeted interventions.

> **Conclusion**:  
These future steps aim to deepen understanding of how financial aid interacts with institutional characteristics to shape student success. They also provide a pathway for transitioning from descriptive insights to actionable strategies that promote educational equity.



```python

```
