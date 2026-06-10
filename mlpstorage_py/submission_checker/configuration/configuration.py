from ..constants import *

class Config:
    def __init__(self, version, submitters, skip_output_file=False, reference_checksum_override=None):
        self.version = version
        self.submitters = submitters
        self.skip_output_file = skip_output_file
        self.reference_checksum_override = reference_checksum_override
        
    def check_submitter(self, submitter):
        if self.submitters is None:
            return True
        return submitter in self.submitters
    
    def get_datagen_required_files(self):
        return DATAGEN_REQUIRED_FILES[self.version]
    
    def get_run_required_files(self):
        return RUN_REQUIRED_FILES[self.version]
    
    def get_checkpoint_required_files(self):
        return CHECKPOINT_REQUIRED_FILES[self.version]
    
    def get_datagen_required_folders(self):
        return DATAGEN_REQUIRED_FOLDERS[self.version]
    
    def get_run_required_folders(self):
        return RUN_REQUIRED_FOLDERS[self.version]
    
    def get_checkpoint_required_folders(self):
        return CHECKPOINT_REQUIRED_FOLDERS[self.version]
    
    def get_num_train_files(self, model):
        return NUM_DATASET_TRAIN_FILES[model]
    
    def get_num_eval_files(self, model):
        return NUM_DATASET_EVAL_FILES[model]
    
    def get_checkpoint_file(self, model):
        return CHECKPOINT_FILE_MAP[model]

    def get_reference_checksum(self, cli_override=None):
        """Resolve the reference MD5 for the current version.

        Precedence: cli_override > self.reference_checksum_override >
        REFERENCE_CHECKSUMS[self.version] > None.

        ``None`` means "not pinned" — the caller emits a warning via
        ``warn_violation`` and treats the check as passing (D-12).

        Args:
            cli_override: Optional hex MD5 string passed from the CLI
                ``--reference-checksum`` flag. Takes highest precedence.

        Returns:
            str | None: The resolved reference checksum, or None if not pinned.
        """
        if cli_override is not None:
            return cli_override
        if self.reference_checksum_override is not None:
            return self.reference_checksum_override
        return REFERENCE_CHECKSUMS.get(self.version)