#!/bin/bash
MEM=$(free -m | awk 'NR==2{printf "%.0f", $3*100/$2}')
DISK=$(df -h / | awk 'NR==2{print $5}' | tr -d '%')
echo "{\"memory\":$MEM,\"disk\":$DISK}" > /var/www/html/metrics.json
