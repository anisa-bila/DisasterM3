## The Problem Statement

Large vision-language models (VLMs) have been shown to achieve good performance in analyzing large-scale satellite imagery and geospatial analysis. In the case of natural disasters, structural damage assessment, disaster-specific impact evaluation, diverse regional analysis, and long-term disaster reports are of concern. However, VLMs are devoid of an in-depth understanding of disaster scenarios due to the lack of specialized disaster-related datasets and training data.

## The Solution

DisasterM3 aims to be a remote sensing vision-language dataset that covers various disaster assessment and responses. It is based on large-scale data involving major historical disaster impacts and multi-sensor data for post-disaster imagery. Perception and reasoning tasks serve as input to encourage and maximize the VLM's reasoning ability to better understand disaster-related objects and relationships.

Furthermore, DisasterM3 supplies input to the models with different reasoning tasks in the context of natural disaster cases. These include prompts related to disaster recognition, damage analysis, disaster referring segmentation, damaged object reasoning, and a comprehensive disaster report. 

## Experimentation and Results

After the design and implementation of DisasterM3's pipeline, benchmark experiments were conducted across various models, ranging from fourteen open source models, two commercial models, and four fine-tuned models. The broad selection of models allows a strong comparison of diverse models being tested with disaster-focused data, with the focus of understanding systems that generate poor outcomes.

Larger VLMs comprise strong reasoning, which resulted in superior performances. On the other hand, some existing VLMs are still unable to fully grasp disaster tasks. With the fine-tuning of models, their generated reports have significantly improved. Other models that undergo degradation in these changes will require further deep investigations in future development.

## References

    Wang, Junjue, et al. “DisasterM3: A Remote Sensing Vision-Language Dataset for Disaster Damage Assessment and Response.” ArXiv.org, 2025, arxiv.org/abs/2505.21089.
    Wang, Junjue, et al. “EarthVL: A Progressive Earth Vision-Language Understanding and Generation Framework.” ArXiv.org, 2026, arxiv.org/abs/2601.02783. Accessed 28 May 2026.
