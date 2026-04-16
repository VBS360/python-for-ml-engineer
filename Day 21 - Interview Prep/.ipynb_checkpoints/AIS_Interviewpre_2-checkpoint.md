# 🚀 AIS Interview – Deep Technical Answers (Final Prep)

---

# ❓ 1. Explain your system and AI’s role in decision-making

> “In my project, I built a health report analyzer combined with a chatbot system.
>
> The pipeline starts when a user uploads a report, which is processed using OCR (Tesseract) to extract text. This text is then converted into embeddings and stored in a vector database.
>
> When a user asks a question, the query is also converted into embeddings, and relevant context is retrieved using similarity search. This context is passed to the LLM to generate accurate responses.
>
> Additionally, I integrated mental health assessments (PHQ-9, WHO-5, self-reflection) and behavioral inputs like diary entries and chat sentiment.
>
> I combined these inputs into a structured decision layer that determines whether the user may require lifestyle changes.
>
> The LLM then uses this structured context to generate personalized recommendations.
>
> So, the AI’s role was both analytical (through structured inputs) and conversational (through LLM responses).”

---

# ❓ 2. How did you implement RAG and handle edge cases?

> “I implemented a user-specific RAG system where each user’s data—health reports, mental assessments, and diary entries—was stored as embeddings.
>
> When a query is made, the system retrieves the most relevant context using similarity search, typically cosine similarity.
>
> For edge cases where insufficient data is available, such as a new user, I implemented baseline logic using predefined medical ranges to provide meaningful insights.
>
> This ensures the system can still provide useful responses even when historical data is limited.”

---

# ❓ 3. How did you ensure recommendations were accurate and trustworthy?

> “I ensured reliability through a combination of prompt engineering, testing, and user feedback.
>
> I used a pre-trained LLM (LLaMA) and designed structured prompts with clear boundaries, including tone, response format, and context usage.
>
> Initially, I observed issues like hallucination and generic responses. To address this, I refined prompts to ensure the model strictly used retrieved context.
>
> I also tested the system with real users (friends and family) and iteratively improved it based on feedback.
>
> This combination of prompt control, real-world testing, and iterative improvement helped ensure trustworthy outputs.”

---

# ❓ 4. How did you ensure data privacy and security?

> “Since the system handles sensitive health data, I focused on multiple layers of security.
>
> I used Supabase as the backend, which provides strong access control and database security.
>
> Sensitive user data such as reports and conversations were stored securely, with encryption applied to chatbot interactions.
>
> Additionally, most processing was done using embeddings, which store data in numerical form, adding an abstraction layer.
>
> Overall, I ensured that user data was securely stored, access-controlled, and not directly exposed.”

---

# ❓ 5. How did you integrate all components of your system?

> “I designed the system in a modular way, where each component handled a specific task.
>
> OCR handled text extraction, embedding models converted data into vectors, the vector database handled storage and retrieval, and the LLM handled response generation.
>
> These components were connected through APIs and function calls, ensuring smooth data flow across the pipeline.
>
> This modular approach made the system easier to manage, debug, and scale.”

---

# ❓ 6. How did you validate your system’s performance?

> “I validated the system using both manual testing and real user feedback.
>
> Initially, I tested different scenarios myself to identify issues like hallucination or irrelevant responses.
>
> Then I onboarded a small group of users who tested the system and provided feedback.
>
> Based on this feedback, I refined prompt structures and retrieval logic.
>
> This iterative testing helped improve both accuracy and user experience.”

---

# 🎯 FINAL STRATEGY

* Speak calmly
* Don’t over-explain
* Always connect answer to your project
* Use phrases like:

  * “At a high level…”
  * “In my system…”

---

# 🔥 FINAL ONE-LINER

> “I focused on building a reliable AI pipeline by combining structured logic with LLM-based reasoning.”

---

⭐ You are now fully ready for AIS interview.
