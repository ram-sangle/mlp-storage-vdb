"""SystemYamlSchemaCheck — Phase 2 D-A1.

Skeleton landed by Plan 02-01 so Plan 02-02 can flesh out the
``schema_validate_all_system_yamls`` method without re-defining
``SCHEMA_ERROR_RULE_MAP``.

Per D-A2, the map covers the four locked field paths plus a default fallback
to (``"2.1.7"``, ``"systemsDirectoryFiles"``) handled by the consumer via
``.get(loc, default)``.

Architecture: mirrors Phase 1's ``SubmissionStructureCheck`` plug-in pattern
(D-02 of Phase 1) — instantiated once before the ``for logs in loader.load():``
loop in ``main.py``, returns bool, feeds the ``valid &= …`` accumulator without
aborting (QUAL-01). Plan 02-02 wires the instance into ``main.py`` and implements
the check method.

Plan 02-02 tasks:
  (a) Implement ``schema_validate_all_system_yamls`` and append to ``self.checks``.
  (b) Verify Pydantic ``err["loc"]`` string format for Capabilities.check_remap_time
      (Rule-13 cross-field validator) empirically and extend SCHEMA_ERROR_RULE_MAP.
  (c) Add ``from ..schema_validator import validate_file`` import.
  (d) Wire instance into ``main.py``.
"""

from .base import BaseCheck
from ..configuration.configuration import Config


class SystemYamlSchemaCheck(BaseCheck):
    """Top-level check that schema-validates every ``systems/<name>.yaml``.

    Runs once before the per-benchmark loader loop (mirrors Phase 1's
    ``SubmissionStructureCheck`` plug-in pattern; D-A1).

    Plan 02-01 ships the skeleton (constructor + rule map). Plan 02-02
    adds ``schema_validate_all_system_yamls()`` and wires the instance
    into ``main.py``.
    """

    SCHEMA_ERROR_RULE_MAP: dict[str, tuple[str, str]] = {
        # D-A2: locked field paths → (rule_id, rule_name) for violation tagging.
        # Fallback for unmapped paths: ("2.1.7", "systemsDirectoryFiles").
        "system_under_test -> solution -> capabilities -> remap_time_in_seconds":
            ("4.7.3", "checkpointRemappingTimeReporting"),
        "system_under_test -> solution -> capabilities -> simultaneous_write":
            ("4.7.4", "checkpointSimultaneousRwSupport"),
        "system_under_test -> solution -> capabilities -> simultaneous_read":
            ("4.7.4", "checkpointSimultaneousRwSupport"),
        "system_under_test -> solution -> capabilities -> multi_host":
            ("4.7.4", "checkpointSimultaneousRwSupport"),
        # Plan 02-02 empirically verifies the Pydantic loc string for
        # Capabilities.check_remap_time (Rule-13 cross-field) and adds
        # that entry; fallback path is ("2.1.7", "systemsDirectoryFiles").
    }

    def __init__(self, log, config: Config, root_path: str):
        """Initialize SystemYamlSchemaCheck.

        Args:
            log: Logger instance (same as other check classes).
            config: Config instance (for version and submitter info).
            root_path: Root of the submission tree — e.g. ``args.input``.
        """
        super().__init__(log=log, path=root_path)
        self.config = config
        self.root_path = root_path
        self.name = "system YAML schema checks"
        self.init_checks()

    def init_checks(self):
        """Register check methods.

        Plan 02-02 appends ``self.schema_validate_all_system_yamls`` here.
        """
        # Plan 02-02 implements schema_validate_all_system_yamls and adds it here.
        self.checks = []
