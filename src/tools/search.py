from src.core.llm_provider import LLMProvider

def search_with_llm(args_str: str, llm: LLMProvider) -> str:
    """
    Tool tìm kiếm giáo trình/tài liệu học tập sử dụng LLM.
    Trả về một danh sách các chủ đề ngắn gọn.
    """
    args_str = args_str.strip("'\" ")
    if not args_str:
        return "Error: Search query cannot be empty. Please provide a topic."
        
    # Xây dựng System Prompt & User Prompt (Tiếng Anh để output chuẩn hơn)
    system_prompt = """
        You are an expert curriculum search engine.
        Your task is to extract the underlying subject from the user's input (even if it is a statement, complaint, or question) and provide a concise, structured syllabus.
        
        RULES:
        1. ALWAYS return a numbered list of core topics to study. NEVER refuse or say materials are not found.
        2. If the user expresses difficulty (e.g., "X is hard"), provide a beginner-friendly breakdown of X to make it easier.
        3. If the input is completely random and lacks a specific subject (e.g., "hello", "I like cats"), provide a generic "Effective Study Skills and Problem Solving" syllabus.
        4. Keep it VERY brief and highly focused (maximum 5 main bullet points).
        5. ABSOLUTELY NO introductory or concluding remarks. Just output the numbered list directly.
        """

    user_prompt = f"Search query: '{args_str}'"
    
    try:
        # Gọi LLM
        result_dict = llm.generate(prompt=user_prompt, system_prompt=system_prompt)
        
        # Trích xuất và dọn dẹp text
        llm_response = result_dict["content"].strip()
        
        return llm_response
        
    except Exception as e:
        return f"Error executing Search Tool: {str(e)}"
