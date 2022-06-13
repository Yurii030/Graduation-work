
function valid(x){
var alphaDigit= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

//아이디의 입력 타당성 검사
if (x.id.value=="") {
alert("ID를 입력해 주세요.");
x.id.focus();
return; 
}
if (x.id.value.length < 4 || x.id.value.length > 15){
alert("ID는 4~15자 이내여야 합니다.");
x.id.focus();
return;
}
if (x.id.value.indexOf(" ") >= 0) {
alert("ID에는 공백이 들어가면 안됩니다.");
x.id.focus();
return;
}
for (i=0; i<x.id.value.length; i++) {
  if (alphaDigit.indexOf(x.id.value.substring(i, i+1)) == -1) {
  alert("ID는 영문과 숫자의 조합만 사용할 수 있습니다.");
  x.id.focus();
  return;
  }
}

// 비밀번호의  타당성 검사
if (x.pass1.value=="") {
alert("비밀번호를 입력하셔야 합니다.")
x.pass1.focus();
return;
}
if (x.pass1.value.length < 4) {
alert("비밀번호는 4자리 이상 입력하셔야 합니다.");
x.pass1.value="";
x.pass1.focus();
return;
}
if (x.pass2.value==""){
alert("비밀번호를 확인 입력해 주셔야 합니다.")
x.pass2.focus();
return;
}
if (x.pass1.value != x.pass2.value) {
alert("비밀번호가 서로 일치하지 않습니다.");
x.pass1.value=x.pass2.value="";
x.pass1.focus();
return;
} 
if (x.pass1.value.indexOf(" ") >= 0) {
alert("비밀번호에는 공백이 들어가면 안됩니다.");
x.pass1.value=x.pass2.value="";
x.pass1.focus();
return;
}
for (i=0; i<x.pass1.value.length; i++) {
  if (alphaDigit.indexOf(x.pass1.value.substring(i, i+1)) < 0) {
  alert("비밀번호는 영문과 숫자의 조합만 사용할 수 있습니다.");
  x.pass1.value=x.pass2.value="";
  x.pass1.focus();
  return;
  } 
}
alert("잘 입력하셨습니다.")
}