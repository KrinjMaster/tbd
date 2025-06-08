const jsdom = require("jsdom");
const base = "https://online.metro-cc.ru";

const fetchData = async () => {
  try {
    const req = await fetch("https://online.metro-cc.ru");
    const res = await req.text();
    const dom = new jsdom.JSDOM(res);

    const menubuttons = dom.window.document.querySelectorAll(".menu-item");

    for (let i = 0; i < menubuttons.length; i++) {
      console.log(menubuttons[i].href);
    }

    return res;
  } catch (e) {
    console.log(e);
  }
};

fetchData();

const slugs = [
  "sobstvennye-brendy-metro-2-47609",
  "tovary-dlya-doma-dachi-sada",
  "alkogolnaya-produkciya",
  "bezalkogolnye-napitki",
  "rybnye",
  "myasnye",
  "zamorozhennye-produkty",
  "myasnye_delikatesy",
  "siry",
  "molochnye-prodkuty-syry-i-yayca",
  "sladosti_",
  "hleb-vypechka-torty",
  "ovoshchi-i-frukty",
  "bakaleya",
  "chipsy-sneki-orehi",
  "chaj-kofe-kakao",
  "zdorovoe-pitanie",
  "gotovye-bljuda-polufabrikaty",
  "detskoe-pitanie",
];
