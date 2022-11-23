// https://curryyou.tistory.com/169      개발환경 구축하기
// https://latte-is-horse.tistory.com/29    코드러너 설치후에도 실행시, 출력 깨질 경우 ( -> node.js를 깔아야함)

// http://tcpschool.com/javascript/js_object_handling  기본적인 javascript 공부 내용 (TCP 스쿨)


// console.log('hello');




//  ************************* [객체 생성 방법] ************************

// 1) 리터럴 객체 생성
var kitty = {
    name: "나비",
    family: "코리안 숏 헤어",
    age: 1,
    weight: 0.1,
    get_plus : function() {
        return this.age + this.weight
    }
};

// 2) 클래스 이용 객체 생성

class user1 {
    constructor() {         // constructor(): 아래 const dave = new user1();에서처럼 선언시 객체를 생성해주는 함수
      this.name = "dave";   // constructor(): python class에서 __init__과 유사한 부분
      this.age = 30;
      this.height = function(){           // 메소드 선언 방법 1
          return 181
      }
    }
    get_message(){                       // 메소드 선언 방법 2
        return 'hello!'
    }
  }
  const dave = new user1();           
  
  console.log(dave.name);
  console.log(dave.age);
  console.log(dave.get_message());    
  console.log(dave.height());



// 3) 생성자를 이용한 객체 생성

function Dog(color, name, age) { // 개에 관한 생성자 함수를 작성함.
    this.color = color;          // 색에 관한 프로퍼티
    this.name = name;            // 이름에 관한 프로퍼티
    this.age = age;              // 나이에 관한 프로퍼티
}
var myDog = new Dog("흰색", "마루", 1); // 이 객체는 Dog라는 프로토타입을 가짐.


// 4) Object.create() 메소드를 이용
var obj = Object.create(null, {             // null 프로토타입을 사용하여 새로운 객체를 만들고
    x: { value: 100, enumerable: true },    // x좌표를 나타내는 열거할 수 있는 프로퍼티와
    y: { value: 200, enumerable: true }     // y좌표를 나타내는 열거할 수 있는 프로퍼티를 추가함.
});




// *****************  [프로퍼티 요소 설정하기]  *********************
// https://moonscode.tistory.com/6

// <속성에 대한 설정값 종류>
    // -value  : 속성값
    // -get & set :   ES6부터 지원, 추후 확인 필요
    // -enumerable (열거 할 수 있는)  : for 문 등으로 열거가능여부를 설정, (열거 불가 설정한다고 조회가 안되는 것은 아님)
    // -wriatable (쓸 수 있는)  : 값에 대한 수정 가능 여부 설정
    // -configurable (구성할 수 있는) : 속성 설정값들에 대해서  변경 가능 여부를 설정한다. (아래 예시)


var ob = {};
Object.defineProperty(ob, 'a', { configurable:false, writable:true, enumerable: true });  // 선언

Object.defineProperty(ob, 'a', { configurable:false, writable:true, enumerable: false });
// 실행시 에러 발생 : TypeError: Cannot redefine property: a
// configurable:false로 설정되었을때는, writable을 제외하고는 설정 변경 불가함 (value 변경은 writable 설정에 귀속됨)

Object.defineProperty(ob, 'a', { configurable:false, writable:true, value: 'b' }); 
console.log(ob.a)  // writable:true이므로 'b'로 출력됨

// <속성 관련 함수>
    // defineProperty : 앞서 설명한 속성들을 defineProperty를 통해서 만들수 있습니다.
    // getOwnPropertyDescriptor : 메서드를 이용하면 정의한 값의 속성을 확인할 수 있습니다.

// 참고자료
    // https://moonscode.tistory.com/6
    // https://poiemaweb.com/js-prototype
    // https://stackoverflow.com/questions/38740610/object-getprototypeof-vs-prototype
    // https://pks2974.medium.com/javascript-%EC%99%80-prototype-%ED%94%84%EB%A1%9C%ED%86%A0-%ED%83%80%EC%9E%85-515f759bff79




// <객체 프로퍼티의 순회>
// 객체의 프로퍼티를 순회하는 방법으로는
// 1. for 문 
// 2. Object.keys()
// 3. Object.getOwnPropertyNames()


// color 프로퍼티의 enumerable 속성을 false로 설정함.
Object.defineProperty(myDog, 'color', {enumerable : false} );
// 객체가 가진 고유 프로퍼티 중에서 열거할 수 있는 프로퍼티 이름을 배열에 담아 반환함.
document.write(Object.keys(myDog) + "<br>");       // 결과: name, age
// 객체가 가진 모든 고유 프로퍼티의 이름을 배열에 담아 반환함.
document.write(Object.getOwnPropertyNames(myDog)); // 결과: color, name, age




{/* <객체간의 비교>  */}

function Dog(color, name, age) {
    this.color = color;
    this.name = name;
    this.age = age;
}

var myDog = new Dog("흰색", "마루", 1);
var hisDog = new Dog("흰색", "마루", 1);		// 모든 프로퍼티의 값이 모두 같은 객체를 생성함.
document.write((myDog == hisDog) + "<br>");		// false, 값은 같으나 객체가 다르므로 다름으로 판단
document.write((myDog === hisDog) + "<br>");	// false, 값은 같으나 객체가 다르므로 다름으로 판단

document.write((myDog.value == hisDog.value) + "<br>");		// true, 객체의 값은 동일
document.write((myDog.value === hisDog.value) + "<br>");	// true, 객체의 값은 동일

var herDog = hisDog;					// hisDog 객체를 변수 herDog에 대입함.  
                                        // 이제부터 변수 herDog은 hisDog 객체를 가리킴
                                        //즉, 객체 레퍼런스는 객체 자체를 저장하는 것이 아니라, 객체가 위치한 주소를 저장하는 것
document.write((hisDog == herDog) + "<br>");	// true
document.write((hisDog === herDog) + "<br>");	// true




// <객체 메소드(method)>  - 자주 쓰이는 객체 메소드
    // 모든 자바스크립트 객체는 Object 객체와 Object.prototype 객체의 모든 프로퍼티와 메소드를 상속받습니다.
    // 1. hasOwnProperty()       : 아래 클래스 설명에 포함, 고유의 프로퍼티만 반환합니다.
    // 2. propertyIsEnumerable()   : Enumerable(순열 가능한지) 여부를 반환
    // 3. isPrototypeOf()    :  아래 설명 존재, 특정 객체의 프로토타입 체인에 현재 객체가 존재하는지를 검사
    // 4. isExtensible()   : 객체에 새로운 프로퍼티를 추가할 수 있는지 여부를 반환합니다.
    // 5. toString()
    // 6. valueOf()    : 아래 설명 존재

// valueOf() 메소드  : 객체의 원시타입의 값을 반환하는 메소드 
// https://blog.naver.com/pis7pis7/221833290628  : 원시타입(string, number 등..)과 object 타입  
//                                                 +  오토박싱/래퍼객체의 개념


function func(n) {
    this.number = n;
}

let myFunc = new func(4);
var a = '123'
document.write(myFunc + 5);		// [object Object]5
document.write("<br><br>")      
document.write(myFunc);	        // [object Object]
document.write("<br><br>")
document.write(typeof a);	    // string
document.write("<br><br>")
document.write(myFunc.number);	// 4

func.prototype.valueOf = function() {
    return this.number;
}
document.write("<br><br>")
document.write(myFunc + 5);		// 9



// isPrototypeOf() 메소드  : 특정 객체의 프로토타입 체인에 현재 객체가 존재하는지를 검사

var day = new Date(); // Date 객체를 생성함.
// 객체 day의 프로토타입이 Date.prototype인지를 검사함.
document.write(Date.prototype.isPrototypeOf(day));          // true
document.write(Date.prototype.isPrototypeOf(new String())); // false




// isExtensible() 메소드
// isExtensible() 메소드는 









// ***************************** class 상속 ****************************

class Animal {
    constructor(name){
        this.name = name
    }
};

class User extends Animal {              // extends와 super() 추가
    constructor(name, age){
        super(name)                     // extends와 super() 추가, super는 물려받는 프로퍼티도 명시해줘야함
        this.age = age

    }
};
    
const dave2 = new User('dave', 15);
console.log(dave2, dave2.name);




class Animal {
    constructor(name){
        this.name = name
    }
    get_message(a){
        return 'hello'+a
    }
};

class User extends Animal {
    constructor(name, age){
        super(name)
        this.age = age
    }

    get_message(a){                 // 상속받은 함수중에서 해당 함수를 수정함. 단, 메소트 명과 입력 인자가 같아야함.
        return 'good!'+a
    }
};

const dave = new User('dave', 15)    
console.log(dave.get_message('이다'))        // 값 good!!이다로 출력됨






// ***************************** class 프로퍼티 추가 선언과 hasOwnProperty  ****************************
class Animal {
    constructor(name){
        this.name = name
    }
    get_message(a){
        return 'hello'+a
    }
};

Animal.prototype.age = '15' 
// class도 prototype 메소드를 활용하면, 추가 프로퍼티 선언이 가능함. (외부선언)
// 단, class 내부에서 선언된 프로퍼티와 외부에서 선언된 프로퍼티는 구분이 가능함 
// hasOwnProperty는 내부에서 선언된 프로퍼티에 대해 True를 출력함
console.log(Animal.prototype.age)
console.log(Animal.hasOwnProperty('name'))   // True
console.log(Animal.hasOwnProperty('age'))    // False





// 객체의 종류
// 전역 객체 vs 래퍼 객체 vs 표준객체
// 전역객체: 전역에 쓰이는 객체
// 래퍼 객체: 아래 상세
    var str = "문자열";   // 문자열 생성
    var len = str.length; // 문자열 프로퍼티인 length 사용
    // 위의 예제에서 생성한 문자열 리터럴 str은 객체가 아닌데도 length 프로퍼티를 사용할 수 있습니다.
    // 프로그램이 문자열 리터럴 str의 프로퍼티를 참조하려고 하면, 자바스크립트는 new String(str)을 호출한 것처럼 문자열 리터럴을 객체로 자동 변환해주기 때문입니다.
    // 이렇게 생성된 임시 객체는 String 객체의 메소드를 상속받아 프로퍼티를 참조하는 데 사용됩니다.
    // 이후 프로퍼티의 참조가 끝나면 사용된 임시 객체는 자동으로 삭제됩니다.
    // 이렇게 숫자, 문자열, 불리언 등 원시 타입의 프로퍼티에 접근하려고 할 때 생성되는 임시 객체를 래퍼 객체(wrapper object)라고 합니다

// 표준 객체 : 1. Number 객체  2. Math 객체  3. Date 객체  4. String 객체  5. Array 객체

// 1. Number 
    // - null은 object 타입이며, 아직 '값'이 정해지지 않은 것을 의미하는 값입니다.
    // - undefined는 null과는 달리 하나의 타입이며, '타입'이 정해지지 않은 것을 의미하는 값이기도 합니다.
    // - NaN은 number 타입이며, '숫자가 아님'을 의미하는 숫자입니다.
    // - Infinity는 number 타입이며, '무한대'를 의미하는 숫자입니다
    // 1. Number.parseFloat()   : 문자열을 파싱하여 실수형태로 반환
    // 2. Number.parseInt()  : 문자열을 파싱하여 정수형태로 반환
    // 3. Number.isNaN()
    // 4. Number.isFinite()   : 유한한 수인지 여부를 반환
    // 5. Number.isInteger() 
    // 6. Number.isSafeInteger() : 안전한 정수(safe integer)인지를 검사, -(253 - 1)부터 (253 - 1)까지의 모든 정수가 안전한 정수에 포함
    // 7. Number.prototype 메소드
        // toExponential() Number 인스턴스를 지수 표기법으로 변환한 후, 그 값을 문자열로 반환함.
        // toFixed() Number 인스턴스의 소수 부분 자릿수를 전달받은 값으로 고정한 후, 그 값을 문자열로 반환함.
        // toPrecision() Number 인스턴스의 가수와 소수 부분의 합친 자릿수를 전달받은 값으로 고정한 후, 그 값을 문자열로 반환함.
        // toString() Number 인스턴스의 값을 문자열로 반환함.
        // valueOf() Number 인스턴스가 가지고 있는 값을 반환함.
            var numObj = new Number(123); // 123의 값을 가지는 Number 인스턴스를 생성함.
            typeof numObj;                // object
            var num = numObj.valueOf();
            num;                          // 123
            typeof num;                   // number


// 2. Math   : 수학에서 자주 사용하는 상수와 함수들을 미리 구현해 놓은 자바스크립트 표준 내장 객체


// 3. Date  :  시간과 날짜에 관한 정보 객체
    // Date.now() 메소드
        // var nowMiliSec = Date.now();
		// document.write(nowMiliSec + "<br>");			// 1627371496724
        // document.write(new Date(nowMiliSec) + "<br>"); // Tue Jul 27 2021 16:38:16 GMT+0900 (Korean Standard Time)
    // 1. getFullYear()
    // 2. getDate()
    // 3. getDay()
    // 4. getTime()
    // 1. setFullYear()
    // 2. setDate()


// 4. String  : 문자열 객체
    // - slice()     var str = "abcDEFabc";  str.slice(2, 6);  
    // - substring() var str = "abcDEFabc";  document.write(str.substring(3, 5))    -> DE
    // - substr()    var str = "abcDEFabc";  document.write(str.substr(3, 5));  -> DEFab
    // - charAt()   
    // 기타 등등 : http://tcpschool.com/javascript/js_standard_stringMethod


// 5. Array :  배열 객체
    // 배열 선언  :  var arr = [1, true, "Java"];
    // Array.isArray()	전달된 값이 Array 객체인지 아닌지를 검사함.
    // Array.from()	배열과 비슷한 객체와 반복할 수 있는 객체를 배열처럼 변환함.(진짜 배열은 아니고, 배열 객체의 자식 클래스가 됨)
    // Array.of()	인수의 수나 타입에 상관없이 인수로 전달받은 값을 가지고 새로운 Array 인스턴스를 생성함.
    // push() 하나 이상의 요소를 배열의 가장 마지막에 추가하고, 배열의 총 길이를 반환함.
    // pop() 배열의 가장 마지막 요소를 제거하고, 그 제거된 요소를 반환함.
    // shift() 배열의 가장 첫 요소를 제거하고, 그 제거된 요소를 반환함.
    // unshift() 하나 이상의 요소를 배열의 가장 앞에 추가하고, 배열의 총 길이를 반환함.
    // reverse() 배열 요소의 순서를 전부 반대로 교체함.
    // sort() 해당 배열의 배열 요소들을 알파벳 순서에 따라 정렬함.
    // splice() 기존의 배열 요소를 제거하거나 새로운 배열 요소를 추가하여 배열의 내용을 변경함.
    // copyWithin()	해당 배열에서 일련의 요소들을 복사하여, 명시된 위치의 요소들을 교체함.
    // fill()	시작 인덱스부터 종료 인덱스 바로 앞까지의 모든 배열 요소를 특정 값으로 교체함.
    // join() 배열의 모든 요소를 하나의 문자열로 반환함.
    // slice() 전달받은 시작 인덱스부터 종료 인덱스 바로 앞까지의 모든 배열 요소를 추출하여 만든 새로운 배열을 반환함.
    // concat() 해당 배열의 뒤에 인수로 전달받은 배열을 합쳐서 만든 새로운 배열을 반환함.
    // toString() 해당 배열의 모든 요소를 하나의 문자열로 반환함.
    // toLocaleString()	해당 배열의 모든 요소를 하나의 문자열로 반환함.
    // indexOf()	전달받은 값과 동일한 배열 요소가 처음으로 등장하는 위치의 인덱스를 반환함.
    // lastIndexOf()	전달받은 값과 동일한 배열 요소가 마지막으로 등장하는 위치의 인덱스를 반환함.
    // forEach()	해당 배열의 모든 요소에 대하여 반복적으로 명시된 콜백 함수를 실행함.
    // map()	해당 배열의 모든 요소에 대하여 반복적으로 명시된 콜백 함수를 실행한 후, 그 실행 결과를 새로운 배열로 반환함.
    // filter()	해당 배열의 모든 요소에 대하여 반복적으로 명시된 콜백 함수를 실행한 후, 그 결괏값이 true인 요소들만을 새로운 배열에 담아 반환함.
    // every()	해당 배열의 모든 요소에 대하여 반복적으로 명시된 콜백 함수를 실행한 후, 그 결괏값이 모두 true일 때에만 true를 반환함.
    // some()	해당 배열의 모든 요소에 대하여 반복적으로 명시된 콜백 함수를 실행한 후, 그 결괏값이 하나라도 true이면 true를 반환함.
    // reduce() 해당 배열의 모든 요소를 하나의 값으로 줄이기 위해, 두 개의 인수를 전달받는 콜백 함수를 실행함. (배열의 첫 번째 요소부터 시작함.)
    // reduceRight()	해당 배열의 모든 요소를 하나의 값으로 줄이기 위해, 두 개의 인수를 전달받는 콜백 함수를 실행함. (배열의 마지막 요소부터 시작함.)
    // entries()	배열 요소별로 키와 값의 한 쌍으로 이루어진 새로운 배열 반복자 객체(Array Iterator Object)를 배열 형태로 반환함.
    // keys()	배열 요소별로 키(key)만 포함하는 새로운 배열 반복자 객체를 배열 형태로 반환함.
    // values()	배열 요소별로 값(value)만 포함하는 새로운 배열 반복자 객체를 배열 형태로 반환함.
    // find()	검사를 위해 전달받은 함수를 만족하는 배열 요소의 값을 반환함. 만족하는 값이 없으면 undefined를 반환함.
    // findIndex()	검사를 위해 전달받은 함수를 만족하는 배열 요소의 인덱스를 반환함. 만족하는 값이 없으면 -1을 반환함.




// 3항 연산자 : 조건 ? 참 실행 : 거짓 실행
    // 3항 연산자가 아닐때
    const data = [1,2];

    if (data.length ===0) {
    console.log('빈 배열')
    }
    else {
    console.log('배열이 있음')
    }

    // 3항 연산자 : 조건 ? 참 실행 : 거짓 실행
    data.length ===0 ? console.log('빈 배열') : console.log('배열이 있습니다')

    // 3항 연산자로 선언과 동시 실행
    const myArray = [1,2];
    let descMyArray = myArray.length === 0 ? '빈배열': '아이템이 있는 배열';


// 선언시 디폴트 값 설정
    function printData(name = 'david') { // 디폴트 값 설정
        console.log(name);
    }
    
    printData()   //'david' 출력됨 (디폴트 값)


// 객체 구조 분해 할당      : 객체 내 프로퍼치를 분해/할당하여 새로운 변수에 대입시키는 것
    const data = {
        name : 'Dave Lee',
        age : 30,
        hobby: 'coding'
    };
    
    let {name : myname, 
        age : myage, 
        myheight = '180', 
        weight : myweight = '80'}   // myweight를 weight로 대입한다, 만약 weight라는 대입 대상이 없다면 값을 80으로 한다.
        = data;
    console.log(myname, myage, myheight, myweight);   //Dave Lee  30  180  80


// 배열 자동 할당   
        let data = [1,2,3];

        const [item1, item2, item3, item4, item5] = data;
        console.log(item1, item2, item3);    // 1 2 3

        const [, item6, item7, item8, item9] = data;
        console.log(item6, item7, item8) ;   // 2 3 undefined  (1은 첫번째 빈 리스트 칸에 대입됨)


// 변수 값 교환

    let a = 1;
    let b = 2;

    [a,b] = [b,a]
    console.log(a,b) // 2 1


// 함수 리턴시 여러값 넘겨주기
    function getData() {
        return [1, 2, 3];
    }
    
    let [a,b,c] = getData()
    console.log(a,b,c) // 1 2 3


// split 함수 활용
    data = 'Dave.Lee.coding'
    let [a,b,c] = data.split('.')
    console.log(a,b,c) // Dave Lee coding


// Rest 파라미터 활용    : 함수에서 입력변수 앞에 ...을 붙이면 배열로 입력받겠다는 의미이다.
    function getData(...rest) {   // Rest함수 활용
        console.log(rest);
    }
    
    getData([1,2,3,4,5]) //  [Array(5)]
    getData(1,2,3,4,5)   //  [1, 2, 3, 4, 5]


// Rest 파라미터 활용 (2)    
    function getData(a, b, ...rest) {   // Rest함수 활용
        console.log(rest);
    }

    getData(1,2,3,4,5)   //  [3, 4, 5]    -> 1, 2는 a, b에 대입되었음


// Spread 파라미터 활용   : Rest와 반대개념으로 ...을 붙이면 배열을 개별값으로 분해시킴
    function getData(a, b, c) {
        console.log(a+b+c);
      }

      const data = [1 ,2 , 3]
      getData(...data)  // 6     -> data라는 배열을 원소들로 분해시킴
      getData(1, 2, 3)  // 6

      const a = [0 , ...data, 4, 5, 6 ,7]
      console.log(a);   // [0, 1, 2 ,3,  4, 5, 6 ,7]




// Hoisting(호이스팅) 현상 : 변수 또는 함수 선언을 위로 끌어올리는 것 ,  javascript에만 있는 특이 기능
                          // -> var 키워드와 함수 선언에서만 가능, let이나 const 등은 호이스팅 없이 에러 처리
                          // -> 호이스팅이 싫다면, 1. let const로 변수 선언   2. 함수 선언식 말고 함수 표현식을 사용해라
        //입력 코드 :    (변수 선언보다 변수 사용이 먼저인 상황)
        console.log(a);
        a = 10 ;
        console.log(a);
        var a = 20;

        //실제 코드 실행 순서 :
        var a;      // -> 변수 선언을 맨 위로 끌어올린다
        console.log(a);
        a = 10 ;
        console.log(a);
        a = 20;
        console.log(a);


        // 함수 표현식 : 함수 객체를 변수처럼 선언한후 함수 표현식을 대입하는 방식으로 호이스팅 불가, 
                        // getData를 먼저 실행할경우 에러 처리
        let getData = function(){ 
            console.log('hello');}

        // 함수 선언식 : 호이스팅 가능
        function getData(){ 
            console.log('hello');}



// Scope : 변수 유효 범위설정 (전역 변수, 함수 변수, 블록 변수)  ,  javascript에만 있는 특이 기능

        // 전역 변수 : 전 범위에서 사용가능
        // 함수 변수 : 함수에서 선언된 변수로, 함수 내에서만 사용 가능
                     // 함수 내에 또 다른 험수가 있는 경우, 바깥 함수에서 선언된 변수는 안쪽 함수에서도 사용 가능 (반대는 불가)
        // 블록 변수 : { let data = 'lee '}와 같이 { }의 블록 안에서 선언된 변수로, 블록 내에서만 사용 가능
                     // 블록 내에 또 다른 블록이 있는 경우, 바깥 블록에서 선언된 변수는 안쪽 블록에서도 사용 가능 (반대는 불가)
                     // if, for 문도 {}의 블록을 활용하기때문에, 동일하게 블록 변수가 적용됨 - 파이썬과 다름
        //*** 단, var로 선언된 변수는 블록 안과 밖 상관없이 사용가능함 (함수는 아님)
        { var data = 1}
        console.log(data)  // 1로 출력 가능함
        //*** 전역변수와 지역 변수(함수, 블록)가 있을때 이름이 동일하다면 지역 내에서는 '지역 변수'로 인식한다.




// 동기와 비동기 처리 
            // 동기: line by line 처럼 한줄 끝나고 다음 한줄을 실행시키는 방식
            // 비동기 : 한줄에 대한 처리가 아직 끝나지 않았는데도, 다음 줄을 실행시키는 경우 
            //         (API 호출과 같이 실행시간이 긴경우 활용) - 자바스크립트에서 지원하는 기능

            
            // setTimeout 함수의 이해  : 몇초간 대기하도록 하는 함수
            console.log('안녕하세요');    //출력 순서 (1)

            setTimeout( () => {
              console.log('Dave Lee 입니다');   //출력 순서 (3)
            }, 3000);                           //3초 대기

            console.log('반갑습니다.');    //출력 순서 (2)
            
            
            // ** call back 활용 **
            // 비동기 함수시 순서를 지정해주고 싶을 경우, 예를 들어 desc에 대한 처리가 완료된 후에야 desc2를 실행해야되는 경우
            console.log('안녕하세요');    //출력 순서 (1)

            function desc(callback){
            setTimeout( () => {
            console.log('Lee 입니다');   //출력 순서 (2)
            callback();
            }, 3000);
            }

            function desc2(){
            console.log('반갑습니다.');  //출력 순서 (3)
            }

            desc(desc2);   // desc 안에 desc2를 인자로 집어넣기, callback()이 console.log('Lee 입니다') 뒤에 있으므로, 
                           // console.log('Lee 입니다')가 다 끝난후 callback() 즉, desc2가 실행됨

            
            // Promise + then : callback을 여러번 연결해야하는 콜백지옥의 단점을 극복
            // - promise의 3가지 상태, pending (대기), fulfulled (이행완료), rejected (실패)
            // <기본 형태> 
            // new Promise((성공시 함수, 실패시 함수))   : Promise의 조건을 정의함.  
            // +   
            // Promise 객체함수.then(성공시 동작 , 실패시 동작) : Promise 조건에 따라 실행시킴

            // Promise 조건 정의
            const runcode = new Promise((resolve, reject) => {
                setTimeout(() => {
                  let number = 10;
                  if (number > 9) {
                    resolve(number);  // resolve 함수 : 해당 케이스시  number를 반환
                  } 
                  else {
                    reject("error");  // reject 함수 : 해당 케이스시, 'error' 문자를 반환
                  }
                }, 1000);   // 1초 대기
              });
              
             // then을 통해 Promise 활용
              runcode.then((item) => {   // item은 resolve 또는 reject 함수의 리턴값   
                                         // ->   .then( (입력인자)=>{정상시 실행내용} , (입력인자)=>{실패시 실행내용} ) 의 형태
                                         // -> 만일 1개만 있을 경우, 정사시의 실행내용만 선언된것으로 간주함
                    console.log("success", item);
                  },
                  (err) => {
                    console.log(err);
                  }
                )
                .then(                   // 두번째 then은 첫번째 then이 다 실행되고나서 실행됨
                  () => {
                    console.log("one more");
                  },
                  () => {
                    console.log("error2");
                  }
                );

            // 위의 코드를 function 형태로 활용
            const runcode = new Promise(function(resolve, reject) {
                setTimeout(() => {
                    let number = 1;
                    if (number > 9) {
                    resolve(number);  // resolve 함수 : 해당 케이스시  number를 반환
                    } 
                    else {
                    reject("error");  // reject 함수 : 해당 케이스시, 'error' 문자를 반환
                    }
                }, 1000);   // 1초 대기
                });
                
                runcode.then(
                    function(item) {   // item은 resolve 또는 reject 함수의 리턴값
                    console.log("success", item);
                    },
                    function(err) {
                    console.log(err);
                    }
                ).then(
                    function() {
                    console.log("one more");
                    },
                    function() {
                    console.log("error2");
                    }
                );

                // then 과 return
                const runcode = new Promise(function(resolve, reject) {
                    setTimeout(() => {
                        let number = 10;
                        if (number > 9) {
                        resolve(number);  // resolve 함수 : 해당 케이스시  number를 반환
                        } 
                        else {
                        reject("error");  // reject 함수 : 해당 케이스시, 'error' 문자를 반환
                        }
                    }, 1000);   // 1초 대기
                    });
                    
                    runcode.then(
                        function(item) {   // item은 resolve 또는 reject 함수의 리턴값
                        console.log("success", item);
                        return 2}          // 다음 then에 물려줄 인자. (return이 없다면, 다음 then의 item은 undefined가 됨)
                    ).then(
                      function(item) {   // item은 resolve 또는 reject 함수의 리턴값
                      console.log("success", item);
                      }
                  )
                    .catch((error) => {
                      console.log(error);
                    }
                    )




// Promise 의 메소드 
            //catch 메소드  : then에서 (이행, 에러) 중 이행만 적혀있을때, 에러 케이스 발생시 Promise에서 정의된 reject 성분으로  
                        //    리턴해줄수 있도록 하는 함수 (만약, then에서 에러에 대해 정의가 되어 있으면 catch 미실행)
                        //    또한 이행도, 에러도 아닌 상황이 (매우 드물겠지만) 발생한다면, 그때도 catch 메소드 작동됨

            const runcode = new Promise(function(resolve, reject) {
                setTimeout(() => {
                    let number = 1;
                    if (number > 9) {
                    resolve(number);  // resolve 함수 : 해당 케이스시  number를 반환
                    } 
                    else {
                    reject("error입니다.");  // reject 함수 : 해당 케이스시, 'error' 문자를 반환
                    }
                }, 1000);   // 1초 대기
                });
                
                runcode.then(
                    function(item) {   // item은 resolve 또는 reject 함수의 리턴값
                    console.log("success", item);  // 이행 case에 대해서만 정의해줌
                    }
                ).catch((error) => {   // 에러 발생시, Promise의 reject 함수의 리턴값을 반환
                  console.log(error);  // 출력 결과 : 'error입니다'
                });


                // error case시, then이 여러개 있을때
                const runcode = new Promise(function(resolve, reject) {
                    setTimeout(() => {
                        let number = 1;
                        if (number > 9) {
                        resolve(number);  // resolve 함수 : 해당 케이스시  number를 반환
                        } 
                        else {
                        reject("error입니다.");  // reject 함수 : 해당 케이스시, 'error' 문자를 반환
                        }
                    }, 1000);   // 1초 대기
                    });
                    
                    runcode.then(
                        function(item) {   
                        console.log("success", item); // 미실행 (여기는 이행 항)
                        return 2}
                    ).then(
                      function(item) {   
                      console.log("success", item);   // 미실행 (여기는 이행 항)
                      }
                    ).catch((error) => {   // 에러 발생시, Promise의 reject 함수의 리턴값을 반환
                      console.log(error);  // 출력 결과 : 'error입니다'
                    });


                // finally  : 거의 모든 경우에 가장 뒤에 실행된다.

                 // 1)에러 케이스가 있을 경우
                const runcode = new Promise(function(resolve, reject) {
                    setTimeout(() => {
                        let number = 1;   
                        if (number > 9) {
                        resolve(number);  // resolve 함수 : 해당 케이스시  number를 반환
                        } 
                        else {
                        reject("error");  // reject 함수 : 해당 케이스시, 'error' 문자를 반환
                        }
                    }, 1000);   // 1초 대기
                    });
                    
                    runcode.then(
                        function(item) {   
                        console.log("success", item); // 미실행 (여기는 이행 항)
                        return 2}
                    ).then(
                      function(item) { 
                      console.log("success", item);  // 미실행 (여기는 이행 항)
                      }
                  )
                    .catch((error) => {
                      console.log(error);    // 출력 : error입니다.
                    }
                    ).finally(() => {
                      console.log('finally'); // 출력 : 'finally'



                    //2) 에러 케이스가 없을 경우
                const runcode = new Promise(function(resolve, reject) {
                    setTimeout(() => {
                        let number = 10;   
                        if (number > 9) {
                        resolve(number);  // resolve 함수 : 해당 케이스시  number를 반환
                        } 
                        else {
                        reject("error");  // reject 함수 : 해당 케이스시, 'error' 문자를 반환
                        }
                    }, 1000);   // 1초 대기
                    });
                    
                    runcode.then(
                        function(item) {   
                        console.log("success", item); // 실행, 출력 : 10
                        return 2}
                    ).then(
                      function(item) { 
                      console.log("success", item);  // 실행, 출력 : 2
                      }
                  )
                    .catch((error) => {
                      console.log(error);    // 미실행
                    }
                    ).finally(() => {
                      console.log('finally'); // 출력 : 'finally'
                //  만약 catch가 finally 뒤에 있다면, finally가 먼저 실행되고, 그다음 catch가 실행됨 (둘은 적힌 순서대로 실행됨)    
                



                // Throw  : 사용자 정의 예외 상황을 만드는 함수 (파이썬의 Exception 같은 기능)
                
                throw new Error('에러 메시지!') // 출력 : Error: 에러 메시지!

                // Promise.all ,   Promise.race      
                // all : 언급된 promise가 모두 실행되면, 실행함
                // race : 언급된 promise 중 한개라도 실행되면, 실행함    
                const promise1 = new Promise((resolve, reject) => {
                    setTimeout(() => resolve("100ms"), 100);
                    console.log('1');
                  })
                  
                  const promise2 = new Promise((resolve, reject) => {
                    setTimeout(() => resolve("500ms"), 500);
                    console.log('2');
                  })
                  
                  const promise3 = new Promise((resolve, reject) => {
                    setTimeout(() => resolve("1500ms"), 1500);
                    console.log('3');
                  })
                  
                  Promise.all([promise1, promise2, promise3]).then((data) => {   // promise 1, 2, 3 모두 실행후,  실행됨
                    console.log('all', data);
                  })
                  
                  Promise.race([promise1, promise2, promise3]).then((data) => {  // 가장 빠른 promise1만 실행하면, 실행됨
                    console.log('race', data);
                  })





// 웹브라우져 객체, DOM, RENDER, Parsing, BOM
// DOM : https://from2020.tistory.com/23
// BROWSER REDERING :  https://beomy.github.io/tech/browser/browser-rendering/
// 렌더링 엔진 : https://namu.wiki/w/%EC%97%94%EC%A7%84/%EC%9B%B9%20%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80

// 웹브라우져 객체 : 최상위 객체로서, 브라우져 환경 전체 객체를 의미함. (DOM , BOM, 자바스크립트 객체 등을 포함함) -> 크롬 콘솔에서 window 객체 쳐보기
// DOM은 문서 객체 모델, RENDERING은 요청받은 내용을 브라우져 화면에 나타내는 것
// Parsing은 문서를 파악하고 의미를 추출하는것 - javascript 실행시 parsing을 멈추고, 렌더링 엔진은 javascript 엔진에 권한을 잠시 넘겨 파싱함.
// 이때문에 <body> 끝에 자바스크립트 코드를 주로 쓴다. (중간에 있으면 html/css 파싱하다말고, 자바로 넘어가버리게 됨 -> 화면 이상 발생 가능성)
// Dom Tree는 html 문서(또는 xml)를 구조화(파싱)하는 것, Style Rule은 Css를 구조화(파싱)하는 것
// Rendering Tree는 Dom Tree(html)과 Style Rule(Css)를 융합하여 구조화(파싱)하는 것
// Bom : brower object model (브라우져 객체 모델), location이나 navigator 등의 브라우져 객체 사용)

// ex) document.body.style.background = 'red'   -> 문서 객체에서 - body - style 에서 background를 red로 만들어라

// -User Interface: 주소 표시줄, 이전/다음 버튼, 북마크 메뉴 등. 요청한 페이지를 보여주는 창을 제외한 나머지 모든 부분
// -Browser Engine: User Interface와 Rendering Engine 사이의 동작을 제어, 
                    // 엔진명이 따로 있다기보다는 브라우저 자체를 의미하는 것으로 보임
// -Rendering Engine: 요청한 콘텐츠를 표시, HTML을 요청하면 HTML과 CSS를 파싱 하여 화면에 표시함
// -Networking: HTTP 요청과 같은 네트워크 호출에 사용됨
// -Javascript Interpreter(또는 Engine): 자바스크립트 코드를 해석하고 실행함. 크롬에서는 V8 엔진을 사용함
// -Display Backend: 기본적인 위젯(콤보 박스 등..)을 그림
// -Data Persistence: Local Storage, 쿠키 등 클라이언트 사이드에서 데이터를 저장하는 영역



// 요소(Node)를 활용한 접급 메소드
    // 1. parentNode : 부모 노드
    // 2. childNodes : 자식 노드 리스트
    // 3. firstChild : 첫 번째 자식 노드
    // 4. lastChild : 마지막 자식 노드
    // 5. nextSibling : 다음 형제 노드
    // 6. previousSibling : 이전 형제 노드




              
// dom 요소를 객체화 하여 이벤트 동작 : mouseover, mouseout

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

                        box.addEventListener('click', () =>{     // 다시 이벤트 함수를 삭제해주는 이벤트 추가 (원상복귀)
                        box.style.background = 'transparent'
                        box.removeEventListener('mouseover', makeRed);  
                        box.removeEventListener('mouseover', makeYellow);
                        })
                        
                        </script>
                        </body>

        </html>




// babel.js : ES6을 지원하지 않는 플랫폼을 사용할때, 사용자는 ES6을 지원하는 문법을 그냥 쓰고 
// ES6 문법을 해당 플랫폼에 적용하가능한 다른 문법으로 자동 변경시켜줌

<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.24.0/babel.js"></script>
<script type="text/babel" src="js/main.js"></script>

