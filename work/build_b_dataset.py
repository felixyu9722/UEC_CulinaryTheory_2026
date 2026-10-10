# -*- coding: utf-8 -*-
"""
build_b_dataset.py
Builds the authentic, natural UEC-style question bank for Version B (B版).
Zero forced sentence length constraints. Natural questions based on UEC past papers and standard syllabus.
"""
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

# We will define or refine the 15 questions per unit.
print("Building dataset...")
