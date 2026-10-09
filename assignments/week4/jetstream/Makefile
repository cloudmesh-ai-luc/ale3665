VM ?= avellucci_vm01
IMAGE ?= Featured-Ubuntu24
FLAVOR ?= m3.tiny
KEY ?= avellucci_ssh
NETWORK ?= auto_allocated_network
SECURITY_GROUP ?= default
PUBLIC_NETWORK ?= public

# Protect the semester VM from accidental deletion
PROTECTED_VM := avellucci_vm01

.PHONY: help list status start stop reboot create delete \
        flavors images networks keys security-groups ips \
        floating-create associate disassociate

help:
	@echo "Jetstream2 VM Management"
	@echo ""
	@echo "Available targets:"
	@echo "  make list                  List all instances"
	@echo "  make status                Show VM information"
	@echo "  make start                 Start a VM"
	@echo "  make stop                  Stop a VM"
	@echo "  make reboot                Reboot a VM"
	@echo "  make create                Create a VM"
	@echo "  make delete                Delete a VM"
	@echo "  make flavors               List flavors"
	@echo "  make images                List images"
	@echo "  make networks              List networks"
	@echo "  make keys                  List SSH key pairs"
	@echo "  make security-groups       List security groups"
	@echo "  make ips                   List floating IPs"
	@echo "  make floating-create       Allocate a floating IP"
	@echo "  make associate             Associate a floating IP"
	@echo "  make disassociate          Remove a floating IP"
	@echo ""
	@echo "Default VM: $(VM)"
	@echo "Override with VM=<name>"
	@echo ""
	@echo "Examples:"
	@echo "  make status VM=test-vm"
	@echo "  make create VM=test-vm"
	@echo "  make associate VM=test-vm FLOATING_IP=149.x.x.x"

list:
	openstack server list

status:
	openstack server show "$(VM)"

start:
	openstack server start "$(VM)"

stop:
	openstack server stop "$(VM)"

reboot:
	openstack server reboot "$(VM)"

create:
	openstack server create \
		--image "$(IMAGE)" \
		--flavor "$(FLAVOR)" \
		--key-name "$(KEY)" \
		--network "$(NETWORK)" \
		--security-group "$(SECURITY_GROUP)" \
		"$(VM)"

delete:
	@if [ "$(VM)" = "$(PROTECTED_VM)" ]; then \
		echo "ERROR: $(VM) is the protected semester VM and will not be deleted."; \
		exit 1; \
	fi
	openstack server delete "$(VM)"

flavors:
	openstack flavor list

images:
	openstack image list

networks:
	openstack network list

keys:
	openstack keypair list

security-groups:
	openstack security group list

ips:
	openstack floating ip list

floating-create:
	openstack floating ip create "$(PUBLIC_NETWORK)"

associate:
	@test -n "$(FLOATING_IP)" || \
		(echo "Usage: make associate VM=<name> FLOATING_IP=<address>"; exit 1)
	openstack server add floating ip "$(VM)" "$(FLOATING_IP)"

disassociate:
	@test -n "$(FLOATING_IP)" || \
		(echo "Usage: make disassociate VM=<name> FLOATING_IP=<address>"; exit 1)
	openstack server remove floating ip "$(VM)" "$(FLOATING_IP)"
