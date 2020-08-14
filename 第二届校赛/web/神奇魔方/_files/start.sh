#!/usr/bin/env sh

# Author : Virink <virink@outlook.com>
# Date   : 2019/09/06, 14:12
# Edit   : Hn13 <root@hn13.top>

export FLAG=zstuctf{d1rec7ory_cr0ss1ng_1s_fun}
FLAG=zstuctf{d1rec7ory_cr0ss1ng_1s_fun}

if [[ ! -f /W3lc0me_7o_2stuctf/flag ]]; then
    rm -rf /W3lc0me_7o_2stuctf
	mkdir -p /W3lc0me_7o_2stuctf
    echo $FLAG >> /W3lc0me_7o_2stuctf/flag
fi



/usr/local/openresty/bin/openresty -g "daemon off;" 