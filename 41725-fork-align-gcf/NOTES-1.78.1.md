# figuring things out 1.78.1


* [\[Python\] grpcio==1.78.1 in python fails with certain googleapis like secrets manager, pubsub, bigquery, workflows (through its sdk) from Cloud Run Functions · Issue #41725 · grpc/grpc](https://github.com/grpc/grpc/issues/41725)
* https://github.com/googlecloudplatform/functions-framework-python
* [Support gRPC Python client-side fork with epoll1 by ericgribkoff · Pull Request #16264 · grpc/grpc](https://github.com/grpc/grpc/pull/16264)

### debugging
* https://github.com/grpc/grpc/blob/master/doc/trace_flags.md

## grpcio==1.78.1 fork off, initial call

> Note: GRPC_TRACE=api seem to be broken
> Fixed with `export GRPC_PYTHON_DISABLE_ABSL_INIT_LOG=1`

**Result: WAI**

```log
I0226 21:18:36.388  70314/140704384082176 main.py:36] ------------ Start: grpc 1.78.1
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1772169516.393326 3695587 trace.cc:91] gRPC Tracers: api
I0000 00:00:1772169516.394469 3695587 init.cc:132] grpc_init(void)
I0000 00:00:1772169516.394504 3695587 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169516.394526 3695587 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169516.394540 3695587 channel_create.cc:249] grpc_channel_create(target=localhost:50051, creds=0x60000197c080, args=0x1041167d0)
I0000 00:00:1772169516.396841 3695587 init.cc:132] grpc_init(void)
I0000 00:00:1772169516.397177 3695587 transport_credentials.cc:33] grpc_channel_credentials_release(creds=0x60000197c080)
I0000 00:00:1772169516.397250 3695587 channel.cc:120] grpc_channel_register_call(channel=0x600002974090, method=/helloworld.Greeter/SayHello, host=(null), reserved=0x0)
I0000 00:00:1772169516.397303 3695587 channel.cc:120] grpc_channel_register_call(channel=0x600002974090, method=/helloworld.Greeter/SayHelloStreamReply, host=(null), reserved=0x0)
I0000 00:00:1772169516.397326 3695587 channel.cc:120] grpc_channel_register_call(channel=0x600002974090, method=/helloworld.Greeter/SayHelloBidiStream, host=(null), reserved=0x0)
I0226 21:18:36.397  70314/140704384082176 main.py:41] ------------ Created the channel



I0226 21:18:36.901  70314/140704384082176 main.py:50] ------------ Running the initial call
I0000 00:00:1772169516.902969 3695587 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169516.903018 3695587 channel.cc:134] grpc_channel_create_registered_call(channel=0x600002974090, parent_call=0x0, propagation_mask=65535, completion_queue=0x7fbb7d1abca0, registered_call_handle=0x600002a602d0, deadline=gpr_timespec { tv_sec: 1772169521, tv_nsec: 901960960, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169516.903149 3695587 metadata_array.cc:27] grpc_metadata_array_init(array=0x104127ad8)
I0000 00:00:1772169516.903158 3695587 metadata_array.cc:27] grpc_metadata_array_init(array=0x1040a6270)
I0000 00:00:1772169516.903164 3695587 call.cc:501] grpc_call_start_batch(call=0x7fbb7911bc20, ops=0x7fbb7d11a890, nops=6, tag=0x104116c00, reserved=0x0)
I0000 00:00:1772169516.903174 3695587 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772169516.903184 3695587 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x600002a71040
I0000 00:00:1772169516.903192 3695587 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772169516.903196 3695587 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x104127ad8
I0000 00:00:1772169516.903200 3695587 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x1041189a0
I0000 00:00:1772169516.903204 3695587 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x1040a6270 status=0x1040a6288 details=0x1040a6290
I0000 00:00:1772169516.903621 3695587 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fbb7d1abca0, deadline=gpr_timespec { tv_sec: 1772169517, tv_nsec: 103621000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169516.906508 3695598 init.cc:132] grpc_init(void)
I0000 00:00:1772169516.906571 3695598 init.cc:132] grpc_init(void)
I0000 00:00:1772169516.906948 3695602 auth_context.cc:181] grpc_auth_context_add_cstring_property(ctx=0x600003f7c360, name=transport_security_type, value=insecure)
I0000 00:00:1772169516.906972 3695602 auth_context.cc:161] grpc_auth_context_add_property(ctx=0x600003f7c360, name=security_level, value=TSI_SECURITY_NONE, value_length=17)
I0000 00:00:1772169516.906988 3695602 auth_context.cc:115] grpc_auth_context_find_properties_by_name(ctx=0x600003f7c360, name=security_level)
I0000 00:00:1772169516.907000 3695602 auth_context.cc:88] grpc_auth_property_iterator_next(it=0x700009237a60)
I0000 00:00:1772169516.907039 3695602 init.cc:132] grpc_init(void)
I0000 00:00:1772169516.907464 3695600 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772169516.908194 3695587 completion_queue.cc:762] cq_end_op_for_next(cq=0x7fbb7d1abca0, tag=0x104116c00, error=OK, done=true, done_arg=0x600002774520, storage=0x600002774568)
I0000 00:00:1772169516.908255 3695587 completion_queue.cc:1101] RETURN_EVENT[0x7fbb7d1abca0]: OP_COMPLETE: tag:0x104116c00 OK
I0000 00:00:1772169516.908284 3695587 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x104127ad8)
I0000 00:00:1772169516.908297 3695587 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x1040a6270)
I0000 00:00:1772169516.908321 3695587 filter_stack_call.cc:265] grpc_call_unref(c=0x7fbb7911bc20)
I0000 00:00:1772169516.908346 3695587 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fbb7d1abca0)
I0000 00:00:1772169516.908353 3695587 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fbb7d1abca0)
I0000 00:00:1772169516.908357 3695587 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fbb7d1abca0)
I0226 21:18:36.908  70314/140704384082176 main.py:52] ------------ Initial call: message: "Hello, init!"




I0226 21:18:36.908  70314/140704384082176 main.py:62] ------------ Initialized the function
D0226 21:18:37.468  70314/123145476177920 selector_events.py:64] Using selector: KqueueSelector


I0226 21:18:42.454  70315/123145492967424 main.py:82] ------------ Invoking hello()
I0000 00:00:1772169522.455369 3695719 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169522.455505 3695719 channel.cc:134] grpc_channel_create_registered_call(channel=0x600002974090, parent_call=0x0, propagation_mask=65535, completion_queue=0x7fbb79f1ff10, registered_call_handle=0x600002a602d0, deadline=gpr_timespec { tv_sec: 1772169527, tv_nsec: 454988032, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169522.455893 3695719 metadata_array.cc:27] grpc_metadata_array_init(array=0x104268518)
I0000 00:00:1772169522.455927 3695719 metadata_array.cc:27] grpc_metadata_array_init(array=0x104186ea0)
I0000 00:00:1772169522.455933 3695719 call.cc:501] grpc_call_start_batch(call=0x7fbb7b8926d0, ops=0x7fbb7980c9d0, nops=6, tag=0x104257880, reserved=0x0)
I0000 00:00:1772169522.455947 3695719 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772169522.455969 3695719 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x7fbb7980ce90
I0000 00:00:1772169522.455977 3695719 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772169522.455980 3695719 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x104268518
I0000 00:00:1772169522.455984 3695719 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x1042319a0
I0000 00:00:1772169522.455988 3695719 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x104186ea0 status=0x104186eb8 details=0x104186ec0
I0000 00:00:1772169522.456481 3695719 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fbb79f1ff10, deadline=gpr_timespec { tv_sec: 1772169522, tv_nsec: 656480000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169522.457081 3695719 completion_queue.cc:762] cq_end_op_for_next(cq=0x7fbb79f1ff10, tag=0x104257880, error=OK, done=true, done_arg=0x7fbb7b8936a0, storage=0x7fbb7b8936e8)
I0000 00:00:1772169522.457114 3695719 completion_queue.cc:1101] RETURN_EVENT[0x7fbb79f1ff10]: OP_COMPLETE: tag:0x104257880 OK
I0000 00:00:1772169522.457154 3695719 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x104268518)
I0000 00:00:1772169522.457166 3695719 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x104186ea0)
I0000 00:00:1772169522.457184 3695719 filter_stack_call.cc:265] grpc_call_unref(c=0x7fbb7b8926d0)
I0000 00:00:1772169522.457213 3695719 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fbb79f1ff10)
I0000 00:00:1772169522.457219 3695719 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fbb79f1ff10)
I0000 00:00:1772169522.457222 3695719 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fbb79f1ff10)
I0226 21:18:42.457  70315/123145492967424 main.py:84] ------------ Response: OK, message: "Hello, you!"



I0226 21:18:57.239  70315/123145492967424 main.py:82] ------------ Invoking hello()
I0000 00:00:1772169537.240435 3695719 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169537.240463 3695719 channel.cc:134] grpc_channel_create_registered_call(channel=0x600002974090, parent_call=0x0, propagation_mask=65535, completion_queue=0x7fbb79f1ff10, registered_call_handle=0x600002a602d0, deadline=gpr_timespec { tv_sec: 1772169542, tv_nsec: 240388096, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169537.240525 3695719 metadata_array.cc:27] grpc_metadata_array_init(array=0x104268658)
I0000 00:00:1772169537.240533 3695719 metadata_array.cc:27] grpc_metadata_array_init(array=0x104186f90)
I0000 00:00:1772169537.240537 3695719 call.cc:501] grpc_call_start_batch(call=0x7fbb7b8926d0, ops=0x7fbb79fd7c50, nops=6, tag=0x10426cbd0, reserved=0x0)
I0000 00:00:1772169537.240543 3695719 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772169537.240549 3695719 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x7fbb79f973e0
I0000 00:00:1772169537.240555 3695719 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772169537.240558 3695719 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x104268658
I0000 00:00:1772169537.240562 3695719 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x104231b20
I0000 00:00:1772169537.240566 3695719 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x104186f90 status=0x104186fa8 details=0x104186fb0
I0000 00:00:1772169537.240661 3695719 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fbb79f1ff10, deadline=gpr_timespec { tv_sec: 1772169537, tv_nsec: 440660000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169537.241163 3695719 completion_queue.cc:762] cq_end_op_for_next(cq=0x7fbb79f1ff10, tag=0x10426cbd0, error=OK, done=true, done_arg=0x7fbb7b8936a0, storage=0x7fbb7b8936e8)
I0000 00:00:1772169537.241191 3695719 completion_queue.cc:1101] RETURN_EVENT[0x7fbb79f1ff10]: OP_COMPLETE: tag:0x10426cbd0 OK
I0000 00:00:1772169537.241209 3695719 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x104268658)
I0000 00:00:1772169537.241217 3695719 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x104186f90)
I0000 00:00:1772169537.241228 3695719 filter_stack_call.cc:265] grpc_call_unref(c=0x7fbb7b8926d0)
I0000 00:00:1772169537.241248 3695719 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fbb79f1ff10)
I0000 00:00:1772169537.241253 3695719 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fbb79f1ff10)
I0000 00:00:1772169537.241256 3695719 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fbb79f1ff10)
I0226 21:18:57.241  70315/123145492967424 main.py:84] ------------ Response: OK, message: "Hello, you!"
```

## grpcio==1.78.1 fork ON, initial call

**Result: ValueError('Cannot invoke RPC on closed channel!')**


```log
$ TEST_INITIAL_CALL=1 GRPC_ENABLE_FORK_SUPPORT=1 GRPC_TRACE=api ff --target=hello
I0226 21:20:07.074  70631/140704384082176 main.py:36] ------------ Start: grpc 1.78.1
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1772169607.078774 3698208 trace.cc:91] gRPC Tracers: api
I0000 00:00:1772169607.078911 3698208 init.cc:132] grpc_init(void)
I0000 00:00:1772169607.079504 3698208 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169607.079536 3698208 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169607.079549 3698208 channel_create.cc:249] grpc_channel_create(target=localhost:50051, creds=0x600000eb4240, args=0x10418e7d0)
I0000 00:00:1772169607.080238 3698208 init.cc:132] grpc_init(void)
I0000 00:00:1772169607.080253 3698208 transport_credentials.cc:33] grpc_channel_credentials_release(creds=0x600000eb4240)
I0000 00:00:1772169607.080294 3698208 channel.cc:120] grpc_channel_register_call(channel=0x600003ea10e0, method=/helloworld.Greeter/SayHello, host=(null), reserved=0x0)
I0000 00:00:1772169607.080347 3698208 channel.cc:120] grpc_channel_register_call(channel=0x600003ea10e0, method=/helloworld.Greeter/SayHelloStreamReply, host=(null), reserved=0x0)
I0000 00:00:1772169607.080425 3698208 channel.cc:120] grpc_channel_register_call(channel=0x600003ea10e0, method=/helloworld.Greeter/SayHelloBidiStream, host=(null), reserved=0x0)
I0226 21:20:07.080  70631/140704384082176 main.py:41] ------------ Created the channel



I0226 21:20:07.581  70631/140704384082176 main.py:50] ------------ Running the initial call
I0000 00:00:1772169607.581285 3698208 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169607.581319 3698208 channel.cc:134] grpc_channel_create_registered_call(channel=0x600003ea10e0, parent_call=0x0, propagation_mask=65535, completion_queue=0x7fd64c658990, registered_call_handle=0x600003da0f50, deadline=gpr_timespec { tv_sec: 1772169612, tv_nsec: 581200896, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169607.581446 3698208 metadata_array.cc:27] grpc_metadata_array_init(array=0x10419fad8)
I0000 00:00:1772169607.581462 3698208 metadata_array.cc:27] grpc_metadata_array_init(array=0x10411e270)
I0000 00:00:1772169607.581466 3698208 call.cc:501] grpc_call_start_batch(call=0x7fd64a0b8020, ops=0x7fd64c615f70, nops=6, tag=0x10418ec00, reserved=0x0)
I0000 00:00:1772169607.581476 3698208 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772169607.581483 3698208 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x600003da1040
I0000 00:00:1772169607.581489 3698208 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772169607.581491 3698208 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x10419fad8
I0000 00:00:1772169607.581495 3698208 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x1041909a0
I0000 00:00:1772169607.581498 3698208 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x10411e270 status=0x10411e288 details=0x10411e290
I0000 00:00:1772169607.581604 3698208 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fd64c658990, deadline=gpr_timespec { tv_sec: 1772169607, tv_nsec: 781603000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169607.582807 3698223 init.cc:132] grpc_init(void)
I0000 00:00:1772169607.582855 3698223 init.cc:132] grpc_init(void)
I0000 00:00:1772169607.583182 3698226 auth_context.cc:181] grpc_auth_context_add_cstring_property(ctx=0x6000028a06c0, name=transport_security_type, value=insecure)
I0000 00:00:1772169607.583210 3698226 auth_context.cc:161] grpc_auth_context_add_property(ctx=0x6000028a06c0, name=security_level, value=TSI_SECURITY_NONE, value_length=17)
I0000 00:00:1772169607.583223 3698226 auth_context.cc:115] grpc_auth_context_find_properties_by_name(ctx=0x6000028a06c0, name=security_level)
I0000 00:00:1772169607.583231 3698226 auth_context.cc:88] grpc_auth_property_iterator_next(it=0x700004aa8a60)
I0000 00:00:1772169607.583308 3698226 init.cc:132] grpc_init(void)
I0000 00:00:1772169607.583692 3698232 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772169607.584819 3698208 completion_queue.cc:762] cq_end_op_for_next(cq=0x7fd64c658990, tag=0x10418ec00, error=OK, done=true, done_arg=0x6000030a1020, storage=0x6000030a1068)
I0000 00:00:1772169607.584869 3698208 completion_queue.cc:1101] RETURN_EVENT[0x7fd64c658990]: OP_COMPLETE: tag:0x10418ec00 OK
I0000 00:00:1772169607.584894 3698208 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x10419fad8)
I0000 00:00:1772169607.584903 3698208 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x10411e270)
I0000 00:00:1772169607.584922 3698208 filter_stack_call.cc:265] grpc_call_unref(c=0x7fd64a0b8020)
I0000 00:00:1772169607.584942 3698208 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fd64c658990)
I0000 00:00:1772169607.584948 3698208 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fd64c658990)
I0000 00:00:1772169607.584951 3698208 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fd64c658990)
I0226 21:20:07.585  70631/140704384082176 main.py:52] ------------ Initial call: message: "Hello, init!"




I0226 21:20:07.585  70631/140704384082176 main.py:62] ------------ Initialized the function
D0226 21:20:08.131  70631/123145402216448 selector_events.py:64] Using selector: KqueueSelector
I0000 00:00:1772169608.137800 3698208 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fd6484e76c0)
I0000 00:00:1772169608.137898 3698208 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fd6484e76c0)
I0000 00:00:1772169608.137904 3698208 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fd6484e76c0)
I0000 00:00:1772169608.137908 3698208 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fd648497790)
I0000 00:00:1772169608.137916 3698208 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fd648497790)
I0000 00:00:1772169608.137920 3698208 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fd648497790)
I0000 00:00:1772169608.137927 3698208 channel.cc:95] grpc_channel_destroy(channel=0x600003ea10e0)
I0000 00:00:1772169608.138129 3698208 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772169608.138523 3698279 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772169608.138777 3698279 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772169608.138910 3698279 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772169608.138955 3698290 init.cc:154] grpc_shutdown_from_cleanup_thread


I0226 21:20:09.162  70633/123145419005952 main.py:82] ------------ Invoking hello()
I0226 21:20:09.164  70633/123145419005952 main.py:84] ------------ Response: Other error: ValueError('Cannot invoke RPC on closed channel!')



I0226 21:20:10.495  70633/123145419005952 main.py:82] ------------ Invoking hello()
I0226 21:20:10.495  70633/123145419005952 main.py:84] ------------ Response: Other error: ValueError('Cannot invoke RPC on closed channel!')
```

## grpcio==1.78.1 fork UNSET, initial call

**Result: WAI**

```log
$ TEST_INITIAL_CALL=1 GRPC_TRACE=api ff --target=hello
I0226 21:20:29.771  70792/140704384082176 main.py:36] ------------ Start: grpc 1.78.1
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1772169629.775269 3699052 trace.cc:91] gRPC Tracers: api
I0000 00:00:1772169629.775391 3699052 init.cc:132] grpc_init(void)
I0000 00:00:1772169629.775416 3699052 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169629.775437 3699052 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169629.775449 3699052 channel_create.cc:249] grpc_channel_create(target=localhost:50051, creds=0x600003010160, args=0x11137a820)
I0000 00:00:1772169629.776102 3699052 init.cc:132] grpc_init(void)
I0000 00:00:1772169629.776120 3699052 transport_credentials.cc:33] grpc_channel_credentials_release(creds=0x600003010160)
I0000 00:00:1772169629.776157 3699052 channel.cc:120] grpc_channel_register_call(channel=0x600000014090, method=/helloworld.Greeter/SayHello, host=(null), reserved=0x0)
I0000 00:00:1772169629.776196 3699052 channel.cc:120] grpc_channel_register_call(channel=0x600000014090, method=/helloworld.Greeter/SayHelloStreamReply, host=(null), reserved=0x0)
I0000 00:00:1772169629.776218 3699052 channel.cc:120] grpc_channel_register_call(channel=0x600000014090, method=/helloworld.Greeter/SayHelloBidiStream, host=(null), reserved=0x0)
I0226 21:20:29.776  70792/140704384082176 main.py:41] ------------ Created the channel



I0226 21:20:30.279  70792/140704384082176 main.py:50] ------------ Running the initial call
I0000 00:00:1772169630.279933 3699052 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169630.280017 3699052 channel.cc:134] grpc_channel_create_registered_call(channel=0x600000014090, parent_call=0x0, propagation_mask=65535, completion_queue=0x7fa39d30f0a0, registered_call_handle=0x600000318730, deadline=gpr_timespec { tv_sec: 1772169635, tv_nsec: 279771904, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169630.280224 3699052 metadata_array.cc:27] grpc_metadata_array_init(array=0x11138bad8)
I0000 00:00:1772169630.280242 3699052 metadata_array.cc:27] grpc_metadata_array_init(array=0x11130a270)
I0000 00:00:1772169630.280251 3699052 call.cc:501] grpc_call_start_batch(call=0x7fa39c0ad420, ops=0x7fa39d30f290, nops=6, tag=0x11137ac50, reserved=0x0)
I0000 00:00:1772169630.280270 3699052 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772169630.280287 3699052 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x6000003188c0
I0000 00:00:1772169630.280302 3699052 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772169630.280309 3699052 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x11138bad8
I0000 00:00:1772169630.280318 3699052 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x11137c9a0
I0000 00:00:1772169630.280327 3699052 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x11130a270 status=0x11130a288 details=0x11130a290
I0000 00:00:1772169630.280526 3699052 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fa39d30f0a0, deadline=gpr_timespec { tv_sec: 1772169630, tv_nsec: 480525000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169630.283012 3699064 init.cc:132] grpc_init(void)
I0000 00:00:1772169630.283091 3699064 init.cc:132] grpc_init(void)
I0000 00:00:1772169630.283598 3699073 auth_context.cc:181] grpc_auth_context_add_cstring_property(ctx=0x60000160c180, name=transport_security_type, value=insecure)
I0000 00:00:1772169630.283629 3699073 auth_context.cc:161] grpc_auth_context_add_property(ctx=0x60000160c180, name=security_level, value=TSI_SECURITY_NONE, value_length=17)
I0000 00:00:1772169630.283642 3699073 auth_context.cc:115] grpc_auth_context_find_properties_by_name(ctx=0x60000160c180, name=security_level)
I0000 00:00:1772169630.283653 3699073 auth_context.cc:88] grpc_auth_property_iterator_next(it=0x700003b62a60)
I0000 00:00:1772169630.283696 3699073 init.cc:132] grpc_init(void)
I0000 00:00:1772169630.284011 3699067 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772169630.285656 3699052 completion_queue.cc:762] cq_end_op_for_next(cq=0x7fa39d30f0a0, tag=0x11137ac50, error=OK, done=true, done_arg=0x600000e14520, storage=0x600000e14568)
I0000 00:00:1772169630.285721 3699052 completion_queue.cc:1101] RETURN_EVENT[0x7fa39d30f0a0]: OP_COMPLETE: tag:0x11137ac50 OK
I0000 00:00:1772169630.285751 3699052 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x11138bad8)
I0000 00:00:1772169630.285764 3699052 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x11130a270)
I0000 00:00:1772169630.285788 3699052 filter_stack_call.cc:265] grpc_call_unref(c=0x7fa39c0ad420)
I0000 00:00:1772169630.285814 3699052 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fa39d30f0a0)
I0000 00:00:1772169630.285821 3699052 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fa39d30f0a0)
I0000 00:00:1772169630.285825 3699052 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fa39d30f0a0)
I0226 21:20:30.285  70792/140704384082176 main.py:52] ------------ Initial call: message: "Hello, init!"




I0226 21:20:30.286  70792/140704384082176 main.py:62] ------------ Initialized the function
D0226 21:20:30.847  70792/123145382981632 selector_events.py:64] Using selector: KqueueSelector


I0226 21:20:34.122  70793/123145399771136 main.py:82] ------------ Invoking hello()
I0000 00:00:1772169634.124054 3699140 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169634.124189 3699140 channel.cc:134] grpc_channel_create_registered_call(channel=0x600000014090, parent_call=0x0, propagation_mask=65535, completion_queue=0x7fa39a668570, registered_call_handle=0x600000318730, deadline=gpr_timespec { tv_sec: 1772169639, tv_nsec: 123672064, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169634.124509 3699140 metadata_array.cc:27] grpc_metadata_array_init(array=0x1114cc518)
I0000 00:00:1772169634.124533 3699140 metadata_array.cc:27] grpc_metadata_array_init(array=0x1113eaea0)
I0000 00:00:1772169634.124538 3699140 call.cc:501] grpc_call_start_batch(call=0x7fa39b041ed0, ops=0x7fa39a30fd80, nops=6, tag=0x1114bb830, reserved=0x0)
I0000 00:00:1772169634.124553 3699140 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772169634.124570 3699140 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x7fa39a314810
I0000 00:00:1772169634.124577 3699140 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772169634.124581 3699140 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x1114cc518
I0000 00:00:1772169634.124585 3699140 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x1114959a0
I0000 00:00:1772169634.124589 3699140 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x1113eaea0 status=0x1113eaeb8 details=0x1113eaec0
I0000 00:00:1772169634.125083 3699140 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fa39a668570, deadline=gpr_timespec { tv_sec: 1772169634, tv_nsec: 325082000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169634.125637 3699140 completion_queue.cc:762] cq_end_op_for_next(cq=0x7fa39a668570, tag=0x1114bb830, error=OK, done=true, done_arg=0x7fa39b042ea0, storage=0x7fa39b042ee8)
I0000 00:00:1772169634.125669 3699140 completion_queue.cc:1101] RETURN_EVENT[0x7fa39a668570]: OP_COMPLETE: tag:0x1114bb830 OK
I0000 00:00:1772169634.125732 3699140 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x1114cc518)
I0000 00:00:1772169634.125744 3699140 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x1113eaea0)
I0000 00:00:1772169634.125765 3699140 filter_stack_call.cc:265] grpc_call_unref(c=0x7fa39b041ed0)
I0000 00:00:1772169634.125791 3699140 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fa39a668570)
I0000 00:00:1772169634.125796 3699140 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fa39a668570)
I0000 00:00:1772169634.125800 3699140 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fa39a668570)
I0226 21:20:34.126  70793/123145399771136 main.py:84] ------------ Response: OK, message: "Hello, you!"



I0226 21:20:38.027  70793/123145399771136 main.py:82] ------------ Invoking hello()
I0000 00:00:1772169638.028726 3699140 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169638.028759 3699140 channel.cc:134] grpc_channel_create_registered_call(channel=0x600000014090, parent_call=0x0, propagation_mask=65535, completion_queue=0x7fa39a668570, registered_call_handle=0x600000318730, deadline=gpr_timespec { tv_sec: 1772169643, tv_nsec: 28674048, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169638.028812 3699140 metadata_array.cc:27] grpc_metadata_array_init(array=0x1114cc658)
I0000 00:00:1772169638.028819 3699140 metadata_array.cc:27] grpc_metadata_array_init(array=0x1113eaf90)
I0000 00:00:1772169638.028823 3699140 call.cc:501] grpc_call_start_batch(call=0x7fa39b041ed0, ops=0x7fa39a66b9a0, nops=6, tag=0x1114d4b80, reserved=0x0)
I0000 00:00:1772169638.028830 3699140 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772169638.028835 3699140 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x7fa39a61d050
I0000 00:00:1772169638.028840 3699140 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772169638.028843 3699140 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x1114cc658
I0000 00:00:1772169638.028847 3699140 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x111495b20
I0000 00:00:1772169638.028851 3699140 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x1113eaf90 status=0x1113eafa8 details=0x1113eafb0
I0000 00:00:1772169638.028987 3699140 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fa39a668570, deadline=gpr_timespec { tv_sec: 1772169638, tv_nsec: 228986000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169638.030034 3699140 completion_queue.cc:762] cq_end_op_for_next(cq=0x7fa39a668570, tag=0x1114d4b80, error=OK, done=true, done_arg=0x7fa39b042ea0, storage=0x7fa39b042ee8)
I0000 00:00:1772169638.030052 3699140 completion_queue.cc:1101] RETURN_EVENT[0x7fa39a668570]: OP_COMPLETE: tag:0x1114d4b80 OK
I0000 00:00:1772169638.030064 3699140 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x1114cc658)
I0000 00:00:1772169638.030073 3699140 metadata_array.cc:33] grpc_metadata_array_destroy(array=0x1113eaf90)
I0000 00:00:1772169638.030082 3699140 filter_stack_call.cc:265] grpc_call_unref(c=0x7fa39b041ed0)
I0000 00:00:1772169638.030098 3699140 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fa39a668570)
I0000 00:00:1772169638.030103 3699140 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7fa39a668570)
I0000 00:00:1772169638.030107 3699140 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7fa39a668570)
I0226 21:20:38.030  70793/123145399771136 main.py:84] ------------ Response: OK, message: "Hello, you!"
```

## grpcio==1.78.1 fork OFF

**Result: Hang**


```log
$ GRPC_ENABLE_FORK_SUPPORT=0 GRPC_TRACE=api ff --target=hello
I0226 21:21:58.362  71371/140704384082176 main.py:36] ------------ Start: grpc 1.78.1
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1772169718.365559 3701396 trace.cc:91] gRPC Tracers: api
I0000 00:00:1772169718.365667 3701396 init.cc:132] grpc_init(void)
I0000 00:00:1772169718.365686 3701396 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169718.365705 3701396 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169718.365716 3701396 channel_create.cc:249] grpc_channel_create(target=localhost:50051, creds=0x600000dec2b0, args=0x10e4d6820)
I0000 00:00:1772169718.366365 3701396 init.cc:132] grpc_init(void)
I0000 00:00:1772169718.366378 3701396 transport_credentials.cc:33] grpc_channel_credentials_release(creds=0x600000dec2b0)
I0000 00:00:1772169718.366413 3701396 channel.cc:120] grpc_channel_register_call(channel=0x600003de4000, method=/helloworld.Greeter/SayHello, host=(null), reserved=0x0)
I0000 00:00:1772169718.366446 3701396 channel.cc:120] grpc_channel_register_call(channel=0x600003de4000, method=/helloworld.Greeter/SayHelloStreamReply, host=(null), reserved=0x0)
I0000 00:00:1772169718.366464 3701396 channel.cc:120] grpc_channel_register_call(channel=0x600003de4000, method=/helloworld.Greeter/SayHelloBidiStream, host=(null), reserved=0x0)
I0226 21:21:58.366  71371/140704384082176 main.py:41] ------------ Created the channel



I0226 21:21:58.366  71371/140704384082176 main.py:62] ------------ Initialized the function
D0226 21:21:58.912  71371/123145415270400 selector_events.py:64] Using selector: KqueueSelector


I0226 21:22:01.712  71373/123145432059904 main.py:82] ------------ Invoking hello()
I0000 00:00:1772169721.713998 3701560 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169721.714136 3701560 channel.cc:134] grpc_channel_create_registered_call(channel=0x600003de4000, parent_call=0x0, propagation_mask=65535, completion_queue=0x7f9f426646a0, registered_call_handle=0x600003ee0410, deadline=gpr_timespec { tv_sec: 1772169726, tv_nsec: 713635072, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169721.714438 3701560 metadata_array.cc:27] grpc_metadata_array_init(array=0x10e628518)
I0000 00:00:1772169721.714450 3701560 metadata_array.cc:27] grpc_metadata_array_init(array=0x10e546ea0)
I0000 00:00:1772169721.714455 3701560 call.cc:501] grpc_call_start_batch(call=0x7f9f43862e20, ops=0x7f9f426e6700, nops=6, tag=0x10e617880, reserved=0x0)
I0000 00:00:1772169721.714469 3701560 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772169721.714482 3701560 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x7f9f426e68e0
I0000 00:00:1772169721.714489 3701560 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772169721.714492 3701560 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x10e628518
I0000 00:00:1772169721.714496 3701560 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x10e5f19a0
I0000 00:00:1772169721.714500 3701560 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x10e546ea0 status=0x10e546eb8 details=0x10e546ec0
I0000 00:00:1772169721.714688 3701560 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f9f426646a0, deadline=gpr_timespec { tv_sec: 1772169721, tv_nsec: 914687000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169721.916019 3701560 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f9f426646a0, deadline=gpr_timespec { tv_sec: 1772169722, tv_nsec: 116018000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169722.117284 3701560 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f9f426646a0, deadline=gpr_timespec { tv_sec: 1772169722, tv_nsec: 317283000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169722.318370 3701560 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f9f426646a0, deadline=gpr_timespec { tv_sec: 1772169722, tv_nsec: 518369000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169722.519449 3701560 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f9f426646a0, deadline=gpr_timespec { tv_sec: 1772169722, tv_nsec: 719447000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169722.720912 3701560 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f9f426646a0, deadline=gpr_timespec { tv_sec: 1772169722, tv_nsec: 920911000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169722.922067 3701560 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f9f426646a0, deadline=gpr_timespec { tv_sec: 1772169723, tv_nsec: 122066000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169723.123134 3701560 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7f9f426646a0, deadline=gpr_timespec { tv_sec: 1772169723, tv_nsec: 323133000, clock_type: 1 }, reserved=0x0)
...

> HANG
```


## grpcio==1.78.1 fork ON

**Result: ValueError('Cannot invoke RPC on closed channel!')**

```log
$ GRPC_ENABLE_FORK_SUPPORT=1 GRPC_TRACE=api ff --target=hello
I0226 21:22:29.081  71509/140704384082176 main.py:36] ------------ Start: grpc 1.78.1
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1772169749.085057 3702214 trace.cc:91] gRPC Tracers: api
I0000 00:00:1772169749.085185 3702214 init.cc:132] grpc_init(void)
I0000 00:00:1772169749.085217 3702214 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169749.085237 3702214 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169749.085254 3702214 channel_create.cc:249] grpc_channel_create(target=localhost:50051, creds=0x600001dc4090, args=0x1076fe820)
I0000 00:00:1772169749.085921 3702214 init.cc:132] grpc_init(void)
I0000 00:00:1772169749.085939 3702214 transport_credentials.cc:33] grpc_channel_credentials_release(creds=0x600001dc4090)
I0000 00:00:1772169749.085982 3702214 channel.cc:120] grpc_channel_register_call(channel=0x600002dc4000, method=/helloworld.Greeter/SayHello, host=(null), reserved=0x0)
I0000 00:00:1772169749.086020 3702214 channel.cc:120] grpc_channel_register_call(channel=0x600002dc4000, method=/helloworld.Greeter/SayHelloStreamReply, host=(null), reserved=0x0)
I0000 00:00:1772169749.086042 3702214 channel.cc:120] grpc_channel_register_call(channel=0x600002dc4000, method=/helloworld.Greeter/SayHelloBidiStream, host=(null), reserved=0x0)
I0226 21:22:29.086  71509/140704384082176 main.py:41] ------------ Created the channel



I0226 21:22:29.086  71509/140704384082176 main.py:62] ------------ Initialized the function
D0226 21:22:29.630  71509/123145340891136 selector_events.py:64] Using selector: KqueueSelector
I0000 00:00:1772169749.637348 3702214 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f7ef02364c0)
I0000 00:00:1772169749.637492 3702214 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7f7ef02364c0)
I0000 00:00:1772169749.637500 3702214 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f7ef02364c0)
I0000 00:00:1772169749.637513 3702214 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f7ef02df200)
I0000 00:00:1772169749.637517 3702214 completion_queue.cc:1426] grpc_completion_queue_destroy(cq=0x7f7ef02df200)
I0000 00:00:1772169749.637555 3702214 completion_queue.cc:1420] grpc_completion_queue_shutdown(cq=0x7f7ef02df200)
I0000 00:00:1772169749.637591 3702214 channel.cc:95] grpc_channel_destroy(channel=0x600002dc4000)
I0000 00:00:1772169749.637740 3702214 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772169749.638020 3702280 init.cc:166] grpc_shutdown(void)
I0000 00:00:1772169749.638114 3702290 init.cc:154] grpc_shutdown_from_cleanup_thread


I0226 21:22:31.385  71512/123145357680640 main.py:82] ------------ Invoking hello()
I0226 21:22:31.386  71512/123145357680640 main.py:84] ------------ Response: Other error: ValueError('Cannot invoke RPC on closed channel!')



I0226 21:22:33.459  71512/123145357680640 main.py:82] ------------ Invoking hello()
I0226 21:22:33.460  71512/123145357680640 main.py:84] ------------ Response: Other error: ValueError('Cannot invoke RPC on closed channel!')
```

## grpcio==1.78.1 fork UNSET

**Result: Hang**

```log
$ GRPC_TRACE=api ff --target=hello
I0226 21:22:50.262  71649/140704384082176 main.py:36] ------------ Start: grpc 1.78.1
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1772169770.266149 3702921 trace.cc:91] gRPC Tracers: api
I0000 00:00:1772169770.266273 3702921 init.cc:132] grpc_init(void)
I0000 00:00:1772169770.266297 3702921 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169770.266318 3702921 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169770.266330 3702921 channel_create.cc:249] grpc_channel_create(target=localhost:50051, creds=0x600001ef01d0, args=0x111be6820)
I0000 00:00:1772169770.266982 3702921 init.cc:132] grpc_init(void)
I0000 00:00:1772169770.266997 3702921 transport_credentials.cc:33] grpc_channel_credentials_release(creds=0x600001ef01d0)
I0000 00:00:1772169770.267038 3702921 channel.cc:120] grpc_channel_register_call(channel=0x600002efc090, method=/helloworld.Greeter/SayHello, host=(null), reserved=0x0)
I0000 00:00:1772169770.267077 3702921 channel.cc:120] grpc_channel_register_call(channel=0x600002efc090, method=/helloworld.Greeter/SayHelloStreamReply, host=(null), reserved=0x0)
I0000 00:00:1772169770.267097 3702921 channel.cc:120] grpc_channel_register_call(channel=0x600002efc090, method=/helloworld.Greeter/SayHelloBidiStream, host=(null), reserved=0x0)
I0226 21:22:50.267  71649/140704384082176 main.py:41] ------------ Created the channel



I0226 21:22:50.267  71649/140704384082176 main.py:62] ------------ Initialized the function
D0226 21:22:50.805  71649/123145516089344 selector_events.py:64] Using selector: KqueueSelector


I0226 21:22:51.783  71650/123145532878848 main.py:82] ------------ Invoking hello()
I0000 00:00:1772169771.784406 3702963 completion_queue.cc:574] grpc_completion_queue_create_internal(completion_type=0, polling_type=0)
I0000 00:00:1772169771.784547 3702963 channel.cc:134] grpc_channel_create_registered_call(channel=0x600002efc090, parent_call=0x0, propagation_mask=65535, completion_queue=0x7fee5626b540, registered_call_handle=0x600002df85f0, deadline=gpr_timespec { tv_sec: 1772169776, tv_nsec: 784018944, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169771.784869 3702963 metadata_array.cc:27] grpc_metadata_array_init(array=0x111d40518)
I0000 00:00:1772169771.784881 3702963 metadata_array.cc:27] grpc_metadata_array_init(array=0x111c5aea0)
I0000 00:00:1772169771.784885 3702963 call.cc:501] grpc_call_start_batch(call=0x7fee57061c20, ops=0x7fee56272a70, nops=6, tag=0x111d2f830, reserved=0x0)
I0000 00:00:1772169771.784899 3702963 filter_stack_call.cc:769] ops[0]: SEND_INITIAL_METADATA(nil)
I0000 00:00:1772169771.784913 3702963 filter_stack_call.cc:769] ops[1]: SEND_MESSAGE ptr=0x7fee5626ed50
I0000 00:00:1772169771.784919 3702963 filter_stack_call.cc:769] ops[2]: SEND_CLOSE_FROM_CLIENT
I0000 00:00:1772169771.784923 3702963 filter_stack_call.cc:769] ops[3]: RECV_INITIAL_METADATA ptr=0x111d40518
I0000 00:00:1772169771.784927 3702963 filter_stack_call.cc:769] ops[4]: RECV_MESSAGE ptr=0x111d059a0
I0000 00:00:1772169771.784930 3702963 filter_stack_call.cc:769] ops[5]: RECV_STATUS_ON_CLIENT metadata=0x111c5aea0 status=0x111c5aeb8 details=0x111c5aec0
I0000 00:00:1772169771.785119 3702963 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fee5626b540, deadline=gpr_timespec { tv_sec: 1772169771, tv_nsec: 985118000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169771.987203 3702963 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fee5626b540, deadline=gpr_timespec { tv_sec: 1772169772, tv_nsec: 187201000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169772.189235 3702963 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fee5626b540, deadline=gpr_timespec { tv_sec: 1772169772, tv_nsec: 389233000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169772.390455 3702963 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fee5626b540, deadline=gpr_timespec { tv_sec: 1772169772, tv_nsec: 590454000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169772.591765 3702963 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fee5626b540, deadline=gpr_timespec { tv_sec: 1772169772, tv_nsec: 791763000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169772.793236 3702963 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fee5626b540, deadline=gpr_timespec { tv_sec: 1772169772, tv_nsec: 993235000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169772.994467 3702963 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fee5626b540, deadline=gpr_timespec { tv_sec: 1772169773, tv_nsec: 194465000, clock_type: 1 }, reserved=0x0)
I0000 00:00:1772169773.196049 3702963 completion_queue.cc:992] grpc_completion_queue_next(cq=0x7fee5626b540, deadline=gpr_timespec { tv_sec: 1772169773, tv_nsec: 396048000, clock_type: 1 }, reserved=0x0)
...

> HANG
```
