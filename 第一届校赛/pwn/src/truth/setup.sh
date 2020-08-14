#!/bin/bash

cat > /home/ctf/run.sh << EOF
#!/bin/sh
ulimit -p 300
/bin/timeout 60 /truth
EOF