// Redirect URLs that used to be served from fenicsproject.org but have since
// moved elsewhere. Anything not matched here falls through to the 404 page.
(function () {
  var prefixes = [
    ["pub/", "https://a654cc05c43271a5d22f-f8befe5e0dcd44ae0dccf352c00b4664.ssl.cf5.rackcdn.com/"],
    ["olddocs/", "https://olddocs.fenicsproject.org/"],
    ["qa/", "https://oldqa.fenicsproject.org/"]
  ];

  var url = document.location.href.replace(/^https?:\/\//, "").replace(/^www\./, "");
  if (url.indexOf("fenicsproject.org/") === 0) {
    url = url.substring("fenicsproject.org/".length);
  }

  for (var i = 0; i < prefixes.length; i++) {
    var prefix = prefixes[i][0];
    var target = prefixes[i][1];
    if (url === prefix.slice(0, -1)) {
      window.location.assign(target);
      return;
    }
    if (url.indexOf(prefix) === 0) {
      window.location.assign(target + url.substring(prefix.length));
      return;
    }
  }
})();
