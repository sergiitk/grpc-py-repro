# Copyright 2026 gRPC authors.
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

import logging
import os
import time

import functions_framework
import grpc

import helloworld_pb2
import helloworld_pb2_grpc

# absl-style logging.
logging.basicConfig(
    level=logging.DEBUG,
    style="{",
    format=(
        "{levelname[0]}{asctime}.{msecs:03.0f}  {process}/{thread} "
        "{filename}:{lineno}] {message}"
    ),
    datefmt="%m%d %H:%M:%S",
)

logging.info("------------ Start: grpc %s", grpc.__version__)

# gRPC channel created at module level (before gunicorn fork)
channel = grpc.insecure_channel("localhost:50051")
stub = helloworld_pb2_grpc.GreeterStub(channel)
logging.info("------------ Created the channel")


def initial_call():
    print()
    print()
    print()
    time.sleep(0.5)

    logging.info("------------ Running the initial call")
    response = stub.SayHello(helloworld_pb2.HelloRequest(name="init"), timeout=5)
    logging.info(f"------------ Initial call: {response}")


if os.getenv("TEST_INITIAL_CALL", "0") == "1":
    initial_call()


print()
print()
print()
logging.info("------------ Initialized the function")

time.sleep(0.5)


def process_call():
    try:
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"), timeout=5)
    except grpc.RpcError as e:
        return f"gRPC error: {e.code().name}\n"
    except Exception as e:
        return f"Other error: {e!r}\n"

    return f"OK, {response}"


@functions_framework.http
def hello(request):
    print()
    print()
    logging.info("------------ Invoking hello()")
    result = process_call()
    logging.info("------------ Response: %s", result)
    return result
