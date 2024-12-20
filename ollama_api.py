import subprocess

def query_ai(prompt):
    """
    Sends a prompt to the Ollama AI model and retrieves the response.
    """
    try:
        # Run the Ollama command
        result = subprocess.run(
            ["ollama", "run", "qwen2:1.5b"],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check for errors
        if result.returncode != 0:
            return f"Error: {result.stderr.strip()}"
        
        # Return the AI's response
        return result.stdout.strip()
    
    except Exception as e:
        return f"Exception occurred: {str(e)}"
