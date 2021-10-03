#!/user/bin/env python
import sys

def mapper():
    '''
    Reads input data and propagates data. Returns print of key and value
    
    Output key: vin_number
    Output value: incident_type, make, year
    '''
    # Input comes from STDIN (standard input)
    for line in sys.stdin:
        # if 'q' == line.strip():
        #     break
        record = line.strip().split(',')
        key = record[2].strip()
        value = record[1].strip(), record[3].strip(), record[5].strip()
        print(f'{key}\t{value}')

    #print('exit')

if __name__ == '__main__':
     mapper()