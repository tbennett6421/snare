#!/bin/bash
for ip in $(seq 1 254);do echo $1.$ip;done > ips
