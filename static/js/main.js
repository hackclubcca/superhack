var rellax = new Rellax('.rellax');
new WOW().init();
$("#checkin").on("mouseover", function() {
   $("#calendar-title").html("Check In");
    $("#calendar-description").html(
        "For the first hour, participants of Super Hack will get their goodies (such as stickers & API codes) as well as the basic rundown of the schedule."
    );
});
$("#teams").on("mouseover", function() {
   $("#calendar-title").html("Team Forming");
    $("#calendar-description").html(
        "Simultaneously to the check in process, groups of 1-4 members will form based on the choosing of our participants."
    );
});
$("#workshop").on("mouseover", function() {
   $("#calendar-title").html("Workshop");
    $("#calendar-description").html("");
});
$("#food").on("mouseover", function() {
   $("#calendar-title").html("Food");
    $("#calendar-description").html("We know what everyone wants at 1PM... food. Of course, students are also welcome to continue working on their projects whilst eating.");
});
$("#judging").on("mouseover", function() {
   $("#calendar-title").html("Judging");
    $("#calendar-description").html("We'll have judges from all over industry review your well-constructed submissions to determine which projects fit which categories best.");
});
$("#keynote").on("mouseover", function() {
   $("#calendar-title").html("Keynote");
    $("#calendar-description").html("This keynote will bring you the takeaway message of Super Hack - it's not about hacking, but rather the experience. An idea you take from Super Hack could emerge as the next big thing.");
});
$("#closing").on("mouseover", function() {
   $("#calendar-title").html("Closing Remarks & Dinner");
    $("#calendar-description").html("You're tired. We're tired. Don't worry, we get it - we just want to thank everyone who helped at this point and get you back home (hopefully with good opinions of the event).");
});
$(document).ready(function(){
    $(window).scroll(function(){
        if($(window).scrollTop() < 200){
            $("#header-logo").css({"display": "none"});
            $("#zxYzUx").css({"display": "none"});
            $(".navbar").css({"background-color":"#0071bc"});
        }
        else {
            $("#header-logo").css({"display": "inline-block"});
            $("#zxYzUx").css({"display": "inline-block"});
            $(".navbar").css({"background-color":"#000"});
        }
    })
});