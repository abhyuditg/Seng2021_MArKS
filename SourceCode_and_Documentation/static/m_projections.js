$(document).ready(function() {

	var ctx = $("#monthly-projections");

	var data = {
		labels : ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"],
		datasets : [
			{
				label : "Projected Savings",
				data : [627.79, 862.86, 982.18, 1385.93, 1631.79, 2117.94, 2332.59, 2737.59, 2986.13, 3214.13, 3872.78, 4127.87],
        backgroundColor : "#5621d9",
				borderColor : "#a182ed",
				fill : false,
				lineTension : 0,
				pointRadius : 5
			},
			{
				label : "Projected Expenditure",
				data : [257, 429.21, 592.29, 905.4, 1702.89, 1892.75, 2034.57, 3232.87, 3952.53, 4217.14, 4627.61, 5109.17],
				backgroundColor : "orange",
				borderColor : "#edbd64",
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
