# figuring things out 1.78.0

> Note: GRPC_TRACE=api seem to be broken

* [\[Python\] grpcio==1.78.1 in python fails with certain googleapis like secrets manager, pubsub, bigquery, workflows (through its sdk) from Cloud Run Functions · Issue #41725 · grpc/grpc](https://github.com/grpc/grpc/issues/41725)
* https://github.com/googlecloudplatform/functions-framework-python
* [Support gRPC Python client-side fork with epoll1 by ericgribkoff · Pull Request #16264 · grpc/grpc](https://github.com/grpc/grpc/pull/16264)

### debugging
* https://github.com/grpc/grpc/blob/master/doc/trace_flags.md

## grpcio==1.78.1 fork off, initial call

**Result: WAI**

```log
$ TEST_INITIAL_CALL=1 GRPC_ENABLE_FORK_SUPPORT=0 GRPC_TRACE=api ff --target=hello
I0226 19:30:20.467  45696/140704384082176 main.py:22] ------------ Start: grpc 1.78.1
I0226 19:30:20.473  45696/140704384082176 main.py:27] ------------ Created the channel



I0226 19:30:20.977  45696/140704384082176 main.py:36] ------------ Running the initial call
I0226 19:30:20.980  45696/140704384082176 main.py:38] ------------ Initial call: message: "Hello, init!"




I0226 19:30:20.980  45696/140704384082176 main.py:48] ------------ Initialized the function
D0226 19:30:21.533  45696/123145336483840 selector_events.py:64] Using selector: KqueueSelector


I0226 19:30:23.068  45702/123145353273344 main.py:68] ------------ Invoking hello()
I0226 19:30:23.071  45702/123145353273344 main.py:70] ------------ Response: OK, message: "Hello, you!"



I0226 19:30:24.020  45702/123145353273344 main.py:68] ------------ Invoking hello()
I0226 19:30:24.021  45702/123145353273344 main.py:70] ------------ Response: OK, message: "Hello, you!"
```

## grpcio==1.78.1 fork ON, initial call

**Result: ValueError('Cannot invoke RPC on closed channel!')**


```log
$ TEST_INITIAL_CALL=1 GRPC_ENABLE_FORK_SUPPORT=1 GRPC_TRACE=api ff --target=hello
I0226 19:29:56.799  45554/140704384082176 main.py:22] ------------ Start: grpc 1.78.1
I0226 19:29:56.809  45554/140704384082176 main.py:27] ------------ Created the channel



I0226 19:29:57.312  45554/140704384082176 main.py:36] ------------ Running the initial call
I0226 19:29:57.321  45554/140704384082176 main.py:38] ------------ Initial call: message: "Hello, init!"




I0226 19:29:57.321  45554/140704384082176 main.py:48] ------------ Initialized the function
D0226 19:29:57.878  45554/123145580445696 selector_events.py:64] Using selector: KqueueSelector


I0226 19:30:00.779  45555/123145597235200 main.py:68] ------------ Invoking hello()
I0226 19:30:00.781  45555/123145597235200 main.py:70] ------------ Response: Other error: ValueError('Cannot invoke RPC on closed channel!')



I0226 19:30:01.931  45555/123145597235200 main.py:68] ------------ Invoking hello()
I0226 19:30:01.931  45555/123145597235200 main.py:70] ------------ Response: Other error: ValueError('Cannot invoke RPC on closed channel!')
```

## grpcio==1.78.1 fork UNSET, initial call

**Result: WAI**

```log
$ TEST_INITIAL_CALL=1 GRPC_TRACE=api ff --target=hello
I0226 19:27:41.289  44791/140704384082176 main.py:22] ------------ Start: grpc 1.78.1
I0226 19:27:41.294  44791/140704384082176 main.py:27] ------------ Created the channel



I0226 19:27:41.796  44791/140704384082176 main.py:36] ------------ Running the initial call
I0226 19:27:41.799  44791/140704384082176 main.py:38] ------------ Initial call: message: "Hello, init!"




I0226 19:27:41.799  44791/140704384082176 main.py:48] ------------ Initialized the function
D0226 19:27:42.357  44791/123145501081600 selector_events.py:64] Using selector: KqueueSelector


I0226 19:27:43.198  44792/123145517871104 main.py:68] ------------ Invoking hello()
I0226 19:27:43.201  44792/123145517871104 main.py:70] ------------ Response: OK, message: "Hello, you!"



I0226 19:27:50.995  44792/123145517871104 main.py:68] ------------ Invoking hello()
I0226 19:27:50.996  44792/123145517871104 main.py:70] ------------ Response: OK, message: "Hello, you!"
```

## grpcio==1.78.1 fork OFF

**Result: Hang**


```log
$ GRPC_ENABLE_FORK_SUPPORT=0 GRPC_TRACE=api ff --target=hello
I0226 19:32:48.210  46121/140704384082176 main.py:22] ------------ Start: grpc 1.78.1
I0226 19:32:48.215  46121/140704384082176 main.py:27] ------------ Created the channel



I0226 19:32:48.215  46121/140704384082176 main.py:48] ------------ Initialized the function
D0226 19:32:48.774  46121/123145519718400 selector_events.py:64] Using selector: KqueueSelector


I0226 19:32:52.417  46123/123145536507904 main.py:68] ------------ Invoking hello()

> HANG
```


## grpcio==1.78.1 fork ON

**Result: ValueError('Cannot invoke RPC on closed channel!')**

```log
$ GRPC_ENABLE_FORK_SUPPORT=1 GRPC_TRACE=api ff --target=hello
I0226 19:33:33.627  46287/140704384082176 main.py:22] ------------ Start: grpc 1.78.1
I0226 19:33:33.633  46287/140704384082176 main.py:27] ------------ Created the channel



I0226 19:33:33.633  46287/140704384082176 main.py:48] ------------ Initialized the function
D0226 19:33:34.182  46287/123145562185728 selector_events.py:64] Using selector: KqueueSelector


I0226 19:33:36.184  46288/123145578975232 main.py:68] ------------ Invoking hello()
I0226 19:33:36.185  46288/123145578975232 main.py:70] ------------ Response: Other error: ValueError('Cannot invoke RPC on closed channel!')



I0226 19:33:38.771  46288/123145578975232 main.py:68] ------------ Invoking hello()
I0226 19:33:38.771  46288/123145578975232 main.py:70] ------------ Response: Other error: ValueError('Cannot invoke RPC on closed channel!')
```

## grpcio==1.78.1 fork UNSET

**Result: Hang**

```log
$ GRPC_TRACE=api ff --target=hello
I0226 19:34:21.595  46519/140704384082176 main.py:22] ------------ Start: grpc 1.78.1
I0226 19:34:21.599  46519/140704384082176 main.py:27] ------------ Created the channel



I0226 19:34:21.599  46519/140704384082176 main.py:48] ------------ Initialized the function
D0226 19:34:22.153  46519/123145402392576 selector_events.py:64] Using selector: KqueueSelector




I0226 19:34:31.784  46524/123145419182080 main.py:68] ------------ Invoking hello()
> HANG
```
