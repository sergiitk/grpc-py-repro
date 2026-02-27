# Reproducing #41725

[\[Python\] grpcio==1.78.1 in python fails with certain googleapis like secrets manager, pubsub, bigquery, workflows (through its sdk) from Cloud Run Functions · Issue #41725 · grpc/grpc](https://github.com/grpc/grpc/issues/41725)

## Results

- https://github.com/sergiitk/grpc-py-repro/blob/main/41725-fork-align-gcf/NOTES-1.78.0.md
- https://github.com/sergiitk/grpc-py-repro/blob/main/41725-fork-align-gcf/NOTES-1.78.1.md


|                    | fork OFF | fork ON        | fork UNSET |
|--------------------|----------|----------------|------------|
| grpc 1.78.0        | Hang     | closed channel | WAI        |
| grpc 1.78.1        | Hang     | closed channel | Hang       |
| grpc 1.78.0 w/init | WAI      | closed channel | Almost WAI |
| grpc 1.78.1 w/init | WAI      | closed channel | WAI        |


\* w/init means issuing initial call on the channel in the main process before forking

### System

```sh
$ sw_vers
ProductName:		macOS
ProductVersion:		15.7.4
BuildVersion:		24G517
$ python -VV
Python 3.12.12 (main, Oct 11 2025, 02:03:32) [Clang 17.0.0 (clang-1700.3.19.1)]
```

## Running

```sh
uv sync

# first window
uv run greeter_server.py &

# second window
uv run functions-framework --target hello

# first window
curl localhost:8080
```

Alternative for the second window:

```sh
source ./.venv/bin/activate

# in the venv
ff --target=hello

# when changing the version in pyproject.toml, do
uv sync
```

More examples for different test cases in the NOTES files.
