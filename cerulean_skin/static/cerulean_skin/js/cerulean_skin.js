$(function(){
  // Make embedded Youtube videos responsive
  $('iframe').each(function()
  {
    if ($(this).attr('src').indexOf('youtube') > -1)
    {
      $(this).attr('class', 'embed-responsive-item');
      $(this).wrap('<div class="embed-responsive embed-responsive-16by9"></div>');
    }
  }); // end iframe.each
  $('.spoiler-text').hide();
  // Toggle spoiler
  $('.spoiler-toggle').click(function()
  {
    if ($(this).html() == '<span class="fa fa-plus-square"></span>&nbsp;Click to show')
    {
      $(this).html('<span class="fa fa-minus-square"></span>&nbsp;Click to hide');
    }
    else
    {
      $(this).html('<span class="fa fa-plus-square"></span>&nbsp;Click to show');
    }
    $(this).next().toggle();
  }); // end spoiler-toggle
}); // end document.ready
