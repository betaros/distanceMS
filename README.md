# distanceMS
Microservice which calculates the distance based on GPS coordinates

Integrated Swagger API documentation

### Routes
#### /
Swagger documentation page

#### /distance/{coord}
API for calculating the distance in km between two points by given coordinates in **WGS84** format.
```
{coord} = Latitude1,Longitude1,Latitude2,Longitude2
```

*e.g.*
```
Berlin = 52.518611°, 13.408333°
Ingolstadt = 48.76415°, 11.42434°

{coord} = 52.518611,13.408333,48.76415,11.42434
```

*Output*
```
{
  "distance": 440.7208978264834
}
```

*Error handling*

In case of wrong values used as coordinates the result of the distance is 0.
```
{
  "distance": 0
}
```


#### Author
Jan Füsting
