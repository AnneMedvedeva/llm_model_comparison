"""
File handling utilities
Manages saving results to JSON and Markdown files
"""

import json
import sys
import os
from typing import List, Dict, Any
from output_formatter import create_json_output, create_markdown_output


def save_results_to_files(file_output: str, prompt: str, models: List[str], results: List[Dict[str, Any]]) -> None:
    """Save results to both JSON and Markdown files in ../output directory."""
    # Create output directory if it doesn't exist
    output_dir = "../output"
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"📁 Created directory: {output_dir}")
        except Exception as e:
            print(f"❌ Error creating output directory: {e}", file=sys.stderr)
            return
    
    # Determine file paths
    base_name = file_output
    if base_name.endswith('.json'):
        base_name = base_name[:-5]  # Remove .json extension
    elif base_name.endswith('.md'):
        base_name = base_name[:-3]  # Remove .md extension
    
    json_file = os.path.join(output_dir, f"{base_name}.json")
    md_file = os.path.join(output_dir, f"{base_name}.md")
    
    # Save JSON file
    try:
        json_data = create_json_output(prompt, models, results)
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        print(f"\n✅ JSON results saved to {json_file}")
    except Exception as e:
        print(f"\n❌ Error saving JSON file: {e}", file=sys.stderr)
    
    # Save Markdown file
    try:
        md_content = create_markdown_output(prompt, results)
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"✅ Markdown results saved to {md_file}")
    except Exception as e:
        print(f"❌ Error saving Markdown file: {e}", file=sys.stderr)