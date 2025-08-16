import random

def has_custom_str(obj):
    if hasattr(obj, '__str__'):
        # Check if the __str__ method is not the one from the base 'object' class
        return getattr(obj, '__str__') is not object.__str__
    return False

import MyMovieGraphQL.Classes
missing_str = []
all_classess = [cls for cls in dir(MyMovieGraphQL.Classes) if not cls.startswith('_')]
for cls in all_classess:
    obj = getattr(MyMovieGraphQL.Classes, cls)
    if has_custom_str(obj):
        continue
    missing_str.append(cls)
print(f"classes missing __str__ method: {len(missing_str)}")
print(random.sample(missing_str, 10))
"""
    def __str__(self):
        pass
    def __repr__(self):
        pass
"""