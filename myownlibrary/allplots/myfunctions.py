def haversine(lon1: float, lat1: float, lon2: float, lat2: float)->float:
    """Calculate the great circle distance between two points on earth, returns the distance in meters
    :param lon1: logitude of first place
    :param lat1: latitude of first place
    :param lon2: longitude of second place
    :param lat2: latitude of second place
    :return: distance in meters between the two seats of coordinates
    """

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    #Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0) **2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km * 1000

def allplots(data=data):
  
  from matplotlib import pyplot as plt
  
  # create figure
  fig = plt.figure(figsize=(200,200))
    
  # setting values to rows and column variables
  rows = 41
  columns = 4
    
  # reading images
  data = data

  for i, color in enumerate(color_maps):
    # Adds a subplot at the 1st position
    fig.add_subplot(rows, columns, i+1)
    
    # showing image
    plt.imshow(data, cmap=color)
    plt.title(color)
  fig.savefig('new_color_map.png', dpi=100)