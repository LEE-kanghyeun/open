class Test {
	constructor () {
		this._a = 'a'
	}

	funcA() {
		console.log(this._a);
	}
}
var t = new Test();

Object.getOwnPropertyDescriptor(t, 'funcA');  
// undefined

Object.getOwnPropertyDescriptor(Object.getPrototypeOf(t), 'funcA');
// {get: ƒ, set: undefined, enumerable: false, configurable: true}
console.log(Object.getPrototypeOf(t));


function Dog(color, name, age) {
    this.color = color;
    this.name = name;
    this.age = age;
}

// 현재 존재하고 있는 Dog 프로토타입에 family 프로퍼티를 추가함.
// Dog.family = 'aaa'

console.dir(Dog);
console.log(Dog.color);


function Person(name) {
    this.name = name;
  }
  
  var foo = new Person('Lee');
  
  console.dir(Person); // prototype 프로퍼티가 있다.
  console.dir(foo);
  console.log(Person.__proto__ === Function.prototype);
  console.log(Person.prototype === foo.__proto__);
  console.log(foo.__proto__ === Person.prototype);
  console.log(Object.getPrototypeOf(foo));
  console.log(Object.getPrototypeOf(Person));


