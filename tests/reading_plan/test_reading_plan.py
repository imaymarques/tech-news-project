from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import MagicMock, patch

data_mock = [
    {
        "url": "https://blog.betrybe.com/novidades/noticia_7.htm",
        "title": "noticia_7",
        "timestamp": "23/11/2020",
        "writer": "Escritor_7",
        "reading_time": 7,
        "summary": "Sumario da noticia_1",
        "category": "Desenvolvimento web",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_8.htm",
        "title": "noticia_8",
        "timestamp": "23/11/2020",
        "writer": "Escritor_7",
        "reading_time": 8,
        "summary": "Sumario da noticia_8",
        "category": "Desenvolvimento web",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_9.htm",
        "title": "noticia_9",
        "timestamp": "23/11/2020",
        "writer": "Escritor_7",
        "reading_time": 5,
        "summary": "Sumario da noticia_9",
        "category": "Linguagem de programação",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_10.htm",
        "title": "noticia_10",
        "timestamp": "23/11/2020",
        "writer": "Escritor_7",
        "reading_time": 25,
        "summary": "Sumario da noticia_10",
        "category": "Linguagem de programação",
    }
]


def test_reading_plan_group_news():
    mock_news = MagicMock(return_value=data_mock)
    with patch.object(
        ReadingPlanService, "_db_news_proxy", mock_news
    ):
        result = ReadingPlanService.group_news_for_available_time(21)
        assert result == {
            "readable": [
                {
                    "unfilled_time": 1,
                    "chosen_news": [
                        ("noticia_7", 7),
                        ("noticia_8", 8),
                        ("noticia_9", 5)
                    ]
                },
            ],
            "unreadable": [("noticia_10", 25)]
        }

    with pytest.raises(
        ValueError, match="'available_time' deve ser maior que zero"
    ):
        with patch.object(
            ReadingPlanService, "_db_news_proxy", mock_news
        ):
            ReadingPlanService.group_news_for_available_time(-21)
