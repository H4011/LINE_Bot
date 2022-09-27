var A_list = [];
var B_list = [];
var A2_list = [];
var B2_list = [];
var need = false;
function jikaannwari() {
  document.querySelectorAll("div.input-field.A").forEach(element => {
    var count = 0;
    var child = element.children[0].children[1].children;
    if(element.classList[2] != "disabled") {
      for (var iterator of child) {
        if (count >= 1) {
          if(iterator.children[0].textContent == "空き"){
            iterator.classList.add("not-display");
          }
        }
        count++;
      }
    }
  });
  document.querySelectorAll("div.input-field.B").forEach(element => {
    var count = 0;
    var child = element.children[0].children[1].children;
    if(element.classList[2] != "disabled") {
      for (var iterator of child) {
        if (count >= 1) {
          if(iterator.children[0].textContent == "空き"){
            iterator.classList.add("not-display");
          }
        }
        count++;
      }
    }
  });
  console.log("fin2");
}

var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://h4011.github.io/LINE_Bot/A.txt', true);
var A_list3 = [];
var A_list4 = [];
xhr.onreadystatechange = function(){
    if((xhr.readyState == 4) && (xhr.status == 200)){
        var A_list2 = xhr.responseText.split("\n");
        A_list2.forEach(element => {
          A_list3.push(element.split(","));
        });
        A_list3.forEach(element => {
          element.forEach(element2 => {
            if (element2 == "") {
              A_list4.push("空き+空き+空き+空き+空き+空き+空き".split("+"));
            } else {
              var kari = ("空き+"+element2).split("+");
              var kari2 = kari.length;
              for (let index = 0; index < 7 - kari2; index++) {
                kari.push("空き");
              }
              A_list4.push(kari);
            }
          });
          A_list.push(A_list4);
          A_list4 = [];
        });
        console.log(A_list);
    }
}
xhr.send(null);
var xhr2 = new XMLHttpRequest();
xhr2.open('GET', 'https://h4011.github.io/LINE_Bot/B.txt', true);
var B_list3 = [];
var B_list4 = [];
xhr2.onreadystatechange = function(){
    if((xhr2.readyState == 4) && (xhr2.status == 200)){
        var B_list2 = xhr2.responseText.split("\n");
        B_list2.forEach(element => {
          B_list3.push(element.split(","));
        });
        B_list3.forEach(element => {
          element.forEach(element2 => {
            if (element2 == "") {
              B_list4.push("空き+空き+空き+空き+空き+空き+空き".split("+"));
            } else {
              var kari = ("空き+"+element2).split("+");
              var kari2 = kari.length;
              for (let index = 0; index < 7 - kari2; index++) {
                kari.push("空き");
              }
              B_list4.push(kari);
            }
          });
          B_list.push(B_list4);
          B_list4 = [];
        });
        console.log(B_list);
    }
}
xhr2.send(null);
var xhr3 = new XMLHttpRequest();
xhr3.open('GET', 'https://h4011.github.io/LINE_Bot/A2.txt', true);
xhr3.onreadystatechange = function(){
    if((xhr3.readyState == 4) && (xhr3.status == 200)){
      A2_list = xhr3.responseText.replaceAll("\n",",").split(",");
    }
}
xhr3.send(null);
var xhr4 = new XMLHttpRequest();
xhr4.open('GET', 'https://h4011.github.io/LINE_Bot/B2.txt', true);
xhr4.onreadystatechange = function(){
    if((xhr4.readyState == 4) && (xhr4.status == 200)){
      B2_list = xhr4.responseText.replaceAll("\n",",").split(",");
    }
}
xhr4.send(null);
function Set_need() {
  need = true;
  Set_jikannwari();
  window.setTimeout(set, 50);
}
function Reset() {
  need = false;
  Set_jikannwari();
  window.setTimeout(set, 50);
}
function Set_jikannwari() {
  var jikan = document.querySelectorAll("div.input-field.A");
  jikan.forEach(element => {
    element.classList.add("remove");
    element.classList.remove("A");
  });
  var jikan2 = document.querySelectorAll("div.input-field.B");
  jikan2.forEach(element => {
    element.classList.add("remove");
    element.classList.remove("B");
  });
  var jikann = document.querySelectorAll("td.select");
  var count0 = 0;
  jikann.forEach(element => {
    var newElementA = document.createElement("div");
    newElementA.setAttribute("class","input-field A");
    newElementA.setAttribute("id","PC");
    var newElementA2 = document.createElement("select");
    var Option0 = document.createElement("option");
    Option0.setAttribute("value","0");
    var Option1 = document.createElement("option");
    Option1.setAttribute("value","1");
    var Option2 = document.createElement("option");
    Option2.setAttribute("value","2");
    var Option3 = document.createElement("option");
    Option3.setAttribute("value","3");
    var Option4 = document.createElement("option");
    Option4.setAttribute("value","4");
    var Option5 = document.createElement("option");
    Option5.setAttribute("value","5");
    var Option6 = document.createElement("option");
    Option6.setAttribute("value","6");
    if(A2_list[count0] == "0" && need == true) {
      Option0.setAttribute("selected","");
    } else if(A2_list[count0] == "1" && need == true) {
      Option1.setAttribute("selected","");
    } else if(A2_list[count0] == "2" && need == true) {
      Option2.setAttribute("selected","");
    } else if(A2_list[count0] == "3" && need == true) {
      Option3.setAttribute("selected","");
    } else if(A2_list[count0] == "4" && need == true) {
      Option4.setAttribute("selected","");
    } else if(A2_list[count0] == "5" && need == true) {
      Option5.setAttribute("selected","");
    } else if(A2_list[count0] == "6" && need == true) {
      Option6.setAttribute("selected","");
    } else {
      Option0.setAttribute("selected","");
    }
    newElementA2.appendChild(Option0);
    newElementA2.appendChild(Option1);
    newElementA2.appendChild(Option2);
    newElementA2.appendChild(Option3);
    newElementA2.appendChild(Option4);
    newElementA2.appendChild(Option5);
    newElementA2.appendChild(Option6);
    newElementA.appendChild(newElementA2);
    var newElementB = document.createElement("div");
    newElementB.setAttribute("class","input-field B");
    newElementB.setAttribute("id","PC");
    var newElementB2 = document.createElement("select");
    var Option10 = document.createElement("option");
    Option10.setAttribute("value","0");
    var Option11 = document.createElement("option");
    Option11.setAttribute("value","1");
    var Option12 = document.createElement("option");
    Option12.setAttribute("value","2");
    var Option13 = document.createElement("option");
    Option13.setAttribute("value","3");
    var Option14 = document.createElement("option");
    Option14.setAttribute("value","4");
    var Option15 = document.createElement("option");
    Option15.setAttribute("value","5");
    var Option16 = document.createElement("option");
    Option16.setAttribute("value","6");
    if(B2_list[count0] == "0" && need == true) {
      Option10.setAttribute("selected","");
    } else if(B2_list[count0] == "1" && need == true) {
      Option11.setAttribute("selected","");
    } else if(B2_list[count0] == "2" && need == true) {
      Option12.setAttribute("selected","");
    } else if(B2_list[count0] == "3" && need == true) {
      Option13.setAttribute("selected","");
    } else if(B2_list[count0] == "4" && need == true) {
      Option14.setAttribute("selected","");
    } else if(B2_list[count0] == "5" && need == true) {
      Option15.setAttribute("selected","");
    } else if(B2_list[count0] == "6" && need == true) {
      Option16.setAttribute("selected","");
    } else {
      Option10.setAttribute("selected","");
    }
    newElementB2.appendChild(Option10);
    newElementB2.appendChild(Option11);
    newElementB2.appendChild(Option12);
    newElementB2.appendChild(Option13);
    newElementB2.appendChild(Option14);
    newElementB2.appendChild(Option15);
    newElementB2.appendChild(Option16);
    newElementB.appendChild(newElementB2);
    element.appendChild(newElementA);
    element.appendChild(newElementB);
    count0++;
  });
  count0 = 0;
  var jikann2 = document.querySelectorAll("td.select2");
  jikann2.forEach(element => {
    var newElementA = document.createElement("div");
    newElementA.setAttribute("class","input-field A");
    newElementA.setAttribute("id","SP");
    var newElementA2 = document.createElement("select");
    var Option0 = document.createElement("option");
    Option0.setAttribute("value","0");
    var Option1 = document.createElement("option");
    Option1.setAttribute("value","1");
    var Option2 = document.createElement("option");
    Option2.setAttribute("value","2");
    var Option3 = document.createElement("option");
    Option3.setAttribute("value","3");
    var Option4 = document.createElement("option");
    Option4.setAttribute("value","4");
    var Option5 = document.createElement("option");
    Option5.setAttribute("value","5");
    var Option6 = document.createElement("option");
    Option6.setAttribute("value","6");
    if(A2_list[count0] == "0" && need == true) {
      Option0.setAttribute("selected","");
    } else if(A2_list[count0] == "1" && need == true) {
      Option1.setAttribute("selected","");
    } else if(A2_list[count0] == "2" && need == true) {
      Option2.setAttribute("selected","");
    } else if(A2_list[count0] == "3" && need == true) {
      Option3.setAttribute("selected","");
    } else if(A2_list[count0] == "4" && need == true) {
      Option4.setAttribute("selected","");
    } else if(A2_list[count0] == "5" && need == true) {
      Option5.setAttribute("selected","");
    } else if(A2_list[count0] == "6" && need == true) {
      Option6.setAttribute("selected","");
    } else {
      Option0.setAttribute("selected","");
    }
    newElementA2.appendChild(Option0);
    newElementA2.appendChild(Option1);
    newElementA2.appendChild(Option2);
    newElementA2.appendChild(Option3);
    newElementA2.appendChild(Option4);
    newElementA2.appendChild(Option5);
    newElementA2.appendChild(Option6);
    newElementA.appendChild(newElementA2);
    var newElementB = document.createElement("div");
    newElementB.setAttribute("class","input-field B");
    newElementB.setAttribute("id","SP");
    var newElementB2 = document.createElement("select");
    var Option10 = document.createElement("option");
    Option10.setAttribute("value","0");
    var Option11 = document.createElement("option");
    Option11.setAttribute("value","1");
    var Option12 = document.createElement("option");
    Option12.setAttribute("value","2");
    var Option13 = document.createElement("option");
    Option13.setAttribute("value","3");
    var Option14 = document.createElement("option");
    Option14.setAttribute("value","4");
    var Option15 = document.createElement("option");
    Option15.setAttribute("value","5");
    var Option16 = document.createElement("option");
    Option16.setAttribute("value","6");
    if(B2_list[count0] == "0" && need == true) {
      Option10.setAttribute("selected","");
    } else if(B2_list[count0] == "1" && need == true) {
      Option11.setAttribute("selected","");
    } else if(B2_list[count0] == "2" && need == true) {
      Option12.setAttribute("selected","");
    } else if(B2_list[count0] == "3" && need == true) {
      Option13.setAttribute("selected","");
    } else if(B2_list[count0] == "4" && need == true) {
      Option14.setAttribute("selected","");
    } else if(B2_list[count0] == "5" && need == true) {
      Option15.setAttribute("selected","");
    } else if(B2_list[count0] == "6" && need == true) {
      Option16.setAttribute("selected","");
    } else {
      Option10.setAttribute("selected","");
    }
    newElementB2.appendChild(Option10);
    newElementB2.appendChild(Option11);
    newElementB2.appendChild(Option12);
    newElementB2.appendChild(Option13);
    newElementB2.appendChild(Option14);
    newElementB2.appendChild(Option15);
    newElementB2.appendChild(Option16);
    newElementB.appendChild(newElementB2);
    element.appendChild(newElementA);
    element.appendChild(newElementB);
    count0++;
  });
  var count = 0;
  var count2 = 0;
  var count3 = 0;
  var count4 = 0;
  var jikannA = document.querySelectorAll("div.A#PC option");
  jikannA.forEach(element => {
    var text = document.createTextNode(A_list[count][count2][count3]);
    element.appendChild(text);
    if(A_list[count][count2][count3] == "空き"){
      count4++;
    }
    if(count4 == 7){
      console.log(7*count+count2);
      document.querySelectorAll("div.A#PC select")[7*count+count2].setAttribute("disabled","");
      document.querySelectorAll("div.A#PC")[7*count+count2].classList.add("disabled");
    }
    count3++;
    if(count3 == 7){
      count3 = 0;
      count4 = 0;
      count2++;
    }
    if(count2 == 7){
      count2 = 0;
      count++;
    }
  });
  count = 0;
  count2 = 0;
  count3 = 0;
  count4 = 0;
  var jikannB = document.querySelectorAll("div.B#PC option");
  jikannB.forEach(element => {
    var text = document.createTextNode(B_list[count][count2][count3]);
    element.appendChild(text);
    if(B_list[count][count2][count3] == "空き"){
      count4++;
    }
    if(count4 == 7){
      console.log(7*count+count2);
      document.querySelectorAll("div.B#PC select")[7*count+count2].setAttribute("disabled","");
      document.querySelectorAll("div.B#PC")[7*count+count2].classList.add("disabled");
    }
    count3++;
    if(count3 == 7){
      count3 = 0;
      count4 = 0;
      count2++;
    }
    if(count2 == 7){
      count2 = 0;
      count++;
    }
  });
  count = 0;
  count2 = 0;
  count3 = 0;
  count4 = 0;
  var jikannASP = document.querySelectorAll("div.A#SP option");
  jikannASP.forEach(element => {
    var text = document.createTextNode(A_list[count][count2][count3]);
    element.appendChild(text);
    if(A_list[count][count2][count3] == "空き"){
      count4++;
    }
    if(count4 == 7){
      console.log(7*count+count2);
      document.querySelectorAll("div.A#SP select")[7*count+count2].setAttribute("disabled","");
      document.querySelectorAll("div.A#SP")[7*count+count2].classList.add("disabled");
    }
    count3++;
    if(count3 == 7){
      count3 = 0;
      count4 = 0;
      count2++;
    }
    if(count2 == 7){
      count2 = 0;
      count++;
    }
  });
  count = 0;
  count2 = 0;
  count3 = 0;
  count4 = 0;
  var jikannBSP = document.querySelectorAll("div.B#SP option");
  jikannBSP.forEach(element => {
    var text = document.createTextNode(B_list[count][count2][count3]);
    element.appendChild(text);
    if(B_list[count][count2][count3] == "空き"){
      count4++;
    }
    if(count4 == 7){
      console.log(7*count+count2);
      document.querySelectorAll("div.B#SP select")[7*count+count2].setAttribute("disabled","");
      document.querySelectorAll("div.B#SP")[7*count+count2].classList.add("disabled");
    }
    count3++;
    if(count3 == 7){
      count3 = 0;
      count4 = 0;
      count2++;
    }
    if(count2 == 7){
      count2 = 0;
      count++;
    }
  });
  $(document).ready(function(){
    $('select').formSelect();
    var re = document.querySelectorAll("div.remove");
    re.forEach(element => {
      element.remove();
    });
    jikaannwari();
  });
  window.setTimeout(set, 50);
  need = false;
  console.log("fin3");
}

function set(){
  document.querySelectorAll("div.AB ul li").forEach(element => {
    element.setAttribute("onclick","window.setTimeout(clickAB, 50);");
  });
}

var ABtf = true;

$(function() {
  // ボタンをクリックしたら発動
    $('div.AB ul li').click(function() {
      window.setTimeout(clickAB, 50);
    });
});

$(function() {
  // ボタンをクリックしたら発動
    $('a.need').click(function() {
      Set_need();
    });
});
$(function() {
  // ボタンをクリックしたら発動
    $('a.reset').click(function() {
      Reset();
    });
});
function clickAB() {
  var AB = document.querySelector("select.ABclass").selectedIndex;
  if (AB == 1 || AB == 2) {
    console.log("A");
    document.documentElement.style.setProperty('--class-B','none');
    document.documentElement.style.setProperty('--class-A','block');
  } else if(AB == 3 || AB == 4){
    console.log("B");
    document.documentElement.style.setProperty('--class-A','none');
    document.documentElement.style.setProperty('--class-B','block');
  }
  if(ABtf){
    Set_jikannwari();
    ABtf = false;
  }
  window.setTimeout(set, 50);
  console.log(AB);
}
/*
var btn = document.querySelector("div.AB ul li");

btn.onclick = function(){
  var AB = document.querySelector("select.ABclass").selectedIndex;
  if (AB == 1 || AB == 2) {
    console.log("A");
    document.documentElement.style.setProperty('--class-B','none');
    document.documentElement.style.setProperty('--class-A','block');
  } else if(AB == 3 || AB == 4){
    console.log("B");
    document.documentElement.style.setProperty('--class-A','none');
    document.documentElement.style.setProperty('--class-B','block');
  }
  Set_jikannwari();
  console.log(AB);
};
*/