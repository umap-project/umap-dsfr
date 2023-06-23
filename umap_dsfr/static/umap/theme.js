import { CountUp } from './vendors/countup.js/countUp.min.js'

window.onload = function() {
  Array.from(document.querySelectorAll('#statistiques big')).forEach((element) => {
    const countUp = new CountUp(element, Number(element.textContent), {
      duration: 1,
      separator: " ",
      enableScrollSpy: true,
      scrollSpyOnce: true
    })
    if (!countUp.error) {
      countUp.start()
    } else {
      console.error(countUp.error)
    }
  })
}
