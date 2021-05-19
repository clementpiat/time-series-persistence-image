import numpy as np
from gudhi.representations.vector_methods import PersistenceImage

def persistence_diagram(f):
    """
    compute PD being given a function f as a list of values (can typically be a time series)
        - f: a list (or a 1D numpy array) of POSITIVE values
    """
    barcodes = []
    
    n_points = len(f)
    sorted_f = sorted([(y+1,i) for i,y in enumerate(f)])
    tmp = np.zeros(n_points)
    
    for y,i in sorted_f:
        y1 = tmp[i-1] if i>0 else 0
        y2 = tmp[i+1] if i<(n_points-1) else 0
        
        if y1 and y2:
            # Then we merge segments
            if y1 <= y2:
                # Spread y1 to the right
                tmp[i] = y1
                j = i+1
                while(j<n_points and tmp[j]==y2):
                    tmp[j] = y1
                    j+=1
                barcodes.append((y2-1, y-1))
            else:
                # Spread y2 to the left
                tmp[i] = y2
                j = i-1
                while(j>=0 and tmp[j]==y1):
                    tmp[j] = y2
                    j-=1
                barcodes.append((y1-1, y-1))
                
        elif y2:
            tmp[i] = tmp[i+1]
        elif y1:
            tmp[i] = tmp[i-1]
        else:
            tmp[i] = y
    
    assert tmp[0] == tmp[-1]
    
    barcodes.append((tmp[0]-1, np.inf))
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