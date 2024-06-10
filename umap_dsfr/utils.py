from pathlib import Path


def each_file_from(source_dir, pattern="*", exclude=None):
    """Walk across the `source_dir` and return the `pattern` file paths."""
    for path in _each_path_from(source_dir, pattern=pattern, exclude=exclude):
        if path.is_file():
            yield path


def _each_path_from(source_dir, pattern="*", exclude=None):
    for path in sorted(Path(source_dir).glob(pattern)):
        if exclude is not None and path.name in exclude:
            continue
        yield path
