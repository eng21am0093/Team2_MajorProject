# Agent Frameworks for VLM-Based Medical Diagnosis



**Multi-agent AI system** that leverages Vision-Language Models and Retrieval-Augmented Generation to deliver explainable, real-time clinical decision support.

# AI Agent Framework for VLM-based Medical Diagnosis

## Overview

This project explores the integration of an AI agent framework with Vision-Language Models (VLMs) to enhance medical diagnostic processes. Our solution leverages VLMs to analyze diverse medical data types, such as images and text, in real-time. By employing a chain-of-thought reasoning model, the AI agents provide reliable and explainable diagnostic insights, generate comprehensive reports, and offer real-time support to clinicians.

## Problem Statement

Current medical diagnostic systems face several challenges:
- Fragmented data sources and integration issues
- Limited adaptive learning capabilities
- Absence of intelligent frameworks for task coordination
- Need for real-time, explainable support
- Scalability and consistency challenges across different contexts

## Solution

Our AI agent framework addresses these challenges through:

- **Multimodal Data Integration**: Seamlessly processes and harmonizes medical images, EHR entries, lab reports, and clinical narratives
- **Adaptive Learning Mechanisms**: Continuously refines diagnostic models based on clinician feedback and emerging guidelines
- **Specialized Agent Coordination**: Orchestrates dedicated modules for vision tasks, language understanding, and numerical lab-value interpretation
- **Explainable Decision Support**: Utilizes chain-of-thought reasoning to provide transparent, interpretable insights
- **Scalable Architecture**: Maintains consistent performance across various clinical scenarios

## Architecture

The system is designed as a collaborative multi-agent framework that mirrors a real-world medical team consulting on a diagnosis. Key components include:

1. **Input Processing Layer**: Ingests multimodal patient data (text and images) and encodes it into a unified knowledge store
2. **Multi-Agent Reasoning Layer**: Specialized agents contribute expert analysis in specific domains
3. **Output Synthesis Layer**: Compiles the agents' findings into a final structured report

   ![Architecture Workflow](architecture)

### Specialized Agents

- **Case Data Extractor**: Processes raw clinical materials and produces structured summaries
- **Patient Historian**: Synthesizes patient background into a coherent narrative
- **Lab Interpreter**: Evaluates diagnostic test data and provides clinical interpretations
- **Medical Researcher**: Retrieves and synthesizes relevant medical literature
- **Ethics Advisor**: Reviews ethical implications of diagnostic and treatment options
- **Diagnostic Specialist**: Performs comprehensive analysis and produces final diagnosis

  ![Architecture Workflow](agents_flow.png)

### Knowledge Base and RAG

The framework utilizes a vector database that powers a Retrieval-Augmented Generation mechanism, serving as the unified knowledge store for both patient-specific data and external medical references.

## Results

Using DeepEval metrics, the framework has achieved:
- GEval score of 0.898
- Perfect faithfulness at 1.000
- High precision and recall in diagnostic outputs

   ![Architecture Workflow](res1.png)
  ![Architecture Workflow](res_2.png)


The sequential chat pattern demonstrated superior performance to group chat approaches, with significantly higher precision (0.90 vs 0.70) and recall (1.00 vs 0.78).

## Future Work

- Develop a comprehensive evaluation framework to benchmark VLMs and agent workflows
- Refine agent workflows for specialized outputs in complex medical cases
- Integrate multi-omic data for precision medicine applications
- Enhance feedback-driven refinement mechanisms

## Requirements

### Hardware Requirements
- CPU: Dual-core (or higher) Intel i5/i7 or AMD Ryzen 5/7, clock speed 2.5 GHz
- Memory: Minimum 8GB (16GB recommended)
- Storage: SSD with 50GB free space

### Software Requirements
- Operating System: Linux (Ubuntu 20.04+) or Windows 10/11 (64-bit)
- Python 3.10+
- Core Libraries: Autogen, crewai & crewai tools
- Vector Database Client: FAISS, Pinecone, or equivalent

## Conclusion

This integrated approach enhances overall diagnostic performance, bridging the gap between general-purpose vision models and the specialized requirements of accurate radiographic diagnosis. The collaborative AI framework streamlines information exchange between healthcare professionals and AI systems, improving the speed and accuracy of diagnoses.

## 👥 Contributors

* **Ratan Ravichandran** (ENG21AM0093) 
* **Sayli Pankaj Bande** (ENG21AM0112) 

Project supervised by **Dr. Vinutha N** (Associate Professor, CSE – AI & ML).

---

```
