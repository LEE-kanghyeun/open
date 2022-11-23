// const backtotop = document.getElementById('backtotop')
const backtotop = document.getElementsByClassName('backtotop')

backtotop[0].addEventListener('click', movescrolltop)
window.addEventListener('scroll', checkscrollY)

function checkscrollY () {
    const pageY = window.scrollY
    if (pageY == 0){

        backtotop[0].style.visibility = 'hidden';
    } 
    else{
        backtotop[0].style.visibility = 'visible';
    }
}


function movescrolltop() {
    window.scrollTo({top:0, behavior : 'smooth'})
}

// ---------------------------------------------


let slideprev = document.getElementsByClassName('slide-prev')
let slidenext = document.getElementsByClassName('slide-next')


for (let i=0; i<slideprev.length; i++){
    cardul = slideprev[i].parentNode.parentNode.nextElementSibling
    cardli =  cardul.getElementsByTagName('li')

    const parentslideprev = slideprev[i].parentNode
    if (cardul.clientWidth >= (cardli.length * 260)) {
        parentslideprev.removeChild(slidenext[i])
        parentslideprev.removeChild(slideprev[i])
        
    }

    slideprev[i].addEventListener('click', clickslideprev)
    // slidenext[i].addEventListener('click', clickslidenext)
    slideprev[i].classList.add('slide-prev-hover')
    // slidenext[i].classList.add('slide-next-hover')
}

// ---------------------------------------------


function clickslideprev(event) {
    let slideprev = event.target
    let slidenext = slideprev.nextElementSibling
    let cardul = slideprev.parentNode.parentNode.nextElementSibling
    let cardli =  cardul.getElementsByTagName('li')
    let cardposition = cardul.getAttribute('data-position')
    
    cardposition = Number(cardposition) - 260

    cardul.style.transform = 'translateX(' + String(cardposition) + 'px)'
    cardul.style.transition = '1s'
    cardul.setAttribute('data-position', String(cardposition))
    
    
    
    slidenext.style.color = 'rgb(47, 48, 89)'
    slidenext.addEventListener('click', clickslidenext)
    slidenext.classList.add('slide-next-hover')
    // alert(cardposition) 

    if (cardul.clientWidth >= (Number(cardposition) + (cardli.length * 260))) { 
        slideprev.style.color = '#cfd8dc'
        slideprev.removeEventListener('click', clickslideprev)
        slideprev.classList.remove('slide-prev-hover')  
    }
 
}


function clickslidenext(event) {
    let slidenext = event.target
    let slideprev = slidenext.previousElementSibling
    let cardul = slidenext.parentNode.parentNode.nextElementSibling
    let cardli =  cardul.getElementsByTagName('li')
    let cardposition = cardul.getAttribute('data-position')
    
    cardposition = Number(cardposition) + 260

    cardul.style.transform = 'translateX(' + String(cardposition) + 'px)'
    cardul.style.transition = '1s'
    cardul.setAttribute('data-position', String(cardposition))

    
    
    slideprev.style.color = 'rgb(47, 48, 89)'
    slideprev.addEventListener('click', clickslideprev) 
    slideprev.classList.add('slide-prev-hover')

    if (cardposition >= 0) { 
        slidenext.style.color = '#cfd8dc'
        slidenext.removeEventListener('click', clickslidenext) 
        slidenext.classList.remove('slide-next-hover')
        
    }
    
    
    

    // alert(cardposition)

}