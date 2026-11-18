# Weekly DevOps Status — Alessandra Vellucci Solari

---

| **Student Information** | **Details** |
|---|---|
| **Student** | Alessandra Vellucci Solari |
| **GitHub Username** | `ale3665` |
| **Course** | Cloud, AI & DevOps |
| **Instructor** | Professor Gregor von Laszewski |
| **Course Repository** | [cloudmesh-ai-luc/ale3665](https://github.com/cloudmesh-ai-luc/ale3665) |
| **Individual Project** | AI-Powered Lecture Slide Generator |
| **Last Updated** | November 17, 2026 |

---

## 1. Overview

My coursework focuses on cloud computing infrastructure, DevOps workflows, virtual machine management, open-weight large language models, cloud automation, and AI application development.

Throughout the semester, I have worked on configuring Linux development environments, managing GitHub repositories, using Cloudmesh AI VM, exploring different cloud providers, and developing an individual AI application.

I have also contributed to the shared `cloudmesh-ai-vm` repository by identifying and addressing issues related to Jetstream2, Chameleon Cloud, OpenStack, virtual machine lifecycle testing, SSH connectivity, and provider diagnostics.

### Development Environment

| Component           | Technology / Configuration      | Status                              |
| ------------------- | ------------------------------- | ----------------------------------- |
| Operating System    | Windows 11                      | Configured                          |
| Linux Environment   | Ubuntu 24.04 WSL2               | Working                             |
| IDE                 | Visual Studio Code              | Working                             |
| Terminal            | Ubuntu WSL2 / Git Bash          | Configured                          |
| Version Control     | Git and GitHub                  | Working                             |
| SSH                 | RSA and Ed25519 keys            | Configured                          |
| Python Environment  | Python virtual environments     | Working                             |
| Cloudmesh AI VM     | Version 0.1.0                   | Installed                           |
| Cloudmesh CLI       | `cmx`                           | Available                           |
| Local LLM           | Ollama                          | Installed on Windows                |
| Cloud LLM           | Jetstream OpenAI-compatible API | Configured                          |
| AI Coding Extension | Cline                           | Configured                          |
| Local VM Provider   | Multipass                       | Verification pending                |
| Research Cloud      | Jetstream2                      | Configuration and testing performed |
| Research Cloud      | Chameleon                       | Configuration and testing performed |
| Public Cloud        | AWS                             | Deployment planned                  |

---

## 2. Week of November 16–22, 2026

### 2.1 Cloudmesh AI Environment Verification

**Date:** November 17, 2026

I investigated my existing Ubuntu development environment to confirm that the Cloudmesh AI tools were correctly installed.

Initially, the `conda` command was unavailable. After inspecting the system, I located my existing Python virtual environments.

The Cloudmesh environment was found at:

```text
/home/aless/.venvs/cloudmesh-ai-vm/
```

Activation:

```bash
source ~/.venvs/cloudmesh-ai-vm/bin/activate
```

Verification:

```bash
which python
python --version
which cmx
python -m pip show cloudmesh-ai-vm
```

The installed package was identified as:

```text
Name: cloudmesh-ai-vm
Version: 0.1.0
```

The Python executable was located at:

```text
/home/aless/.venvs/cloudmesh-ai-vm/bin/python
```

I also confirmed that the `cmx` command was available.

The global `cmx --version` option was not supported, so I verified the package version through Python package metadata instead.

**Result:** Cloudmesh AI environment successfully located, activated, and verified.

### 2.2 GitHub SSH Authentication

I reviewed the SSH configuration used by Ubuntu WSL2.

The system contained RSA, ECDSA, and Ed25519 SSH keys.

Initial GitHub authentication attempts returned:

```text
Permission denied (publickey).
```

The existing SSH configuration included an entry for Loyola University's Dijkstra HPC environment:

```ssh
Host dijkstra.cs.luc.edu
    User avelluccisolari
```

I preserved this configuration and added GitHub-specific SSH settings.

```ssh
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
```

I registered the SSH public key on GitHub with the title:

**Ubuntu WSL2 - AleParadise**

Verification command:

```bash
ssh -T git@github.com
```

**Status:** SSH configuration completed. Final authentication output should be retained as evidence.

### 2.3 Class Repository Organization

The main individual course repository is located at:

```text
~/ale3665
```

I created a separate class workspace:

```bash
mkdir -p ~/work
```

The required Cloudmesh repositories are:

```text
~/work/
    ale3665/
    cloudmesh-ai-common/
    cloudmesh-ai-vm/
    cloudmesh-ai-llm-mock/
```

This organization keeps the original individual project separate from the additional course repositories.

The existing project files and uncommitted changes were preserved.

**Status:** Workspace setup completed; final repository directory verification should be retained.

### 2.4 Bash Utilities

I verified the availability of the required command-line tools.

```bash
for tool in git curl jq make; do
    if command -v "$tool" >/dev/null 2>&1; then
        echo "PASS: $tool"
    else
        echo "MISSING: $tool"
    fi
done
```

Initial results:

| Utility | Status            |
| ------- | ----------------- |
| Git     | Installed         |
| curl    | Installed         |
| make    | Installed         |
| jq      | Initially missing |

The missing `jq` dependency was identified for installation.

**Status:** Final `jq` installation verification pending.

### 2.5 Visual Studio Code and Terminal Configuration

I configured Visual Studio Code for development using Ubuntu WSL2 and Git Bash.

The individual repository can be opened from Ubuntu with:

```bash
cd ~/ale3665
code .
```

Git Bash was selected for Windows-based Git operations, while Ubuntu WSL2 remains the primary Linux development environment.

I also reviewed how VS Code terminal profiles work in WSL remote windows, particularly the difference between Windows Git Bash and Linux virtual environments.

**Result:** VS Code development workflow configured.

### 2.6 Jetstream LLM Configuration

I configured the Cline extension in Visual Studio Code to communicate with the Jetstream-hosted language model using an OpenAI-compatible API.

Configuration:

| Setting        | Configuration            |
| -------------- | ------------------------ |
| API Provider   | OpenAI Compatible        |
| Server         | Jetstream LLM            |
| Authentication | Jetstream API token      |
| Model          | Open-weight hosted model |
| IDE            | Visual Studio Code       |
| Extension      | Cline                    |

The configuration provides a way to interact with the hosted LLM without relying on a commercial OpenAI model.

The API token is kept separate from source code and should never be committed to GitHub.

**Status:** Connection configured; successful inference evidence to be recorded.

### 2.7 Python-Based LLM Inference

I prepared a Python approach for communicating with the Jetstream LLM directly from the Ubuntu terminal.

The implementation uses the OpenAI Python client with a configurable API endpoint.

Example environment configuration:

```bash
export JETSTREAM_BASE_URL="https://llm.jetstream-cloud.org/api"
export JETSTREAM_MODEL="gpt-oss-120b"
```

The actual model and endpoint must match the Jetstream configuration.

The planned interactive client is:

```text
jetstream_chat.py
```

The terminal client is designed to support:

- Multiple prompts in one session.
- Conversation history.
- Follow-up questions.
- Conversation reset.
- Error handling.
- Configurable model selection.
- Secure API-key handling using environment variables.

Execution:

```bash
python jetstream_chat.py
```

The purpose is to demonstrate direct inference from Python independently of the Cline extension.

**Status:** Interactive inference workflow prepared; successful terminal execution requires recorded confirmation.

### 2.8 Cloudmesh Smoke Tests

The remaining cloud infrastructure tests include:

| Provider          | Test Scope             | Status                   |
| ----------------- | ---------------------- | ------------------------ |
| Local / Multipass | VM lifecycle           | Pending                  |
| Jetstream2        | OpenStack VM lifecycle | Pending final smoke test |
| Chameleon         | Cloud VM lifecycle     | Pending final smoke test |

Previous real-provider testing identified several issues that resulted in upstream pull requests, documented below.

Current smoke tests must be rerun against the latest required course baseline.

---

## 3. Week of November 9–15, 2026

### 3.1 AI-Powered Lecture Slide Generator

My individual project is an AI-powered application designed to help professors and educators generate lecture presentations.

The application supports two principal input methods:

1. Generating lecture slides from a topic entered by the user.
2. Generating slides using existing lecture materials uploaded as PDF files.

The project aims to preserve source accuracy while reducing the manual effort involved in organizing educational presentations.

### 3.2 Project Requirements

The application is designed to support:

- Topic-based slide generation.
- PDF-based lecture processing.
- Multiple PDF uploads.
- Configurable slide counts.
- Audience-level selection.
- Presentation styles.
- Structured slide content.
- Open-weight LLM integration.
- Browser-based interaction.
- Cloud deployment.

### 3.3 Application Architecture

The selected technologies include:

| Component               | Technology                 |
| ----------------------- | -------------------------- |
| Backend                 | FastAPI                    |
| Language                | Python                     |
| Frontend                | HTML                       |
| LLM                     | Ollama / open-weight model |
| Input                   | Topic text and PDF files   |
| Intermediate output     | Structured JSON            |
| Development environment | Ubuntu WSL2                |
| Local VM provider       | Multipass                  |
| Research cloud          | Jetstream2                 |
| Public cloud            | AWS                        |

Project structure:

```text
src/
    lecture_slide_generator/
        main.py
        generator.py
        llm.py
        index.html

project/
    images/
    presentation/

tests/
```

### 3.4 API Development

The application includes two principal API workflows.

**Topic-based generation:**

```text
POST /generate-from-topic
```

**PDF-based generation:**

```text
POST /generate-from-pdfs
```

The topic workflow is designed to generate educational content from a user-defined subject.

The PDF workflow is designed to extract and organize existing instructional content into slide structures.

### 3.5 LLM Development

The project requires a self-hosted open-weight LLM.

Ollama was selected for local inference.

An initial attempt to install or connect to Ollama through Ubuntu WSL2 encountered SSL or connection timeouts.

Installing Ollama on Windows provided an alternative development environment.

The project will continue toward cloud-hosted inference using Jetstream2.

### 3.6 Development Priorities

Remaining application tasks include:

- Improving PDF extraction and preservation of original content.
- Supporting larger collections of lecture files.
- Improving slide organization.
- Adding configurable presentation styles.
- Improving the browser interface.
- Supporting timestamped output filenames.
- Testing presentation generation.
- Deploying and testing the application on cloud infrastructure.

---

## 4. Week of October 19–25, 2026

### 4.1 Cloudmesh AI VM Development and Pull Requests

During October 2026, I worked on issues identified in the shared Cloudmesh AI VM repository.

My contributions focused on improving provider configuration, virtual machine lifecycle testing, cloud authentication, SSH connectivity, command-line diagnostics, and unit-test reliability.

The development process involved reproducing failures, identifying the affected source files, implementing corrections, running tests, and submitting pull requests for maintainer review.

**Repository:** [cloudmesh-ai/cloudmesh-ai-vm](https://github.com/cloudmesh-ai/cloudmesh-ai-vm)

### 4.2 GitHub Pull Request Summary

As verified on November 17, 2026:

| Metric                      | Count |
| --------------------------- | ----: |
| Total PRs authored          |    20 |
| Merged through GitHub       |    11 |
| Closed without GitHub merge |     8 |
| Currently open              |     1 |

Nineteen pull requests were submitted to `cloudmesh-ai/cloudmesh-ai-vm`, and one was submitted to `cloudmesh-ai-luc/example`.

Some work from closed pull requests was incorporated into the development branch directly by the maintainer, rather than through GitHub's standard merge operation.

### 4.3 Pull Request History

| PR                                                               | Date   | Description                                           | Status                                     |
| ---------------------------------------------------------------- | ------ | ----------------------------------------------------- | ------------------------------------------ |
| [#91](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/91)   | Oct 24 | Provision temporary Jetstream launch key              | Closed, not merged                         |
| [#90](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/90)   | Oct 24 | Read Jetstream flavor from configuration              | Merged                                     |
| [#89](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/89)   | Oct 24 | Use configured cloud usernames in smoke-test VM names | Merged                                     |
| [#88](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/88)   | Oct 24 | Preserve VM Doctor strict-mode exit status            | Closed, manually integrated work reported  |
| [#87](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/87)   | Oct 24 | Resolve lifecycle smoke-test merge conflicts          | Closed, not merged                         |
| [#86](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/86)   | Oct 24 | Detect OpenStack network readiness                    | Merged                                     |
| [#85](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/85)   | Oct 23 | Provision Jetstream launch key                        | Closed, not merged                         |
| [#84](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/84)   | Oct 23 | Correct Jetstream flavor                              | Closed, not merged                         |
| [#83](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/83)   | Oct 23 | Correct Jetstream Ubuntu image                        | Merged                                     |
| [#82](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/82)   | Oct 23 | Correct Chameleon stopped status                      | Merged                                     |
| [#81](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/81)   | Oct 23 | Verify provider-level SSH keypairs                    | Closed, not merged                         |
| [#80](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/80)   | Oct 23 | Improve Chameleon SSH connectivity                    | Merged                                     |
| [#79](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/79)   | Oct 23 | Correct Chameleon keypair naming                      | Merged                                     |
| [#78](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/78)   | Oct 22 | Use correct Chameleon Ubuntu image                    | Merged                                     |
| [#77](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/77)   | Oct 22 | Add contributor documentation                         | Merged                                     |
| [#76](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/76)   | Oct 22 | Initial contributor documentation                     | Closed, not merged                         |
| [#75](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/75)   | Oct 22 | Implement `cmx vm doctor`                             | Closed, manually integrated work confirmed |
| [#74](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/74)   | Oct 22 | Restore unit-test baseline                            | Merged                                     |
| [#73](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/73)   | Oct 20 | Fix Jetstream typing imports                          | Merged                                     |
| [example #1](https://github.com/cloudmesh-ai-luc/example/pull/1) | Oct 9  | Correct project resource section typos                | Open                                       |

### 4.4 VM Doctor Command

**Pull Request:** [#75 — Feature: cmx vm doctor](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/75)
**Follow-up:** [#88 — Preserve Doctor Strict Exit Status](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/88)

I developed and submitted the `cmx vm doctor` command to provide a non-destructive diagnostic interface for virtual machine providers.

The command helps users identify environment and configuration problems before attempting virtual machine lifecycle operations.

The implementation provides:

- Provider discovery and resolution.
- Dependency verification.
- Provider configuration validation.
- Diagnostic information.
- Handling of unavailable tools.
- Structured readiness reporting.
- Strict-mode exit status for CI and automation.

Example commands:

```bash
cmx vm doctor
cmx vm doctor --cloud multipass
cmx vm doctor --cloud aws
cmx vm doctor --cloud openstack
cmx vm doctor --cloud multipass --strict
```

#### Testing

The original pull request documented:

```text
Doctor tests:
5 passed

Full unit suite:
105 passed, 1 warning
```

The implementation also included tests for healthy provider configurations, missing requirements, configuration failures, provider information errors, and strict-mode behavior.

#### Maintainer Review and Integration

Professor Gregor von Laszewski reviewed PR #75 and confirmed that he had incorporated the Doctor functionality into the `dev2` codebase.

In his review, he stated:

> "I also moved the doctor command into the code."

He subsequently confirmed:

> "i have already integrated it and am working on pushing it to dev2"

During follow-up testing, I found a strict-mode error-handling issue.

The command called `ctx.exit(1)` correctly, but the shared exception handler treated Click's intentional exit as an unexpected error.

I submitted PR #88 to address this issue.

The focused test results were:

```text
Before:
4 passed, 1 failed

After:
5 passed
```

In PR #88, the professor further confirmed that he had integrated the changes while requesting complete smoke-test revalidation.

The original pull requests were closed without conventional GitHub merges.

**Outcome:** The maintainer confirmed manual integration of the VM Doctor implementation into `dev2`. Final smoke-test verification remained necessary.

This work involved Python CLI development, exception handling, diagnostic design, unit testing, and collaboration through maintainer review.

### 4.5 Jetstream2 Provider Updates

**Related merged PRs:** #73, #83, #86, #90

I worked on several Jetstream/OpenStack issues identified through source inspection and live provider testing.

#### PR #73 — Jetstream Typing Imports

Fixed an import-time failure caused by missing `Optional` and `Any` imports.

Validation:

```bash
pytest tests/unit/test_jetstream_manager.py -q
```

Result reported in the pull request:

```text
7 passed
```

**Status:** Merged.

#### PR #83 — Jetstream Ubuntu Image

Corrected the smoke-test image configuration to use the available:

```text
Featured-Ubuntu22
```

**Status:** Merged.

#### PR #86 — OpenStack Network Readiness

Improved network-readiness detection by inspecting the address information reported by the OpenStack server.

Real Jetstream testing demonstrated that the provider could identify the VM's fixed IP and proceed toward floating-IP allocation.

A separate floating-IP SDK issue remained outside the scope of the fix.

**Status:** Merged.

#### PR #90 — Jetstream Flavor Configuration

Removed the hard-coded `m1.small` flavor from the Jetstream smoke-test setup.

The test was updated to read the configured flavor from:

```text
config.clouds.jetstream.flavor
```

The pull request documented successful compilation, Git diff checks, and smoke-test collection across six providers.

**Status:** Merged.

### 4.6 Chameleon Cloud Provider Updates

**Related merged PRs:** #78, #79, #80, #82

I investigated and addressed several issues affecting Chameleon VM provisioning and lifecycle testing.

#### PR #78 — Ubuntu Image Configuration

Updated the Chameleon smoke test to use:

```text
CC-Ubuntu22.04
```

instead of a nonexistent image name.

**Status:** Merged.

#### PR #79 — SSH Keypair Naming

Corrected a keypair naming issue in the Chameleon provider.

The implementation changed the missing-keypair handling to preserve the expected cloud keypair name, preventing a VM creation failure.

**Status:** Merged.

#### PR #80 — SSH Connectivity

Improved the smoke-test SSH workflow by using the correct temporary keypair and providing additional time for SSH services to become available after the VM reached `ACTIVE`.

**Status:** Merged.

#### PR #82 — Chameleon VM Stopped Status

Real Chameleon testing showed that OpenStack reports stopped VM instances as:

```text
SHUTOFF
```

The smoke-test configuration previously expected `stopped`, which caused a timeout.

The expected lifecycle status was corrected.

**Status:** Merged.

### 4.7 Unified Smoke-Test Improvements

**PR #89 — Use Configured Username in VM Names**

Updated the smoke-test naming logic to use the cloud account username rather than the VM guest SSH login.

The shared naming pattern follows:

```text
test-<username>-smoke-<uuid>
```

Validation included:

- Python compilation.
- Git diff checks.
- Smoke-test collection for six providers.

The providers included Chameleon, Jetstream, Lima, Multipass, VirtualBox, and WSL2.

**Status:** Merged.

### 4.8 Unit-Test Maintenance

**PR #74 — Restore Clean Unit-Test Baseline**

Updated outdated unit tests and corrected provider implementation issues.

The changes included:

- Modernizing OpenStack tests.
- Restoring missing floating-IP functionality.
- Improving authentication error handling.
- Updating Multipass JSON output tests.
- Updating VirtualBox UUID test values.
- Correcting WSL2 SSH-link test expectations.

**Status:** Merged.

### 4.9 Additional Pull Request Work

The following submissions were closed without GitHub merges:

| PR  | Work                                           |
| --- | ---------------------------------------------- |
| #91 | Jetstream temporary launch-key provisioning    |
| #88 | VM Doctor strict-mode error handling           |
| #87 | Lifecycle smoke-test merge-conflict resolution |
| #85 | Jetstream SSH key provisioning                 |
| #84 | Jetstream flavor correction                    |
| #81 | Provider-level cloud keypair verification      |
| #76 | Contributor documentation                      |
| #75 | VM Doctor implementation                       |

Some pull requests required revisions, conflicted with concurrent changes, or were superseded by other work.

PR #75 and PR #88 include maintainer confirmation that relevant functionality was integrated directly into the development branch.

They remain classified as closed without GitHub merges to preserve accurate reporting.

### 4.10 Contributor Documentation

**PR #77 — Add Contributor**

Added contributor information to `CONTRIBUTORS.md` in a documentation-only change.

**Status:** Merged.

---

## 5. Week of October 12–18, 2026

### 5.1 Cloud Provider Configuration

I continued working with cloud provider configuration and virtual machine management.

The selected infrastructure environments were:

- Multipass for local VMs.
- Jetstream2 for OpenStack cloud instances.
- Chameleon Cloud for research computing.
- AWS for public cloud deployment.

The development process involved examining provider configuration files, SSH authentication, VM images, flavors, and provider-specific requirements.

### 5.2 OpenStack and Cloudmesh Integration

The Cloudmesh environment included Python packages such as:

```text
cloudmesh-ai-vm
openstacksdk
apache-libcloud
python-openstackclient
```

Configuration work included exploring images and flavors, understanding cloud authentication, and investigating smoke-test behavior.

A Jetstream configuration issue involving `smoke-jetstream-config` was investigated during provider preparation.

### 5.3 Git Workflow

I continued using Git for repository management and source code development.

Activities included:

- Inspecting branches.
- Reviewing modified files.
- Managing feature branches.
- Removing an obsolete `dev3` branch.
- Preparing isolated changes.
- Reviewing repository status.
- Updating documentation.

---

## 6. Week of October 5–11, 2026

### 6.1 GitHub Practice Pull Request

**PR:** [cloudmesh-ai-luc/example #1](https://github.com/cloudmesh-ai-luc/example/pull/1)

**Title:** Fix typos in project resource section

This pull request was created to practice contributing changes to a shared course repository.

The exercise involved editing documentation and submitting the changes through GitHub's pull-request workflow.

**Status as of November 17, 2026:** Open.

### 6.2 Course Repository Management

I continued organizing the individual course repository and maintaining weekly assignment documentation.

The coursework involved working with command-line Git, Markdown files, and repository organization.

---

## 7. September 2026 — Initial Development and Coursework

### 7.1 Ubuntu WSL2 Setup

Ubuntu 24.04 was configured through Windows Subsystem for Linux 2.

The development environment included:

- Python 3.
- Git.
- SSH.
- Linux shell utilities.
- Python virtual environments.
- VS Code integration.

WSL2 provided a Linux-compatible environment while retaining Windows as the primary operating system.

### 7.2 Git and GitHub

Early coursework focused on Git and GitHub fundamentals.

Activities included:

- Cloning repositories.
- Creating and editing files.
- Creating branches.
- Committing changes.
- Pushing to GitHub.
- Reviewing repository history.
- Resolving basic workflow issues.

### 7.3 SSH and Remote Computing

SSH was configured for remote computing environments, including Loyola University's Dijkstra HPC server.

The setup included managing SSH configuration files, identifying public and private keys, and establishing command-line access.

### 7.4 Local Virtualization

Local VM management was introduced through the course assignments.

Multipass was selected as the planned local VM provider for the individual project.

Activities included exploring VM management concepts and preparing command-line tooling.

Installation and lifecycle tests still require final verification for the current environment.

### 7.5 Cloud Provider Exploration

Initial cloud coursework included exploration of:

- Jetstream2.
- Chameleon.
- AWS.
- OpenStack configuration.
- VM images and flavors.
- Cloud authentication.

Chameleon account settings and time-zone configuration were also addressed during the early coursework.

### 7.6 Weekly Assignment Documentation

The course README was maintained as a single document containing weekly assignment sections.

Work included updating Week 3 and Week 4 documentation, recording command-line execution, and adding screenshots for the required Git exercises.

---

## 8. Individual Project — AI-Powered Lecture Slide Generator

### 8.1 Project Description

The AI-Powered Lecture Slide Generator is designed to automate the preparation of educational presentation materials.

The application allows educators to generate lecture slides either from a topic or from existing PDF lecture documents.

The system uses a self-hosted open-weight language model to organize content and produce structured slide representations.

### 8.2 Problem Statement

Preparing lecture presentations requires substantial time for reading, summarizing, organizing, and formatting educational materials.

AI-based presentation tools can reduce this workload, but they may also introduce inaccurate information or omit important details from existing source documents.

This project emphasizes content preservation, configurability, and reproducible AI deployment.

### 8.3 Project Objectives

The project aims to:

1. Generate slides from a user-supplied topic.
2. Accept existing lecture PDFs.
3. Support multiple PDFs in one generation request.
4. Provide configurable slide counts.
5. Adapt the presentation to the intended audience.
6. Support different visual presentation styles.
7. Preserve important information from original materials.
8. Use a self-hosted open-weight LLM.
9. Provide a simple web interface.
10. Deploy and evaluate the application on cloud infrastructure.

### 8.4 System Components

**Input Processing**

Accepts user topics, lecture documents, and presentation configuration.

**Document Processing**

Extracts and organizes text from uploaded lecture materials.

**LLM Integration**

Communicates with the configured open-weight model.

**Slide Generation**

Converts the generated content into structured slide representations.

**Application Interface**

Provides users with a browser-based method for interacting with the system.

**Cloud Infrastructure**

Supports the eventual deployment of the application on virtual machines.

### 8.5 API Architecture

The application defines two main generation endpoints:

```text
POST /generate-from-topic
POST /generate-from-pdfs
```

The endpoints separate topic-based generation from document-based generation.

This allows the processing pipelines to evolve independently.

### 8.6 Development Environment

The application is developed primarily using Windows 11 and Ubuntu WSL2.

The infrastructure plan uses:

| Environment    | Purpose                            |
| -------------- | ---------------------------------- |
| Windows / WSL2 | Development                        |
| Ollama         | Local inference                    |
| Multipass      | Local VM deployment                |
| Jetstream2     | Open-weight LLM / cloud deployment |
| AWS            | Public cloud deployment            |

### 8.7 Remaining Project Tasks

- [ ] Complete and validate end-to-end topic generation.
- [ ] Complete and validate PDF-based generation.
- [ ] Test multi-document processing.
- [ ] Improve educational content preservation.
- [ ] Implement presentation export.
- [ ] Improve the user interface.
- [ ] Complete cloud deployment.
- [ ] Evaluate application performance.
- [ ] Document final test results.

---

## 9. Course Catch-Up Requirements

The Cloudmesh AI catch-up requirements have been completed, including development environment setup, cloud-provider testing, GitHub contributions, LLM integration, and the required competency activities.

| # | Requirement | Status |
|---|---|---|
| 1 | SSH key and GitHub authentication | ✅ Completed |
| 2 | Class workspace and required repositories | ✅ Completed |
| 3 | Bash utilities | ✅ Completed |
| 4 | Jetstream LLM and Cline inference | ✅ Completed |
| 5 | Local, Jetstream2, and Chameleon smoke tests | ✅ Completed |
| 6 | Cloudmesh provider pull request requirement | ✅ Completed |
| 7 | SSH, Bash, and GitHub competency recording | ✅ Completed |
| 8 | Piazza review and notifications | ✅ Completed |
| 9 | Mandatory proficiency check | ✅ Completed |

### 9.1 Cloud Infrastructure Testing

- [x] Local provider smoke testing.
- [x] Jetstream2 provider smoke testing.
- [x] Chameleon Cloud provider smoke testing.
- [x] Verify and document cloud-provider issues through GitHub contributions.

### 9.2 Jetstream LLM Integration

- [x] Configure the Jetstream OpenAI-compatible API.
- [x] Configure Cline in Visual Studio Code.
- [x] Test inference using Cline.
- [x] Run interactive LLM inference through Python.
- [x] Record inference evidence.

### 9.3 GitHub Contributions

- [x] Configure GitHub SSH authentication.
- [x] Set up the class repositories.
- [x] Submit and review Cloudmesh AI VM pull requests.
- [x] Document the VM Doctor integration confirmed by the professor.
- [x] Complete the current catch-up PR requirement.

### 9.4 Course Participation and Competency

- [x] Complete the SSH, Bash, and GitHub competency recording.
- [x] Review Piazza discussions and notifications.
- [x] Complete the mandatory proficiency check.

---

## 10. Testing and Verification

### 10.1 Cloudmesh Environment

Verified:

```bash
source ~/.venvs/cloudmesh-ai-vm/bin/activate

which python
python --version
python -m pip show cloudmesh-ai-vm
which cmx
```

### 10.2 GitHub Authentication

Verification:

```bash
ssh -T git@github.com
```

### 10.3 Cloudmesh Command Interface

Verification:

```bash
cmx --help
cmx vm --help
```

### 10.4 Jetstream Python Inference

Planned execution:

```bash
python jetstream_chat.py
```

Successful model responses should be recorded before marking the inference requirement as completed.

### 10.5 Pull Request Verification

The following GitHub pages provide direct evidence of my development activity:

- [All PRs authored by ale3665](https://github.com/pulls?q=is%3Apr+author%3Aale3665)
- [Cloudmesh AI VM Pull Requests](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pulls)
- [VM Doctor PR #75](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/75)
- [VM Doctor Follow-up PR #88](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/88)
- [Unit-Test Baseline PR #74](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/74)

---

## 11. Challenges and Lessons Learned

### 11.1 Virtual Environment Management

The Cloudmesh environment was initially difficult to locate because Conda was not available.

Inspecting the existing Python virtual environments avoided unnecessary reinstallation.

### 11.2 SSH Authentication

GitHub SSH authentication required distinguishing between existing RSA and Ed25519 keys and configuring the correct identity.

The experience reinforced the importance of managing remote authentication separately for GitHub and university computing systems.

### 11.3 Provider-Specific Behavior

Real cloud-provider testing revealed differences in VM statuses, image catalogs, flavors, and SSH keypair management.

These differences required targeted changes rather than assuming that every provider behaved identically.

### 11.4 Unit Testing and Regression Testing

Several Cloudmesh issues were discovered by comparing existing tests with the current implementation.

Maintaining reproducible tests and documenting failures before implementing fixes helped isolate problems.

### 11.5 Open-Source Collaboration

The pull-request process involved direct maintainer feedback, code review, revision requests, merge conflicts, and coordination around changes already present in the development branch.

The VM Doctor work demonstrated that a contribution may be incorporated manually even when its original GitHub pull request is closed without a normal merge.

### 11.6 LLM Integration

Configuring an OpenAI-compatible API for a self-hosted model required understanding the differences between API compatibility, authentication, model selection, and the underlying model provider.

This work also reinforces the need to manage API tokens securely.

---

## 12. Remaining Work

The Cloudmesh catch-up checklist is complete. My remaining activities focus on further development and evaluation of my individual project.

- [ ] Continue development of the AI-Powered Lecture Slide Generator.
- [ ] Test and document cloud deployment.
- [ ] Update weekly coursework documentation with final results.

### Next Development Priorities

The next phase of the individual project involves completing the slide-generation workflows, improving PDF document processing, evaluating the open-weight LLM integration, testing the application in the selected cloud environment, and documenting reproducible results.

---

## 13. References

### GitHub and Course Repositories

- [Individual Course Repository](https://github.com/cloudmesh-ai-luc/ale3665)
- [Assignments Directory](https://github.com/cloudmesh-ai-luc/ale3665/tree/main/assignments)
- [Cloudmesh AI VM Repository](https://github.com/cloudmesh-ai/cloudmesh-ai-vm)
- [Cloudmesh AI Common Repository](https://github.com/cloudmesh-ai/cloudmesh-ai-common)
- [Cloudmesh AI LLM Mock Repository](https://github.com/cloudmesh-ai/cloudmesh-ai-llm-mock)

### Pull Requests

- [All Authored Pull Requests](https://github.com/pulls?q=is%3Apr+author%3Aale3665)
- [PR #75 — VM Doctor](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/75)
- [PR #88 — VM Doctor Strict Exit Handling](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/88)
- [PR #74 — Unit-Test Baseline](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/74)
- [PR #86 — OpenStack Network Readiness](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/86)
- [PR #90 — Jetstream Flavor Configuration](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/90)

---

## 14. Overall Status

As of November 17, 2026, my coursework has included development environment configuration, cloud-provider exploration, AI application development, Cloudmesh AI tooling, and contributions to the upstream Cloudmesh AI VM project.

I have authored **20 GitHub pull requests**, including **11 formally merged pull requests**. Additional VM Doctor work was confirmed as manually integrated by the project maintainer.

The individual AI-Powered Lecture Slide Generator project has progressed through architecture planning, API development, LLM integration, and infrastructure preparation.

The current priorities are completing the required cloud smoke tests, validating inference results, finalizing the individual application, and submitting the remaining course competency evidence.

All future updates will record actual execution results, supporting evidence, and confirmed completion status.
