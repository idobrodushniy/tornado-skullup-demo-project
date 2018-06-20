while true; do
 NMAP=$(nmap -p 8000 tornado_web)
 if echo "$NMAP" | grep "Host is up"; then
    echo "Nginx will be started and connected to the 'tornado_web' service"
    break
 fi
 sleep 2
 done

sh -c "nginx -g 'daemon off;'"
