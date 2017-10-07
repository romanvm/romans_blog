$(function() {
  $('img').each(function(i, elem) {
    $(elem).wrap('<span class="image"><span/>');
  });
  $('table').each(function(i, elem) {
    $(elem).wrap('<div class="table-wrapper"></div>');
  });
  $('.spoiler-text').hide();
  // Toggle spoiler
  $('.spoiler-toggle').click(function()
  {
    if ($(this).html() == '<span class="fa fa-plus-square"></span>&nbsp;Click to show') {
      $(this).html('<span class="fa fa-minus-square"></span>&nbsp;Click to hide');
    } else {
      $(this).html('<span class="fa fa-plus-square"></span>&nbsp;Click to show');
    }
    $(this).next().toggle();
  }); // end spoiler-toggle
}); // end document.ready
