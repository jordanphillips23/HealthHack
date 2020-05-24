/* globals Chart:false, feather:false */

drawChart = function(data) {
  'use strict'

  feather.replace()

  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        '1 am',
        '2 am',
        '3 am',
        '4 am',
        '5 am',
        '6 am',
        '7 am',
        '8 am',
        '9 am',
        '10 am',
        '11 am',
        '12 pm',
        '1 pm',
        '2 pm',
        '3 pm',
        '4 pm',
        '5 pm',
        '6 pm',
        '7 pm',
        '8 pm',
        '9 pm',
        '10 pm',
        '11 pm',
        '12 am'
      ],
      datasets: [{
        data: data,
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })
}
