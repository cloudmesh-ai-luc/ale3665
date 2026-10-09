# Week 4

## W4.1 VM on Local Machine via Makefile

Oracle VirtualBox was used as the local virtual machine framework. The existing `Ubuntu-VM` instance was managed from Ubuntu/WSL by calling the Windows `VBoxManage.exe` executable.

A Makefile was created in:

```text
assignments/week4/local/Makefile
```

The Makefile includes targets for listing registered and running VMs, starting a VM, starting it with the GUI, stopping it gracefully, forcing power off, pausing, resuming, resetting, displaying the VM state, and displaying detailed VM information.

The Makefile was tested successfully with commands including:

```bash
make help
make list
make status
make start
make running
```

The VM name is parameterized with the `VM` variable, so the same Makefile can manage multiple VirtualBox machines. For example:

```bash
make status VM=Another-VM
make start VM=Another-VM
```

Different environments are organized into separate directories so that provider-specific Makefiles and settings remain isolated:

```text
assignments/week4/
├── local/
├── jetstream/
├── chameleon/
└── python/
```

## W4.2 VM on Jetstream2

The OpenStack command-line client was installed with `pipx` as required:

```bash
pipx install python-openstackclient
```

Jetstream2 CLI access was configured using an application credential created through Horizon. The downloaded OpenRC file was stored outside the Git repository and sourced from a private configuration directory.

The CLI was verified using commands such as:

```bash
openstack server list
openstack image list --name Featured-Ubuntu24
openstack flavor list
openstack keypair list
openstack network list
openstack security group list
openstack floating ip list
```

The existing Jetstream2 VM was identified as `avellucci_vm01`. Its configuration used `Featured-Ubuntu24`, `m3.tiny`, `avellucci_ssh`, and `auto_allocated_network`.

A provider-specific Makefile was created in:

```text
assignments/week4/jetstream/Makefile
```

The Makefile includes VM lifecycle targets, information targets, floating-IP management, and protection against accidental deletion of the semester VM. Multiple machines can be managed by overriding the `VM` variable.

## W4.3 VM on Chameleon Cloud

The existing OpenStack CLI installation was extended with Chameleon's reservation plugin:

```bash
pipx inject python-openstackclient chameleon-blazarclient
```

A dedicated Python virtual environment was created and `python-chi` was installed:

```bash
python3 -m venv ~/.venvs/chameleon
source ~/.venvs/chameleon/bin/activate
pip install python-chi
```

The installation was verified with:

```bash
python -c "import chi; print('python-chi installed successfully')"
```

Chameleon CLI authentication was configured with a separate application credential and OpenRC file.

The Chameleon environment was inspected with:

```bash
openstack server list
openstack flavor list
openstack image list --name CC-Ubuntu24.04
openstack keypair list
openstack network list
openstack security group list
openstack floating ip list
openstack reservation lease list
```

The selected automation configuration was:

```text
Image:          CC-Ubuntu24.04
Flavor:         m1.small
Flavor ID:      2
Key pair:       avellucci_ssh
Network:        sharednet1
Public network: public
Security group: avellucci-ssh
```

A Makefile was created in:

```text
assignments/week4/chameleon/Makefile
```

The Makefile includes lease management, VM lifecycle targets, information targets, floating-IP handling, and multi-VM support. Non-destructive commands were used for validation so that unnecessary shared cloud resources were not consumed.

## W4.4 Python Review

A dedicated Python review environment was created with `venv`, and `click` was installed with `pip`.

A review program was created in:

```text
assignments/week4/python/review.py
```

The program demonstrates:

- virtual environments with `venv`
- package installation with `pip`
- `pipx`
- import statements
- functions
- the `if __name__ == "__main__":` entry-point pattern
- command-line arguments
- the `click` framework
- `os.system()`
- `subprocess.run()`

The program was tested with:

```bash
python review.py --help
python review.py greet --name Alessandra --repeat 2
python review.py os-system
python review.py subprocess
```

All review commands executed successfully.
