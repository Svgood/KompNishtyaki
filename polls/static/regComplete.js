$(document).ready(function() {
	msg = "Регистрация успешно завершена! \n";
	msg += "Браузер: " + navigator.appName + " " + navigator.appVersion + "\n";
	msg += "Расположение: " + location.host + " " + location.protocol + "\n";
	msg += "Высота ширина: " + window.innerHeight + " " + window.innerWidth + "\n";
	msg += "Имя, полосы прокрутки, строка статуса: " + window.name + " " + window.scrollY + " " + window.status + "\n";
	msg += "История: " + window.history.length + " " + window.location.href + "\n";
	$("#regComplete").text(msg)
});