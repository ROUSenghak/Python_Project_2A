# Convert expected date to obtain month, is_weekend, saison
def calendar_features(d):
    """
    Input: 
    - d: date expected
    Return:
    month, is_weekend and season
    """
    month = d.month
    dayofweek = d.weekday()             # Monday=0, Sunday=6
    is_weekend = 1 if dayofweek >= 5 else 0
    saison = (month % 12) // 3
    return month, is_weekend, saison
