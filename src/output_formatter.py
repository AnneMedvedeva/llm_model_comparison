"""
Output formatting utilities
Handles console output, JSON, and Markdown formatting
"""

import time
import json
from typing import List, Dict, Any


def format_console_output(result: Dict[str, Any]) -> str:
    """Format the result for console display."""
    if not result["success"]:
        return f"\n{'='*60}\nModel: {result['model']}\nLatency: {result['latency']:.2f}s\nERROR: {result['error']}\n{'='*60}"
    
    tokens = result["tokens"]
    output = f"\n{'='*60}\n"
    output += f"Model: {result['model']}\n"
    output += f"Latency: {result['latency']:.2f}s\n"
    output += f"Tokens: {tokens['prompt']} prompt + {tokens['completion']} completion = {tokens['total']} total\n"
    output += f"{'='*60}\n"
    output += f"{result['response']}\n"
    output += f"{'='*60}"
    
    return output


def create_markdown_output(prompt: str, results: List[Dict[str, Any]]) -> str:
    """Create markdown formatted output."""
    md_content = f"# Model Comparison Results\n\n"
    md_content += f"**Question:** {prompt}\n\n"
    md_content += f"**Generated:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    md_content += "---\n\n"
    
    for i, result in enumerate(results, 1):
        md_content += f"## {i}. {result['model']}\n\n"
        
        if result["success"]:
            tokens = result["tokens"]
            md_content += f"**Tokens:** {tokens['prompt']} prompt + {tokens['completion']} completion = {tokens['total']} total\n\n"
            md_content += f"{result['response']}\n\n"
        else:
            md_content += f"**Error:** {result['error']}\n\n"
        
        md_content += "---\n\n"
    
    return md_content


def create_json_output(prompt: str, models: List[str], results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Create JSON formatted output."""
    return {
        "metadata": {
            "prompt": prompt,
            "models": models,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_models": len(models),
            "successful_responses": sum(1 for r in results if r["success"])
        },
        "results": results
    }
