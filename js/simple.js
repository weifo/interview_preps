// 1 Object.freeze()
const box={
    x:10,
    y:20
}
Object.freeze(box);
const shape=box;
shape.x=100
// console.log(shape)
test=Object.isFrozen(12)
// true

// 2 解构赋值
const {name:myName}={name:'Lydia'}
// name -->ReferenceError
// console.log(myName)
const {name}={name:'Lydia'}

// arrow function,closure
const add=()=>{
    const cache={};
    return num=>{
        if(num in cache){
            return `From cache! ${cache[num]}`
        }else{
            const result=num+10;
            cache[num]=result;
            return `Calculated ${result}`;
        }
    }
}

// const addFunc=add()
// console.log(addFunc(5))
// console.log(addFunc(15))
// console.log(addFunc(5*3))

// 3 for loop usage
const myitems=['us','uk','ufo','un']
for(let item in myitems){
    // index
    // console.log(item)
}

for(let item of myitems){
    // item
    // console.log(item)
}

// 4
const list=[1+2,1*2,1/2]
// console.log(list)

// 5 default argument
function sayHi(name) {
    return `Hi there,${name}`
}
// Hi there,undefined
// console.log(sayHi())

// 6
var status='happy'
setTimeout(()=>{
    const status='sad'

    const data={
        status:'angry',
        getStatus(){
            return this.status
        }
    }
    // console.log(data.getStatus())
    // console.log(data.getStatus.call(this))
    
    // node:'angry' undefined
    // 'browser':'angry' 'happy'
},0)
// 'this' differs in node and browser
// node:inside unbind function,this == global;outside func,this=={}
// browser:inside and outside unbind function,this==window,any varibles or functions will be added to this

function test_this() {
    // undefined
    console.log(this.status)
    return 'abc'
}
// test_this()

// 7
function checkAge(age){
    if(age<18){
        const message='Sorry,you\'re too young '
    }else{
        const message ='Ok,you\'re old enough'
    }
    return message
}
// reference error,块级作用域
// checkAge(20)

// 8 Symbol类型不可枚举
const info={
    [Symbol('a')]:'aaa'
}
// console.log(info)
// []
// console.log(Object.keys(info))
// console.log(Object.getOwnPropertySymbols(info))

// 9 箭头函数返回一个对象时，必须使用（）
// ()=>({name:'weifo',age:18})

{
    console.log(app)
    let=app=15
}


