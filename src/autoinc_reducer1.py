#!/user/bin/env python

import sys
import re

def reset(make_year):
    return make_year == []

# Run for end of every group
def flush(accident):
    print(f'{accident}')

def reducer():
    '''
    Reads mapper output. Within each vin_number group, iterate through all the records to find the one that has the make and year available and captures that in group-level master info. Filter accident records and modify by adding the master info before outputing the accident records.

    Assumption: mapper output sorted by key (i.e. vin) before passed to the reducer.
    '''
    current_vin = None
    make_year = []
    accident = None
    
    # Input comes from STDIN
    for line in sys.stdin:
        # if 'q' == line.strip():
        #     break
        # [parse the input we got from mapper and update the master info]
        vin, record = line.strip().split('\t', 1)
        # [deter key changes]
        if current_vin != vin:
            if current_vin != None and accident != None:
                # Write result to STDOUT
                flush(accident)
            reset(make_year)

        # [update more master info after the key change handling]
        current_vin = vin

        value = record.split(',')
        value = [re.sub('[\W_]', '', x) for x in value] # Clean stringified list
        print('value[0] is ', value[0])

        if value[0] == 'I':
            make_year = [value[1+i] for i in range(2)]
            print('make_year is', make_year)
        elif value[0] == 'A':
            value[1], value[2] = make_year[0], make_year[1]
            accident = value

    # Output the last group if needed
    flush(accident)

if __name__ == '__main__':    
    reducer()