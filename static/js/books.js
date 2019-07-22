

$(function () {

  $(".js-create-article").click(function () {
    $.ajax({
      url: '{% url 'article:addArticle'%}',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-article").modal("show");
      },
      success: function (data) {
        $("#modal-article .modal-content").html(data.html_form);
      }
    });
  });

});

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#article-table tbody").html(data.html_book_list);
          $("#modal-article").modal("hide");
        }
        else {
          $("#modal-article .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-article").click(loadForm);
  $("#modal-article").on("submit", ".js-article-create-form", saveForm);

  // Update book
  $("#article-table").on("click", ".js-update-article", loadForm);
  $("#modal-article").on("submit", ".js-article-update-form", saveForm);

  // Delete book
  $("#book-table").on("click", ".js-delete-article", loadForm);
  $("#modal-article").on("submit", ".js-article-delete-form", saveForm);

});
