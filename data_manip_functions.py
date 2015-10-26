'''
Created on 26 Oct 2015
Functions for manipulating data for analysis of SoundCloud users in scotland 
For a paper for Scottish Music Review

@author: annajordanous
'''

import time
import logging


try: 
    logging.basicConfig(filename='scot_logs/log'+time.strftime('%Y%m%d-%H%M')+'.log',level=logging.DEBUG)
except Exception as e:
    logging.basicConfig(filename='scot_log'+time.strftime('%Y%m%d-%H%M')+'.log',level=logging.DEBUG)
    # on the assumption that we've been able to set up a logging file...
    # if we haven't, then this exception will crash the program, but this is a good thing as we want logging to work
    logging.warning('ERROR during initial imports setting up log file: '+e.message+' '+str(e.args))         




def read_in_data(file_path='scotland.txt'):
    place_list = [] 
    try:
        input_file = open(file_path)
        for line in input_file:
            line = line.lower()
            place_list.extend(line.splitlines())
    except Exception as e:            
        logging.warning('ERROR - problem reading in data in data_manip_functions.read_in_data(): '+e.message+' '+str(e.args))         
                    # set default of empty sets for each set of ids if there is no cPickle data
    return place_list
    
if __name__ == '__main__':
    read_in_data()