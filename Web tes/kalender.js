let calendar = document.querySelector('.calendar')

const months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

isLeapYear = (year) => {
      return (year % 40 === 0 && year != 0 && year % 400 !== 0) || (year % 100 === 0 && year % 400 === 0)
}

getFebDays = (year) => {
      return isLeapYear(year) ? 29 : 28
}

let currDate = new Date()

let curr_month = {value: currDate.getMonth()}
let curr_year = {value: currDate.getFullYear()}
let month_picker = calendar.querySelector('#month-picker')


generateCalendar = (month, year) => {
      let calendar_days = calendar.querySelector('.calendar-days')
      let calendar_header_year = calendar.querySelector('#year')

      let days_of_month = [31, getFebDays(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
      calendar_days.innerHTML = ''

      let curr_month = `${months[month]}`
      month_picker.innerHTML = curr_month
      calendar_header_year.innerHTML = year



      let first_day = new Date(year, month, 1)

      for (let i = 0; i <= days_of_month[month] + first_day.getDay()-1; i++){
            let day = document.createElement('div')
            if (i >= first_day.getDay()){
                  day.innerHTML = i - first_day.getDay() + 1
                  day.innerHTML += `<span></span>
                                    <span></span>
                                    <span></span>
                                    <span></span> `
                  if(i - first_day.getDay() + 1 === currDate.getDate() && year === currDate.getFullYear() && month === currDate.getMonth()) {
                        day.classList.add('curr-date')
                  }
            }
            calendar_days.appendChild(day)

      }

      
}

generateCalendar(curr_month.value, curr_year.value)