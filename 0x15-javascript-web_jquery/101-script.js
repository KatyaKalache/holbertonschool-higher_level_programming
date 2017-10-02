$('#add_item').click(function () {
  $('UL').append('<li>Item</li>');
});
$('#remove_item').click(function () {
  $('LI:last-child').remove();
});
$('#clear_list').click(function () {
  $('UL').remove();
});
