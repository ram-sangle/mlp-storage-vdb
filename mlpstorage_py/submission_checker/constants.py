from .parsers.json_parser import JSONParser
from .parsers.yaml_parser import YamlParser

VERSIONS = ["v2.0", "v3.0"]
VALID_DIVISIONS = ["open", "closed"]

SYSTEM_PATH = {
    "v2.0": "{division}/{submitter}/systems/{system}.yaml",
    "v3.0": "{division}/{submitter}/systems/{system}.yaml",
    "default": "{division}/{submitter}/systems/{system}.yaml",
}

PARSER_MAP = {
    "System": YamlParser,
    "Summary": JSONParser,
    "Metadata": JSONParser,
    "default": JSONParser
}

DATAGEN_REQUIRED_FILES = {
    "v2.0": [r"training_datagen\.stdout.log", r"training_datagen.stderr\.log", r".*output\.json$", r".*per_epoch_stats\.json$", r".*summary\.json$", r"dlio\.log"],
    "v3.0": [r"training_datagen\.stdout.log", r"training_datagen.stderr\.log", r".*output\.json$", r".*per_epoch_stats\.json$", r",*summary\.json$", r"dlio\.log"],
    "default": [r"training_datagen\.stdout.log", r"training_datagen.stderr\.log", r".*output\.json$", r".*per_epoch_stats\.json$", r".*summary\.json$", r"dlio\.log"],
}

DATAGEN_REQUIRED_FOLDERS = {
    "v2.0": ["dlio_config"],
    "v3.0": ["dlio_config"],
    "default": ["dlio_config"],
}

RUN_REQUIRED_FILES = {
    "v2.0": [r"training_run\.stdout.log", r"training_run\.stderr.log", r".*output\.json", r".*per_epoch_stats\.json", r".*summary\.json", r"dlio\.log"],
    "v3.0": [r"training_run\.stdout.log", r"training_run\.stderr.log", r".*output\.json", r".*per_epoch_stats\.json", r".*summary\.json", r"dlio\.log"],
    "default": [r"training_run\.stdout.log", r"training_run\.stderr.log", r".*output\.json", r".*per_epoch_stats\.json", r".*summary\.json", r"dlio\.log"],
}

RUN_REQUIRED_FOLDERS = {
    "v2.0": ["dlio_config"],
    "v3.0": ["dlio_config"],
    "default": ["dlio_config"],
}

CHECKPOINT_REQUIRED_FILES = {
    "v2.0": [r"training_run\.stdout.log", r"training_run\.stderr.log", r".*output\.json", r".*per_epoch_stats\.json", r".*summary\.json", r"dlio\.log"],
    "v3.0": [r"training_run\.stdout.log", r"training_run\.stderr.log", r".*output\.json", r".*per_epoch_stats\.json", r".*summary\.json", r"dlio\.log"],
    "default": [r"training_run\.stdout.log", r"training_run\.stderr.log", r".*output\.json", r".*per_epoch_stats\.json", r".*summary\.json", r"dlio\.log"],
}

CHECKPOINT_REQUIRED_FOLDERS = {
    "v2.0": ["dlio_config"],
    "v3.0": ["dlio_config"],
    "default": ["dlio_config"],
}

# TODO: Ask for correct values
NUM_DATASET_TRAIN_FILES = {
    "cosmoflow": 524288,
    "resnet50": 10391,
    "unet3d": 14000
}

NUM_DATASET_EVAL_FILES = {
    "cosmoflow": 0,
    "resnet50": 0,
    "unet3d": 0
}

NUM_DATASET_TRAIN_FOLDERS = {
    "cosmoflow": 0,
    "resnet50": 0,
    "unet3d": 0
}

NUM_DATASET_EVAL_FOLDERS = {
    "cosmoflow": 0,
    "resnet50": 0,
    "unet3d": 0
}

CHECKPOINT_FILE_MAP = {
    "llama3-1t": "llama3_1t.yaml",
    "llama3-8b": "llama3_8b.yaml",
    "llama3-70b": "llama3_70b.yaml",
    "llama3-405b": "llama3_405b.yaml",
}

# Rules.md 2.1.6 / 3.6.1 codeDirectoryContents / trainingClosedSubmissionChecksum
# Reference hex MD5 of the canonical code/ tree per version. None means
# "not yet pinned" — runtime check will emit a WARNING via warn_violation
# (D-12) and pass. Use `python -m mlpstorage_py.submission_checker.tools.\
# compute_code_checksum <path>` to regenerate.
REFERENCE_CHECKSUMS: dict[str, str | None] = {
    "v2.0": None,
    "v3.0": None,
    "default": None,
}

# Rules.md 2.1.17 runTimestamps — exactly 6 (1 warm-up + 5 measured)
RUN_TIMESTAMP_COUNT = 6

# Directory-name prefixes excluded from the code-tree MD5 (Rules.md 2.1.6).
# Match is against POSIX-joined relative paths with a trailing slash so that
# `.gitignore` (file) does not collide with `.git/` (directory prefix).
MD5_EXCLUDE_PREFIXES: tuple[str, ...] = (
    ".git/",
    "__pycache__/",
    ".pytest_cache/",
    ".venv/",
    "node_modules/",
    "build/",
    "dist/",
    ".tox/",
)

# Filename patterns excluded from the code-tree MD5 (Rules.md 2.1.6).
# Matched against the basename. ``.egg-info`` is handled at the prefix level
# (any directory ending in ``.egg-info``) — keep that in the predicate, not here.
MD5_EXCLUDE_FILENAMES: tuple[str, ...] = (
    "*.pyc",
    "*.pyo",
    ".DS_Store",
    "Thumbs.db",
)