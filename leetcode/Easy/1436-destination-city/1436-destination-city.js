/**
 * @param {string[][]} paths
 * @return {string}
 */
var destCity = function (paths) {
  let start = new Set();
  let end = new Set();
  for (path of paths) {
    let s = path[0];
    let e = path[1];
    start.add(s);
    end.add(e);
  }
  return [...end].filter((x) => !start.has(x))[0];
};
