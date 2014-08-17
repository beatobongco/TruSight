function fetchKeen(analysis, event_collect, div, chart_options, filters, target, groupby){
  var targets = ['minimum', 'maximum', 'count_unique', 'average', 'median']
  var gb = ''
  if(groupby != "null"){
    gb = groupby
  }
  if(targets.indexOf(analysis) == -1){
    var query = new Keen.Query(analysis, {
      eventCollection: event_collect,
      filters: filters,
      groupBy: gb
    })
  }
  else{
    var query = new Keen.Query(analysis, {
      eventCollection: event_collect,
      filters: filters,
      targetProperty: target
    })
  }

  keen_client.draw(query, document.getElementById(div), chart_options)
}