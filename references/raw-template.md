---
title: "{{title}}"
type: image|video|audio|text|diary
source_url: "{{source_url}}"
collected_date: "{{collected_date}}"
published_date: "{{published_date}}"
media_type: "{{media_type}}"
media_path: "{{media_path}}"
transcript: |
  {{transcript_if_audio_video}}
tags:
  - tag1
  - tag2
---

# {{title}}

## Description

{{description_generated_by_vlm}}

## Key Information

- **Date**: {{date}}
- **Location**: {{location_if_available}}
- **People**: {{people_identified}}
- **Activities**: {{activities_shown}}

## Transcript

{{transcript_if_audio_video}}

## Notes

{{additional_notes}}
