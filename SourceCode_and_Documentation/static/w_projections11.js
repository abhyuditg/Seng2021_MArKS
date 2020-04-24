$(document).ready(function() {

	var ctx = $("#weekly-projections");

	var data = {
		labels : ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"],
		datasets : [
			{
				label : "Projected Savings",
				data : [23, 17, 0, 0, 23, 19, 28],
				backgroundColor : "#21b4d9",
				borderColor : "#a7dbe8",
				fill : false,
				lineTension : 0,
				pointRadius : 5
			},
			{
				label : "Projected Expenditure",
				data : [19.12, 11.82, 0, 0, 10.92, 13.01, 11.47],
				backgroundColor : "#5621d9",
				borderColor : "#a182ed",
				fill : false,
				lineTension : 0,
				pointRadius : 5
			}
		]
	};

	var options = {
		legend : {
			display : true,
			position : "bottom"
		}
	};

	var chart = new Chart( ctx, {
		type : "line",
		data : data,
		options : options
	} );

});
