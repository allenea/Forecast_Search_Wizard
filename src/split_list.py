# Forecast Search Wizard
def split_list(lst, split):
    """Yield successive n-sized chunks from l."""
    if split == 0:
        split = len(lst)
    outlst = [lst[i:i + split] for i in range(0, len(lst), split)]
    return outlst