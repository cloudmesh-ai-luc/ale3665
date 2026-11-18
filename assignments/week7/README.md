# Week 7 — Cloud, AI & DevOps

## Overview

Week 7 focuses on Python-driven virtual machine management, contributing to the shared Cloudmesh AI VM implementation, and advancing the individual course project. My required platforms for the personal project and applicable Cloudmesh provider tests are **Jetstream2, Amazon Web Services (AWS), Google Cloud, and Multipass**.

This report distinguishes implementation and documented contributions from provider tests or deployments that need their own execution evidence.

## W7.1 — Virtual Machines Using Python

### Objective

Explore Python-based cloud and virtual machine management as an alternative to invoking cloud commands manually. Compare provider-specific APIs and use a consistent workflow for infrastructure configuration, provisioning, inspection, connectivity, and cleanup.

### Tools and environments

- Windows 11 with Ubuntu 24.04 on WSL2
- Python virtual environments
- Cloudmesh AI VM and `cmx`
- OpenStack SDK for Jetstream2
- Cloud-provider APIs and SDKs where configured
- Multipass for local virtualization
- Git and GitHub for source control

### Required provider coverage

| Provider | Environment | Planned validation |
|---|---|---|
| Multipass | Local Ubuntu VM | VM lifecycle, status, SSH, cleanup |
| Jetstream2 | OpenStack research cloud | Authentication, image/flavor selection, launch, networking, SSH, cleanup |
| AWS | EC2 public cloud | Authentication, instance lifecycle, SSH, application smoke test, cleanup |
| Google Cloud | Compute Engine public cloud | Project authentication, instance lifecycle, SSH, application smoke test, cleanup |

### Python/Cloudmesh environment

The existing Cloudmesh AI VM environment is located at `~/.venvs/cloudmesh-ai-vm` and was verified with package version `0.1.0`.

```bash
source ~/.venvs/cloudmesh-ai-vm/bin/activate
which python
python -m pip show cloudmesh-ai-vm
cmx --help
cmx vm --help
```

### Verification and evidence

Provider-specific test commands and outcomes belong in the final evidence log. Having the CLI installed does not establish that a live instance test succeeded.

- [x] Identify and activate the Cloudmesh Python environment.
- [x] Verify the `cmx` command is available.
- [ ] Attach the executed lifecycle test command/output for Multipass.
- [ ] Attach the executed lifecycle test command/output for Jetstream2.
- [ ] Attach the executed lifecycle test command/output for AWS.
- [ ] Attach the executed lifecycle test command/output for Google Cloud.

The last four items are evidence placeholders, not claims that testing has not occurred; attach the existing logs or screenshots if already completed.

---

## W7.2 — Contribution to Cloudmesh AI VM (`cmx`)

### Objective

Contribute practical improvements to the shared Cloudmesh AI VM project, evaluate behavior against real provider environments, and use GitHub pull requests for review and integration.

**Upstream repository:** [cloudmesh-ai/cloudmesh-ai-vm](https://github.com/cloudmesh-ai/cloudmesh-ai-vm)

### Authored pull requests

My GitHub account `ale3665` has **20 authored pull requests** in the verified history as of November 17, 2026: **11 GitHub-merged**, **8 closed without a GitHub merge**, and **1 open**. Nineteen target `cloudmesh-ai/cloudmesh-ai-vm`; the remaining PR is a course example repository contribution.

| PR | Change | GitHub status |
|---|---|---|
| [#73](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/73) | Fix Jetstream missing typing imports | Merged |
| [#74](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/74) | Restore unit-test baseline | Merged |
| [#75](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/75) | Implement `cmx vm doctor` diagnostics | Closed; maintainer confirmed manual integration |
| [#76](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/76) | Contributor documentation (initial submission) | Closed, not merged |
| [#77](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/77) | Add contributor documentation | Merged |
| [#78](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/78) | Correct Chameleon Ubuntu image | Merged |
| [#79](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/79) | Correct Chameleon keypair naming | Merged |
| [#80](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/80) | Improve Chameleon SSH verification | Merged |
| [#81](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/81) | Verify cloud keypairs using provider registry | Closed, not merged |
| [#82](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/82) | Use Chameleon `SHUTOFF` state in lifecycle smoke test | Merged |
| [#83](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/83) | Correct Jetstream Ubuntu image | Merged |
| [#84](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/84) | Correct Jetstream flavor (earlier submission) | Closed, not merged |
| [#85](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/85) | Provision Jetstream SSH launch key | Closed, not merged |
| [#86](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/86) | Detect OpenStack network readiness from server addresses | Merged |
| [#87](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/87) | Resolve lifecycle smoke-test merge conflicts | Closed, not merged |
| [#88](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/88) | Preserve VM Doctor strict exit behavior | Closed; maintainer reported integrating changes |
| [#89](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/89) | Use configured cloud username in test VM names | Merged |
| [#90](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/90) | Read Jetstream flavor from provider configuration | Merged |
| [#91](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/91) | Provision temporary Jetstream launch key | Closed, not merged |
| [Course example #1](https://github.com/cloudmesh-ai-luc/example/pull/1) | Correct documentation typos | Open |

### `cmx vm doctor` implementation

**PR:** [#75](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/75)  
**Follow-up:** [#88](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/88)

I developed and submitted a non-destructive provider diagnostic command, `cmx vm doctor`, to check provider availability, requirements, configuration, and readiness before attempting VM lifecycle actions. It also includes a strict mode for automation-friendly exit codes.

Example interface:

```bash
cmx vm doctor
cmx vm doctor --cloud multipass
cmx vm doctor --cloud openstack
cmx vm doctor --cloud multipass --strict
```

The original PR reported **5 passing targeted Doctor tests** and **105 passing unit tests with one warning**. During follow-up testing, I identified a strict-mode exception handling issue; the focused fix in PR #88 reported an improvement from **4 passed / 1 failed** to **5 passed**.

In the PR #75 discussion, Professor von Laszewski stated, “I also moved the doctor command into the code,” and later confirmed integration while preparing `dev2`. In PR #88, he reported that he had integrated the changes but requested full smoke-test revalidation. Thus the work was **maintainer-integrated, not formally GitHub-merged through those two PRs**.

### Testing observations

The upstream PRs document live and unit-test findings, including:

- Jetstream images, flavors, SSH keys, and fixed-IP detection.
- Chameleon image selection, SSH keypair names, SSH readiness, and `SHUTOFF` state.
- Unit-test compatibility with provider implementations.
- Shared smoke-test VM naming and configuration.

For current course tests, applicable changes will be checked against **Jetstream2, AWS, Google Cloud, and Multipass**. Historical PR validation on Chameleon remains part of the contribution record; it is not a substitute for the four required current providers.

---

## W7.3 — Individual Project: AI-Powered Lecture Slide Generator

### Project description

The application helps educators generate structured presentations from either a lecture topic or one or more existing lecture PDFs. In PDF mode, the goal is to retain essential source information while restructuring it into slides.

### Core requirements

1. Generate slides from a user-entered topic.
2. Accept existing lecture PDF materials.
3. Support combining multiple PDFs.
4. Configure slide count, audience level, and presentation style.
5. Use a **self-hosted open-weight LLM**.
6. Produce structured slide content and support presentation output.
7. Deploy and test on **Multipass, Jetstream2, AWS, and Google Cloud**.

### Application stack

| Component | Technology / plan |
|---|---|
| Backend | Python, FastAPI |
| Frontend | HTML interface |
| LLM | Open-weight model; Ollama for local development, configurable cloud inference |
| PDF processing | Python extraction and content organization |
| Slide generation | Structured slide planner and presentation formatting |
| Deployment | VM-based environments across the four required providers |
| Testing | Python tests, API tests, provider-specific smoke tests |

### API design

```text
POST /generate-from-topic
POST /generate-from-pdfs
```

### Project source organization

```text
src/lecture_slide_generator/
    main.py
    generator.py
    llm.py
    index.html

project/
    project.md
    images/
    presentation/

tests/
```

The development branch `feature/lecture-planner-v07` has been used for lecture-planning work, and the project proposal belongs in [`project/project.md`](https://github.com/cloudmesh-ai-luc/ale3665/blob/main/project/project.md).

### Deployment and evaluation matrix

| Requirement | Multipass | Jetstream2 | AWS | Google Cloud |
|---|---|---|---|---|
| VM configuration and lifecycle | Required | Required | Required | Required |
| SSH connectivity | Required | Required | Required | Required |
| FastAPI application deployment | Required | Required | Required | Required |
| Topic-based slide request | Required | Required | Required | Required |
| PDF-based slide request | Required | Required | Required | Required |
| LLM endpoint access | Required | Required | Required | Required |
| API and performance measurements | Required | Required | Required | Required |
| Resource cleanup | Required | Required | Required | Required |

Record actual commands, model endpoint placement, responses, and failures for each provider. An application hosted on one VM may use a separately hosted self-managed LLM; the report should document that distinction.

### Development status

The project architecture and API workflows have been defined, and initial application and LLM integration development has been undertaken. Complete end-to-end tests, four-provider deployment evidence, and presentation-export verification should be documented as results become available.

---

## Week 7 Summary

Week 7 work ties together Python-based virtual machine management, practical contributions to the upstream Cloudmesh AI VM project, and development of an educational AI application. The Cloudmesh work provides direct experience with provider-specific debugging, unit tests, smoke tests, and maintainers' review. The lecture generator extends those skills into a multi-cloud application integrating FastAPI, document processing, and open-weight LLM inference.

## Evidence and References

- [Individual course repository](https://github.com/cloudmesh-ai-luc/ale3665)
- [Project proposal](https://github.com/cloudmesh-ai-luc/ale3665/blob/main/project/project.md)
- [Cloudmesh AI VM upstream repository](https://github.com/cloudmesh-ai/cloudmesh-ai-vm)
- [VM Doctor PR #75](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/75)
- [VM Doctor follow-up PR #88](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/88)
- [All authored pull requests](https://github.com/pulls?q=is%3Apr+author%3Aale3665)
- [Course status report](https://github.com/cloudmesh-ai-luc/ale3665/blob/main/assignments/STATUS.md)

**Note:** This is a Week 7 activity and submission summary based on the available coursework history; consult the Week 7 Piazza/assignment page to confirm any additional required submission artifacts or grading criteria.
