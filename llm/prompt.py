def build_prompt(question, retrieved_chunks):
    context = ""
    for i, chunk in enumerate(retrieved_chunks):
        context += f"""
--- Chunk {i+1} ---
File: {chunk['file_path']}
Lines: {chunk['start_line']} to {chunk['end_line']}
Code:
{chunk['content']}
"""
    prompt = f"""You are an expert code assistant.
Answer the user's question using ONLY the provided code context below.
If the answer is not in the context, say "I couldn't find that in the codebase."
Always mention which file and line number the answer comes from.
CODE CONTEXT:
{context}
USER QUESTION:
{question}
ANSWER:  """
    
    return prompt