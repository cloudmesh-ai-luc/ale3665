VBOX := "/mnt/c/Program Files/Oracle/VirtualBox/VBoxManage.exe"
VM ?= Ubuntu-VM

.PHONY: help list running start gui stop poweroff pause resume reset status info

help:
	@echo "VirtualBox VM Management"
	@echo ""
	@echo "Available targets:"
	@echo "  make list                 List all registered VMs"
	@echo "  make running              List currently running VMs"
	@echo "  make start                Start the VM in headless mode"
	@echo "  make gui                  Start the VM with the VirtualBox GUI"
	@echo "  make stop                 Request a graceful shutdown"
	@echo "  make poweroff             Force the VM to power off"
	@echo "  make pause                Pause the VM"
	@echo "  make resume               Resume the VM"
	@echo "  make reset                Reset the VM"
	@echo "  make status               Display the current VM state"
	@echo "  make info                 Display detailed VM information"
	@echo ""
	@echo "Default VM: $(VM)"
	@echo "Another VM can be selected with VM=<name>"
	@echo "Example: make status VM=Test-VM"

list:
	$(VBOX) list vms

running:
	$(VBOX) list runningvms

start:
	$(VBOX) startvm "$(VM)" --type headless

gui:
	$(VBOX) startvm "$(VM)" --type gui

stop:
	$(VBOX) controlvm "$(VM)" acpipowerbutton

poweroff:
	$(VBOX) controlvm "$(VM)" poweroff

pause:
	$(VBOX) controlvm "$(VM)" pause

resume:
	$(VBOX) controlvm "$(VM)" resume

reset:
	$(VBOX) controlvm "$(VM)" reset

status:
	@$(VBOX) showvminfo "$(VM)" --machinereadable | grep '^VMState='

info:
	$(VBOX) showvminfo "$(VM)"
