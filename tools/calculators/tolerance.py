"""Basic 1D tolerance-stack math. Sign convention must be defined by the caller."""
import math

def worst_case(nominals, plus_minus):
    if len(nominals)!=len(plus_minus): raise ValueError('length mismatch')
    nominal=sum(nominals); tol=sum(abs(x) for x in plus_minus)
    return {'nominal':nominal,'min':nominal-tol,'max':nominal+tol,'plus_minus':tol}

def rss(nominals, one_sigma_or_equivalent):
    """RSS is statistical; only use when the supplied tolerances are valid inputs for the chosen statistical model."""
    if len(nominals)!=len(one_sigma_or_equivalent): raise ValueError('length mismatch')
    nominal=sum(nominals); t=math.sqrt(sum(float(x)**2 for x in one_sigma_or_equivalent))
    return {'nominal':nominal,'min':nominal-t,'max':nominal+t,'plus_minus':t}
