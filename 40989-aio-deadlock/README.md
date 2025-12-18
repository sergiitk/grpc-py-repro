# Repro for https://github.com/grpc/grpc/pull/40989

Hang reproduced

```
$ ss -xpnm state connected | grep 139574
u_str ESTAB 0      0      * 516168  * 516167 users:(("python3",pid=139574,fd=5))  skmem:(r0,rb8192,t0,tb8192,f0,w0,o0,bl0,d0)
u_str ESTAB 0      11264  * 503168  * 503167 users:(("python3",pid=139574,fd=9))  skmem:(r0,rb8192,t11264,tb8192,f0,w0,o0,bl0,d0)
u_str ESTAB 8188   0      * 503167  * 503168 users:(("python3",pid=139574,fd=8))  skmem:(r0,rb8192,t0,tb8192,f0,w0,o0,bl0,d0)
u_str ESTAB 0      0      * 516167  * 516168 users:(("python3",pid=139574,fd=4))  skmem:(r0,rb8192,t0,tb8192,f0,w0,o0,bl0,d0)
```

```
sudo cat /proc/139574/task/139578/stack
[<0>] sock_alloc_send_pskb+0x168/0x240
[<0>] unix_stream_sendmsg+0x167/0x6a0
[<0>] bpf_trampoline_6442564013+0xc1/0x16b
[<0>] unix_stream_sendmsg+0x9/0x6a0
[<0>] sock_write_iter+0x18e/0x1a0
[<0>] vfs_write+0x3b4/0x450
[<0>] ksys_write+0xbe/0xe0
[<0>] bpf_trampoline_6442502961+0x71/0x11b
[<0>] __x64_sys_write+0x9/0x20
[<0>] do_syscall_64+0x84/0x320
[<0>] entry_SYSCALL_64_after_hwframe+0x76/0x7e
```

Client log with with `net.core.rmem_default` set to 8192:

```sh
$ python client.py
I1217 23:36:46.803 139785671926016 client.py:39] Verifying sysctl
I1217 23:36:46.805 139785671926016 client.py:43] sysctl LGTM
I1217 23:36:46.809 139785671926016 client.py:51] sending requests
I1217 23:36:46.809 139785671926016 client.py:31] sending from 0
I1217 23:36:46.809 139785671926016 client.py:31] sending from 1
I1217 23:36:46.809 139785671926016 client.py:31] sending from 2
I1217 23:36:46.809 139785671926016 client.py:31] sending from 3
I1217 23:36:46.809 139785671926016 client.py:31] sending from 4
I1217 23:36:46.809 139785671926016 client.py:31] sending from 5
I1217 23:36:46.809 139785671926016 client.py:31] sending from 6
I1217 23:36:46.809 139785671926016 client.py:31] sending from 7
I1217 23:36:46.809 139785671926016 client.py:31] sending from 8
I1217 23:36:46.810 139785671926016 client.py:31] sending from 9
I1217 23:36:46.815 139785671926016 client.py:35] #0 Greeter client received: Hello, you 0!
I1217 23:36:46.815 139785671926016 client.py:35] #8 Greeter client received: Hello, you 0!
I1217 23:36:46.816 139785671926016 client.py:35] #2 Greeter client received: Hello, you 0!
I1217 23:36:46.816 139785671926016 client.py:35] #5 Greeter client received: Hello, you 0!
I1217 23:36:46.816 139785671926016 client.py:35] #7 Greeter client received: Hello, you 0!
I1217 23:36:46.817 139785671926016 client.py:35] #3 Greeter client received: Hello, you 0!
I1217 23:36:46.817 139785671926016 client.py:35] #1 Greeter client received: Hello, you 0!
I1217 23:36:46.817 139785671926016 client.py:35] #9 Greeter client received: Hello, you 0!
I1217 23:36:46.817 139785671926016 client.py:35] #6 Greeter client received: Hello, you 0!
I1217 23:36:46.817 139785671926016 client.py:35] #4 Greeter client received: Hello, you 0!
I1217 23:37:07.144 139785671926016 client.py:35] #8 Greeter client received: Hello, you 30!
I1217 23:37:07.145 139785671926016 client.py:35] #0 Greeter client received: Hello, you 30!
I1217 23:37:07.731 139785671926016 client.py:35] #2 Greeter client received: Hello, you 30!
I1217 23:37:07.731 139785671926016 client.py:35] #5 Greeter client received: Hello, you 30!
I1217 23:37:07.732 139785671926016 client.py:35] #7 Greeter client received: Hello, you 30!
I1217 23:37:07.732 139785671926016 client.py:35] #3 Greeter client received: Hello, you 30!
I1217 23:37:07.732 139785671926016 client.py:35] #1 Greeter client received: Hello, you 30!
I1217 23:37:08.321 139785671926016 client.py:35] #9 Greeter client received: Hello, you 30!
I1217 23:37:08.321 139785671926016 client.py:35] #6 Greeter client received: Hello, you 30!
I1217 23:37:08.321 139785671926016 client.py:35] #4 Greeter client received: Hello, you 30!
I1217 23:37:27.940 139785671926016 client.py:35] #8 Greeter client received: Hello, you 60!
I1217 23:37:28.544 139785671926016 client.py:35] #0 Greeter client received: Hello, you 60!
I1217 23:37:28.544 139785671926016 client.py:35] #2 Greeter client received: Hello, you 60!
I1217 23:37:28.544 139785671926016 client.py:35] #5 Greeter client received: Hello, you 60!
I1217 23:37:28.544 139785671926016 client.py:35] #6 Greeter client received: Hello, you 60!
I1217 23:37:29.139 139785671926016 client.py:35] #7 Greeter client received: Hello, you 60!
I1217 23:37:29.139 139785671926016 client.py:35] #3 Greeter client received: Hello, you 60!
I1217 23:37:29.140 139785671926016 client.py:35] #1 Greeter client received: Hello, you 60!
I1217 23:37:29.140 139785671926016 client.py:35] #9 Greeter client received: Hello, you 60!
I1217 23:37:29.140 139785671926016 client.py:35] #4 Greeter client received: Hello, you 60!
I1217 23:37:48.736 139785671926016 client.py:35] #8 Greeter client received: Hello, you 90!
I1217 23:37:49.325 139785671926016 client.py:35] #0 Greeter client received: Hello, you 90!
I1217 23:37:49.325 139785671926016 client.py:35] #2 Greeter client received: Hello, you 90!
I1217 23:37:49.325 139785671926016 client.py:35] #5 Greeter client received: Hello, you 90!
I1217 23:37:49.899 139785671926016 client.py:35] #6 Greeter client received: Hello, you 90!
I1217 23:37:49.899 139785671926016 client.py:35] #7 Greeter client received: Hello, you 90!
I1217 23:37:49.899 139785671926016 client.py:35] #3 Greeter client received: Hello, you 90!
I1217 23:37:49.899 139785671926016 client.py:35] #1 Greeter client received: Hello, you 90!
I1217 23:37:49.899 139785671926016 client.py:35] #9 Greeter client received: Hello, you 90!
I1217 23:37:49.900 139785671926016 client.py:35] #4 Greeter client received: Hello, you 90!
I1217 23:37:56.420 139785671926016 client.py:53] done sending requests
```

Client log with both `net.core.rmem_default` and `net.core.wmem_default` set to 8192:

```sh
$ python client.py
I1217 23:07:36.708 140057533591808 client.py:39] Verifying sysctl
I1217 23:07:36.712 140057533591808 client.py:46] sysctl LGTM
I1217 23:07:36.714 140057533591808 client.py:54] sending requests
I1217 23:07:36.714 140057533591808 client.py:31] sending from 0
I1217 23:07:36.714 140057533591808 client.py:31] sending from 1
I1217 23:07:36.714 140057533591808 client.py:31] sending from 2
I1217 23:07:36.714 140057533591808 client.py:31] sending from 3
I1217 23:07:36.714 140057533591808 client.py:31] sending from 4
I1217 23:07:36.714 140057533591808 client.py:31] sending from 5
I1217 23:07:36.715 140057533591808 client.py:31] sending from 6
I1217 23:07:36.715 140057533591808 client.py:31] sending from 7
I1217 23:07:36.715 140057533591808 client.py:31] sending from 8
I1217 23:07:36.715 140057533591808 client.py:31] sending from 9
I1217 23:07:36.754 140057533591808 client.py:35] #9 Greeter client received: Hello, you 0!
I1217 23:07:36.789 140057533591808 client.py:35] #1 Greeter client received: Hello, you 0!
I1217 23:07:36.857 140057533591808 client.py:35] #5 Greeter client received: Hello, you 0!
I1217 23:07:36.925 140057533591808 client.py:35] #6 Greeter client received: Hello, you 0!
I1217 23:07:36.993 140057533591808 client.py:35] #3 Greeter client received: Hello, you 0!
I1217 23:07:37.070 140057533591808 client.py:35] #7 Greeter client received: Hello, you 0!
I1217 23:07:37.139 140057533591808 client.py:35] #4 Greeter client received: Hello, you 0!
I1217 23:07:37.207 140057533591808 client.py:35] #2 Greeter client received: Hello, you 0!
I1217 23:07:37.276 140057533591808 client.py:35] #8 Greeter client received: Hello, you 0!
I1217 23:07:37.310 140057533591808 client.py:35] #0 Greeter client received: Hello, you 0!
I1217 23:07:57.389 140057533591808 client.py:35] #9 Greeter client received: Hello, you 30!
I1217 23:07:57.423 140057533591808 client.py:35] #1 Greeter client received: Hello, you 30!
I1217 23:07:57.493 140057533591808 client.py:35] #5 Greeter client received: Hello, you 30!
I1217 23:07:57.561 140057533591808 client.py:35] #6 Greeter client received: Hello, you 30!
I1217 23:07:57.630 140057533591808 client.py:35] #3 Greeter client received: Hello, you 30!
I1217 23:07:57.698 140057533591808 client.py:35] #7 Greeter client received: Hello, you 30!
I1217 23:07:57.767 140057533591808 client.py:35] #4 Greeter client received: Hello, you 30!
I1217 23:07:57.835 140057533591808 client.py:35] #2 Greeter client received: Hello, you 30!
I1217 23:07:57.903 140057533591808 client.py:35] #8 Greeter client received: Hello, you 30!
I1217 23:07:57.936 140057533591808 client.py:35] #0 Greeter client received: Hello, you 30!
I1217 23:08:17.975 140057533591808 client.py:35] #9 Greeter client received: Hello, you 60!
I1217 23:08:18.016 140057533591808 client.py:35] #1 Greeter client received: Hello, you 60!
I1217 23:08:18.083 140057533591808 client.py:35] #5 Greeter client received: Hello, you 60!
I1217 23:08:18.151 140057533591808 client.py:35] #6 Greeter client received: Hello, you 60!
I1217 23:08:18.219 140057533591808 client.py:35] #3 Greeter client received: Hello, you 60!
I1217 23:08:18.287 140057533591808 client.py:35] #7 Greeter client received: Hello, you 60!
I1217 23:08:18.355 140057533591808 client.py:35] #4 Greeter client received: Hello, you 60!
I1217 23:08:18.423 140057533591808 client.py:35] #2 Greeter client received: Hello, you 60!
I1217 23:08:18.492 140057533591808 client.py:35] #8 Greeter client received: Hello, you 60!
I1217 23:08:18.526 140057533591808 client.py:35] #0 Greeter client received: Hello, you 60!
I1217 23:08:38.600 140057533591808 client.py:35] #9 Greeter client received: Hello, you 90!
I1217 23:08:38.634 140057533591808 client.py:35] #1 Greeter client received: Hello, you 90!
I1217 23:08:38.702 140057533591808 client.py:35] #5 Greeter client received: Hello, you 90!
I1217 23:08:38.769 140057533591808 client.py:35] #6 Greeter client received: Hello, you 90!
I1217 23:08:38.837 140057533591808 client.py:35] #3 Greeter client received: Hello, you 90!
I1217 23:08:38.905 140057533591808 client.py:35] #7 Greeter client received: Hello, you 90!
I1217 23:08:38.974 140057533591808 client.py:35] #4 Greeter client received: Hello, you 90!
I1217 23:08:39.051 140057533591808 client.py:35] #2 Greeter client received: Hello, you 90!
I1217 23:08:39.120 140057533591808 client.py:35] #8 Greeter client received: Hello, you 90!
I1217 23:08:39.155 140057533591808 client.py:35] #0 Greeter client received: Hello, you 90!
I1217 23:08:45.335 140057533591808 client.py:56] done sending requests
```
