# 🚀 AIS Interview – Final Answers (GenAI + Project Focus)

This document contains **interview-ready spoken answers** based on mock session questions.

---

# ❓ 1. Explain your AI pipeline end-to-end

In my project, the pipeline starts when the user uploads a health report, which can be a PDF, Word, or text file.

First, I use OCR, specifically Tesseract, to extract text from the report. This extracted text is then processed and converted into embeddings using a pre-trained embedding model like OpenAI embeddings.

These embeddings are stored in a vector database, in my case using Supabase with vector support.

When the user asks a question, the query is also converted into an embedding. The system then performs a similarity search in the vector database to retrieve the most relevant context.

This context, along with the user’s query, is passed to the LLM, which generates a response.

So overall, the pipeline is: OCR → Embeddings → Vector DB → Retrieval → LLM Response.

---

# ❓ 2. How do you retrieve the most relevant data from the vector database?

When a user asks a question, the query is converted into an embedding.

The system then compares this embedding with stored embeddings in the vector database using similarity measures like cosine similarity.

The closest matching embeddings are retrieved as relevant context and passed to the model to generate an accurate response.

---

# ❓ 3. How do you handle hallucination in your system?

To reduce hallucination, I primarily rely on a RAG-based approach, where the model is grounded with real data from the vector database.

This ensures that responses are based on actual user data rather than assumptions.

Additionally, I use prompt engineering to guide the model to stay within context and avoid generating unsupported information.

If needed, fine-tuning or improving data quality can also help reduce hallucination.

---

# ❓ 4. How does LangChain fit into your system?

LangChain helps in managing the workflow of the entire system.

Instead of manually handling each step, like embedding generation, retrieval, and response generation, LangChain allows us to create structured chains that connect all these components.

It simplifies the process of building AI pipelines by handling prompts, retrieval, and model interaction in a modular way.

---

# ❓ 5. How would you handle scaling of your system?

To handle scaling, I would ensure that the vector database can efficiently handle large volumes of embeddings, either by optimizing indexing or using managed services.

For the LLM, I would rely on scalable API-based models that can handle multiple requests.

Additionally, techniques like caching frequently asked queries and optimizing retrieval can help maintain performance as the number of users increases.

---

# ❓ 6. How did you select your LLM?

While selecting the LLM, I focused on factors like context window, cost, latency, and reliability.

I chose a model that provided a good balance between performance and cost, while also ensuring fast response time and stable uptime.

Since my use case was health-related insights, I also ensured that the model could handle structured and contextual responses effectively.

---

# ❓ 7. What are embeddings and how did you use them?

Embeddings are numerical representations of text that capture semantic meaning.

In my system, I convert both the report data and user queries into embeddings.

These embeddings are stored in a vector database, and when a user asks a question, similarity search is used to find relevant data, which is then passed to the LLM.

---

# ❓ 8. Difference between LLM and RAG?

A standalone LLM generates responses based only on its training data, which can sometimes be outdated or generic.

RAG, on the other hand, enhances the model by retrieving relevant data from an external source before generating a response.

This makes the output more accurate, context-aware, and reduces hallucination.

---

# ❓ 9. What is an AI pipeline?

An AI pipeline is a sequence of steps that process user input and generate output.

In my case, it includes data ingestion, text extraction, embedding generation, data storage, retrieval, and response generation using an LLM.

It ensures smooth data flow from input to final output.

---

# ❓ 10. What is the role of a vector database?

A vector database stores embeddings and allows fast similarity search.

It helps in retrieving relevant context based on meaning rather than exact keywords, which is essential for building RAG-based systems.

---

# ❓ 11. How did you integrate all components of your system?

I structured the system in a modular way, where each component handled a specific task like OCR, embedding generation, storage, and retrieval.

These components were connected through APIs and function calls, allowing smooth data flow between them.

This modular design made it easier to manage and scale the system.

---

# ❓ 12. Biggest challenge and how you solved it?

One of the biggest challenges was maintaining context across user interactions.

Initially, the system only had temporary memory, and data was lost after each session.

I solved this by storing embeddings in a vector database, which allowed the system to retain historical data and provide context-aware responses.

This significantly improved user experience and system accuracy.

---

# 🎯 FINAL TIP

* Keep answers simple
* Use your project in every answer
* Speak slowly and confidently

---

⭐ You are interview-ready.
