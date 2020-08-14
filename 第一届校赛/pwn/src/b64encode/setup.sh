#!/bin/bash

cat > /home/ctf/run.sh << EOF
#!/bin/sh
ulimit -p 300
/bin/timeout 60 /b64encode
EOF