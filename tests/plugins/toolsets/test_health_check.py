from holmes.plugins.toolsets.grafana.loki.toolset_grafana_loki import (
    GrafanaLokiToolset,
)
from holmes.plugins.toolsets.grafana.toolset_grafana_tempo import GrafanaTempoToolset
from holmes.plugins.toolsets.prometheus.prometheus import PrometheusToolset


class TestHealthCheck:
    def test_grafana_loki(self):
        """Test that CoreInvestigationToolset is created correctly."""
        glts = GrafanaLokiToolset()
        assert glts.prerequisites_callable({"url": "http://localhost:3100"}) == (
            True,
            "",
        )

    def test_grafana_tempo(self):
        """Test that the toolset includes the TodoWrite tool."""
        gtts = GrafanaTempoToolset()
        assert gtts.prerequisites_callable({"url": "http://localhost:3201"}) == (
            True,
            "",
        )

    def test_grafana_mimir(self):
        """Test that the toolset includes the TodoWrite tool."""
        gtts = PrometheusToolset()
        assert gtts.prerequisites_callable(
            {"prometheus_url": "http://localhost:9009"}
        ) == (
            True,
            "",
        )
