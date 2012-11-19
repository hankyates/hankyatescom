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
