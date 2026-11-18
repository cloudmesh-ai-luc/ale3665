# Project Proposal — AI-Powered Lecture Slide Generator Using Self-Hosted Open-Weight LLMs and Multi-Cloud Infrastructure

| | |
|---|---|
| **Course** | Cloud Computing, DevOps, and AI |
| **Student** | Alessandra Vellucci Solari |
| **GitHub ID** | `ale3665` |
| **Repository** | [cloudmesh-ai-luc/ale3665](https://github.com/cloudmesh-ai-luc/ale3665) |
| **Instructor** | Professor Gregor von Laszewski |
| **Project Type** | Individual Project |
| **Development Environment** | Windows 11, Ubuntu 24.04 WSL2 |
| **Required Platforms** | Jetstream2, AWS, Google Cloud, Multipass |
| **Date** | November 17, 2026 |

---

## 2. Executive Summary (150–250 Words)

**Problem:** Preparing lecture presentations from educational topics and existing course materials is time-consuming. Educators must organize instructional content, summarize lengthy documents, and create coherent slides while preserving the accuracy of the original information. Existing AI presentation tools may omit important details, introduce unsupported information, or depend on proprietary hosted models. In addition, deploying AI applications across different cloud platforms introduces challenges involving infrastructure configuration, reproducibility, resource availability, and cost.

**Proposed Solution:** This project develops an **AI-Powered Lecture Slide Generator**, a web-based application that transforms lecture topics or uploaded PDF documents into structured educational presentations using a self-hosted open-weight large language model. Users can configure slide count, audience level, and presentation style. The system uses FastAPI, Python, document-processing components, and an LLM-based slide-generation pipeline.

The application will be deployed and evaluated across **four required infrastructure environments: Jetstream2, Amazon Web Services (AWS), Google Cloud Platform (GCP), and Multipass**. Cloudmesh AI VM will support infrastructure management, provider testing, and reproducible deployment workflows.

**Benefits:**

- Reduce manual lecture preparation.
- Preserve important educational content.
- Support topic-based and PDF-based generation.
- Enable customizable presentations.
- Use self-hosted open-weight AI.
- Demonstrate portable multi-cloud deployment.
- Compare performance, reliability, and infrastructure requirements across four providers.

The project will be evaluated through functional testing, source-content preservation, API reliability, deployment reproducibility, inference performance, and resource utilization.

---

## 3. Objectives & Success Criteria

The project combines two major objectives: developing a reliable AI application and evaluating its deployment across four infrastructure environments.

### 3.1 Application Objectives

| # | Objective | Proposed Success Metric |
|---|---|---|
| 1 | Implement topic-based slide generation | Successfully generate structured slides for at least 10 representative lecture topics |
| 2 | Support PDF-based lecture conversion | Process at least 10 valid text-based lecture PDFs |
| 3 | Support multiple lecture documents | Process at least 5 PDF files in a single request |
| 4 | Preserve important source information | Achieve at least 90% coverage of manually identified essential concepts |
| 5 | Support configurable slide count | Meet the requested slide count in at least 95% of valid test requests |
| 6 | Support audience levels and presentation styles | Correctly apply configuration settings in at least 90% of evaluation cases |
| 7 | Integrate a self-hosted open-weight LLM | Demonstrate generation without requiring a proprietary paid inference API |
| 8 | Provide browser and API access | Both generation workflows operate through FastAPI endpoints and the frontend |
| 9 | Support presentation output | Generate a downloadable presentation file from structured slide content |

### 3.2 Multi-Cloud and DevOps Objectives

| # | Objective | Proposed Success Metric |
|---|---|---|
| 10 | Deploy the application using Multipass | Complete local VM deployment and application smoke tests |
| 11 | Deploy the application on Jetstream2 | Complete OpenStack VM deployment and application smoke tests |
| 12 | Deploy the application on AWS | Complete cloud VM deployment and application smoke tests |
| 13 | Deploy the application on Google Cloud | Complete GCP VM deployment and application smoke tests |
| 14 | Integrate Cloudmesh AI VM | Use supported Cloudmesh commands and provider configurations for infrastructure validation |
| 15 | Implement repeatable deployment workflows | Document and successfully repeat deployment procedures across all four environments |
| 16 | Evaluate application performance across platforms | Collect comparable response-time, reliability, and resource-usage measurements |
| 17 | Establish a testing workflow | Execute automated application tests and applicable provider smoke tests |
| 18 | Document reproducibility and results | Provide configuration instructions, commands, evidence, and test results for every provider |

These success criteria are evaluation targets and do not imply that all deployments or tests have already been completed.

---

## 4. Scope

| In-Scope | Out-of-Scope |
|---|---|
| Topic-based lecture generation | Training a foundation LLM from scratch |
| PDF-based slide generation | Complete OCR support for arbitrary scanned documents |
| Multiple PDF uploads | Unlimited document sizes and quantities |
| Slide-count and audience customization | Automated certification of instructional quality |
| Presentation style configuration | Professional design software equivalence |
| Self-hosted open-weight LLM inference | Mandatory dependence on paid proprietary inference APIs |
| FastAPI backend | Enterprise-scale API management |
| Browser-based interface | Enterprise user administration |
| Structured slide representation | Advanced multimedia and animation authoring |
| Presentation export | Full-featured presentation editing platform |
| Multipass deployment | Production-grade availability guarantees |
| Jetstream2 deployment | Multi-region research cloud deployment |
| AWS deployment | Large-scale commercial operation |
| Google Cloud deployment | Large-scale commercial operation |
| Cloudmesh AI VM integration | Reimplementation of the entire Cloudmesh framework |
| Provider-specific smoke tests | Unsupported or unsafe infrastructure operations |
| Cross-cloud performance comparison | Comprehensive production benchmarking |
| GitHub-based development and documentation | Enterprise compliance certification |

The central application will share a common implementation across providers. Infrastructure configuration may vary according to each platform's operating system, networking, authentication, and compute resources.

---

## 5. Technical Approach

### 5.1 Multi-Cloud Architecture

The proposed architecture separates application functionality from infrastructure-specific deployment details.

A single FastAPI application will provide the generation endpoints. Its LLM client will communicate with a configurable self-hosted inference service.

The same application will be deployed to VM environments managed or validated through Cloudmesh AI VM and provider-specific tooling.

### Required Infrastructure Providers

| Provider | Infrastructure Type | Primary Role |
|---|---|---|
| **Multipass** | Local virtual machines | Local deployment, reproducibility, and development testing |
| **Jetstream2** | Research cloud / OpenStack | Cloud-hosted application and LLM evaluation |
| **AWS** | Public cloud / EC2 | Public-cloud application deployment and testing |
| **Google Cloud** | Public cloud / Compute Engine | Alternative public-cloud deployment and testing |

All four providers are required for infrastructure and application evaluation.

### Application Components

| Component | Technology | Function |
|---|---|---|
| Frontend | HTML, CSS, JavaScript | Accept user inputs and display results |
| API | FastAPI | Provide REST endpoints |
| Topic processor | Python | Prepare topic-based generation requests |
| PDF processor | Python PDF libraries | Extract text from lecture documents |
| Document organizer | Python | Combine and structure source material |
| Slide planner | Python | Create presentation outlines |
| LLM client | Ollama or OpenAI-compatible interface | Communicate with the selected self-hosted model |
| Model server | Open-weight LLM runtime | Generate lecture content |
| Slide formatter | Python | Convert generated text into slide structures |
| Export component | Python presentation library | Produce presentation files |
| Infrastructure manager | Cloudmesh AI VM | Manage or validate provider configurations and VM lifecycle operations |
| Testing | pytest, HTTP smoke tests | Verify functionality and deployment |

### Proposed Architecture Diagram

```text
                    EDUCATOR / USER
                           |
                           v
                 WEB USER INTERFACE
                           |
                           v
                      FASTAPI
                           |
               +-----------+-----------+
               |                       |
               v                       v
          TOPIC INPUT              PDF UPLOAD
               |                       |
               v                       v
         TOPIC PLANNER          PDF EXTRACTION
               |                       |
               |                 DOCUMENT MERGING
               |                       |
               +-----------+-----------+
                           |
                           v
                  SLIDE PLANNING
                           |
                           v
                  LLM CLIENT LAYER
                           |
                           v
             SELF-HOSTED OPEN-WEIGHT LLM
                           |
                           v
                STRUCTURED SLIDE DATA
                           |
                           v
                PRESENTATION FORMATTER
                           |
                           v
                 PREVIEW / EXPORT
```

### Multi-Cloud Deployment Layer

```text
                 GITHUB REPOSITORY
                         |
                         v
                  DEVOPS WORKFLOW
                         |
                         v
                  CLOUDMESH AI VM
                         |
       +-----------------+-----------------+
       |                 |                 |
       v                 v                 v
    MULTIPASS        JETSTREAM2          AWS
   LOCAL VM           OPENSTACK          EC2
       |                 |                 |
       +-----------------+-----------------+
                         |
                         v
                GOOGLE CLOUD (GCE)

       Each environment runs the application
       and undergoes provider-specific tests.
```

The deployment diagram represents the four required targets, not a sequential dependency between providers.

### 5.2 Provider Deployment Strategy

#### Multipass — Local Virtualization

Multipass will provide a local Ubuntu virtual machine for application deployment and repeatable testing.

Planned workflow:

1. Verify the Multipass installation.
2. Create and configure an Ubuntu VM.
3. Install Python and application dependencies.
4. Deploy the FastAPI application.
5. Configure access to the self-hosted LLM.
6. Run API health checks and generation tests.
7. Record results.
8. Stop and delete test VMs when appropriate.

Multipass will serve as a baseline for understanding application behavior in a controlled local environment.

#### Jetstream2 — Research Cloud

Jetstream2 will provide an OpenStack-based research cloud environment.

Planned workflow:

1. Configure authentication and cloud access.
2. Verify the selected image and flavor.
3. Provision the required VM.
4. Configure SSH and network connectivity.
5. Install and launch the application.
6. Configure access to an open-weight model.
7. Run API and inference tests.
8. Record performance and errors.
9. Clean up temporary resources.

Jetstream2 is particularly relevant for investigating cloud-hosted model inference and larger compute configurations when allocated resources permit.

#### AWS — Amazon Web Services

AWS will be used to evaluate deployment on public-cloud virtual machines.

The project will primarily consider EC2 instances for a comparable VM-based deployment.

Planned workflow:

1. Configure AWS credentials and region.
2. Select an appropriate EC2 instance type.
3. Configure networking and SSH access.
4. Provision the instance.
5. Install application dependencies.
6. Deploy the FastAPI service.
7. Configure inference connectivity.
8. Execute application tests.
9. Monitor resource usage and costs.
10. Terminate experimental infrastructure.

GPU-enabled instances will only be considered if access, quotas, and budget permit.

#### Google Cloud — GCP

Google Cloud will provide an additional public-cloud deployment environment.

Compute Engine will be used to evaluate VM-based application deployment.

Planned workflow:

1. Configure the GCP project and authentication.
2. Select the deployment region and VM machine type.
3. Configure networking and firewall permissions.
4. Provision a Compute Engine VM.
5. Deploy the application.
6. Configure the model endpoint.
7. Run application and infrastructure tests.
8. Collect resource and performance metrics.
9. Stop or delete temporary infrastructure.

The Google Cloud deployment will provide an additional comparison against AWS and Jetstream2.

### 5.3 Cloudmesh AI VM Integration

Cloudmesh AI VM will support infrastructure management and validation across the four required platforms wherever provider functionality is implemented and available.

The project will evaluate:

- Provider configuration.
- VM provisioning.
- VM lifecycle operations.
- SSH access.
- Instance status reporting.
- Provider-specific errors.
- Resource cleanup.
- Infrastructure smoke tests.

The same four providers will also be included in relevant Cloudmesh class testing and development activities.

For pull requests affecting provider-independent functionality, the goal will be to test the change against all four providers where applicable.

Provider-specific changes will additionally require focused testing of the affected platform.

Test reports will distinguish between successful results, expected skips, unsupported operations, and failures.

### 5.4 DevOps Pipeline

| Stage | Tools | Description |
|---|---|---|
| Source Control | Git and GitHub | Maintain repository and development history |
| Development | VS Code, Python, WSL2 | Implement backend, frontend, and processing |
| Environment | Python virtual environments | Manage project dependencies |
| Build | Python packaging / Docker where appropriate | Prepare deployable application |
| Unit Testing | pytest | Validate processing and generation logic |
| API Testing | FastAPI test client / HTTP requests | Validate endpoints |
| Infrastructure Testing | Cloudmesh AI VM | Test providers and VM lifecycle behavior |
| Deployment | Multipass, Jetstream2, AWS, GCP | Deploy the application |
| Smoke Testing | Python and HTTP commands | Verify deployed services |
| Evaluation | Python scripts and logs | Compare reliability and performance |
| Documentation | Markdown / GitHub | Record procedures and evidence |

The project will prioritize automated validation and reproducible setup procedures.

A GitHub Actions workflow may be used for code-quality checks, tests, and build validation.

Cloud resources should not be provisioned automatically on every commit unless safeguards and appropriate credentials are configured.

### 5.5 AI / Model Serving

The project requires a self-hosted open-weight LLM.

Ollama is the initial local model-serving interface.

Potential models include Qwen, Llama, Gemma, and Mistral, with the final selection based on available hardware and evaluation results.

The same model version and inference configuration should be used across environments when resources permit, to support fair comparisons.

However, application hosting and model hosting may be separated when a VM does not have sufficient compute resources to run inference locally.

Therefore, each deployment will document:

- Application hosting environment.
- Model hosting environment.
- Model name and version.
- Quantization, if applicable.
- Inference endpoint.
- CPU/GPU availability.
- Relevant resource constraints.

This distinction is important because successful application deployment does not necessarily imply that the LLM itself is running on the same virtual machine.

### 5.6 Topic-Based Generation

The user enters a lecture topic and selects the presentation options.

Example request:

```json
{
  "topic": "Introduction to Machine Learning",
  "slide_count": 15,
  "audience_level": "undergraduate",
  "style": "academic"
}
```

The backend prepares the prompt and passes it to the configured LLM.

The response is validated and transformed into structured slide content.

### 5.7 PDF-Based Generation

The PDF workflow will support educators who already have lecture materials.

The processing pipeline will:

1. Validate uploaded PDFs.
2. Extract text.
3. Combine documents where requested.
4. Split large content into manageable sections.
5. Identify key concepts.
6. Develop an outline.
7. Generate slides grounded in the extracted material.
8. Evaluate preservation of essential content.
9. Format the resulting presentation.

The project will seek to minimize unsupported content additions.

For multi-PDF inputs, document provenance should be retained where practical.

### 5.8 Application API

The two core API endpoints are:

```text
POST /generate-from-topic
POST /generate-from-pdfs
```

Example structured response:

```json
{
  "title": "Introduction to Machine Learning",
  "slides": [
    {
      "slide_number": 1,
      "title": "Overview",
      "bullet_points": [
        "Definition of machine learning",
        "Major learning approaches",
        "Real-world applications"
      ]
    }
  ]
}
```

Both workflows will share a common presentation output format.

### 5.9 Multi-Cloud Testing Plan

The application will be evaluated across the four providers using comparable procedures.

| Test Category | Multipass | Jetstream2 | AWS | Google Cloud |
|---|---|---|---|---|
| Authentication / configuration | Required | Required | Required | Required |
| VM creation | Required | Required | Required | Required |
| VM status inspection | Required | Required | Required | Required |
| VM stop and restart | Required | Required | Required | Required |
| SSH connectivity | Required | Required | Required | Required |
| Application deployment | Required | Required | Required | Required |
| API health check | Required | Required | Required | Required |
| Topic generation | Required | Required | Required | Required |
| PDF generation | Required | Required | Required | Required |
| LLM communication | Required | Required | Required | Required |
| Error handling | Required | Required | Required | Required |
| Resource monitoring | Required | Required | Required | Required |
| Resource cleanup | Required | Required | Required | Required |

These are required test categories, not completed test results. Provider limitations or unavailable resources will be documented explicitly.

### 5.10 Security

Security controls will include:

- Environment-variable-based credential management.
- No API keys or private SSH keys in GitHub.
- Restricted network access.
- Controlled cloud firewall and security-group rules.
- Validation of user inputs and PDF uploads.
- Configurable file size limits.
- Temporary file cleanup.
- Error messages that avoid exposing secrets.
- Provider-specific least-privilege permissions.
- Secure model endpoint configuration.

Cloud credentials will remain separate for Jetstream2, AWS, and Google Cloud.

---

## 6. Project Plan & Timeline

| Phase | Tasks | Target Period |
|---|---|---|
| 1. Requirements | Define functionality and select four required infrastructure providers | September–October 2026 |
| 2. Architecture | Design FastAPI, PDF pipeline, LLM interface, and cloud deployment strategy | October 2026 |
| 3. Initial Development | Implement topic and PDF generation workflows | October–November 2026 |
| 4. LLM Integration | Configure Ollama and open-weight model inference | October–November 2026 |
| 5. Application Testing | Validate generation logic, PDF processing, API endpoints, and export | November–December 2026 |
| 6. Multipass Deployment | Deploy and verify application locally | November–December 2026 |
| 7. Jetstream2 Deployment | Configure and test OpenStack deployment | November–December 2026 |
| 8. AWS Deployment | Deploy to EC2 and execute tests | November–December 2026 |
| 9. Google Cloud Deployment | Deploy to Compute Engine and execute tests | November–December 2026 |
| 10. Comparative Evaluation | Compare reliability, latency, and resource requirements | December 2026 |
| 11. Final Documentation | Complete report, evidence, and final presentation | December 2026 |

The exact completion dates will be recorded in the implementation report.

### Milestones

**Milestone 1 — Functional Application**

Deliver the core FastAPI service with topic and PDF workflows.

**Milestone 2 — Open-Weight LLM Integration**

Demonstrate application inference through a self-hosted model.

**Milestone 3 — Multi-Cloud Deployment**

Deploy the application on Multipass, Jetstream2, AWS, and Google Cloud.

**Milestone 4 — Provider Testing**

Execute infrastructure and application smoke tests across all four environments.

**Milestone 5 — Evaluation**

Compare results and document infrastructure-specific differences.

**Milestone 6 — Final Deliverables**

Complete documentation, architecture diagrams, deployment evidence, and final presentation.

---

## 7. Resources & Budget

The project will prioritize educational and research resources while controlling public-cloud costs.

| Resource | Quantity | Estimated Cost | Purpose |
|---|---|---|---|
| Windows 11 / Ubuntu WSL2 | 1 development workstation | No additional cloud fee | Development |
| Python / FastAPI / VS Code | Open-source tools | $0 software cost | Application development |
| Ollama | 1 local runtime | $0 software cost | Local model inference |
| Open-weight LLM | 1 selected model | License-dependent, generally no per-token API fee for self-hosting | Generation |
| Multipass | Local VM environment | No additional cloud fee | Local deployment |
| Jetstream2 | Research cloud allocation | Subject to allocation | OpenStack deployment |
| AWS EC2 | Temporary VM resources | Usage-dependent | Public-cloud testing |
| Google Compute Engine | Temporary VM resources | Usage-dependent | Public-cloud testing |
| Cloud storage | Small experimental allocation | Usage-dependent | Temporary artifacts |
| GitHub | Course repository | Existing access | Version control |
| **Total** | | **Determined by actual usage and available credits** | |

### Cost Controls

To minimize unnecessary spending, the project will:

1. Develop and test locally first.
2. Use the smallest suitable VM configuration.
3. Avoid unnecessary GPU allocations.
4. Set budgets and usage alerts for AWS and Google Cloud.
5. Shut down resources after experiments.
6. Use research allocations where permitted.
7. Document actual costs and resource consumption.

The cost comparison will account for differences in cloud pricing, compute type, usage duration, and available educational credits.

---

## 8. Risk Management

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Inaccurate generated lecture content | High | High | Ground PDF content in sources and evaluate factual preservation |
| Missing important PDF concepts | Medium | High | Evaluate source-to-slide concept coverage |
| Context-window limitations | High | Medium | Use chunking and structured slide planning |
| Insufficient CPU/GPU resources | Medium | High | Use smaller or quantized models and separate application/model hosting when necessary |
| Multipass VM configuration issues | Medium | Medium | Validate VM setup and document local requirements |
| Jetstream2 allocation or authentication issues | Medium | High | Verify credentials, images, flavors, and quotas before deployment |
| AWS cost overruns | Medium | High | Set budgets, limits, and cleanup procedures |
| Google Cloud cost overruns | Medium | High | Set budgets and terminate unused resources |
| Provider-specific API differences | High | Medium | Use provider adapters and configuration-specific tests |
| SSH and networking failures | Medium | High | Validate credentials, firewall rules, and connectivity |
| Cloudmesh provider incompatibility | Medium | Medium | Run supported smoke tests and document failures |
| LLM inference service unavailable | Medium | High | Add health checks, timeouts, and clear error handling |
| Sensitive credential exposure | Low | High | Use secret management and restrict access |
| Inconsistent cross-cloud measurements | Medium | High | Standardize test inputs, model versions, and workload conditions |
| Incomplete deployment evidence | Medium | Medium | Preserve logs, screenshots, command outputs, and configuration summaries |

---

## 9. Evaluation & Success Metrics

The evaluation will address both application functionality and infrastructure behavior.

### 9.1 Application Evaluation

| Metric | Target | Method |
|---|---|---|
| Topic generation success | ≥ 90% | Automated API tests |
| PDF processing success | ≥ 90% | PDF test dataset |
| Multi-PDF processing | At least 5 PDFs | Integration testing |
| Requested slide-count compliance | ≥ 95% | Output validation |
| Essential source concept coverage | ≥ 90% | Manual concept annotation and comparison |
| Presentation export success | ≥ 90% | File generation and validation tests |
| API response reliability | Report observed success rate | HTTP tests |
| Model response time | Measure median and p95 | Timing logs |

### 9.2 Infrastructure Evaluation

The following metrics will be collected for Multipass, Jetstream2, AWS, and Google Cloud.

| Metric | Measurement |
|---|---|
| VM provisioning success | Successful vs. failed deployment attempts |
| Provisioning duration | Time from request to ready VM |
| SSH readiness | Time until successful SSH connection |
| Application deployment duration | Time required to install and start the application |
| API availability | Successful health checks |
| Generation latency | Topic and PDF request duration |
| CPU utilization | Measured during test requests |
| Memory utilization | Measured during test requests |
| GPU utilization | Where GPU resources are available |
| Reliability | Successful requests / total requests |
| Resource cleanup | Successful termination and cleanup |
| Direct infrastructure cost | Observed cloud usage cost |

### 9.3 Cross-Cloud Comparison

The comparison will use the same representative request set across providers.

Whenever possible, tests will use:

- The same application version.
- The same Python dependency versions.
- The same test prompts and PDF documents.
- Equivalent generation settings.
- The same LLM model and configuration.
- Comparable VM resources.

When model hosting differs between platforms, the evaluation will clearly separate network and inference effects from application-host performance.

Results will be presented in tables and graphs showing:

1. Deployment success and reliability.
2. VM provisioning time.
3. API response latency.
4. LLM inference duration.
5. CPU and memory utilization.
6. Resource requirements.
7. Estimated or observed operational cost.
8. Provider-specific limitations.

No performance advantage will be claimed without measured evidence.

### 9.4 Testing and Evidence

Evidence for each provider will include:

- VM configuration.
- Provider and region/site.
- VM image and flavor or machine type.
- Deployment commands.
- Relevant Cloudmesh commands.
- API test results.
- Generation sample output.
- Error logs where applicable.
- Resource cleanup result.

Cloudmesh class-related PRs will additionally document affected functionality, tests performed, and the outcome of maintainer review.

---

## 10. Deliverables

| Deliverable | Format | Description |
|---|---|---|
| Project proposal | `project/project.md` | Objectives, architecture, infrastructure, and evaluation |
| Architecture diagram | PNG / SVG | Application components and four-provider infrastructure |
| FastAPI backend | Python | Topic and PDF API workflows |
| Browser frontend | HTML / CSS / JavaScript | User interface |
| PDF processing modules | Python | Extract and organize lecture content |
| LLM integration | Python | Self-hosted model communication |
| Slide planner | Python | Convert content into structured slides |
| Presentation exporter | Python | Generate presentation files |
| Unit tests | pytest | Validate application logic |
| Integration tests | pytest / HTTP | Validate LLM and API behavior |
| Multipass deployment | Scripts and configuration | Local VM execution |
| Jetstream2 deployment | Scripts and configuration | Research cloud execution |
| AWS deployment | Scripts and configuration | EC2 execution |
| Google Cloud deployment | Scripts and configuration | Compute Engine execution |
| Cloudmesh provider tests | Logs and test reports | Provider lifecycle validation |
| Cross-cloud comparison | Tables and graphs | Reliability and performance results |
| Security and configuration documentation | Markdown | Credentials and deployment procedures |
| Final technical report | PDF or document | Implementation and evaluation |
| Final presentation | Slides | Project demonstration and findings |

### Proposed Repository Structure

```text
ale3665/
├── project/
│   ├── project.md
│   ├── images/
│   └── presentation/
├── src/
│   └── lecture_slide_generator/
│       ├── main.py
│       ├── generator.py
│       ├── llm.py
│       └── index.html
├── tests/
├── deployments/
│   ├── multipass/
│   ├── jetstream/
│   ├── aws/
│   └── gcp/
├── assignments/
│   └── STATUS.md
└── README.md
```

The `deployments/` structure is proposed and may be adapted to the final implementation.

---

## 11. References

1. FastAPI. *Official Documentation.* https://fastapi.tiangolo.com/

2. Ollama. *Documentation.* https://docs.ollama.com/

3. Jetstream2. *Research Cloud Infrastructure.* https://jetstream-cloud.org/

4. Amazon Web Services. *Amazon EC2 Documentation.* https://docs.aws.amazon.com/ec2/

5. Google Cloud. *Compute Engine Documentation.* https://cloud.google.com/compute/docs

6. Canonical. *Multipass Documentation.* https://documentation.ubuntu.com/multipass/

7. OpenStack. *Official Documentation.* https://docs.openstack.org/

8. GitHub. *GitHub Actions Documentation.* https://docs.github.com/en/actions

9. Cloudmesh AI. *Cloudmesh AI VM Repository.* https://github.com/cloudmesh-ai/cloudmesh-ai-vm

10. Cloudmesh AI. *Cloudmesh AI Common Repository.* https://github.com/cloudmesh-ai/cloudmesh-ai-common

11. Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* https://arxiv.org/abs/2005.11401

12. Python Software Foundation. *Python Documentation.* https://docs.python.org/3/

13. Course Repository. *AI-Powered Lecture Slide Generator.* https://github.com/cloudmesh-ai-luc/ale3665

---

## Project Status

The AI-Powered Lecture Slide Generator is an individual Cloud Computing, DevOps, and AI project combining educational content generation with multi-cloud infrastructure management.

The project targets two functional workflows: generating presentations from lecture topics and adapting existing PDF materials into structured slides.

**The four required infrastructure environments are Jetstream2, AWS, Google Cloud, and Multipass.** Each will be used for application deployment and testing, with provider-specific Cloudmesh AI VM testing where applicable.

Current development includes environment setup, application architecture, FastAPI development, slide-planning logic, document-processing development, and open-weight LLM integration.

The next phases focus on implementation validation, deployment across the four platforms, infrastructure smoke testing, performance evaluation, and final documentation.

Successful deployment and test results will be documented individually for each platform rather than assumed from local development progress.
