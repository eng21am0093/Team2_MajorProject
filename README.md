# Agent Frameworks for VLM-Based Medical Diagnosis

![Architecture Workflow](docs/images/architecture_workflow.png)

**Multi-agent AI system** that leverages Vision-Language Models and Retrieval-Augmented Generation to deliver explainable, real-time clinical decision support.

---

## 📖 Table of Contents

- [Overview](#overview)  
- [Key Features](#key-features)  
- [Proposed Architecture](#proposed-architecture)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
- [Usage](#usage)  
- [Repository Structure](#repository-structure)  
- [Figures & Diagrams](#figures--diagrams)  
- [Contributors](#contributors)  
- [License](#license)  

---

## 🧐 Overview

Modern diagnostic workflows suffer from fragmented data across imaging, EHRs, and lab reports. This project introduces a **chain-of-thought**, **multi-agent AI framework** that:

1. Integrates **Vision-Language Models** (e.g., LLaMA 3.2 11B-Vision) to interpret scans.  
2. Uses **CrewAI** (or Autogen/LangChain) to orchestrate specialized agents—Patient Historian, Lab Interpreter, Medical Researcher, Ethics Advisor, and Diagnosis Specialist.  
3. Employs a **Vector DB + RAG pipeline** to ground outputs in patient history and up-to-date literature.  
4. Generates comprehensive, **explainable diagnostic reports** with embedded clinical reasoning.

---

## 🔑 Key Features

- **Multimodal Input**: Seamless ingestion of images, free-text notes, structured labs.  
- **Retrieval-Augmented Generation**: Semantic search over patient data & medical literature.  
- **Chain-of-Thought Agents**: Each agent focuses on a discrete subtask, then hands off to the next.  
- **Explainability**: Transparent reasoning log—every decision step is traceable.  
- **Adaptive Learning**: Plug-in SME feedback loops to fine-tune agent prompts and knowledge.  
- **Ethical Oversight**: Built-in Ethics Advisor agent flags privacy, consent, and bias issues.  

---

## 🏗 Proposed Architecture

1. **Input Layer**  
   - Image → VLM → textual observations  
   - Text → segmentation & embedding → Vector DB  

2. **Agent Orchestration**  
   - Sequential Chat pattern managed by CrewAI  
   - Shared context + short/long-term memory  

3. **RAG Pipeline**  
   1. Chunk & embed documents  
   2. Nearest-neighbor retrieval  
   3. LLM synthesis with tool invocation (MDXSearchTool, SerperDevTool, etc.)  

4. **Output**  
   - Final Diagnosis Specialist → structured report  

![Proposed Model Diagram](docs/images/proposed_model.png)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+  
- Access to a Vision-Language Model (e.g., LLaMA 3.2 with vision extension)  
- API keys for OpenAI / Azure OpenAI (GPT-4o Mini)  
- A vector database (FAISS, Pinecone, or similar)  
- Docker & Docker Compose (optional, for local orchestration)  

---

## ⚙️ Usage

1. **Configure your vector DB** in `config/vector_db.yaml`.

2. **Prepare patient data** under `data/` (images, EHR text, lab reports).

3. **Launch orchestration**:

   ```bash
   python main.py
   ```

4. **View outputs** in the `outputs/` directory:

   * `diagnostic_report.md`
   * `treatment_plan.md`
   * `ethics_assessment.md`

---

## 📁 Repository Structure

```
.
├── README.md
├── main.py
├── diagnosis/
│   ├── crew.py
│   ├── config/
│   │   ├── agents.yaml
│   │   └── tasks.yaml
│   └── data/
│       ├── patient_history.txt
│       ├── lab_history.txt
│       └── imaging_data.txt
├── docs/
│   └── images/
│       ├── architecture_workflow.png
│       └── proposed_model.png
├── requirements.txt
└── outputs/
```

---

## 📊 Figures & Diagrams

* **Figure 4.1**: High-level multi-agent workflow
* **Proposed Model Diagram**: End-to-end data & agent flow
* **Experimentation Results**: Precision/Recall & ROUGE comparisons

---

## 👥 Contributors

* **Ratan Ravichandran** (ENG21AM0093) — System design, orchestration, evaluation
* **Sayli Pankaj Bande** (ENG21AM0112) — Data preprocessing, prompt engineering, documentation

Project supervised by **Dr. Vinutha N** (Associate Professor, CSE – AI & ML).

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

```
