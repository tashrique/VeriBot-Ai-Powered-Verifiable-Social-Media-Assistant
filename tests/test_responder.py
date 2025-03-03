"""
Tests for the responder module.
"""

import pytest
from veribot.ai.responder import filter_ai_response, inject_real_projects

def test_filter_ai_response_safe():
    """Test filtering of safe AI responses."""
    response = "Blockchain technology provides a secure and transparent way to record transactions."
    filtered = filter_ai_response(response)
    assert filtered == response

def test_filter_ai_response_unsafe():
    """Test filtering of unsafe AI responses."""
    response = "This token is going to pump and dump soon, buy now!"
    filtered = filter_ai_response(response)
    assert "⚠️ This response was flagged" in filtered

def test_filter_ai_response_too_long():
    """Test filtering of too long AI responses."""
    response = "A" * 300  # Create a string longer than 280 characters
    filtered = filter_ai_response(response)
    assert len(filtered) <= 280
    assert filtered.endswith("...")

def test_inject_real_projects():
    """Test injection of real project names."""
    response = "You might want to check out [Project A] and [Project B] for DeFi solutions."
    injected = inject_real_projects(response)
    assert "[Project A]" not in injected
    assert "[Project B]" not in injected 