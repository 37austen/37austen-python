This is a library that provides access to 37AUSTEN"s proprietary algorithms.

## Installation

```

pip install thirtysevena 

```
## Full API Documentation 

The full API documentation can be found via https://www.37austen.com/api/documentation 

## Usage:

The functions in this library are:

1. Login
2. Token Refresh
3. Future Movement Algorithm 
4. Future Movement Group Algorithm 
5. Future Movement FX Algorithm 
6. Future Movement Token Algorithm 
7. Correlation Algorithm 

The accepted licence types are:

1. Trial - t 
2. Single User - s 
3. Enterprise - e 

## Token Refresh

```

import thirtysevena as tsa

email = "name@email.com"
password = "notpassword"
licence = "e"

client = tsa.Client(email, password, licence)
client.token_refresh()

```

## Future Movement Algorithm Example

```
import thirtysevena as tsa

email = "name@email.com"
password = "notpassword"
licence = "e"

client = tsa.Client(email, password, licence)
client.login()

data = {

"Metadata" : { "Label" : "Gamestop", "ID" : "Equity", "Timeframe" : "Daily" },

"P1" : { "Date" : "2020-12-01 00:00:00", "Open" : 17.11, "High" : 17.4, "Low" : 15.76, "Close" : 15.8 },

"P2" : { "Date" : "2020-12-02 00:00:00", "Open" : 15.7, "High" : 16.68, "Low" : 15.38, "Close" : 16.58 },

"P3" : { "Date" : "2020-12-03 00:00:00", "Open" : 16.48, "High" : 16.64, "Low" : 15.87, "Close" : 16.12 },

"P4" : { "Date" : "2020-12-04 00:00:00", "Open" : 16.3, "High" : 17.29, "Low" : 16.26, "Close" : 16.9 },

"P5" : { "Date" : "2020-12-07 00:00:00", "Open" : 17.0, "High" : 17.5, "Low" : 16.22, "Close" : 16.35 },

"P6" : { "Date" : "2020-12-08 00:00:00", "Open" : 16.37, "High" : 17.21, "Low" : 15.93, "Close" : 16.94 },

"P7" : { "Date" : "2020-12-09 00:00:00", "Open" : 13.92, "High" : 14.73, "Low" : 13.225, "Close" : 13.66 },

"P8" : { "Date" : "2020-12-10 00:00:00", "Open" : 13.12, "High" : 14.41, "Low" : 13.05, "Close" : 14.12 },

"P9" : { "Date" : "2020-12-11 00:00:00", "Open" : 13.91, "High" : 14.0, "Low" : 13.02, "Close" : 13.31 },

"P10" : { "Date" : "2020-12-14 00:00:00", "Open" : 13.34, "High" : 13.4335, "Low" : 12.14, "Close" : 12.72 },

"P11" : { "Date" : "2020-12-15 00:00:00", "Open" : 13.0 }

}

response = client.future_movement(data)

```

## Future Movement Group Algorithm Example

```
import thirtysevena as tsa

email = "name@email.com"
password = "notpassword"
licence = "e"

client = tsa.Client(email, password, licence)
client.login()

data = {

"Metadata" : {"Label" : "Hypothetical Asset", "ID" : "Index", "Timeframe" : "3 Days" },

"P1" : { "Date" : "2020-02-03 00:00:00", "Open" : 26189.61, "High" : 26512.58, "Low" : 26145.59, "Close" : 26356.98 },

"P2" : { "Date" : "2020-02-04 00:00:00", "Open" : 26491.66, "High" : 26730.26, "Low" : 26491.66, "Close" : 26675.98 },

"P3" : { "Date" : "2020-02-05 00:00:00", "Open" : 26869.32, "High" : 26926.12, "Low" : 26641.92, "Close" : 26786.74 },

"P4" : { "Date" : "2020-02-06 00:00:00", "Open" : 27174.53, "High" : 27608.22, "Low" : 27029.49, "Close" : 27493.7 },

"P5" : { "Date" : "2020-02-07 00:00:00", "Open" : 27356.28, "High" : 27410.58, "Low" : 27224.12, "Close" : 27404.27 },

"P6" : { "Date" : "2020-02-10 00:00:00", "Open" : 27092.15, "High" : 27314.64, "Low" : 27044.88, "Close" : 27241.34 },

"P7" : { "Date" : "2020-02-11 00:00:00", "Open" : 27514.25, "High" : 27674.81, "Low" : 27436.99, "Close" : 27583.88 },

"P8" : { "Date" : "2020-02-12 00:00:00", "Open" : 27717.22, "High" : 27892.48, "Low" : 27614.83, "Close" : 27823.66 },

"P9" : { "Date" : "2020-02-13 00:00:00", "Open" : 27953.65, "High" : 27953.65, "Low" : 27695.6, "Close" : 27730.0 },

"P10" : { "Date" : "2020-02-14 00:00:00", "Open" : 27698.56, "High" : 27960.66, "Low" : 27695.59, "Close" : 27815.6 },

"P11" : { "Date" : "2020-02-17 00:00:00", "Open" : 27766.71, "High" : 28055.58, "Low" : 27766.71, "Close" : 27959.6 },

"P12" : { "Date" : "2020-02-18 00:00:00", "Open" : 27766.5, "High" : 27771.3, "Low" : 27496.25, "Close" : 27530.2 },

"P13" : { "Date" : "2020-02-19 00:00:00", "Open" : 27486.46, "High" : 27697.46, "Low" : 27448.6, "Close" : 27655.81 },

"P14" : { "Date" : "2020-02-20 00:00:00", "Open" : 27767.28, "High" : 27767.28, "Low" : 27383.13, "Close" : 27609.16 },

"P15" : { "Date" : "2020-02-21 00:00:00", "Open" : 27450.46, "High" : 27484.53, "Low" : 27264.78, "Close" : 27308.81 },

"P16" : { "Date" : "2020-02-24 00:00:00", "Open" : 27105.35, "High" : 27105.35, "Low" : 26813.22, "Close" : 26820.88 },

"P17" : { "Date" : "2020-02-25 00:00:00", "Open" : 26722.39, "High" : 26914.05, "Low" : 26667.04, "Close" : 26893.23 },

"P18" : { "Date" : "2020-02-26 00:00:00", "Open" : 26479.9, "High" : 26776.06, "Low" : 26479.9, "Close" : 26696.49 },

"P19" : { "Date" : "2020-02-27 00:00:00", "Open" : 26529.17, "High" : 26849.57, "Low" : 26419.97, "Close" : 26778.62 },

"P20" : { "Date" : "2020-02-28 00:00:00", "Open" : 26249.06, "High" : 26313.55, "Low" : 25989.41, "Close" : 26129.93 },

"P21" : { "Date" : "2020-03-02 00:00:00", "Open" : 26077.73, "High" : 26375.91, "Low" : 26077.73, "Close" : 26291.68 },

"P22" : { "Date" : "2020-03-03 00:00:00", "Open" : 26419.13, "High" : 26527.75, "Low" : 26233.39, "Close" : 26284.82 },

"P23" : { "Date" : "2020-03-04 00:00:00", "Open" : 26321.56, "High" : 26372.48, "Low" : 26038.39, "Close" : 26222.07 },

"P24" : { "Date" : "2020-03-05 00:00:00", "Open" : 26348.16, "High" : 26805.58, "Low" : 26315.36, "Close" : 26767.87 },

"P25" : { "Date" : "2020-03-06 00:00:00", "Open" : 26397.78, "High" : 26408.8, "Low" : 26084.23, "Close" : 26146.67 },

"P26" : { "Date" : "2020-03-09 00:00:00", "Open" : 25134.02, "High" : 25321.28, "Low" : 24948.38, "Close" : 25040.46 },

"P27" : { "Date" : "2020-03-10 00:00:00", "Open" : 25285.68, "High" : 25578.61, "Low" : 24978.97, "Close" : 25392.51 },

"P28" : { "Date" : "2020-03-11 00:00:00", "Open" : 25459.96, "High" : 25493.23, "Low" : 25140.38, "Close" : 25231.61 },

"P29" : { "Date" : "2020-03-12 00:00:00", "Open" : 24657.67, "High" : 24657.67, "Low" : 24117.94, "Close" : 24309.07 },

"P30" : { "Date" : "2020-03-13 00:00:00", "Open" : 22519.32, "High" : 24184.48, "Low" : 22519.32, "Close" : 24032.91 },

"P31" : { "Date" : "2020-03-16 00:00:00", "Open" : 23317.81 }

}

response = client.future_movement_group(data)

```

## Future Movement FX Algorithm Example

```
import thirtysevena as tsa

email = "name@email.com"
password = "notpassword"
licence = "e"

client = tsa.Client(email, password, licence)
client.login()

data = {

"Metadata" : {"Label" : "GBP/EUR", "ID" : "FX", "Timeframe" : "Daily" },

"P1" : { "Date" : "2021-02-08 00:00:00", "Open" : 1.1401, "High" : 1.1412, "Low" : 1.1373, "Close" : 1.1401 },

"P2" : { "Date" : "2021-02-09 00:00:00", "Open" : 1.1403, "High" : 1.1411, "Low" : 1.1366, "Close" : 1.1404 },

"P3" : { "Date" : "2021-02-10 00:00:00", "Open" : 1.1402, "High" : 1.1425, "Low" : 1.1387, "Close" : 1.14 },

"P4" : { "Date" : "2021-02-11 00:00:00", "Open" : 1.1411, "High" : 1.1424, "Low" : 1.1381, "Close" : 1.1411 },

"P5" : { "Date" : "2021-02-12 00:00:00", "Open" : 1.1385, "High" : 1.1434, "Low" : 1.1372, "Close" : 1.1383 },

"P6" : { "Date" : "2021-02-15 00:00:00", "Open" : 1.1442, "High" : 1.147, "Low" : 1.1439, "Close" : 1.1441 },

"P7" : { "Date" : "2021-02-16 00:00:00", "Open" : 1.1467, "High" : 1.1495, "Low" : 1.1441, "Close" : 1.1464 },

"P8" : { "Date" : "2021-02-17 00:00:00", "Open" : 1.1486, "High" : 1.1519, "Low" : 1.1467, "Close" : 1.1484 },

"P9" : { "Date" : "2021-02-18 00:00:00", "Open" : 1.151, "High" : 1.1569, "Low" : 1.1491, "Close" : 1.151 },

"P10" : { "Date" : "2021-02-19 00:00:00", "Open" : 1.1551, "High" : 1.1568, "Low" : 1.1523, "Close" : 1.1551 },

"P11" : { "Date" : "2021-02-22 00:00:00", "Open" : 1.1569 }

}

response = client.future_movement_fx(data)

```

## Future Movement Token Algorithm Example

```
import thirtysevena as tsa

email = "name@email.com"
password = "notpassword"
licence = "e"

client = tsa.Client(email, password, licence)
client.login()

data = {

"Metadata" : {"Label" : "Example Token", "ID" : "Crypto Token", "Timeframe" : "Daily" },

"P1" : { "Date" : "2021-07-26 00:00:00", "Open " : 1.174122334, "High" : 1.174398184, "Low" : 1.174122334, "Close" : 1.174260259 },

"P2" : { "Date" : "2021-07-27 00:00:00", "Open " : 1.174260259, "High" : 1.174260259, "Low" : 1.174122334, "Close" : 1.174122334 },

"P3" : { "Date" : "2021-07-28 00:00:00", "Open " : 1.174122334, "High" : 1.174398184, "Low" : 1.174122334, "Close" : 1.174122334 },

"P4" : { "Date" : "2021-07-29 00:00:00", "Open " : 1.174398184, "High" : 1.174398184, "Low" : 1.173984528, "Close" : 1.173984528 },

"P5" : { "Date" : "2021-07-30 00:00:00", "Open " : 1.173984528, "High" : 1.174398184, "Low" : 1.173984528, "Close" : 1.173984528 },

"P6" : { "Date" : "2021-08-02 00:00:00", "Open " : 1.173984528, "High" : 1.174260259, "Low" : 1.173984528, "Close" : 1.173984528 },

"P7" : { "Date" : "2021-08-03 00:00:00", "Open " : 1.173846722, "High" : 1.173984528, "Low" : 1.173846722, "Close" : 1.173984528 },

"P8" : { "Date" : "2021-08-04 00:00:00", "Open " : 1.173846722, "High" : 1.174260259, "Low" : 1.173846722, "Close" : 1.173846722 },

"P9" : { "Date" : "2021-08-05 00:00:00", "Open " : 1.174260259, "High" : 1.174260259, "Low" : 1.173984528, "Close" : 1.173984528 },

"P10" : { "Date" : "2021-08-06 00:00:00", "Open " : 1.173984528, "High" : 1.173984528, "Low" : 1.173984528, "Close" : 1.173984528 },

"P11" : { "Date" : "2021-08-07 00:00:00", "Open " : 1.173846722 }

}

response = client.future_movement_token(data)

```

## Future Movement Correlation Algorithm Example

```
import thirtysevena as tsa

email = "name@email.com"
password = "notpassword"
licence = "e"

client = tsa.Client(email, password, licence)
client.login()

data = {

"Metadata" : { "A_Label" : "Asset 1", "B_Label" : "Asset 2", "Timeframe" : "Daily"},

"A_P1" : { "Date" : "2000-01-01 00:00:00", "Open" : 364.02, "High" : 364.31, "Low" : 364.01, "Close" : 364.31 },

"A_P2" : { "Date" : "2000-01-02 00:00:00", "Open" : 364.31, "High" : 364.58, "Low" : 364.01, "Close" : 364.01 },

"A_P3" : { "Date" : "2000-01-03 00:00:00", "Open" : 364.01, "High" : 364.21, "Low" : 364.01, "Close" : 364.11 },

"B_P1" : { "Date" : "2000-01-01 00:00:00", "Open" : 364.02, "High" : 364.31, "Low" : 364.01, "Close" : 364.31 },

"B_P2" : { "Date" : "2000-01-02 00:00:00", "Open" : 364.31, "High" : 364.58, "Low" : 364.01, "Close" : 364.01 },

"B_P3" : { "Date" : "2000-01-03 00:00:00", "Open" : 364.01, "High" : 364.21, "Low" : 364.01, "Close" : 364.11 }

}

response = client.correlation(data)

```

## License
Copyright 2021 37AUSTEN

This repository is licensed under MIT license. See LICENSE for details.
