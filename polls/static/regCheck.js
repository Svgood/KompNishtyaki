$(document).ready(function() {

	$("#regBtn").click( function(){

		var logMessage = ""

		if (noDigits.test($("#regName").val())){
			$("#regName").css("border-color", "green");
		}
		else {
			$("#regName").css("border-color", "red");
			logMessage += "Цифры в имени \n"
		}


		if (noDigits.test($("#regLastName").val())){
			$("#regLastName").css("border-color", "green");
		}
		else {
			$("#regLastName").css("border-color", "red");
			logMessage += "Цифры в Фамилии \n"
		}

		console.log($("#regPassword").val())
		if (pas.test($("#regPassword").val())){
			$("#regPassword").css("border-color", "green");
		}
		else {
			$("#regPassword").css("border-color", "red");
			logMessage += "Пароль должен содержать минимум 1 цифру и букву \n"
		}


		if ($("#regLogin").val().length > 3) {
			$("#regLogin").css("border-color", "green");
		}
		else {
			$("#regLogin").css("border-color", "red");
			logMessage += "Длина логина минимум 4 символа \n"
		}

		if (logMessage.length > 0)
			alert(logMessage)
		else {
			//$("#regForm").submit();
			//window.location.replace("regcomplete.html");
		}
	});
	
});

function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('time').innerHTML =
    h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
	}
	
	function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
	}