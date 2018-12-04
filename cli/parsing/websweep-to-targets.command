cat $in_file | grep -v Status | grep -v Nmap | cut -d  -f2 > webservers.lst
