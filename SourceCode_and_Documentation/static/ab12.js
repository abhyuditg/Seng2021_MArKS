$(document).ready(function () {

	var ctx = $("#bar-ab");

	var data = {
		labels : months_aB,
		datasets : [
			{

				data : data_aB,
				backgroundColor : [
          "rgba(209, 224, 224, 1)",
					"rgba(193, 227, 227, 1)",
          "rgba(181, 232, 232, 1)",
					"rgba(164, 224, 224, 1)",
					"rgba(149, 222, 222, 1)",
          "rgba(138, 222, 222, 1)",
					"rgba(121, 219, 219, 1)",
					"rgba(106, 217, 217, 1)",
					"rgba(90, 209, 209, 1)",
					"rgba(72, 212, 212, 1)",
					"rgba(72, 193, 212, 1)",
					"rgba(72, 172, 212, 1)",
					"rgba(72, 158, 212, 1)"
				],
				borderColor : [
          "rgba(0, 0, 0, 1)",
					"rgba(0, 0, 0, 1)",
          "rgba(0, 0, 0, 1)",
          "rgba(0, 0, 0, 1)",
					"rgba(0, 0, 0, 1)",
          "rgba(0, 0, 0, 1)",
          "rgba(0, 0, 0, 1)",
					"rgba(0, 0, 0, 1)",
          "rgba(0, 0, 0, 1)",
          "rgba(0, 0, 0, 1)",
					"rgba(0, 0, 0, 1)",
          "rgba(0, 0, 0, 1)",
					"rgba(0, 0, 0, 1)"
				],
				borderWidth : 2

			}
		]
	};

	var options = {
		title : {
			display : true,
			position : "top",
			text : "Account Balance",
			fontSize : 18,
			fontColor : "#111"
		},
		legend : {
			display : false
		},
		scales : {
			yAxes : [{
				ticks : {
					min : 0
				}
			}]
		}
	};
	var chart = new Chart( ctx, {
		type : "bar",
		data : data,
		options : options
	});

});
