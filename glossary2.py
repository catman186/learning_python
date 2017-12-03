jobs = {
    'mary': 'doctor',
    'billy': 'hair-stylist',
    'margaret': 'racecar driver',
    'greg': 'waiter',
    'susan': 'engineer',
    }

jobs['peter'] = 'nurse'
jobs['edna'] = 'estate agent'
jobs['wilson'] = 'teacher'
jobs['jacob'] = 'footballer'
jobs['hillary'] = 'accountant'

for name, job in jobs.items():
    print(name.title() + " is a " + job.title())
