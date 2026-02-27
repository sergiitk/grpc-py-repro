# figuring things out 1.78.0

* [\[Python\] grpcio==1.78.1 in python fails with certain googleapis like secrets manager, pubsub, bigquery, workflows (through its sdk) from Cloud Run Functions · Issue #41725 · grpc/grpc](https://github.com/grpc/grpc/issues/41725)
* https://github.com/googlecloudplatform/functions-framework-python
* [Support gRPC Python client-side fork with epoll1 by ericgribkoff · Pull Request #16264 · grpc/grpc](https://github.com/grpc/grpc/pull/16264)

### debugging
* https://github.com/grpc/grpc/blob/master/doc/trace_flags.md

## grpcio==1.78.0 fork OFF, initial call

**Result: WAI**

```log
$ TEST_INITIAL_CALL=1 GRPC_ENABLE_FORK_SUPPORT=0 GRPC_TRACE=api ff --target=hello
I0226 19:39:40.548  47375/140704384082176 main.py:36] ------------ Start: grpc 1.78.0
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1772163580.568798 3534552 trace.cc:91] gRPC Tracers: api
I0000 00:00:1772163580.568977 3534552 init.cc:132] grpc_init(void)
I0000 00:00:1772163580.569021 3534552 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163580.569056 3534552 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163580.569076 3534552 channel_create.cc:249] grpc_channel_create(target=localhost:50051, creds=0x6000003781a0, args=0x1115cf770)
I0000 00:00:1772163580.570194 3534552 init.cc:132] grpc_init(void)
I0000 00:00:1772163580.570215 3534552 transport_credentials.cc:33] grpc_channel_credentials_release(creds=0x6000003781a0)
I0000 00:00:1772163580.570303 3534552 channel.cc:120] grpc_channel_register_call(channel=0x60000337c090, method=/helloworld.Greeter/SayHello, host=(null), reserved=0x0)
I0000 00:00:1772163580.570354 3534552 channel.cc:120] grpc_channel_register_call(channel=0x60000337c090, method=/helloworld.Greeter/SayHelloStreamReply, host=(null), reserved=0x0)
I0000 00:00:1772163580.570377 3534552 channel.cc:120] grpc_channel_register_call(channel=0x60000337c090, method=/helloworld.Greeter/SayHelloBidiStream, host=(null), reserved=0x0)
I0226 19:39:40.570  47375/140704384082176 main.py:41] ------------ Created the channel



I0226 19:39:41.071  47375/140704384082176 main.py:50] ------------ Running the initial call
I0000 00:00:1772163581.072003 3534552 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163581.072045 3534552 channel.cc:134] grpc_channel_create_registered_call(channel=0x60000337c090, parent_call=0x0, propagation_mask=65535, completion_queue=0x7f884cbb5550, registered_call_handle=0x6000030744b0, deadline=gpr_timespec { tv_sec: 1772163586, tv_nsec: 71920128, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163581.072163 3534552 metadata_array.cc:27] grpc_metadata_array_init(array=0x11159d738)
I0000 00:00:1772163581.072177 3534552 metadata_array.cc:27] grpc_metadata_array_init(array=0x11146e090)
I0000 00:00:1772163581.072184 3534552 call.cc:501] grpc_call_start_batch(call=0x7f884e0d0420, ops=0x7f884cbaa250, nops=6, tag=0x1115cfba0, reserved=0x0)
I0000 00:00:1772163581.072306 3534552 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772163581.072341 3534552 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x60000307c320
I0000 00:00:1772163581.072357 3534552 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772163581.072363 3534552 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x11159d738
I0000 00:00:1772163581.072368 3534552 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x1114c2ea0
I0000 00:00:1772163581.072374 3534552 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x11146e090 status=0x11146e0a8 details=0x11146e0b0
I0000 00:00:1772163581.072472 3534552 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f884cbb5550, deadline=gpr_timespec { tv_sec: 1772163581, tv_nsec: 272468000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163581.074553 3534729 init.cc:132] grpc_init(void)
I0000 00:00:1772163581.074649 3534729 init.cc:132] grpc_init(void)
I0000 00:00:1772163581.075191 3534729 auth_context.cc:181] grpc_auth_context_add_cstring_property(ctx=0x6000025704e0, name=transport_security_type, value=insecure)
I0000 00:00:1772163581.075219 3534729 auth_context.cc:161] grpc_auth_context_add_property(ctx=0x6000025704e0, name=security_level, value=TSI_SECURITY_NONE, value_length=17)
I0000 00:00:1772163581.075232 3534729 auth_context.cc:115] grpc_auth_context_find_properties_by_name(ctx=0x6000025704e0, name=security_level)
I0000 00:00:1772163581.075243 3534729 auth_context.cc:88] grpc_auth_property_iterator_next(it=0x70000ad04a60)
I0000 00:00:1772163581.075266 3534729 init.cc:132] grpc_init(void)
I0000 00:00:1772163581.075949 3534732 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772163581.076893 3534552 completion_queue.cc:762] cq_end_op_for_next(cq=0x7f884cbb5550, tag=0x1115cfba0, error=OK, done=true, done_arg=0x600003d60020, storage=0x600003d60068)
I0000 00:00:1772163581.076966 3534552 completion_queue.cc:1101] RETURN_EVENT[0x7f884cbb5550]: OP_COMPLETE: tag:0x1115cfba0 OK
I0000 00:00:1772163581.077002 3534552 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x11159d738)
I0000 00:00:1772163581.077019 3534552 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x11146e090)
I0000 00:00:1772163581.077049 3534552 filter_stack_call.cc:265] grpc_call_unref(c=0x7f884e0d0420)
I0000 00:00:1772163581.077082 3534552 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f884cbb5550)
I0000 00:00:1772163581.077093 3534552 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7f884cbb5550)
I0000 00:00:1772163581.077098 3534552 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f884cbb5550)
I0226 19:39:41.077  47375/140704384082176 main.py:52] ------------ Initial call: message: "Hello, init!"




I0226 19:39:41.077  47375/140704384082176 main.py:62] ------------ Initialized the function
D0226 19:39:41.628  47375/123145506963456 selector_events.py:64] Using selector: KqueueSelector


I0226 19:39:45.549  47381/123145523752960 main.py:82] ------------ Invoking hello()
I0000 00:00:1772163585.550542 3534853 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163585.550671 3534853 channel.cc:134] grpc_channel_create_registered_call(channel=0x60000337c090, parent_call=0x0, propagation_mask=65535, completion_queue=0x7f884ca410f0, registered_call_handle=0x6000030744b0, deadline=gpr_timespec { tv_sec: 1772163590, tv_nsec: 550135040, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163585.550983 3534853 metadata_array.cc:27] grpc_metadata_array_init(array=0x111612b38)
I0000 00:00:1772163585.550996 3534853 metadata_array.cc:27] grpc_metadata_array_init(array=0x111577080)
I0000 00:00:1772163585.551002 3534853 call.cc:501] grpc_call_start_batch(call=0x7f884d8532d0, ops=0x7f884ca34380, nops=6, tag=0x111624310, reserved=0x0)
I0000 00:00:1772163585.551014 3534853 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772163585.551026 3534853 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x7f884ca11970
I0000 00:00:1772163585.551034 3534853 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772163585.551037 3534853 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x111612b38
I0000 00:00:1772163585.551041 3534853 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x1114d69a0
I0000 00:00:1772163585.551045 3534853 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x111577080 status=0x111577098 details=0x1115770a0
I0000 00:00:1772163585.551544 3534853 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f884ca410f0, deadline=gpr_timespec { tv_sec: 1772163585, tv_nsec: 751541000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163585.552115 3534853 completion_queue.cc:762] cq_end_op_for_next(cq=0x7f884ca410f0, tag=0x111624310, error=OK, done=true, done_arg=0x7f884d8542a0, storage=0x7f884d8542e8)
I0000 00:00:1772163585.552147 3534853 completion_queue.cc:1101] RETURN_EVENT[0x7f884ca410f0]: OP_COMPLETE: tag:0x111624310 OK
I0000 00:00:1772163585.552204 3534853 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x111612b38)
I0000 00:00:1772163585.552215 3534853 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x111577080)
I0000 00:00:1772163585.552234 3534853 filter_stack_call.cc:265] grpc_call_unref(c=0x7f884d8532d0)
I0000 00:00:1772163585.552262 3534853 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f884ca410f0)
I0000 00:00:1772163585.552268 3534853 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7f884ca410f0)
I0000 00:00:1772163585.552271 3534853 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f884ca410f0)
I0226 19:39:45.552  47381/123145523752960 main.py:84] ------------ Response: OK, message: "Hello, you!"



I0226 19:39:49.770  47381/123145523752960 main.py:82] ------------ Invoking hello()
I0000 00:00:1772163589.770730 3534853 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163589.770772 3534853 channel.cc:134] grpc_channel_create_registered_call(channel=0x60000337c090, parent_call=0x0, propagation_mask=65535, completion_queue=0x7f884c968180, registered_call_handle=0x6000030744b0, deadline=gpr_timespec { tv_sec: 1772163594, tv_nsec: 770685952, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163589.770836 3534853 metadata_array.cc:27] grpc_metadata_array_init(array=0x111612c78)
I0000 00:00:1772163589.770845 3534853 metadata_array.cc:27] grpc_metadata_array_init(array=0x111577170)
I0000 00:00:1772163589.770849 3534853 call.cc:501] grpc_call_start_batch(call=0x7f884d04aed0, ops=0x7f884c96d240, nops=6, tag=0x111625620, reserved=0x0)
I0000 00:00:1772163589.770855 3534853 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772163589.770864 3534853 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x7f884c9388d0
I0000 00:00:1772163589.770869 3534853 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772163589.770873 3534853 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x111612c78
I0000 00:00:1772163589.770876 3534853 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x1114d6b20
I0000 00:00:1772163589.770880 3534853 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x111577170 status=0x111577188 details=0x111577190
I0000 00:00:1772163589.770997 3534853 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f884c968180, deadline=gpr_timespec { tv_sec: 1772163589, tv_nsec: 970997000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163589.771499 3534853 completion_queue.cc:762] cq_end_op_for_next(cq=0x7f884c968180, tag=0x111625620, error=OK, done=true, done_arg=0x7f884d04bea0, storage=0x7f884d04bee8)
I0000 00:00:1772163589.771517 3534853 completion_queue.cc:1101] RETURN_EVENT[0x7f884c968180]: OP_COMPLETE: tag:0x111625620 OK
I0000 00:00:1772163589.771529 3534853 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x111612c78)
I0000 00:00:1772163589.771537 3534853 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x111577170)
I0000 00:00:1772163589.771546 3534853 filter_stack_call.cc:265] grpc_call_unref(c=0x7f884d04aed0)
I0000 00:00:1772163589.771560 3534853 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f884c968180)
I0000 00:00:1772163589.771565 3534853 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7f884c968180)
I0000 00:00:1772163589.771568 3534853 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f884c968180)
I0226 19:39:49.771  47381/123145523752960 main.py:84] ------------ Response: OK, message: "Hello, you!"
```

## grpcio==1.78.0 fork ON, initial call

**Result: ValueError('Cannot invoke RPC on closed channel!')**

```log
$ TEST_INITIAL_CALL=1 GRPC_ENABLE_FORK_SUPPORT=1 GRPC_TRACE=api ff --target=hello
I0226 19:41:03.693  47630/140704384082176 main.py:36] ------------ Start: grpc 1.78.0
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1772163663.697520 3537778 trace.cc:91] gRPC Tracers: api
I0000 00:00:1772163663.697641 3537778 init.cc:132] grpc_init(void)
I0000 00:00:1772163663.697680 3537778 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163663.697703 3537778 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163663.697716 3537778 channel_create.cc:249] grpc_channel_create(target=localhost:50051, creds=0x6000020940e0, args=0x1065aa6e0)
I0000 00:00:1772163663.698413 3537778 init.cc:132] grpc_init(void)
I0000 00:00:1772163663.698430 3537778 transport_credentials.cc:33] grpc_channel_credentials_release(creds=0x6000020940e0)
I0000 00:00:1772163663.698475 3537778 channel.cc:120] grpc_channel_register_call(channel=0x600001094000, method=/helloworld.Greeter/SayHello, host=(null), reserved=0x0)
I0000 00:00:1772163663.698514 3537778 channel.cc:120] grpc_channel_register_call(channel=0x600001094000, method=/helloworld.Greeter/SayHelloStreamReply, host=(null), reserved=0x0)
I0000 00:00:1772163663.698536 3537778 channel.cc:120] grpc_channel_register_call(channel=0x600001094000, method=/helloworld.Greeter/SayHelloBidiStream, host=(null), reserved=0x0)
I0226 19:41:03.698  47630/140704384082176 main.py:41] ------------ Created the channel



I0226 19:41:04.199  47630/140704384082176 main.py:50] ------------ Running the initial call
I0000 00:00:1772163664.199582 3537778 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163664.199643 3537778 channel.cc:134] grpc_channel_create_registered_call(channel=0x600001094000, parent_call=0x0, propagation_mask=65535, completion_queue=0x7fdbd7e21840, registered_call_handle=0x60000138c5f0, deadline=gpr_timespec { tv_sec: 1772163669, tv_nsec: 199441920, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163664.199799 3537778 metadata_array.cc:27] grpc_metadata_array_init(array=0x1065c0dd8)
I0000 00:00:1772163664.199815 3537778 metadata_array.cc:27] grpc_metadata_array_init(array=0x106542180)
I0000 00:00:1772163664.199821 3537778 call.cc:501] grpc_call_start_batch(call=0x7fdbd50ac620, ops=0x7fdbd4209f70, nops=6, tag=0x1065aab10, reserved=0x0)
I0000 00:00:1772163664.199834 3537778 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772163664.199844 3537778 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x600001388320
I0000 00:00:1772163664.199859 3537778 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772163664.199866 3537778 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x1065c0dd8
I0000 00:00:1772163664.199873 3537778 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x1065ac9a0
I0000 00:00:1772163664.199879 3537778 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x106542180 status=0x106542198 details=0x1065421a0
I0000 00:00:1772163664.200011 3537778 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fdbd7e21840, deadline=gpr_timespec { tv_sec: 1772163664, tv_nsec: 400006000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163664.201602 3537819 init.cc:132] grpc_init(void)
I0000 00:00:1772163664.201666 3537819 init.cc:132] grpc_init(void)
I0000 00:00:1772163664.202096 3537824 auth_context.cc:181] grpc_auth_context_add_cstring_property(ctx=0x600000698300, name=transport_security_type, value=insecure)
I0000 00:00:1772163664.202125 3537824 auth_context.cc:161] grpc_auth_context_add_property(ctx=0x600000698300, name=security_level, value=TSI_SECURITY_NONE, value_length=17)
I0000 00:00:1772163664.202136 3537824 auth_context.cc:115] grpc_auth_context_find_properties_by_name(ctx=0x600000698300, name=security_level)
I0000 00:00:1772163664.202144 3537824 auth_context.cc:88] grpc_auth_property_iterator_next(it=0x700010067a60)
I0000 00:00:1772163664.202178 3537824 init.cc:132] grpc_init(void)
I0000 00:00:1772163664.202464 3537827 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772163664.203212 3537778 completion_queue.cc:762] cq_end_op_for_next(cq=0x7fdbd7e21840, tag=0x1065aab10, error=OK, done=true, done_arg=0x600001e94020, storage=0x600001e94068)
I0000 00:00:1772163664.203274 3537778 completion_queue.cc:1101] RETURN_EVENT[0x7fdbd7e21840]: OP_COMPLETE: tag:0x1065aab10 OK
I0000 00:00:1772163664.203304 3537778 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x1065c0dd8)
I0000 00:00:1772163664.203316 3537778 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x106542180)
I0000 00:00:1772163664.203342 3537778 filter_stack_call.cc:265] grpc_call_unref(c=0x7fdbd50ac620)
I0000 00:00:1772163664.203367 3537778 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fdbd7e21840)
I0000 00:00:1772163664.203377 3537778 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fdbd7e21840)
I0000 00:00:1772163664.203381 3537778 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fdbd7e21840)
I0226 19:41:04.203  47630/140704384082176 main.py:52] ------------ Initial call: message: "Hello, init!"




I0226 19:41:04.203  47630/140704384082176 main.py:62] ------------ Initialized the function
D0226 19:41:04.756  47630/123145591717888 selector_events.py:64] Using selector: KqueueSelector
I0000 00:00:1772163665.182152 3537778 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fdbd4177410)
I0000 00:00:1772163665.182278 3537778 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fdbd4177410)
I0000 00:00:1772163665.182287 3537778 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fdbd4177410)
I0000 00:00:1772163665.182296 3537778 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fdbd7d2cd00)
I0000 00:00:1772163665.182308 3537778 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fdbd7d2cd00)
I0000 00:00:1772163665.182314 3537778 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fdbd7d2cd00)
I0000 00:00:1772163665.182324 3537778 channel.cc:95] grpc_channel_destroy(channel=0x600001094000)
I0000 00:00:1772163665.182549 3537778 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772163665.182917 3537879 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772163665.183145 3537879 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772163665.183304 3537879 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772163665.183366 3537889 init.cc:154] grpc_shutdown_from_cleanup_thread


I0226 19:41:08.529  47634/123145608507392 main.py:82] ------------ Invoking hello()
I0226 19:41:08.530  47634/123145608507392 main.py:84] ------------ Response: Other error: ValueError('Cannot invoke RPC on closed channel!')



I0226 19:41:10.727  47634/123145608507392 main.py:82] ------------ Invoking hello()
I0226 19:41:10.728  47634/123145608507392 main.py:84] ------------ Response: Other error: ValueError('Cannot invoke RPC on closed channel!')
```

## grpcio==1.78.0 fork UNSET, initial call

**Result: Almost WAI**

The first RPC issued in a forked proccess returns UNAVAILABLE, the following OK. 

```log
$ TEST_INITIAL_CALL=1 GRPC_TRACE=api ff --target=hello
I0226 19:41:47.042  47805/140704384082176 main.py:36] ------------ Start: grpc 1.78.0
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1772163707.046097 3539163 trace.cc:91] gRPC Tracers: api
I0000 00:00:1772163707.046219 3539163 init.cc:132] grpc_init(void)
I0000 00:00:1772163707.046243 3539163 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163707.046265 3539163 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163707.046278 3539163 channel_create.cc:249] grpc_channel_create(target=localhost:50051, creds=0x600003fc8090, args=0x110b66730)
I0000 00:00:1772163707.046979 3539163 init.cc:132] grpc_init(void)
I0000 00:00:1772163707.046997 3539163 transport_credentials.cc:33] grpc_channel_credentials_release(creds=0x600003fc8090)
I0000 00:00:1772163707.047037 3539163 channel.cc:120] grpc_channel_register_call(channel=0x600000fd8090, method=/helloworld.Greeter/SayHello, host=(null), reserved=0x0)
I0000 00:00:1772163707.047072 3539163 channel.cc:120] grpc_channel_register_call(channel=0x600000fd8090, method=/helloworld.Greeter/SayHelloStreamReply, host=(null), reserved=0x0)
I0000 00:00:1772163707.047092 3539163 channel.cc:120] grpc_channel_register_call(channel=0x600000fd8090, method=/helloworld.Greeter/SayHelloBidiStream, host=(null), reserved=0x0)
I0226 19:41:47.047  47805/140704384082176 main.py:41] ------------ Created the channel



I0226 19:41:47.550  47805/140704384082176 main.py:50] ------------ Running the initial call
I0000 00:00:1772163707.550461 3539163 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163707.550492 3539163 channel.cc:134] grpc_channel_create_registered_call(channel=0x600000fd8090, parent_call=0x0, propagation_mask=65535, completion_queue=0x7f897721d380, registered_call_handle=0x600000cc87d0, deadline=gpr_timespec { tv_sec: 1772163712, tv_nsec: 550384128, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163707.550577 3539163 metadata_array.cc:27] grpc_metadata_array_init(array=0x110b7cdd8)
I0000 00:00:1772163707.550584 3539163 metadata_array.cc:27] grpc_metadata_array_init(array=0x110afe180)
I0000 00:00:1772163707.550587 3539163 call.cc:501] grpc_call_start_batch(call=0x7f89748b1020, ops=0x7f897721ca10, nops=6, tag=0x110b66b60, reserved=0x0)
I0000 00:00:1772163707.550595 3539163 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772163707.550600 3539163 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x600000cd4320
I0000 00:00:1772163707.550608 3539163 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772163707.550610 3539163 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x110b7cdd8
I0000 00:00:1772163707.550614 3539163 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x110b689a0
I0000 00:00:1772163707.550617 3539163 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x110afe180 status=0x110afe198 details=0x110afe1a0
I0000 00:00:1772163707.550753 3539163 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f897721d380, deadline=gpr_timespec { tv_sec: 1772163707, tv_nsec: 750751000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163707.551817 3539168 init.cc:132] grpc_init(void)
I0000 00:00:1772163707.551867 3539168 init.cc:132] grpc_init(void)
I0000 00:00:1772163707.552203 3539167 auth_context.cc:181] grpc_auth_context_add_cstring_property(ctx=0x6000019d8660, name=transport_security_type, value=insecure)
I0000 00:00:1772163707.552227 3539167 auth_context.cc:161] grpc_auth_context_add_property(ctx=0x6000019d8660, name=security_level, value=TSI_SECURITY_NONE, value_length=17)
I0000 00:00:1772163707.552236 3539167 auth_context.cc:115] grpc_auth_context_find_properties_by_name(ctx=0x6000019d8660, name=security_level)
I0000 00:00:1772163707.552242 3539167 auth_context.cc:88] grpc_auth_property_iterator_next(it=0x70000c54ba60)
I0000 00:00:1772163707.552263 3539167 init.cc:132] grpc_init(void)
I0000 00:00:1772163707.552524 3539174 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772163707.553148 3539163 completion_queue.cc:762] cq_end_op_for_next(cq=0x7f897721d380, tag=0x110b66b60, error=OK, done=true, done_arg=0x6000001d0020, storage=0x6000001d0068)
I0000 00:00:1772163707.553191 3539163 completion_queue.cc:1101] RETURN_EVENT[0x7f897721d380]: OP_COMPLETE: tag:0x110b66b60 OK
I0000 00:00:1772163707.553213 3539163 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x110b7cdd8)
I0000 00:00:1772163707.553222 3539163 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x110afe180)
I0000 00:00:1772163707.553242 3539163 filter_stack_call.cc:265] grpc_call_unref(c=0x7f89748b1020)
I0000 00:00:1772163707.553260 3539163 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f897721d380)
I0000 00:00:1772163707.553265 3539163 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7f897721d380)
I0000 00:00:1772163707.553268 3539163 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f897721d380)
I0226 19:41:47.553  47805/140704384082176 main.py:52] ------------ Initial call: message: "Hello, init!"




I0226 19:41:47.553  47805/140704384082176 main.py:62] ------------ Initialized the function
D0226 19:41:48.088  47805/123145532420096 selector_events.py:64] Using selector: KqueueSelector


I0226 19:41:50.661  47808/123145549209600 main.py:82] ------------ Invoking hello()
I0000 00:00:1772163710.662307 3539275 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163710.662402 3539275 channel.cc:134] grpc_channel_create_registered_call(channel=0x600000fd8090, parent_call=0x0, propagation_mask=65535, completion_queue=0x7f8972f78a70, registered_call_handle=0x600000cc87d0, deadline=gpr_timespec { tv_sec: 1772163715, tv_nsec: 661959936, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163710.662666 3539275 metadata_array.cc:27] grpc_metadata_array_init(array=0x110cba458)
I0000 00:00:1772163710.662679 3539275 metadata_array.cc:27] grpc_metadata_array_init(array=0x110bdedb0)
I0000 00:00:1772163710.662685 3539275 call.cc:501] grpc_call_start_batch(call=0x7f89730834d0, ops=0x7f8977506590, nops=6, tag=0x110cb3790, reserved=0x0)
I0000 00:00:1772163710.662698 3539275 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772163710.662709 3539275 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x7f8972fde290
I0000 00:00:1772163710.662718 3539275 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772163710.662721 3539275 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x110cba458
I0000 00:00:1772163710.662725 3539275 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x110c85720
I0000 00:00:1772163710.662729 3539275 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x110bdedb0 status=0x110bdedc8 details=0x110bdedd0
I0000 00:00:1772163710.663387 3539275 completion_queue.cc:762] cq_end_op_for_next(cq=0x7f8972f78a70, tag=0x110cb3790, error=OK, done=true, done_arg=0x7f89730844a0, storage=0x7f89730844e8)
I0000 00:00:1772163710.663522 3539275 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f8972f78a70, deadline=gpr_timespec { tv_sec: 1772163710, tv_nsec: 863518000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163710.663538 3539228 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772163710.663543 3539275 completion_queue.cc:1101] RETURN_EVENT[0x7f8972f78a70]: OP_COMPLETE: tag:0x110cb3790 OK
I0000 00:00:1772163710.663619 3539275 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x110cba458)
I0000 00:00:1772163710.663637 3539275 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x110bdedb0)
I0000 00:00:1772163710.663664 3539275 filter_stack_call.cc:265] grpc_call_unref(c=0x7f89730834d0)
I0000 00:00:1772163710.663813 3539275 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772163710.663823 3539275 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f8972f78a70)
I0000 00:00:1772163710.663831 3539275 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7f8972f78a70)
I0000 00:00:1772163710.663834 3539275 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f8972f78a70)
I0226 19:41:50.664  47808/123145549209600 main.py:84] ------------ Response: gRPC error: UNAVAILABLE



I0226 19:41:53.710  47808/123145549209600 main.py:82] ------------ Invoking hello()
I0000 00:00:1772163713.711180 3539275 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163713.711213 3539275 channel.cc:134] grpc_channel_create_registered_call(channel=0x600000fd8090, parent_call=0x0, propagation_mask=65535, completion_queue=0x7f8973e9abe0, registered_call_handle=0x600000cc87d0, deadline=gpr_timespec { tv_sec: 1772163718, tv_nsec: 711129088, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163713.711281 3539275 metadata_array.cc:27] grpc_metadata_array_init(array=0x110cba458)
I0000 00:00:1772163713.711290 3539275 metadata_array.cc:27] grpc_metadata_array_init(array=0x110bdef90)
I0000 00:00:1772163713.711294 3539275 call.cc:501] grpc_call_start_batch(call=0x7f89768846d0, ops=0x7f8973e9add0, nops=6, tag=0x110cc8bd0, reserved=0x0)
I0000 00:00:1772163713.711300 3539275 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772163713.711306 3539275 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x7f8973e0b740
I0000 00:00:1772163713.711311 3539275 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772163713.711314 3539275 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x110cba458
I0000 00:00:1772163713.711318 3539275 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x110c85920
I0000 00:00:1772163713.711322 3539275 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x110bdef90 status=0x110bdefa8 details=0x110bdefb0
I0000 00:00:1772163713.711438 3539275 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f8973e9abe0, deadline=gpr_timespec { tv_sec: 1772163713, tv_nsec: 911438000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163713.711504 3539222 init.cc:132] grpc_init(void)
I0000 00:00:1772163713.711593 3539222 init.cc:132] grpc_init(void)
I0000 00:00:1772163713.711965 3539228 auth_context.cc:181] grpc_auth_context_add_cstring_property(ctx=0x7f8973f180c0, name=transport_security_type, value=insecure)
I0000 00:00:1772163713.712015 3539228 auth_context.cc:161] grpc_auth_context_add_property(ctx=0x7f8973f180c0, name=security_level, value=TSI_SECURITY_NONE, value_length=17)
I0000 00:00:1772163713.712027 3539228 auth_context.cc:115] grpc_auth_context_find_properties_by_name(ctx=0x7f8973f180c0, name=security_level)
I0000 00:00:1772163713.712034 3539228 auth_context.cc:88] grpc_auth_property_iterator_next(it=0x70000c85da60)
I0000 00:00:1772163713.712083 3539228 init.cc:132] grpc_init(void)
I0000 00:00:1772163713.712373 3539231 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772163713.712979 3539275 completion_queue.cc:762] cq_end_op_for_next(cq=0x7f8973e9abe0, tag=0x110cc8bd0, error=OK, done=true, done_arg=0x7f89768856a0, storage=0x7f89768856e8)
I0000 00:00:1772163713.713027 3539275 completion_queue.cc:1101] RETURN_EVENT[0x7f8973e9abe0]: OP_COMPLETE: tag:0x110cc8bd0 OK
I0000 00:00:1772163713.713044 3539275 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x110cba458)
I0000 00:00:1772163713.713052 3539275 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x110bdef90)
I0000 00:00:1772163713.713063 3539275 filter_stack_call.cc:265] grpc_call_unref(c=0x7f89768846d0)
I0000 00:00:1772163713.713078 3539275 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f8973e9abe0)
I0000 00:00:1772163713.713083 3539275 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7f8973e9abe0)
I0000 00:00:1772163713.713087 3539275 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f8973e9abe0)
I0226 19:41:53.713  47808/123145549209600 main.py:84] ------------ Response: OK, message: "Hello, you!"



I0226 19:41:55.503  47808/123145549209600 main.py:82] ------------ Invoking hello()
I0000 00:00:1772163715.504589 3539275 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163715.504632 3539275 channel.cc:134] grpc_channel_create_registered_call(channel=0x600000fd8090, parent_call=0x0, propagation_mask=65535, completion_queue=0x7f8973e9ba70, registered_call_handle=0x600000cc87d0, deadline=gpr_timespec { tv_sec: 1772163720, tv_nsec: 504547072, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163715.504717 3539275 metadata_array.cc:27] grpc_metadata_array_init(array=0x110cba598)
I0000 00:00:1772163715.504728 3539275 metadata_array.cc:27] grpc_metadata_array_init(array=0x110bdf350)
I0000 00:00:1772163715.504735 3539275 call.cc:501] grpc_call_start_batch(call=0x7f897687ced0, ops=0x7f8973e9abe0, nops=6, tag=0x110cc8c70, reserved=0x0)
I0000 00:00:1772163715.504742 3539275 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772163715.504750 3539275 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x7f8973e7ae70
I0000 00:00:1772163715.504755 3539275 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772163715.504758 3539275 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x110cba598
I0000 00:00:1772163715.504762 3539275 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x110c85aa0
I0000 00:00:1772163715.504766 3539275 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x110bdf350 status=0x110bdf368 details=0x110bdf370
I0000 00:00:1772163715.504934 3539275 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f8973e9ba70, deadline=gpr_timespec { tv_sec: 1772163715, tv_nsec: 704933000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163715.505476 3539275 completion_queue.cc:762] cq_end_op_for_next(cq=0x7f8973e9ba70, tag=0x110cc8c70, error=OK, done=true, done_arg=0x7f897687dea0, storage=0x7f897687dee8)
I0000 00:00:1772163715.505495 3539275 completion_queue.cc:1101] RETURN_EVENT[0x7f8973e9ba70]: OP_COMPLETE: tag:0x110cc8c70 OK
I0000 00:00:1772163715.505508 3539275 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x110cba598)
I0000 00:00:1772163715.505517 3539275 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x110bdf350)
I0000 00:00:1772163715.505527 3539275 filter_stack_call.cc:265] grpc_call_unref(c=0x7f897687ced0)
I0000 00:00:1772163715.505542 3539275 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f8973e9ba70)
I0000 00:00:1772163715.505547 3539275 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7f8973e9ba70)
I0000 00:00:1772163715.505550 3539275 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f8973e9ba70)
I0226 19:41:55.505  47808/123145549209600 main.py:84] ------------ Response: OK, message: "Hello, you!"
```

## grpcio==1.78.0 fork OFF

**Result: Hang**


```log
$ GRPC_ENABLE_FORK_SUPPORT=0 GRPC_TRACE=api ff --target=hello
I0226 19:43:12.306  48087/140704384082176 main.py:36] ------------ Start: grpc 1.78.0
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1772163792.310573 3540995 trace.cc:91] gRPC Tracers: api
I0000 00:00:1772163792.310681 3540995 init.cc:132] grpc_init(void)
I0000 00:00:1772163792.310732 3540995 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163792.310754 3540995 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163792.310766 3540995 channel_create.cc:249] grpc_channel_create(target=localhost:50051, creds=0x6000019151b0, args=0x1089326e0)
I0000 00:00:1772163792.311440 3540995 init.cc:132] grpc_init(void)
I0000 00:00:1772163792.311452 3540995 transport_credentials.cc:33] grpc_channel_credentials_release(creds=0x6000019151b0)
I0000 00:00:1772163792.311489 3540995 channel.cc:120] grpc_channel_register_call(channel=0x600002908000, method=/helloworld.Greeter/SayHello, host=(null), reserved=0x0)
I0000 00:00:1772163792.311522 3540995 channel.cc:120] grpc_channel_register_call(channel=0x600002908000, method=/helloworld.Greeter/SayHelloStreamReply, host=(null), reserved=0x0)
I0000 00:00:1772163792.311540 3540995 channel.cc:120] grpc_channel_register_call(channel=0x600002908000, method=/helloworld.Greeter/SayHelloBidiStream, host=(null), reserved=0x0)
I0226 19:43:12.311  48087/140704384082176 main.py:41] ------------ Created the channel



I0226 19:43:12.311  48087/140704384082176 main.py:62] ------------ Initialized the function
D0226 19:43:12.857  48087/123145553633280 selector_events.py:64] Using selector: KqueueSelector


I0226 19:43:15.869  48088/123145570422784 main.py:82] ------------ Invoking hello()
I0000 00:00:1772163795.870660 3541064 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163795.870800 3541064 channel.cc:134] grpc_channel_create_registered_call(channel=0x600002908000, parent_call=0x0, propagation_mask=65535, completion_queue=0x7fc293d36de0, registered_call_handle=0x600002a1c550, deadline=gpr_timespec { tv_sec: 1772163800, tv_nsec: 870137088, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163795.871138 3541064 metadata_array.cc:27] grpc_metadata_array_init(array=0x108a86458)
I0000 00:00:1772163795.871151 3541064 metadata_array.cc:27] grpc_metadata_array_init(array=0x1089aedb0)
I0000 00:00:1772163795.871157 3541064 call.cc:501] grpc_call_start_batch(call=0x7fc295822420, ops=0x7fc293d36fd0, nops=6, tag=0x108a7f740, reserved=0x0)
I0000 00:00:1772163795.871170 3541064 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772163795.871182 3541064 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x7fc293d371b0
I0000 00:00:1772163795.871190 3541064 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772163795.871194 3541064 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x108a86458
I0000 00:00:1772163795.871197 3541064 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x108a51720
I0000 00:00:1772163795.871201 3541064 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x1089aedb0 status=0x1089aedc8 details=0x1089aedd0
I0000 00:00:1772163795.871385 3541064 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fc293d36de0, deadline=gpr_timespec { tv_sec: 1772163796, tv_nsec: 71382000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163796.073479 3541064 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fc293d36de0, deadline=gpr_timespec { tv_sec: 1772163796, tv_nsec: 273476000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163796.275611 3541064 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fc293d36de0, deadline=gpr_timespec { tv_sec: 1772163796, tv_nsec: 475610000, clock_type: 1 }, reserved=0x0)
...

> HANG
```


## grpcio==1.78.0 fork ON

**Result: ValueError('Cannot invoke RPC on closed channel!')**

```log
$ GRPC_ENABLE_FORK_SUPPORT=1 GRPC_TRACE=api ff --target=hello
I0226 19:45:07.742  48458/140704384082176 main.py:36] ------------ Start: grpc 1.78.0
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1772163907.747778 3543919 trace.cc:91] gRPC Tracers: api
I0000 00:00:1772163907.748902 3543919 init.cc:132] grpc_init(void)
I0000 00:00:1772163907.748948 3543919 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163907.748971 3543919 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163907.748986 3543919 channel_create.cc:249] grpc_channel_create(target=localhost:50051, creds=0x6000015e00e0, args=0x1039aa780)
I0000 00:00:1772163907.751158 3543919 init.cc:132] grpc_init(void)
I0000 00:00:1772163907.751507 3543919 transport_credentials.cc:33] grpc_channel_credentials_release(creds=0x6000015e00e0)
I0000 00:00:1772163907.751563 3543919 channel.cc:120] grpc_channel_register_call(channel=0x6000025fc120, method=/helloworld.Greeter/SayHello, host=(null), reserved=0x0)
I0000 00:00:1772163907.751601 3543919 channel.cc:120] grpc_channel_register_call(channel=0x6000025fc120, method=/helloworld.Greeter/SayHelloStreamReply, host=(null), reserved=0x0)
I0000 00:00:1772163907.751624 3543919 channel.cc:120] grpc_channel_register_call(channel=0x6000025fc120, method=/helloworld.Greeter/SayHelloBidiStream, host=(null), reserved=0x0)
I0226 19:45:07.751  48458/140704384082176 main.py:41] ------------ Created the channel



I0226 19:45:07.751  48458/140704384082176 main.py:62] ------------ Initialized the function
D0226 19:45:08.311  48458/123145463681024 selector_events.py:64] Using selector: KqueueSelector
I0000 00:00:1772163908.319644 3543919 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fc8c24c7f60)
I0000 00:00:1772163908.319771 3543919 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fc8c24c7f60)
I0000 00:00:1772163908.319779 3543919 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fc8c24c7f60)
I0000 00:00:1772163908.319785 3543919 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fc8c24bccf0)
I0000 00:00:1772163908.319795 3543919 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fc8c24bccf0)
I0000 00:00:1772163908.319801 3543919 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fc8c24bccf0)
I0000 00:00:1772163908.319811 3543919 channel.cc:95] grpc_channel_destroy(channel=0x6000025fc120)
I0000 00:00:1772163908.319944 3543919 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772163908.320151 3543964 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772163908.320245 3543975 init.cc:154] grpc_shutdown_from_cleanup_thread


I0226 19:45:10.463  48459/123145480470528 main.py:82] ------------ Invoking hello()
I0226 19:45:10.465  48459/123145480470528 main.py:84] ------------ Response: Other error: ValueError('Cannot invoke RPC on closed channel!')



I0226 19:45:12.845  48459/123145480470528 main.py:82] ------------ Invoking hello()
I0226 19:45:12.845  48459/123145480470528 main.py:84] ------------ Response: Other error: ValueError('Cannot invoke RPC on closed channel!')
```

## grpcio==1.78.0 fork UNSET

**Result: WAI**

```log
$ GRPC_TRACE=api ff --target=hello
I0226 19:45:40.942  48629/140704384082176 main.py:36] ------------ Start: grpc 1.78.0
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1772163940.946606 3544765 trace.cc:91] gRPC Tracers: api
I0000 00:00:1772163940.946739 3544765 init.cc:132] grpc_init(void)
I0000 00:00:1772163940.946765 3544765 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163940.946789 3544765 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163940.946802 3544765 channel_create.cc:249] grpc_channel_create(target=localhost:50051, creds=0x600003d70090, args=0x102fd26e0)
I0000 00:00:1772163940.947435 3544765 init.cc:132] grpc_init(void)
I0000 00:00:1772163940.947452 3544765 transport_credentials.cc:33] grpc_channel_credentials_release(creds=0x600003d70090)
I0000 00:00:1772163940.947495 3544765 channel.cc:120] grpc_channel_register_call(channel=0x600000d6c000, method=/helloworld.Greeter/SayHello, host=(null), reserved=0x0)
I0000 00:00:1772163940.947532 3544765 channel.cc:120] grpc_channel_register_call(channel=0x600000d6c000, method=/helloworld.Greeter/SayHelloStreamReply, host=(null), reserved=0x0)
I0000 00:00:1772163940.947556 3544765 channel.cc:120] grpc_channel_register_call(channel=0x600000d6c000, method=/helloworld.Greeter/SayHelloBidiStream, host=(null), reserved=0x0)
I0226 19:45:40.947  48629/140704384082176 main.py:41] ------------ Created the channel



I0226 19:45:40.947  48629/140704384082176 main.py:62] ------------ Initialized the function
D0226 19:45:41.495  48629/123145455296512 selector_events.py:64] Using selector: KqueueSelector


I0226 19:45:44.848  48633/123145472086016 main.py:82] ------------ Invoking hello()
I0000 00:00:1772163944.849877 3544904 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163944.849995 3544904 channel.cc:134] grpc_channel_create_registered_call(channel=0x600000d6c000, parent_call=0x0, propagation_mask=65535, completion_queue=0x7fbf8bd16710, registered_call_handle=0x600000e7c410, deadline=gpr_timespec { tv_sec: 1772163949, tv_nsec: 849474048, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163944.850703 3544904 metadata_array.cc:27] grpc_metadata_array_init(array=0x10311e458)
I0000 00:00:1772163944.850725 3544904 metadata_array.cc:27] grpc_metadata_array_init(array=0x10304adb0)
I0000 00:00:1772163944.850732 3544904 call.cc:501] grpc_call_start_batch(call=0x7fbf8708cc20, ops=0x7fbf87b74c90, nops=6, tag=0x1031176f0, reserved=0x0)
I0000 00:00:1772163944.850762 3544904 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772163944.850775 3544904 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x7fbf87bb3170
I0000 00:00:1772163944.850785 3544904 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772163944.850789 3544904 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x10311e458
I0000 00:00:1772163944.850793 3544904 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x1030ed720
I0000 00:00:1772163944.850797 3544904 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x10304adb0 status=0x10304adc8 details=0x10304add0
I0000 00:00:1772163944.851012 3544904 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fbf8bd16710, deadline=gpr_timespec { tv_sec: 1772163945, tv_nsec: 51008000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163944.854855 3544827 init.cc:132] grpc_init(void)
I0000 00:00:1772163944.855016 3544827 init.cc:132] grpc_init(void)
I0000 00:00:1772163944.855526 3544830 auth_context.cc:181] grpc_auth_context_add_cstring_property(ctx=0x7fbf86fda510, name=transport_security_type, value=insecure)
I0000 00:00:1772163944.855588 3544830 auth_context.cc:161] grpc_auth_context_add_property(ctx=0x7fbf86fda510, name=security_level, value=TSI_SECURITY_NONE, value_length=17)
I0000 00:00:1772163944.855604 3544830 auth_context.cc:115] grpc_auth_context_find_properties_by_name(ctx=0x7fbf86fda510, name=security_level)
I0000 00:00:1772163944.855613 3544830 auth_context.cc:88] grpc_auth_property_iterator_next(it=0x700007d47a60)
I0000 00:00:1772163944.856056 3544833 init.cc:132] grpc_init(void)
I0000 00:00:1772163944.856521 3544834 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772163944.857314 3544904 completion_queue.cc:762] cq_end_op_for_next(cq=0x7fbf8bd16710, tag=0x1031176f0, error=OK, done=true, done_arg=0x7fbf87b9d2c0, storage=0x7fbf87b9d308)
I0000 00:00:1772163944.857375 3544904 completion_queue.cc:1101] RETURN_EVENT[0x7fbf8bd16710]: OP_COMPLETE: tag:0x1031176f0 OK
I0000 00:00:1772163944.857431 3544904 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x10311e458)
I0000 00:00:1772163944.857446 3544904 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x10304adb0)
I0000 00:00:1772163944.857471 3544904 filter_stack_call.cc:265] grpc_call_unref(c=0x7fbf8708cc20)
I0000 00:00:1772163944.857508 3544904 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fbf8bd16710)
I0000 00:00:1772163944.857514 3544904 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fbf8bd16710)
I0000 00:00:1772163944.857518 3544904 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fbf8bd16710)
I0226 19:45:44.857  48633/123145472086016 main.py:84] ------------ Response: OK, message: "Hello, you!"



I0226 19:45:47.506  48633/123145472086016 main.py:82] ------------ Invoking hello()
I0000 00:00:1772163947.507413 3544904 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772163947.507448 3544904 channel.cc:134] grpc_channel_create_registered_call(channel=0x600000d6c000, parent_call=0x0, propagation_mask=65535, completion_queue=0x7fbf8bd16710, registered_call_handle=0x600000e7c410, deadline=gpr_timespec { tv_sec: 1772163952, tv_nsec: 507342080, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163947.507504 3544904 metadata_array.cc:27] grpc_metadata_array_init(array=0x10311e638)
I0000 00:00:1772163947.507512 3544904 metadata_array.cc:27] grpc_metadata_array_init(array=0x10304aea0)
I0000 00:00:1772163947.507516 3544904 call.cc:501] grpc_call_start_batch(call=0x7fbf870944d0, ops=0x7fbf86f053c0, nops=6, tag=0x10312ca90, reserved=0x0)
I0000 00:00:1772163947.507522 3544904 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772163947.507528 3544904 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x7fbf8bd0a5e0
I0000 00:00:1772163947.507533 3544904 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772163947.507536 3544904 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x10311e638
I0000 00:00:1772163947.507541 3544904 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x1030ed8a0
I0000 00:00:1772163947.507544 3544904 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x10304aea0 status=0x10304aeb8 details=0x10304aec0
I0000 00:00:1772163947.507690 3544904 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fbf8bd16710, deadline=gpr_timespec { tv_sec: 1772163947, tv_nsec: 707689000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772163947.508206 3544904 completion_queue.cc:762] cq_end_op_for_next(cq=0x7fbf8bd16710, tag=0x10312ca90, error=OK, done=true, done_arg=0x7fbf870954a0, storage=0x7fbf870954e8)
I0000 00:00:1772163947.508255 3544904 completion_queue.cc:1101] RETURN_EVENT[0x7fbf8bd16710]: OP_COMPLETE: tag:0x10312ca90 OK
I0000 00:00:1772163947.508274 3544904 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x10311e638)
I0000 00:00:1772163947.508284 3544904 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x10304aea0)
I0000 00:00:1772163947.508295 3544904 filter_stack_call.cc:265] grpc_call_unref(c=0x7fbf870944d0)
I0000 00:00:1772163947.508312 3544904 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fbf8bd16710)
I0000 00:00:1772163947.508317 3544904 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fbf8bd16710)
I0000 00:00:1772163947.508320 3544904 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fbf8bd16710)
I0226 19:45:47.508  48633/123145472086016 main.py:84] ------------ Response: OK, message: "Hello, you!"
```
