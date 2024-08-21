from ec2_dev_machine.core import DevMachine

if __name__ == "__main__":

    config_file = "config.yaml"
    dev_machine = DevMachine(config_file)
    dev_machine.synth()
