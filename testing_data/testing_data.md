# Bank Marketing Dataset - Random 20 Rows

| age |        job       |  marital  |  education | default | balance | housing |  loan | contact |  day | month | campaign | pdays | previous | poutcome | deposit |
|-----|-----------------|-----------|------------|---------|---------|---------|-------|---------|------|-------|----------|-------|----------|----------|---------|
|  58 |   management    |  married  |  tertiary  |   no    |  2143   |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |   yes   |
|  44 |   technician    |   single  | secondary  |   no    |   29    |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |    no   |
|  33 | entrepreneur    |  married  | secondary  |   no    |    2    |   yes   |  yes  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |   yes   |
|  47 |   blue-collar   |  married  |  unknown   |   no    |  1506   |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |    no   |
|  33 |   unknown       |   single  |  unknown   |   no    |    1    |    no   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |   yes   |
|  35 | management_self |  married  |  tertiary  |   no    |  231    |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |    no   |
|  28 |   unknown       |   single  |  tertiary  |   no    |  447    |   yes   |  yes  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |   yes   |
|  42 |   entrepreneur  | divorced  |  tertiary  |  yes    |    2    |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |   yes   |
|  58 |    retired      |  married  |  primary   |   no    |    121  |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |    no   |
|  43 |   technician    |   single  | secondary  |   no    |   593   |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |   yes   |
|  41 |   admin.        | divorced  | secondary  |   no    |    270  |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |   yes   |
|  29 |   admin.        |   single  | secondary  |   no    |   390   |   yes   |   no  | unknown |   5  |  may  |    2     |  -1   |    0     | unknown  |    no   |
|  53 |   technician    |  married  | secondary  |   no    |    6    |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |    no   |
|  58 |   technician    |  married  |  unknown   |   no    |    71   |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |    no   |
|  57 |    services     |  married  | secondary  |   no    |    162  |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |   yes   |
|  51 |    retired      |  married  |  tertiary  |   no    |    229  |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |   yes   |
|  45 |   technician    |  married  |  unknown   |   no    |    13   |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |    no   |
|  57 |   technician    |  married  |  tertiary  |   no    |    52   |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |   yes   |
|  60 |    retired      |  married  |  primary   |   no    |    60   |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |    no   |
|  33 |   services      |  married  | secondary  |   no    |    0    |   yes   |   no  | unknown |   5  |  may  |    1     |  -1   |    0     | unknown  |   yes   |

# Additional Information

Input variables:
- bank client data:
  1. age (numeric)
  2. job: type of job (categorical: admin.,blue-collar,entrepreneur,housemaid,management,retired,self-employed,services,student,technician,unemployed,unknown)
  3. marital: marital status (categorical: divorced,married,single,unknown; note: divorced means divorced or widowed)
  4. education (categorical: basic.4y,basic.6y,basic.9y,high.school,illiterate,professional.course,university.degree,unknown)
  5. default: has credit in default? (categorical: no,yes,unknown)
  6. housing: has housing loan? (categorical: no,yes,unknown)
  7. loan: has personal loan? (categorical: no,yes,unknown)
- related with the last contact of the current campaign:
  8. contact: contact communication type (categorical: cellular,telephone) 
  9. month: last contact month of year (categorical: jan, feb, mar, ..., nov, dec)
  10. day_of_week: last contact day of the week (categorical: mon,tue,wed,thu,fri)
  11. duration: last contact duration, in seconds (numeric). Important note:  this attribute highly affects the output target (e.g., if duration=0 then y=no). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.
- other attributes:
  12. campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
  13. pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
  14. previous: number of contacts performed before this campaign and for this client (numeric)
  15. poutcome: outcome of the previous marketing campaign (categorical: failure,nonexistent,success)
- social and economic context attributes:
  16. emp.var.rate: employment variation rate - quarterly indicator (numeric)
  17. cons.price.idx: consumer price index - monthly indicator (numeric)     
  18. cons.conf.idx: consumer confidence index - monthly indicator (numeric)     
  19. euribor3m: euribor 3 month rate - daily indicator (numeric)
  20. nr.employed: number of employees - quarterly indicator (numeric)

Output variable (desired target):
  21. y - has the client subscribed a term deposit? (binary: yes,no)

