# Time Series to Persistence Image
Little module to transform a time series into a persistent image.

Can be used to convert an arbitrarily long time series into a fixed size representation that embed topological information about the signal.

![Illustration](https://raw.githubusercontent.com/clementpiat/time-series-persistence-image/main/pipeline.png "ts2pi")

### Quickstart

Install with `pip install ts2pi` and use the function this way:
```python
from ts2pi import persistence_image
im = persistence_image([1,4.3,3,5.1,1.5]) # numpy array of shape (40,40)
```

### Overview

You might need to change the default values of the function parameters, because they highly depend on the time series you are manipulating.

```python
from ts2pi import persistence_image
import matplotlib.pyplot as plt

l = [1,4.3,3,5.1,1.5]
im = persistence_image(l, resolution=[40,40], t=3, bandwidth=0.1) # numpy array of shape <resolution>
plt.imshow(im)
```

Try changing the values of `t` and `bandwidth` and see how it looks. Ideally, you could expect to see several patches on the image, like in the example above.
