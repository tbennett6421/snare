cat $in_file | grep -v ^# | cut -d" " -f2 > dnsservers-targets.lst
