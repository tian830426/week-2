// Answer 1
function calculate(min, max, step){
  var total = [];
  for(var i=min; i<=max; i+=step){
      total.push(i);
  }
  console.log(total.reduce((a,b)=>a+b));
} 
calculate(1, 3, 1); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2); // 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2); // 你的程式要能夠計算 -1+1，最後印出 0

// Answer 2
function avg(data){
  var non_manger_salary=[];
  for(var i=0; i < data["employees"].length; i++) {
        if (data['employees'][i]["manager"]==false){
            non_manger_salary.push(data['employees'][i]['salary']);
        }
  }
  var avg_salary = non_manger_salary.reduce((a,b)=>a+b)/non_manger_salary.length;
  // console.log(non_manger_salary);
  console.log(avg_salary);
}
avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":false
},
{
"name":"Bob",
"salary":60000,
"manager":true
},
{
"name":"Jenny",
"salary":50000,
"manager":false
},
{
"name":"Tony",
"salary":40000,
"manager":false
}
]
}); // 呼叫 avg 函式

//Answer 3
function func(a){
  function cal(b, c){
      return(a+(b*c));
  }
return(cal)
}
console.log(func(2)(3, 4)); // 你補完的函式能印出 2+(3*4) 的結果 14
console.log(func(5)(1, -5)); // 你補完的函式能印出 5+(1*-5) 的結果 0
console.log(func(-3)(2, 9)); // 你補完的函式能印出 -3+(2*9) 的結果 15

//Answer 4
function maxProduct(nums){
    var num = [];
    for(var i=0; i<nums.length; i++){
        for(var j=1; j<nums.length; j++){
            if (i<j){
              num.push(nums[i]*nums[j]);
            }
        }
    }
    console.log(Math.max.apply(null, num));
}
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([10, -20, 0, -3]) // 得到 60
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0 或 -0
maxProduct([5, -1, -2, 0]) // 得到 2
maxProduct([-5, -2]) // 得到 10

//Answer 5
function twoSum(nums, target){
  for(var i=0; i<nums.length; i++){
      for(var j=1; j<nums.length; j++){
          if (i<j && nums[i]+nums[j]==target){ 
            return [i, j];
          }
      }
  }
}
let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

// Answer 6
function maxZeros(nums){
  var str_num = nums.join('');
  var zero = str_num.split('1');
 var zero_len = zero.map(zero=>zero.length);
console.log(Math.max.apply(null, zero_len));
}
maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]) // 得到 3