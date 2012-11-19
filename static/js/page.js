define([], function(){
  Page = Backbone.Model.extend({
    defaults: function() {
      return {
        title: "empty todo...",
        visible: false
      };
    },

    initialize: function() {
      if (!this.get("title")) {
        this.set({"title": this.defaults.title});
      }
    },

    toggle: function() {
      this.save({done: !this.get("done")});
    },

    clear: function() {
      this.destroy();
    }
  });

  Pages = Backbone.Collection.extend({
    model: Page,
    url: '/pages'
  });

  PageView = Backbone.View.extend({
    tagName:  "div",
    el: $("#main"),

    template: _.template($('#page-home').html()),

    events: {
    },

    initialize: function() {
    },

    render: function() {
      var collection = this.collection,
          model = this.model,
          self = this;
      if(model){
        this.$el.html(this.template(model.toJSON()));
      }else if(collection){
        collection.each(function(item){
          self.$el.html(self.template(item.toJSON()));
        })
      }

      return this;
    },
  });
});
