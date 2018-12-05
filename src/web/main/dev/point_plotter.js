var points = svg.append('g');

points.selectAll('path')
  .data('data/test_results_geo_small.json'.features).enter()
  .append('path')
  .attr('fill', '#900')
  .attr('stroke', '#999')
  .attr('d', geoPath);
