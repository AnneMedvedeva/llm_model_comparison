# ai_model_comparison
Python program that compares responses from different AI models via OpenRouter


---
Models I used:
```
DEFAULT_MODELS = [
        "openai/gpt-3.5-turbo",
        "anthropic/claude-3.5-haiku",
        "meta-llama/llama-3.3-70b-instruct:free",
        "deepseek/deepseek-chat-v3-0324:free",
        "google/gemini-2.0-flash-001"
    ]
```
Example command: `python3 compare_models.py --prompt "I need a formal request to get an approval for attached document in email." --file-output formal_test_prompts`


---

### Question 1: `Which Transformer component most directly enables parallel training, and why?`

Simple answer: `Self-attention`. \
Explored `why?` answers in [Model Comparison Results File](output/q1_transformer_components.md)

---

### Question 2: `After comparing system prompts, list three recurring design patterns you observed.`

Recurring design patterns I personally noticed were:

1) Role definition (e.g., 'You are a helpful assistant/You are an expert in X').

2) Many prompts include tone/style instructions (e.g., 'Answer concisely/Simplify/Answer with formal language').

3) Ethical guidelines (e.g., 'Do not provide harmful advice').

4) (Bonus) Formatted responses (e.g. bullet points, lists, step-by-step explanations)

---

### Question 3: `How did different models vary in tone, length, or factuality for the same prompt?`

> <b>Friendly check</b>: [`Heyy! Can you please help me understand self-attention in simple terms? Thank you`](output/friendly_test_prompts.md) \
> <b>Formal check</b>: [`I need a formal request to get an approval for attached document in email.`](output/formal_test_prompts.md) \
> <b>Creative non-technical</b>: [`Hello, I need 3 ideas for children storybook`](output/creative_test_prompts.md) \
> <b>Creative technical</b>: [`Explain transformers to a 5‑year‑old (as in AI/LLM transformer)`](output/q4_comparison.md) \
> <b>Technical</b>: [`Explain photosynthesis to a college student`](output/q3_comparison.md)


> Factual checks varied:
> - <b>Standard historical data</b>: [`When was the first moon landing, and which country achieved it?`](output/factual_test_1_prompts.md)
> - <b>Current data</b>: [`As of 2025, who is the CEO of Tesla?`](output/factual_test_2_prompts.md)
> - <b>Riddle test</b>: `Riddle used from: https://medium.com/@htobochnik/mathematical-problem-solving-that-chatgpt-cant-do-a3c83e935c6b` [Result Output](output/solving_riddle_test_prompts.md)


##### <b>GPT 3.5 (openai/gpt-3.5-turbo)</b>

> <b>Tone</b>: adaptive, longer sentences and formal \
> <b>Length</b>: Average word count: ~88 \
> <b>Format</b>: Minimal formatting, no lists, 1-2 paragraphs max. \
> <b>Factuality</b>: Standard✅ | Current✅ | Riddle❌

##### <b>Claude 3.5 (anthropic/claude-3.5-haiku)</b>

> <b>Tone</b>: less adaptive, shorter sentences, and formal \
> <b>Length</b>: Average word count: ~167 \
> <b>Format</b>: Formatting in steps and clear lists of relative information \
> <b>Factuality</b>: Standard✅ | Current✅ | Riddle❌

##### <b>Llama 3.3 (meta-llama/llama-3.3-70b-instruct)</b>

> <b>Tone</b>: less adaptive, longer sentences, formal \
> <b>Length</b>: Average word count: ~308 (more expanded on technical prompts, less on creative non-technical prompts)\
> <b>Format</b>: Formatting in sentences, similar to GPT 3.5, sometimes including simple lists in middle\
> <b>Factuality</b>: Standard✅ | Current✅ | Riddle❌

##### <b>Deepseek V3 (deepseek/deepseek-chat-v3-0324)</b>

> <b>Tone</b>: adaptive, short sentences, friendly most of the cases\
> <b>Length</b>: Average word count: ~208\
> <b>Format</b>: Formatting in short sentences, usually lists and bullet points, includes rich formatting including boldening/emojis\
> <b>Factuality</b>: Standard✅ | Current✅ | Riddle✅

##### <b>Gemini 2.0 (google/gemini-2.0-flash-001)</b>

> <b>Tone</b>: adaptive, longer sentences, formal mostly\
> <b>Length</b>: Average word count: ~460 (more expanded on technical prompts, less on creative non-technical prompts)\
> <b>Format</b>: Formatting in longer sentences, including lists and bullet points in most cases\
> <b>Factuality</b>: Standard✅ | Current✅ | Riddle✅



