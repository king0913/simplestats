def mean(vals):
    """Computes the mean from a list of values."""
    try:
        total = float(sum(vals))
        length = len(vals)
    except TypeError:
        raise TypeError("The list was not numbers.")
    except:
        print "Something unknown happened with the list."
<<<<<<< HEAD
    return float(total)/length
=======
    return total/length

def median(vals):
    """please implement this function"""
    return 1
>>>>>>> b1e0aaacc890acaf24797ececbd3d83c4f4a7923

def mode(vals):
    """Computes the mode from a list of values."""
    pass

def std(vals):
    """Computes the standard deviation from a list of values."""
    n = len(vals)
    if n == 0:
        return 0.0
    mu = sum(vals) / n
    if mu == 1e500:
        return NotImplemented
    var = 0.0
    for val in vals:
        var = var + (val - mu)**2
    return (var / n)**0.5

def var(vals):
    """Computes the variance from a list of values."""
    pass
 

