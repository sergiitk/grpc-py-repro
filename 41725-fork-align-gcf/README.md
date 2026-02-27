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
