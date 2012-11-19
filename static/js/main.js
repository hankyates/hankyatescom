$(window).on('load', function(){
  require.config({
      urlArgs: "cache=disabled" + (new Date()).getTime()
  });

  require([
    'static/js/page'
    ], function(){
      var pages = new Pages();
      var page_view = new PageView({collection: pages});

      pages.fetch({
        success: function(){
          page_view.render();
        }
      });
  });
});
