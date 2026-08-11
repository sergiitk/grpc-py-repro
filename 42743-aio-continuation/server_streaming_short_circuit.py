import asyncio
import grpc
from grpc.aio import ServerInterceptor


class CachingServerInterceptor(ServerInterceptor):
    async def intercept_service(self, continuation, handler_call_details):
        print(
            "[Server Interceptor] Short-circuiting! Returning cached stream from server interceptor."
        )

        async def dummy_behavior(request, context):
            # The request comes in as raw bytes since we short-circuit before deserialization
            yield b"Server Cached 1"
            yield b"Server Cached 2"

        return grpc.unary_stream_rpc_method_handler(dummy_behavior)


async def main():
    server = grpc.aio.server(interceptors=[CachingServerInterceptor()])
    # No need to actually add a service, the interceptor handles it!
    server.add_insecure_port("[::]:50051")
    await server.start()

    try:
        async with grpc.aio.insecure_channel("localhost:50051") as channel:
            stub = channel.unary_stream(
                "/DummyService/DummyStream",
                request_serializer=lambda x: x.encode(),
                response_deserializer=lambda x: x.decode(),
            )

            call = stub("dummy request")

            print("Iterating over the stream:")
            async for response in call:
                print(f" -> Received: {response}")

            print(
                "\nNow trying to access metadata (this should work fine for server interceptors!):"
            )
            meta = await call.initial_metadata()
            print(f"Metadata: {meta}")
    finally:
        await server.stop(None)


if __name__ == "__main__":
    asyncio.run(main())
