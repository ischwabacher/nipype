# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.freesurfer.preprocess import ParseDICOMDir

def test_ParseDICOMDir_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    dicom_dir=dict(argstr='--d %s',
    mandatory=True,
    ),
    dicom_info_file=dict(argstr='--o %s',
    usedefault=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    sortbyrun=dict(argstr='--sortbyrun',
    ),
    subjects_dir=dict(),
    summarize=dict(argstr='--summarize',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    )
    inputs = ParseDICOMDir.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_ParseDICOMDir_outputs():
    output_map = dict(dicom_info_file=dict(),
    )
    outputs = ParseDICOMDir.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

