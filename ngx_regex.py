__author__ = 'xuguojun'

'''

# qiyi message nginx log format

log_format  notice  '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for" '
                    '$request_length $upstream_response_time $request_time $upstream_addr';

# the regex patten matches the log_format strictly.
patten = '\A(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s-\s(.*)\s\[(.*)\]\s"(.*)"\s(\d{3})\s(\d+)\s"(.*)"\s"(.*)"\s"(.*)"\s(\d+)\s([0-9]{1,}[.][0-9]*)\s([0-9]{1,}[.][0-9]*)\s(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d+)\Z'

'''


LOG_PATTEN = r'\A'
# '$remote_addr '
LOG_PATTEN += '(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s'
# '- '
LOG_PATTEN += '-\s'
# '$remote_user '
LOG_PATTEN += '(.*)\s'
# '[$time_local] '
LOG_PATTEN += '\[(.*)\]\s'
# '"$request" '
LOG_PATTEN += '"(.*)"\s'
# '$status $body_bytes_sent '
LOG_PATTEN += '(\d{3})\s(\d+)\s'
# '"$http_referer" '
LOG_PATTEN += '"(.*)"\s'
# '"$http_user_agent" '
LOG_PATTEN += '"(.*)"\s'
# '"$http_x_forwarded_for" '
LOG_PATTEN += '"(.*)"\s'
# '$request_length $upstream_response_time $request_time '
decimal = '([0-9]{1,}[.][0-9]*)'
LOG_PATTEN += '(\d+)\s' + decimal+'\s'+decimal+'\s'
# '$upstream_addr''
LOG_PATTEN += '(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d+)'
LOG_PATTEN += '\Z'
