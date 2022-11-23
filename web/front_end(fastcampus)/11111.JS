// class user1 {
//     constructor() {       // constructor(): 아래 const dave = new user1();에서처럼 선언시 객체를 생성해주는 함수
//       this.name = "dave";
//       this.age = 30;
//       this.height = function(){
//           return 181
//       }
//     }
//     get_message(){
//         return 'hello!'
//     }
//   }
//   const dave = new user1();
  
//   console.log(dave.name);
//   console.log(dave.age);
//   console.log(dave.get_message());
//   console.log(dave.height());
//   console.log(user1.prototype.height);


// class Animal {
//     constructor(name){
//         this.name = name
//     }
// };

// class User extends Animal {
//     constructor(name, age){
//         super(name)
//         this.age = age

//     }
// };

// const dave = new User('dave', 15)
// console.log(dave, dave.name)


// class Animal {
//     constructor(name){
//         this.name = name
//     }
//     get_message(a){
//         return 'hello'+a
//     }
// };

// class User extends Animal {
//     constructor(name, age){
//         super(name)
//         this.age = age
//     }

//     get_message(a){                 // 상속받은 함수중에서 해당 함수를 수정함. 단, 메소트 명과 사용 인자가 같아야함.
//         return 'good!'+a
//     }
// };


// const dave = new User('dave', 15)
// console.log(dave.get_message('이다'))



// class Animal {
//     constructor(name){
//         this.name = name
//     }
//     get_message(a){
//         return 'hello'+a
//     }
// };

// Animal.prototype.age = '15'  
// console.log(Animal.prototype.age)
// console.log(Animal.hasOwnProperty('name'))  
// console.log(Animal.hasOwnProperty('age'))

// function Dog(name, age) {

//     this.color = 'red';

//     this.name = name;

//     this.age = age;

// }

// var myDog = new Dog("흰색", "마루", 1);

// myDog.family = "시베리안 허스키"; // 품종에 관한 프로퍼티를 추가함.

// myDog.breed = function() {        // 털색을 포함한 품종을 반환해 주는 메소드를 추가함.
//     return this.color + " " + this.family;
// }
// Dog.prototype.code = '12345'
// Dog.prototype.code2 = '123456'

// console.log(myDog, Dog, Dog.prototype, Dog.prototype.code, Dog.color, Dog.prototype.color);

// function Dog(color, name, age) {

//     this.color = color;

//     this.name = name;

//     this.age = age;

// }

// var myDog = new Dog("흰색", "마루", 1);

// var hisDog = new Dog("흰색", "마루", 1);      // 모든 프로퍼티의 값이 모두 같은 객체를 생성함.

// document.write((myDog == hisDog) + "<br>");   // false

// document.write((myDog === hisDog) + "<br>");  // false

 

// var herDog = hisDog;                          // hisDog 객체를 변수 herDog에 대입함.

// document.write((hisDog == herDog) + "<br>");  // true

// document.write((hisDog === herDog) + "<br>"); // true


// function arrayFrom() {

//     return Array.from(arguments);

// }

// console.log(Array.from(arrayFrom(1, 2, 3)));        // [1, 2, 3]

// var myMap = new Map(([1, 2], [3, 4]));

// console.log(Array.from(myMap));                     // [1, 2, 3, 4]

// console.log(Array.from("JavaScript"));              // [J,a,v,a,S,c,r,i,p,t]









// 이벤트 동작 : mouseover, mouseout
<!DOCTYPE html>
<html>


        <body>
                <div class="box1">ease</div>
                
                <script>
                const makeRed = () =>box.style.background = 'red';
                const makeYellow = () =>box.style.background = 'yellow';
                
                const box = document.querySelector(".box1")
                box.addEventListener('mouseover', makeRed);
                box.addEventListener('mouseout', makeYellow);
                box.addEventListener('click', () =>{
                  box.removeEventListener('mouseover', makeRed);
                  box.removeEventListener('mouseover', makeYellow);
                })
                
                </script>
                </body>

</html>