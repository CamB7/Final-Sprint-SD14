// Desc:
// Author:
// Dates:

var $ = function (id) {
  return document.getElementById(id);
};

// Define format options for printing.
const cur2Format = new Intl.NumberFormat('en-CA', {
  style: 'currency',
  currency: 'CAD',
  minimumFractionDigits: '2',
  maximumFractionDigits: '2',
});

const per2Format = new Intl.NumberFormat('en-CA', {
  style: 'percent',
  minimumFractionDigits: '2',
  maximumFractionDigits: '2',
});

const com2Format = new Intl.NumberFormat('en-CA', {
  style: 'decimal',
  minimumFractionDigits: '2',
  maximumFractionDigits: '2',
});

// Start function definitions here.

function welcomeMsg() {
  // Display a welcome message.
  cur_date = new Date();
  let msg = 'Good ';
  if (cur_date.getHours() < 12) {
    msg += 'Morning ';
  } else if (cur_date.getHours() < 18) {
    msg += 'Afternoon ';
  } else {
    msg += 'Evening ';
  }

  // Add a random quote to the message.
  quoteLst = [
    ' -  The only way to do great work is to love what you do. ',
    ' -  Think big thoughts, but relish the small pleasures. ',
    ' -  The best way to predict the future is to create it. ',
    ' -  The only limit to our realization of tomorrow is our doubts of today. ',
    ' -  The future belongs to those who believe in the beauty of their dreams. ',
    ' -  Success is not the key to happiness. Happiness is the key to success. ',
  ];

  msg += quoteLst[Math.floor(Math.random() * quoteLst.length)];

  // Add date to the message.
  msg += ' -  ' + cur_date.toLocaleDateString();

  document.getElementById('welcome').innerHTML = msg;
}
