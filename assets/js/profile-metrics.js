(function () {
  var metricsUrl =
    "https://raw.githubusercontent.com/JackieWang9811/JackieWang9811.github.io/master/_data/profile_metrics.yml";

  function parseMetrics(text) {
    return text.split(/\r?\n/).reduce(function (metrics, line) {
      var match = line.match(/^([a-z_]+):\s*["']?([^"']*)["']?\s*$/);
      if (match && match[2]) {
        metrics[match[1]] = match[2];
      }
      return metrics;
    }, {});
  }

  function updateMetric(key, value) {
    var nodes = document.querySelectorAll('[data-profile-metric="' + key + '"]');
    Array.prototype.forEach.call(nodes, function (node) {
      node.textContent = value;
    });
  }

  fetch(metricsUrl + "?t=" + Date.now(), { cache: "no-store" })
    .then(function (response) {
      if (!response.ok) {
        throw new Error("Unable to fetch profile metrics");
      }
      return response.text();
    })
    .then(parseMetrics)
    .then(function (metrics) {
      updateMetric("google_scholar_citations", metrics.google_scholar_citations);
      updateMetric("github_stars", metrics.github_stars);
      updateMetric("csdn_views", metrics.csdn_views);
    })
    .catch(function () {
      // Keep the statically rendered fallback values.
    });
})();
