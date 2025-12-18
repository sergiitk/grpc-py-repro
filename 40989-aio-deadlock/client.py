# Copyright 2020 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python AsyncIO implementation of the GRPC helloworld.Greeter client."""

import asyncio
import logging
import subprocess

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

# net.core.rmem_default = 212992
# net.core.wmem_default = 212992

# net.core.rmem_default = 8192


async def send_requests(
    stub: helloworld_pb2_grpc.GreeterStub, id: int, num: int = 100
):
    logging.info(f"sending from {id}")
    for i in range(num):
        resp = await stub.SayHello(helloworld_pb2.HelloRequest(name=f"you {i}"))
        if i % 30 == 0:
            logging.info(f"#{id} Greeter client received: " + resp.message)


async def run() -> None:
    logging.info("Verifying sysctl")
    rmem_default = subprocess.check_output(["sysctl", "net.core.rmem_default"])
    rmem_default = rmem_default.decode().strip()
    assert rmem_default == "net.core.rmem_default = 6144", f"{rmem_default=}"
    wmem_default = subprocess.check_output(["sysctl", "net.core.wmem_default"])
    wmem_default = wmem_default.decode().strip()
    assert wmem_default == "net.core.wmem_default = 6144", f"{wmem_default=}"
    logging.info("sysctl LGTM")

    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        tasks = []
        for i in range(10):
            tasks.append(send_requests(stub, i))

        logging.info("sending requests")
        await asyncio.gather(*tasks)
        logging.info("done sending requests")


if __name__ == "__main__":
    # absl-style logging.
    logging.basicConfig(
        level=logging.INFO,
        style="{",
        format=(
            "{levelname[0]}{asctime}.{msecs:03.0f} {thread} "
            "{filename}:{lineno}] {message}"
        ),
        datefmt="%m%d %H:%M:%S",
    )
    asyncio.run(run())
