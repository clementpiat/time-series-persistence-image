import numpy as np
from gudhi.representations.vector_methods import PersistenceImage

def persistence_diagram(f):
    """
    compute PD being given a function f as a list of values (can typically be a time series)
        - f: a list (or a 1D numpy array) of POSITIVE values
    """
    barcodes = []
    
    n_points = len(f)
    sorted_f = sorted([(y,i) for i,y in enumerate(f)])
    tmp = [[-1,0,0]]*n_points
    
    for y,i in sorted_f:
        y1 = tmp[i-1][0] if i>0 else -1
        y2 = tmp[i+1][0] if i<(n_points-1) else -1
        
        if y1>=0 and y2>=0:
            # Then we merge barcodes
            i2 = tmp[i+1][2]
            i1 = tmp[i-1][1]
            barcodes.append((max(y1,y2), y))            
            tmp[i1] = tmp[i2] = [min(y1,y2),i1,i2]
        elif y2>=0:
            i2 = tmp[i+1][2]
            tmp[i] = tmp[i2] = [y2,i,i2]
        elif y1>=0:
            i1 = tmp[i-1][1]
            tmp[i] = tmp[i1] = [y1,i1,i]
        else:
            tmp[i] = [y,i,i]
            
    # We don't add the last barcode because its upper-bound is the infinity
    return barcodes


def persistence_image(x, resolution=[40,40], t=3, bandwidth=0.1):
    """
    compute persistence image from a time series x
        - x: a list (or a 1D numpy array) of POSITIVE values
        - resolution: resolution of the output image
        - t: parameter of the weight function
        - bandwidth: parameter of the gaussian kernel
    """
    pd = persistence_diagram(x)[:-1] # get rid of the last feature because it has an infinite upper bound

    if not pd: 
        # then x is probably a constant time series
        return np.zeros(resolution)

    pi = PersistenceImage(resolution=resolution, bandwidth=bandwidth, weight=lambda x: min(x[1]/t, 1))
    im = pi.fit_transform(np.array([pd]))
    
    return im.reshape(resolution)