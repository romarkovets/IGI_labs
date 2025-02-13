document.getElementById('id_date_of_birth').addEventListener('change', function() {
  const date_of_birth = new Date(this.value);
  const today = new Date();

  let age = today.getFullYear() - date_of_birth.getFullYear();
  const monthDiff = today.getMonth() - date_of_birth.getMonth();
  if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < date_of_birth.getDate())) {
      age--;
  }

  const daysOfWeek = ["воскресенье", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота"];
  const dayOfWeek = daysOfWeek[date_of_birth.getDay()];

  const ageInfoDiv = document.getElementById('age-info');
  if (age < 18) {
      alert("Необходимо разрешение родителей на использование сайта.");
  } else {
      ageInfoDiv.innerHTML = `Вы родились в ${dayOfWeek}.`;
  }
});