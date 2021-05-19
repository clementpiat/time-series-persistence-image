# Time Series to Persistence Image
Little module to transform a time series into a persistence image.

Can be used to convert an arbitrary long time series into a fixed size representation that embed topological information about the signal.

### Quickstart

Install with `pip install ts2pi` and use the function this way:
```python
from ts2pi import persistence_image
im = persistence_image([1,4.3,3,2,1.5])
```


