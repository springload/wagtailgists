
(function() {
  (function($) {
    return $.widget("IKS.togglemarkdown", {
      options: {
        uuid: '',
        editable: null
      },
      populateToolbar: function(toolbar) {
        var button, widget;
 
        widget = this;
        button = $('<span></span>');
        button.hallobutton({
          uuid: this.options.uuid,
          editable: this.options.editable,
          label: 'Show Markdown editor',
          icon: 'fa fa-toggle-off',
          command: null
        });
        toolbar.append(button);
        return button.on("click", function(event) {
          var icon_off = $(this).find("i.fa-toggle-off").first();
          var icon_on = $(this).find("i.fa-toggle-on").first();
          icon_off.switchClass( "fa-toggle-off", "fa-toggle-on");
          icon_on.switchClass( "fa-toggle-on", "fa-toggle-off");
          var parent = widget.element.parent().first();
          var markdown_hidden = parent.children("textarea.markdown.hidden");
          var markdown_visible = parent.children("textarea.markdown.visible");
          markdown_hidden.switchClass( "hidden", "visible");
          markdown_visible.switchClass( "visible", "hidden");
          return widget.options.editable.element.trigger('change');
          
        });
      }
    });
  })(jQuery);
 
}).call(this);

jQuery(document).ready(function() {

  $( ".richtext" ).each(function( index ) {
    var markdownTextArea = $('<textarea class="markdown hidden"></textarea>').html($(this).html());
    markdownTextArea.insertAfter($(this));
    // Update Markdown every time content is modified
    var richtext = $(this)
    richtext.bind('hallomodified', function(event, data) {
      showSource(data.content, markdownTextArea);
    });
    markdownTextArea.bind('keyup', function() {
      updateHtml(this.value, richtext);
    });
  });


  var markdownize = function(content) {
    var html = content.split("\n").map($.trim).filter(function(line) { 
      return line != "";
    }).join("\n");
    return toMarkdown(html);
  };

  var converter = new Showdown.converter();
  var htmlize = function(content) {
    return converter.makeHtml(content);
  };

  // Method that converts the HTML contents to Markdown
  var showSource = function(content, markdownTextArea) {
    var markdown = markdownize(content);
    if (markdownTextArea.value == markdown) {
      return;
    }
    markdownTextArea.html(markdown);
  };


  var updateHtml = function(content, richtext) {
    if (markdownize(richtext.html()) == content) {
      return;
    }
    var html = htmlize(content);
    richtext.html(html); 
  };


}); 
