$(document).ready(function(){
    $("#add_item").click(function(){
      var freItem = $("<li>Item</li>");
      $("ul.my_list").append(freItem);
    });
  });
