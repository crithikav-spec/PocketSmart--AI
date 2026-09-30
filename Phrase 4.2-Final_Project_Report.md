# PocketSmartAI: Final Project Report

## Executive Summary
PocketSmartAI successfully integrates FastAPI with Gemini 1.5 Flash Pro to deliver cross-platform, budget-tailored recommendations for home decor, party planning, and apparel matching.

## Architecture & Workflow
1. **Frontend**: Jinja2 HTML templates collect user constraints and outfit images.
2. **Backend**: FastAPI routes handle requests, manage sessions, and invoke the generative model.
3. **AI Engine**: Gemini 1.5 Flash Pro parses text/images and maps outputs to platform-specific options (Amazon, Flipkart, IKEA, Zomato).

## Conclusion
The project demonstrates an end-to-end GenAI application capable of automating complex multi-category financial planning.