// call vs apply
function somefunc(...vars){
    if('sing' in this){
        this.sing()
    }
    if('name' in this){
        console.log(this.name)
    }
    console.log(vars)
}

let o1={
    sing:()=>{
        console.log('I can sing')
    },
    name:'weifo'
}
somefunc(o1)
somefunc.apply(o1,[1,9,9,6],2019,1996)
somefunc.call(o1,'1201','winter','christmas')