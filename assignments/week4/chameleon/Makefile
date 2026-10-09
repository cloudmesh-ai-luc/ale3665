VM ?= avellucci_chameleon_week4
LEASE ?= avellucci_week4
IMAGE ?= CC-Ubuntu24.04
FLAVOR_ID ?= 2
KEY ?= avellucci_ssh
NETWORK ?= sharednet1
SECURITY_GROUP ?= avellucci-ssh
PUBLIC_NETWORK ?= public

.PHONY: help list status start stop reboot create delete \
        flavors images networks keys security-groups ips \
        lease-list lease-show lease-create lease-delete \
        associate disassociate

help:
	@echo "Chameleon Cloud VM Management"
	@echo ""
	@echo "VM targets:"
	@echo "  make list                  List VMs"
	@echo "  make status                Show VM details"
	@echo "  make start                 Start VM"
	@echo "  make stop                  Stop VM"
	@echo "  make reboot                Reboot VM"
	@echo "  make create                Create VM from reservation"
	@echo "  make delete                Delete VM"
	@echo ""
	@echo "Reservation targets:"
	@echo "  make lease-list            List leases"
	@echo "  make lease-show            Show lease details"
	@echo "  make lease-create          Reserve one m1.small VM"
	@echo "  make lease-delete          Delete lease"
	@echo ""
	@echo "Information targets:"
	@echo "  make flavors"
	@echo "  make images"
	@echo "  make networks"
	@echo "  make keys"
	@echo "  make security-groups"
	@echo "  make ips"
	@echo ""
	@echo "Floating IP targets:"
	@echo "  make associate FLOATING_IP=<address>"
	@echo "  make disassociate FLOATING_IP=<address>"
	@echo ""
	@echo "Examples:"
	@echo '  make lease-create START="2026-10-09 03:30" END="2026-10-09 04:30"'
	@echo "  make lease-show"
	@echo "  make create RESERVATION_ID=<reservation-id>"
	@echo "  make status VM=another-vm"

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
	@test -n "$(RESERVATION_ID)" || \
		(echo "ERROR: RESERVATION_ID is required."; \
		 echo "Run: make lease-show"; \
		 echo "Then: make create RESERVATION_ID=<reservation-id>"; exit 1)
	openstack server create \
		--flavor "reservation:$(RESERVATION_ID)" \
		--image "$(IMAGE)" \
		--key-name "$(KEY)" \
		--network "$(NETWORK)" \
		--security-group "$(SECURITY_GROUP)" \
		"$(VM)"

delete:
	openstack server delete "$(VM)"

lease-list:
	openstack reservation lease list

lease-show:
	openstack reservation lease show "$(LEASE)"

lease-create:
	@test -n "$(START)" || \
		(echo 'ERROR: START required. Example START="2026-10-09 03:30"'; exit 1)
	@test -n "$(END)" || \
		(echo 'ERROR: END required. Example END="2026-10-09 04:30"'; exit 1)
	openstack reservation lease create \
		--reservation "resource_type=flavor:instance,flavor_id=$(FLAVOR_ID),amount=1" \
		--start-date "$(START)" \
		--end-date "$(END)" \
		"$(LEASE)"

lease-delete:
	openstack reservation lease delete "$(LEASE)"

flavors:
	openstack flavor list

images:
	openstack image list --name "$(IMAGE)"

networks:
	openstack network list

keys:
	openstack keypair list

security-groups:
	openstack security group list

ips:
	openstack floating ip list

associate:
	@test -n "$(FLOATING_IP)" || \
		(echo "Usage: make associate FLOATING_IP=<address>"; exit 1)
	openstack server add floating ip "$(VM)" "$(FLOATING_IP)"

disassociate:
	@test -n "$(FLOATING_IP)" || \
		(echo "Usage: make disassociate FLOATING_IP=<address>"; exit 1)
	openstack server remove floating ip "$(VM)" "$(FLOATING_IP)"
