# Repro for https://github.com/grpc/grpc/pull/40989

Client log:

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
