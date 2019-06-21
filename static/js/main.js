var rellax = new Rellax('.rellax');
new WOW().init();
$("#checkin").on("click", function() {
   $("#calendar-title").html("Check In");
    $("#calendar-description").html("For the first hour, participants of Raven Hack will get their goodies (such as stickers & API codes) as well as the basic rundown of the schedule.");
});
$("#workshop").on("click", function() {
   $("#calendar-title").html("Workshop");
    $("#calendar-description").html("We understand that some students, regardless of their expertise, will have trouble finding a starting point. In light of aiding these very students, we will host workshops throughout Raven Hack to introduce new APIs and technologies for our hackers to use.");
});
$("#food").on("click", function() {
   $("#calendar-title").html("Food");
    $("#calendar-description").html("🍕🍕🍕🍪🍪🥤");
});
$("#judging").on("click", function() {
   $("#calendar-title").html("Judging");
    $("#calendar-description").html("For the first hour, participants of Raven Hack will get their goodies (such as stickers & API codes) as well as the basic rundown of the schedule.");
});