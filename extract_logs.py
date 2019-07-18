import os
import sys
import re
import datetime

###Supported timestamp formats
### [Sun Mar  7 17:27:37 2004] [info]......
### 64.242.88.10 - - [07/Mar/2004:16:33:53 -0800] "GET ....."

def get_filtered_messages(logfile, start_timestamp_str, end_timestamp_str, date_format_string):
    def select_pattern(line):
        for i, rgx in enumerate(compiled_ts_regexes):
            match = rgx.search(line)
            if match:
                return rgx, match
        return None, None
    def get_datetime(m):
        date_string = '{0}/{1}/{2:0>2}:{3}'.format(m.group('YYYY'), \
                                    m.group('MMM'), m.group('DD'), m.group('TIME'))
        return datetime.datetime.strptime(date_string, date_format_string)
    
    # Using pattern with Named Groups for easy access
    suported_timestamp_patters = [
        r'(\[\w{3}\s+(?P<MMM>\w{3})\s+(?P<DD>\d{1,2})\s+(?P<TIME>\d{2}:\d{2}:\d{2})\s+(?P<YYYY>\d{4})\])',
        r'(\[(?P<DD>\d{1,2})\/(?P<MMM>\w{3})\/(?P<YYYY>\d{4}):(?P<TIME>\d{2}:\d{2}:\d{2})[^\]]*\])'
    ]
    start_datetime = datetime.datetime.strptime(start_timestamp_str, date_format_string)
    end_datetime = datetime.datetime.strptime(end_timestamp_str, date_format_string)

    compiled_ts_regexes = []
    for patt in suported_timestamp_patters:
        compiled_ts_regexes.append(re.compile(patt))

    filtered_messages = []
    with open(logfile) as f:
        filtering_started = False
        selected_pattern = None
        # Reading line by line to handle huge log files (instead of readlines)
        line = f.readline()
        while line:
            if selected_pattern:
                match = selected_pattern.search(line)
            else:
                # Select one of the timestamp patterns based on first occurance;
                # then use that for the rest of the file
                selected_pattern, match = select_pattern(line)
            if match:
                line_datetime = get_datetime(match)
                if line_datetime >= start_datetime and line_datetime <= end_datetime:
                    filtering_started = True
                    filtered_messages.append(line[:-1])
                else:
                    filtering_started = False
            elif filtering_started:
                # This will add all the lines without the timestamp immediately after the 
                # matching line like stack trace, exceptions etc
                if line.strip():
                    filtered_messages.append(line[:-1])
            line = f.readline()
    return filtered_messages

def main():
    logfile = '/Users/ayusuf/Downloads/apache-samples/LOGS/error_log'
    start_timestamp_str = '2004/Mar/08:14:27:46'
    end_timestamp_str = '2004/Mar/11:02:27:34'
    #logfile = '/Users/ayusuf/Downloads/apache-samples/LOGS/access_log'
    #start_timestamp_str = '2004/Mar/11:20:49:38'
    #end_timestamp_str = '2004/Mar/12:05:25:26'

    date_format_string = '%Y/%b/%d:%H:%M:%S'  # Format YYYY/Mmm/DD:24HH:MI:SS

    selected_messages = get_filtered_messages(logfile, start_timestamp_str, \
                                    end_timestamp_str, date_format_string)

    print 'Searching for logs between (including both): {0} and {1}\n'.format(start_timestamp_str, \
                                                        end_timestamp_str)
    if not selected_messages:
        print 'No matching lines'
    else:
        for line in selected_messages:
            print line

if __name__ == "__main__":
    main()
