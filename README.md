<h1 align="center">Nexus-RAG: Autonomous Multi-Agent Knowledge Engine</h1>

<p align="center">
  <strong>A sophisticated Graph-based RAG system orchestrating multi-agent workflows for high-precision document intelligence.</strong>
</p>

<div align="center">
  <img src="https://img.shields.io/badge/Framework-LangGraph-blue" alt="LangGraph">
  <img src="https://img.shields.io/badge/VectorDB-Qdrant-red" alt="Qdrant">
  <img src="https://img.shields.io/badge/LLM-Ollama%20%2F%20-orange" alt="LLM">
  <img src="https://img.shields.io/badge/Interface-Gradio-green" alt="Gradio">
</div>

---

## 🚀 Executive Summary
**Nexus-RAG** transcends traditional RAG architectures by implementing an agentic loop via **LangGraph**. Unlike standard "top-k" retrieval systems, Nexus-RAG treats retrieval as a reasoning task—evaluating context relevance, rewriting queries for better alignment, and utilizing hierarchical indexing to ensure the LLM receives the most pertinent information without losing the broader context.



---

## 📸 Working Prototype

### 1. Document Management & Ingestion
The system features a robust ingestion pipeline that converts complex PDFs into structural Markdown, preserving the semantic integrity of tables and headers before they are embedded into the **Qdrant** vector store.

<p align="center">
  <img src="Screenshot 2026-01-09 233134.png" width="800" alt="Document Ingestion">
</p>

### 2. High-Precision Statistical Retrieval
The agentic reasoning engine excels at extracting specific technical details. In the example below, it accurately retrieves and synthesizes information regarding **Factor Analysis** and latent variables from academic sources.

<p align="center">
  <img src="Screenshot 2026-01-09 233207.png" width="800" alt="Statistical Reasoning">
</p>

### 3. Contextual Feature Analysis
By leveraging hierarchical chunking, the system can distinguish between closely related concepts, such as **Feature Selection** and **Feature Extraction**, providing a comprehensive comparative analysis.

<p align="center">
  <img src="Screenshot 2026-01-09 233224.png" width="800" alt="Contextual Analysis">
</p>

---

## 🧠 Technical Deep Dive

Nexus-RAG is structured as a **Stateful Directed Acyclic Graph (DAG)**. Below is the breakdown of the core agentic nodes that drive the system:

### **A. The Orchestration Graph**
The "brain" of the project is built using **LangGraph**, which manages the following node logic:
* **`retrieve`**: Performs a hybrid search against the Qdrant database using child chunks.
* **`grade_documents`**: A critic agent that evaluates if the retrieved snippets are actually relevant to the user's query. It filters out "noise" to prevent hallucinations.
* **`transform_query`**: If the retrieved documents are insufficient, this node uses an LLM to rewrite the original query, optimizing it for a better search on the second pass.
* **`generate`**: The final synthesis node that takes the refined context and produces a structured, cited response.

### **B. Hierarchical Indexing Strategy**
To solve the "context vs. precision" trade-off, I implemented a **Parent-Child Chunking** strategy:
1.  **Child Chunks**: Small segments (e.g., 200-400 tokens) are used for high-granularity vector search.
2.  **Parent Context**: When a child is "hit," the system retrieves the entire parent section to provide the LLM with the full narrative context, significantly increasing the factual accuracy of the output.



---

## 🛠️ Installation & Setup

<h3>1. Clone the Project</h3>
  <pre><code>git clone https://github.com/anupam-iiitm/Nexus-RAG.git
cd Nexus-RAG</code></pre>

  <p><b>Alternative (if repository already initialized locally):</b></p>
  <pre><code>git init
git remote add origin https://github.com/anupam-iiitm/Nexus-RAG.git
git pull origin main</code></pre>

  <h3>2. Setup Python Environment</h3>
  <pre><code>python -m venv venv</code></pre>

  <p><b>Activate the environment:</b></p>

  <p>Windows</p>
  <pre><code>venv\Scripts\activate</code></pre>

  <p>Linux / macOS</p>
  <pre><code>source venv/bin/activate</code></pre>

  <p><b>Install dependencies:</b></p>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h3>3. Local LLM Configuration</h3>
  <p>Ensure <b>Ollama</b> is installed and pull the required model:</p>

  <pre><code>ollama pull qwen3:4b-instruct-2507-q4_K_M</code></pre>

  <h3>4. Launch the Application</h3>
  <pre><code>python project/app.py</code></pre>

  <hr />

  <p align="center">
    Developed by <b>Anupam Shukla</b><br /><br />
    <a href="https://github.com/anupam-iiitm" target="_blank">GitHub</a> •
    <a href="https://www.linkedin.com/in/your-linkedin-username/" target="_blank">LinkedIn</a>
  </p>
