(function () {
  var metricsUrl =
    "https://api.github.com/repos/JackieWang9811/JackieWang9811.github.io/contents/_data/profile_metrics.yml?ref=master";

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
    if (!value) {
      return;
    }
    var nodes = document.querySelectorAll('[data-profile-metric="' + key + '"]');
    Array.prototype.forEach.call(nodes, function (node) {
      node.textContent = value;
    });
  }

  function updateProjectStars() {
    var starNodes = document.querySelectorAll("[data-github-stars]");
    Array.prototype.forEach.call(starNodes, function (node) {
      var repo = node.getAttribute("data-github-stars");
      if (!repo) {
        return;
      }

      fetch("https://api.github.com/repos/" + repo, { cache: "no-store" })
        .then(function (response) {
          if (!response.ok) {
            throw new Error("Unable to fetch repository stars");
          }
          return response.json();
        })
        .then(function (repoInfo) {
          if (typeof repoInfo.stargazers_count === "number") {
            node.textContent = repoInfo.stargazers_count.toLocaleString();
          }
        })
        .catch(function () {
          // Keep the statically rendered fallback value.
        });
    });
  }

  fetch(metricsUrl, { cache: "no-store" })
    .then(function (response) {
      if (!response.ok) {
        throw new Error("Unable to fetch profile metrics");
      }
      return response.json();
    })
    .then(function (payload) {
      return atob(payload.content.replace(/\s/g, ""));
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

  updateProjectStars();
})();
