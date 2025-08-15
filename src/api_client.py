"""
API Client for OpenRouter
Handles all API communication and response processing
"""

import time
import requests
import json
from typing import Dict, Any


def query_model(model_id: str, prompt: str, api_key: str) -> Dict[str, Any]:
    """Query a single model and return response with metadata."""
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/your-username/model-comparison",  # Optional
        "X-Title": "Model Comparison Tool"  # Optional
    }
    
    payload = {
        "model": model_id,
        "messages": [
            {
                "role": "user", 
                "content": prompt
            }
        ]
    }
    
    start_time = time.time()
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        
        end_time = time.time()
        latency = end_time - start_time
        
        data = response.json()
        
        return {
            "success": True,
            "model": model_id,
            "response": data["choices"][0]["message"]["content"],
            "latency": latency,
            "tokens": {
                "prompt": data.get("usage", {}).get("prompt_tokens", 0),
                "completion": data.get("usage", {}).get("completion_tokens", 0),
                "total": data.get("usage", {}).get("total_tokens", 0)
            }
        }
        
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "model": model_id,
            "error": str(e),
            "latency": time.time() - start_time
        }
    except (KeyError, json.JSONDecodeError) as e:
        return {
            "success": False,
            "model": model_id,
            "error": f"Invalid response format: {str(e)}",
            "latency": time.time() - start_time
        }
