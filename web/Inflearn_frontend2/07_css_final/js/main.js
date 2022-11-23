const backtotop = document.getElementById('backtotop')

function pageYcheck () {
    const pageY = window.scrollY
    if (pageY == 0){
        backtotop.classList.remove('show')
    }
    else {
        backtotop.classList.add('show')
    }
    
}

function movebacktotop () {
    window.scrollTo({top:0, behavior:'smooth' })   //top, left, behavior 세가지 지정 가능
}


backtotop.addEventListener('click', movebacktotop)
window.addEventListener('scroll', pageYcheck)

// ----------------------------------- 

function transformnext (event) {
    const slidenext = event.target
    // alert('111')
    const slideprev = slidenext.previousElementSibling
    const classList = slidenext.parentNode.parentNode.nextElementSibling
    const card = classList.getElementsByTagName('li')
    let activeposition = classList.getAttribute('data-position')

    if (Number(activeposition) < 0) {
        activeposition = Number(activeposition) +260
        slideprev.classList.add('slide-prev-hover')
        slideprev.addEventListener('click', transformprev)
        slideprev.style.color = '#2f3059'


        if (Number(activeposition) === 0){
            slidenext.style.color = '#cfd8dc'
            slidenext.classList.remove('slide-next-hover')
            slidenext.removeEventListener('click', transformprev)

        }
    } 

    classList.style.transition = 'transform 1s'  // 1초동안 변화되게 함 (시간 설정)
    classList.style.transform = 'translateX(' + String(activeposition) + 'px)' // 해당 px만큼 이동되게 함
    classList.setAttribute('data-position' , activeposition) // 이동된 data-position 속성을 다시 재설정함.

}

function transformprev (event) {
    const slideprev = event.target  // 이벤트 함수의 타켓(slideprevList[i].addEventListener('click', transformprev)에서 slideprevList[i]를 의미)을 가져옴
    const slidenext = slideprev.nextElementSibling
    
    const classList = slideprev.parentNode.parentNode.nextElementSibling
    const card = classList.getElementsByTagName('li')
    let activeposition = classList.getAttribute('data-position')
    // alert(activeposition)

    if (classList.clientWidth < (card.length * 260 + Number(activeposition))) {
        activeposition = Number(activeposition)-260
        slidenext.style.color = '#2f3059'
        slidenext.classList.add('slide-next-hover')
        slidenext.addEventListener('click', transformnext)

        if (classList.clientWidth > (card.length * 260 + Number(activeposition))){
            slideprev.style.color = '#cfd8dc'
            slideprev.classList.remove('slide-prev-hover')
            slideprev.removeEventListener('click', transformprev)
        }
        
    }

    classList.style.transition = 'transform 1s'  // 1초동안 변화되게 함 (시간 설정)
    classList.style.transform = 'translateX(' + String(activeposition) + 'px)' // 해당 px만큼 이동되게 함
    classList.setAttribute('data-position' , activeposition) // 이동된 data-position 속성을 다시 재설정함.

}


const slideprevList = document.getElementsByClassName('slide-prev')
const slidenextList = document.getElementsByClassName('slide-next')

for  (let i=0; i<slideprevList.length; i++){
    const classList = slideprevList[i].parentNode.parentNode.nextElementSibling
    const cardList = classList.getElementsByClassName('class-card')


    if (classList.clientWidth < (cardList.length * 260)) {

        slideprevList[i].classList.add('slide-prev-hover')
        slideprevList[i].addEventListener('click', transformprev)
        slidenextList[i].classList.add('slide-next-hover')
        slidenextList[i].addEventListener('click', transformnext)
        
    }
    else {
        
        const arrowcontainer = slideprevList[i].parentNode
        arrowcontainer.removeChild(slideprevList[i].nextElementSibling)
        arrowcontainer.removeChild(slideprevList[i])

    }

}