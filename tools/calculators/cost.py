"""Commercial arithmetic only. Does not invent labor rates, material prices or overheads."""

def price_from_margin(cost:float, margin_fraction:float)->float:
    if cost < 0: raise ValueError('cost must be >=0')
    if not 0 <= margin_fraction < 1: raise ValueError('margin_fraction must be in [0,1)')
    return cost/(1-margin_fraction)

def price_from_markup(cost:float, markup_fraction:float)->float:
    if cost < 0 or markup_fraction < 0: raise ValueError('cost and markup must be >=0')
    return cost*(1+markup_fraction)

def rollup(lines):
    """lines iterable of dict(name, amount, category?, evidence?)."""
    total=0.0; by_category={}; by_evidence={}
    for line in lines:
        amount=float(line['amount']); total+=amount
        cat=line.get('category','other'); by_category[cat]=by_category.get(cat,0.0)+amount
        ev=line.get('evidence','UNKNOWN'); by_evidence[ev]=by_evidence.get(ev,0.0)+amount
    return {'total':total,'by_category':by_category,'by_evidence':by_evidence}
