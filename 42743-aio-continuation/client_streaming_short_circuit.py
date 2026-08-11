import asyncio

import grpc
from grpc.aio import UnaryStreamClientInterceptor


class CachingInterceptor(UnaryStreamClientInterceptor):
    async def intercept_unary_stream(self, continuation, client_call_details, request):
        print("[Interceptor] Short-circuiting! Returning cached stream.")

        async def cached_stream():
            yield "Response 1 from cache"
            yield "Response 2 from cache"

        return cached_stream()


async def main():
    async with grpc.aio.insecure_channel(
        "localhost:50051", interceptors=[CachingInterceptor()]
    ) as channel:
        # We don't even need a real server because we short-circuit!
        stub = channel.unary_stream(
            "/DummyService/DummyStream",
            request_serializer=lambda x: x.encode(),
            response_deserializer=lambda x: x.decode(),
        )

        call = stub("dummy request")

        print("Iterating over the stream:")
        async for response in call:
            print(f" -> Received: {response}")

        print("\nNow trying to access metadata (this will crash on 1.83.0):")
        try:
            await call.initial_metadata()
        except AttributeError as e:
            print(f"CRASH: {e}")


if __name__ == "__main__":
    asyncio.run(main())
