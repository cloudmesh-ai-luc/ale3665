# Alessandra Vellucci
# ale3665

*  Accounts: [ale3665](https://piazza.com/class/mt5rkdsycb31c3/post/18)

Note:
*  put files in `<repor>/assignments/week3/`
*  Update all YOURREPO

## Week 4 Tasks (Due Sep 24, 2026, 9am)

### Assignment W4.1: VM on Local Machine via Makefile

- [x] Pick a local VM framework and ensure it is installed.
  - Selected Oracle VirtualBox on Windows 11.
  - Used the existing `Ubuntu-VM` instance.
  - Managed VirtualBox from WSL2 using `VBoxManage.exe`.

- [x] Write a Makefile with all necessary targets to manage a single VM.
  - Created `assignments/week4/local/Makefile`.
  - Implemented targets for listing, starting, stopping, pausing, resuming, resetting, and inspecting virtual machines.
  - Successfully tested `make help`, `make list`, `make status`, `make start`, and `make running`.

- [x] Configure/determine how to manage multiple machines.
  - Implemented a configurable `VM` variable.
  - Example: `make status VM=Another-VM`.

- [x] Organize different Makefiles for different local and cloud environments using directories.
  - Organized the assignments into separate directories:
    - `assignments/week4/local/`
    - `assignments/week4/jetstream/`
    - `assignments/week4/chameleon/`
    - `assignments/week4/python/`

**Documentation:** [Local VM Makefile](assignments/week4/local/Makefile)

### Assignment W4.2: VM on Jetstream2

- [x] Install the OpenStack command-line client.
  - Installed `python-openstackclient` using pipx.
  - Configured authentication using OpenStack application credentials.
  - Verified connectivity using OpenStack CLI commands.

- [x] Write a Makefile with all necessary targets to manage a single VM.
  - Created `assignments/week4/jetstream/Makefile`.
  - Implemented VM lifecycle management, status inspection, and floating-IP management.
  - Added safeguards against accidental deletion of the semester VM.

- [x] Configure/determine how to manage multiple machines.
  - Implemented configurable VM names using the `VM` variable.
  - Verified the existing Jetstream2 virtual machine.
  - Used Ubuntu 24.04, the `m3.tiny` flavor, and SSH authentication.

- [x] Check your work into your repository.
  - Committed the Jetstream2 Makefile and supporting files.
  - Verified the files are available on the GitHub `main` branch.

**Documentation:** [Jetstream2 Makefile](assignments/week4/jetstream/Makefile)

### Assignment W4.3: VM on Chameleon Cloud

- [x] Install the OpenStack command-line client.
  - Used the existing OpenStack CLI installation.
  - Installed the Chameleon reservation plugin.
  - Configured Chameleon authentication through OpenStack application credentials.

- [x] Install python-chi.
  - Created a dedicated Python virtual environment using `venv`.
  - Installed `python-chi` using pip.
  - Verified the installation through a successful Python import.

- [x] Write a Makefile with all necessary targets to manage a single VM.
  - Created `assignments/week4/chameleon/Makefile`.
  - Implemented reservation management, VM lifecycle operations, information retrieval, and floating-IP management.
  - Validated non-destructive commands to avoid unnecessary cloud resource consumption.

- [x] Configure/determine how to manage multiple machines.
  - Implemented configurable VM names.
  - Configured Ubuntu 24.04, the `m1.small` flavor, SSH keys, networking, and security groups.
  - Included resource reservation and lease-management support.

- [x] Check your work into your repository.
  - Committed the Chameleon Cloud Makefile and supporting files.
  - Verified the files are available on the GitHub `main` branch.

**Documentation:** [Chameleon Makefile](assignments/week4/chameleon/Makefile)

### Assignment W4.4: Review Python

- [x] Set up a Python virtual environment using venv or pyenv.
  - Created a dedicated Python virtual environment using `python3 -m venv`.
  - Used `venv` instead of Conda or Miniconda.

- [x] Ensure the OpenStack command-line tool is installed via pipx.
  - Installed `python-openstackclient` using pipx.

- [x] Review using pip install and pipx install.
  - Used pip for Python project dependencies.
  - Used pipx for standalone command-line applications.

- [x] Review import statements and os.system.
  - Created a Python program demonstrating `os.system()` and shell command execution.

- [x] Review how to create a `__main__` block.
  - Implemented the `if __name__ == "__main__":` entry-point pattern.

- [x] Review how to write a function.
  - Defined and executed reusable Python functions.

- [x] Review how to pass command-line arguments using click.
  - Implemented a Click-based command-line interface.
  - Tested argument passing and command options.

- [x] Review how to run shell commands from Python using os.system() and subprocess.run().
  - Implemented and successfully tested both approaches.

- [x] Did the assignment take more than 3 hours?
  - [x] Yes
  - [ ] No
  - The Python review and environment setup required more than three hours.

**Documentation:** [Python Review](assignments/week4/python/review.py)

**Week 4 README:** [Week 4 Documentation](assignments/week4/README.md)

---

## Week 3 Tasks (Due Sep 17, 2026, 9am)

### Assignment W3.1: VM on Jetstream2

- [x] Start a VM on Jetstream and follow the tutorial provided.
  - Created a Jetstream2 virtual machine using OpenStack Horizon.
  - Selected an Ubuntu 24.04 image.
  - Configured SSH authentication, networking, and a floating IP address.
  - Successfully connected to the virtual machine using SSH.
  - Verified the operating system with Linux terminal commands.

- [ ] Improve the tutorial while creating pull requests in the lecture notes if issues are identified.
  - No lecture-notes improvement pull request has been confirmed.

- [x] Document activity with a screenshot of the terminal.
  - Uploaded `jetstream.png`.
  - Terminal screenshot is included in the repository.

- [x] Provide VM documentation.
  - [Jetstream2 VM Documentation](assignments/week3/vms.md)
  - [Jetstream2 Screenshot](assignments/week3/jetstream.png)

### Assignment W3.2: VM on Chameleon Cloud

- [x] Set your preferred time zone in Chameleon settings.
  - Configured the preferred time zone in the Chameleon Cloud portal.

- [x] Make sure you have an SSH key in your laptop's `.ssh` directory and upload the public key to Chameleon.
  - Configured SSH public-key authentication.
  - Used the configured key pair for remote access.

- [x] Explore the Chameleon portal and develop a plan.
  - Explored the KVM@TACC environment.
  - Reviewed available VM images, compute flavors, networking, and reservation options.

- [x] Make a reservation not exceeding 1 hour.
  - Created a one-hour reservation using the `m1.small` flavor.
  - Configured the required compute resources before launching the VM.

- [x] Start a VM using a Chameleon Ubuntu 24.04 image with the smallest suitable image size.
  - Created `avellucci-chameleon-vm`.
  - Used the `CC-Ubuntu24.04` image and `m1.small` flavor.
  - Configured SSH access, networking, security groups, and a floating IP.
  - Successfully connected to the virtual machine.

- [x] Document activity with a screenshot of the terminal.
  - Uploaded `chameleon.png`.
  - Terminal screenshot is included in the repository.

- [x] Provide VM documentation.
  - [Chameleon VM Documentation](assignments/week3/vms.md)
  - [Chameleon Screenshot](assignments/week3/chameleon.png)

### Assignment W3.3: OPTIONAL — VM on Public Cloud

- [x] Create a VM on a public cloud using a Free Tier eligible configuration.
  - Selected Amazon Web Services (AWS).
  - Created an Amazon EC2 instance running Ubuntu Server 24.04 LTS.
  - Selected the `t3.micro` instance type.
  - Configured SSH access, a security group, and a public IP address.
  - Successfully connected to the instance through SSH.
  - Verified the operating system using Linux terminal commands.

- [x] Document VM creation with screenshots.
  - Uploaded `aws-terminal.png`.
  - Documented the virtual machine configuration and terminal verification.

- [x] Provide VM documentation.
  - [AWS EC2 VM Documentation](assignments/week3/vms.md)
  - [AWS Terminal Screenshot](assignments/week3/aws-terminal.png)

### Assignment W3.4: Compare

- [x] Compare the experience of starting a VM locally versus using Chameleon Cloud.
  - Compared local Oracle VirtualBox with Chameleon Cloud.
  - Evaluated VM configuration, resource allocation, networking, SSH access, and reservation requirements.
  - Extended the comparison to Jetstream2 and AWS EC2.

**Comparison Summary:**

| Platform | Advantages | Limitations |
|----------|------------|-------------|
| VirtualBox | Complete control over local VM configuration | Consumes local CPU, RAM, and storage |
| Jetstream2 | Preconfigured Ubuntu images, OpenStack support, remote access | Requires cloud authentication and network configuration |
| Chameleon Cloud | Research-oriented infrastructure with reservations | Requires advance resource planning and lease management |
| AWS EC2 | Integrated deployment and flexible cloud infrastructure | Requires monitoring of resource usage and potential charges |

**Conclusion:**

VirtualBox provides direct control over virtual hardware and operating-system installation. Jetstream2 simplifies VM deployment through preconfigured images and OpenStack services. Chameleon Cloud introduces explicit resource reservations and additional planning requirements. AWS EC2 offers a streamlined public-cloud deployment process but requires careful monitoring of resource consumption and potential charges.

All four platforms successfully supported Ubuntu-based virtual machines, demonstrating different approaches to virtualization, cloud infrastructure management, and remote access.

- [x] Put all assignment answers into the repository documentation.
  - Week 3 and Week 4 assignment checklists are maintained in the main `README.md`.
  - Detailed Week 3 VM documentation is available in `assignments/week3/vms.md`.

- [x] Provide VM documentation.
  - [Week 3 VM Documentation](assignments/week3/vms.md)

### Assignment W3.5: README.md

- [x] Include assignment documentation in the main README.md.
  - Maintained one central `README.md` containing the weekly assignments.
  - Included Week 3 and Week 4 tasks, completion checklists, descriptions, and documentation links.
  - Organized supporting files in their respective assignment directories.

**Repository:** [ale3665](https://github.com/cloudmesh-ai-luc/ale3665)

**Main README:** [README.md](https://github.com/cloudmesh-ai-luc/ale3665/blob/main/README.md)

**Week 3 Documentation:** [vms.md](assignments/week3/vms.md)

**Week 4 Documentation:** [README.md](assignments/week4/README.md)

### Assignment W3.6: Git from Command Line

- [x] Work with a fork using GitHub.
  - Verified existing forked repositories under the GitHub account.

- [x] Practice `git clone`.
  - Practiced cloning and accessing Git repositories using the command line.

- [x] Practice `git commit -a`.
  - Practiced committing changes to tracked files.

- [x] Practice `git commit -m`.
  - Created Git commits with descriptive messages.

- [x] Practice `git push`.
  - Pushed repository changes to GitHub.

- [x] Practice `git pull`.
  - Successfully executed `git pull origin main`.
  - Verified that the remote branch was already up to date.

- [x] Create a pull request using GitHub.
  - Completed the pull-request exercise.

- [x] Accept or merge a pull request.
  - Completed the pull-request workflow.

- [x] Configure Git username and email.
  - Verified Git username and email configuration.

- [x] Document Git command-line operations.
  - Verified Git version 2.43.0.
  - Verified the repository's remote configuration.
  - Reviewed commit history using `git log`.
  - Verified branch management using `git branch`.
  - Captured and uploaded terminal evidence.

**Documentation:**
- Repository: `cloudmesh-ai-luc/ale3665`
- Environment: WSL2 Ubuntu
- Git version: 2.43.0
- Verified Git commands, repository configuration, commits, and synchronization.

**Screenshot:** [Week 3 Assignment 3.6 — Git Command Line](assignments/week3/week3_assignment_3.6.png)

**Pull Request:** Completed; add the PR URL if required by the professor.



## Week 2
  
* [x] Assignment W2.1: Google Account, Piazza Account post cleanup (Due Sep 10, 2026, 9am)
  * [x] Locate your account post in Piazza and add your google account.
  * [x] Correct your Chameleon ID to the registered email.
  * [x] Fix your subject line to `Firstname Lastname (lucid@luc.edu)`.


* [x] Assignment W2.2: GitHub Repository (Due Sep 10, 2026, 9am)
  * [x] Verify that you can write into a file in your assigned GitHub repository.
  * [x] Put something useful into the README such as your first and last name. [LINK]
  * [x] Upload your public key. [LINK]


* [x] Assignment W2.3: Backup Your Computer (Due Sep 10, 2026, 9am)
  * [x] Write a one‑paragraph explanation (4–6 sentences) on why backing up a computer is important. 
  * [x] List three real‑world consequences of not having a backup.
  * [x] Choose one backup method and outline the setup steps.
  * [x] Create a weekly backup schedule (day, time, what to back up).
  * [x] Research an example from cloud computing where a missing backup strategy led to issues and write a short incident case.
  * [x] Submit to `/assignments/week2/backup.md`. [LINK]


* [x] Assignment W2.4: Local VM (Due Sep 10, 2026, 9am)
  * [x] Windows: Install a terminal on Windows (Git Bash/WSL). [Which OS do you have?] Windows, both work
  * [x] Pick a hypervisor (VirtualBox, VMware, Hyper-V, Multipass). [Which?] virtualBox
  * [x] Create and start a minimal VM (e.g., Ubuntu 22.04).
  * [x] Capture proof of login with a terminal screenshot (≤ 800×600 px) showing your prompt and a command.
  * [x] Write/update the tutorial in `assignments/week1/local-vm.md` and save the screenshot as `assignments/week1/vm-login.png`. [LINK/s]
The proof of successful login can be viewed here:
[View the VM login screenshot](assignments/week1/vm-login.png)


* [x] Assignment W2.5: Project proposal (Due Sep 10, 2026, 9am)
  * [x] Start working towards a project proposal and fill out administrative fields and text. [LINK]


# Week 1

  * [x] Assignment W1.1: What hardware do you have? (Past Due) [LINK]
  * [x] Fill out the LUC Hardware Questionnaire.


* [x] Assignment W1.2: Lecture review (Past Due)
  * [x] Review all sections under LECTURES -> INTRODUCTIONS and post questions on Piazza.


* [x] Assignment W1.3: Look over the assignment sections (Past Due)
  * [x] Review all sections under ASSIGNMENTS (Overview and weekly sections).


* [x] Assignment W1.4: Create class accounts (Past Due)
  * [x] Create an account on access-ci.org.
  * [x] Create an account on chameleoncloud.org.
  * [x] Set up a GitHub account.
  * [x] Post account information to Piazza under the accounts category. [LINK]


* [x] Assignment W1.5: Work ahead: Refresh knowledge about Python and Linux (Past Due)
  * [x] Review optional material in the class documentation.


* [x] Assignment W1.6: Improve the Web Site (Past Due)
  * [x] Update errors or notify instructors throughout the semester.

