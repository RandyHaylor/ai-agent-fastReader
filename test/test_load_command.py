import os
import shutil
import tempfile
import json
import pytest
from src.fastReader.commands.load import run_load
from src.fastReader.cache import generate_hash
from src.fastReader.models import Document

def test_run_load_basic():
    """T21-T26: Verify run_load returns manifest_id and count summary."""
    cache_dir = tempfile.mkdtemp()
    try:
        stdin_text = "# Chapter 1\nContent line\n## Section A\nMore content"
        config = {
            "chapter": {"patterns": ["^# "]},
            "section": {"patterns": ["^## "]},
            "subsection": {"patterns": []},
            "page_break": {"patterns": []},
            "page": {"patterns": []},
            "double_line_break": {"patterns": []},
            "block": {"size": 800}
        }

        result = run_load(stdin_text, cache_dir, config)

        # Check manifest_id is 8-char hash
        h = generate_hash(stdin_text)
        assert result["manifest_id"] == h
        assert len(h) == 8

        # Check summary contains counts
        assert "summary" in result
        summary = result["summary"]
        assert "chapters" in summary
        assert "sections" in summary
        assert summary["chapters"] == 1
        assert summary["sections"] == 1

    finally:
        shutil.rmtree(cache_dir)

def test_run_load_empty_document():
    """T26: run_load with empty document returns summary with zero counts."""
    cache_dir = tempfile.mkdtemp()
    try:
        stdin_text = ""
        config = {
            "chapter": {"patterns": ["^# "]},
            "section": {"patterns": ["^## "]},
            "subsection": {"patterns": []},
            "page_break": {"patterns": []},
            "page": {"patterns": []},
            "double_line_break": {"patterns": []},
            "block": {"size": 800}
        }
        result = run_load(stdin_text, cache_dir, config)
        assert "manifest_id" in result
        assert "summary" in result
        assert result["summary"]["chapters"] == 0
        assert result["summary"]["sections"] == 0
    finally:
        shutil.rmtree(cache_dir)
