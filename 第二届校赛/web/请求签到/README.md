**考点：**HTTP请求基础

**难度：**易

**Payload：**curl --location --request POST '127.0.0.1:7997/hn13/zstuctf?find=flag&%26%3D%26%3D%26=%2500%0a' \
--header 'X-Forwarded-For: hn13' \
--header 'User-Agent: hn13Browser' \
--header 'Accept-Language: fr' \
--header 'Connection: Close' \
--header 'Referer: https://www.hn13.top/' \
--header 'Authorization: Basic aG4xMzphRzR4TTJsemRHaGxZbVZ6ZEE9PQ=='

**Flag：**zstuctf{W31c0me_t0_25tuc7f}

