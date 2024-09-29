from aws_cdk import Aspects
from aws_cdk.assertions import Annotations, Match, Template
from cdk_nag import AwsSolutionsChecks

from ec2_dev_machine import DevMachine


def test_dev_machine_synthesizes(snapshot_json, temp_yaml_config):
    # Create test stack
    dev_machine = DevMachine(temp_yaml_config)
    test_stack = dev_machine.stack

    # Get Template
    template = Template.from_stack(test_stack)

    assert template.to_json() == snapshot_json()

    # Run cdk-nag
    Aspects.of(test_stack).add(AwsSolutionsChecks(verbose=True))

    nag_warnings = Annotations.from_stack(test_stack).find_warning("*", Match.string_like_regexp("AwsSolutions-.*"))
    assert nag_warnings == []

    nag_errors = Annotations.from_stack(test_stack).find_error("*", Match.string_like_regexp("AwsSolutions-.*"))
    assert nag_errors == []
