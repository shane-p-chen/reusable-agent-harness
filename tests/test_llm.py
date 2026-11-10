from unittest.mock import MagicMock, patch

import pytest

from agent_core.llm import ask_model

def test_missing_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="OPENAI_API_KEY is missing"):
        ask_model("Hello")

@patch("agent_core.llm.OpenAI")
def test_ask_model_returns_response(mock_openai, monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")

    fake_response = MagicMock()
    fake_response.output_text = "Hello from the model!"

    mock_client = mock_openai.return_value
    mock_client.responses.create.return_value = fake_response

    result = ask_model("Say hello")

    assert result == "Hello from the model!"

    mock_client.responses.create.assert_called_once_with(
        model="gpt-4.1-mini",
        instructions="You are a helpful AI assistant.",
        input="Say hello",
    )