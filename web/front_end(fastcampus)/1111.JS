// function ParentClass() {};

// function ChildClass() {};

// ChildClass.prototype = new ParentClass();

// var mychild = new ChildClass();
// var myparent = new ParentClass();

// console.log(mychild);
// console.log(myparent);

// console.log(mychild.prototype);
// console.log(myparent.prototype);

// console.log(Object.getPrototypeOf(mychild));
// console.log(Object.getPrototypeOf(myparent));


// console.log(Object.getPrototypeOf(ChildClass.prototype))   // ParentClass {}
// console.log(Object.getPrototypeOf(mychild))                // ParentClass {}
// console.log(Object.getPrototypeOf(ParentClass.prototype))  // {}
// console.log(Object.getPrototypeOf(myparent))               // ParentClass {}


// console.log(ParentClass.prototype)                         // ParentClass {}
// console.log(myparent.prototype)                            // undefined
// console.log(ChildClass.prototype)                          // ParentClass {}
// console.log(mychild.prototype)                             // undefined


function Dog(color, name, age) {
    this.color = color;
    this.name = name;
    this.age = age;
}

var myDog = new Dog("흰색", "마루", 1);
var hisDog = new Dog("흰색", "마루", 1);		// 모든 프로퍼티의 값이 모두 같은 객체를 생성함.
console.log((myDog == hisDog) + "<br>");		// false, 값은 같으나 객체가 다르므로 다름으로 판단
// document.write((myDog === hisDog) + "<br>");	// false, 값은 같으나 객체가 다르므로 다름으로 판단

// document.write((myDog.value == hisDog.value) + "<br>");		// true, 객체의 값은 동일
// document.write((myDog.value === hisDog.value) + "<br>");	// true, 객체의 값은 동일