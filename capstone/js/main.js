

//로그인 

$('.message a').click(function(){
  $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});



//이용 약관 동의 

const termsCheckbox = (event) => {
  event.preventDefault();
  const agreement1 = document.querySelector(".js-agreement1");
  const agreement2 = document.querySelector(".js-agreement2");
 
  if (!agreement1.checked) {
    window.alert("이용약관 이용동의는 필수입니다.");
  } else if (!agreement2.checked) {
    window.alert("개인정보의 수집 및 이용동의는 필수입니다.");
  } else {
    signupAnimate();
  }
};

const onNoregisterClick = (event) => {
  event.preventDefault();
  if (window.confirm("회원가입을 취소하고 BOOKREST 첫 화면으로 돌아가시겠습니까?")) {
    location.replace("/");
  }
};

const loadName = () => {
  if (name.value.length === 0) {
    errorRed(name, `사용자 이름은 2자 이상이어야 합니다`);
  } else if (name.value.length >= 2) {
    successLight(name);
  } else {
    errorRed(name, `사용자 이름은 2자 이상이어야 합니다`);
  }
};

const signInit = () => {
  name.addEventListener("input", loadName);
  email.addEventListener("input", checkEmail);
  password.addEventListener("input", checkPassword);
  studentID.addEventListener("input", checkstudentID);
  checkbox.addEventListener("change", handleCheckboxForm);

  signupForm.addEventListener("submit", (e) => {
    e.preventDefault();
    checkPassword(password, 1, 6);
    loadName();
    checkEmail(email);
    checkstudentID(studentID);
    handleCheckboxForm();
  });
};

signInit();

const successLight = (input) => {
  const formControl = input.parentElement;
  formControl.classList.remove("error");
};

const checkEmail = () => {
  const emailRule =
    /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  if (emailRule.test(email.value.trim())) {
    successLight(email);
  } else {
    errorRed(email, `이메일이 유효하지 않습니다`);
  }
};


//차트

 