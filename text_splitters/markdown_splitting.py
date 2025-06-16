from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text="""

# Use Case: AI-Powered Content Repurposing

## Overview
In today's fast-paced digital marketing landscape, brands struggle to keep up with content demand across platforms like Instagram, YouTube, LinkedIn, TikTok, and blogs. The challenge lies in not just producing enough content, but in tailoring it to the format, audience, and tone of each channel—without exhausting internal teams.

## The Problem
Marketing teams often repurpose content manually, which is labor-intensive, error-prone, and inconsistent in tone. This leads to wasted potential in existing content libraries and an inability to maintain a cohesive omnichannel presence.

## The Solution
An AI-powered content repurposing tool analyzes long-form assets (webinars, podcasts, blog posts) and transforms them into short-form versions optimized for different platforms:
- Video clips with auto-generated captions for social media
- Short blog summaries for email newsletters
- Quote graphics with context-aware background
- LinkedIn carousels summarizing key ideas

The tool uses LLMs to preserve brand voice and platform-specific formatting, applying prompt-engineered rules and recursive text parsing for long content input. It also scores content for engagement potential before exporting.

## Benefits
- Cut content production time by 70%
- Achieve consistent brand voice across channels
- Get 10–15 repurposed assets from every original piece
- Free up creative teams for strategy, not formatting

## Technical Highlights
- Uses RecursiveCharacterTextSplitter from LangChain for segmentation
- Integrates OpenAI's GPT model for summarization and tone control
- Outputs platform-ready JSON blocks for automated publishing



"""
splitter= RecursiveCharacterTextSplitter.from_language(
    language = Language.MARKDOWN,
    chunk_size=100,
    chunk_overlap=2
)

chunks= splitter.split_text(text)

print(chunks[0])