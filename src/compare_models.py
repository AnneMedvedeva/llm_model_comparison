#!/usr/bin/env python3
"""
AI Model Comparison Tool
Compares responses from multiple AI models via OpenRouter API
"""

import argparse
import os
import sys
from typing import List

# Import our modules
from api_client import query_model
from output_formatter import format_console_output
from file_utils import save_results_to_files


def get_api_key() -> str:
    """Get API key from environment variable."""
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        print("Error: OPENROUTER_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)
    return api_key


def get_prompt_input(args) -> str:
    """Get prompt from command line args or stdin."""
    if args.prompt:
        return args.prompt
    else:
        # Check if there's data available in stdin
        if not sys.stdin.isatty():
            # Data is being piped in
            prompt = sys.stdin.read().strip()
            if not prompt:
                print("Error: No prompt provided via stdin", file=sys.stderr)
                sys.exit(1)
            return prompt
        else:
            # No prompt flag and no piped input
            print("Error: Please provide a prompt using --prompt flag or pipe input", file=sys.stderr)
            print("Usage examples:")
            print("  python compare_models.py --prompt 'Your question here'")
            print("  echo 'Your question' | python compare_models.py")
            sys.exit(1)


def main():
    # Default model trio (updated with correct OpenRouter model IDs)
    DEFAULT_MODELS = [
        "openai/gpt-3.5-turbo",
        "anthropic/claude-3.5-haiku",
        "meta-llama/llama-3.3-70b-instruct:free",
        # "x-ai/grok-3",
        "deepseek/deepseek-chat-v3-0324:free",
        "google/gemini-2.0-flash-001"
    ]
    
    parser = argparse.ArgumentParser(description="Compare responses from multiple AI models")
    parser.add_argument(
        "--models",
        type=str,
        help="Comma-separated list of model IDs to query"
    )
    parser.add_argument(
        "--prompt",
        type=str,
        help="Input prompt for the models"
    )
    parser.add_argument(
        "--file-output",
        type=str,
        help="Save results to JSON and Markdown files (e.g., --file-output results)"
    )
    
    args = parser.parse_args()
    
    # Determine models to use
    if args.models:
        models = [model.strip() for model in args.models.split(',')]
    else:
        models = DEFAULT_MODELS
    
    # Get prompt
    prompt = get_prompt_input(args)
    
    # Get API key
    api_key = get_api_key()
    
    print(f"Querying {len(models)} models with prompt: '{prompt[:50]}{'...' if len(prompt) > 50 else ''}'")
    print(f"Models: {', '.join(models)}")
    
    # Query all models
    results = []
    for model in models:
        print(f"\nQuerying {model}...")
        result = query_model(model, prompt, api_key)
        results.append(result)
    
    # Print results to console
    print("\n" + "="*80)
    print("RESULTS")
    print("="*80)
    
    for result in results:
        print(format_console_output(result))
    
    # Save to files if requested
    if args.file_output:
        save_results_to_files(args.file_output, prompt, models, results)


if __name__ == "__main__":
    main()