import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

const app = express();
const port = 3000;

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const folderMap = {
  "01_Zagrebačka županija": "01_Zagrebaƒka ºupanija",
  "02_Krapinsko-zagorska županija": "02_Krapinsko-zagorska ºupanija",
  "03_Sisačko-moslavačka županija": "03_Sisaƒko-moslavaƒka ºupanija",
  "04_Karlovačka županija": "04_Karlovaƒka ºupanija",
  "05_Varaždinska županija": "05_Varaºdinska ºupanija",
  "06_Koprivničko-križevačka županija": "06_Koprivniƒko-kriºevaƒka ºupanija",
  "07_Bjelovarsko-bilogorska županija": "07_Bjelovarsko-bilogorska ºupanija",
  "08_Primorsko-goranska županija": "08_Primorsko-goranska ºupanija",
  "09_Ličko-senjska županija": "09_Liƒko-senjska ºupanija",
  "10_Virovitičko-podravska županija": "10_Virovitiƒko-podravska ºupanija",
  "11_Požeško-slavonska županija": "11_Poºeƒko-slavonska ºupanija",
  "12_Brodsko-posavska županija": "12_Brodsko-posavska ºupanija",
  "13_Zadarska županija": "13_Zadarska ºupanija",
  "14_Osječko-baranjska županija": "14_Osjeƒko-baranjska ºupanija",
  "15_Šibensko-kninska županija": "15_Šibensko-kninska ºupanija",
  "16_Vukovarsko-srijemska županija": "16_Vukovarsko-srijemska ºupanija",
  "17_Splitsko-dalmatinska županija": "17_Splitsko-dalmatinska ºupanija",
  "18_Istarska županija": "18_Istarska ºupanija",
  "19_Dubrovačko-neretvanska županija": "19_Dubrovaƒko-neretvanska ºupanija",
  "20_Međimurska županija": "20_Meƒimurska ºupanija",
  "21_Grad Zagreb": "21_Grad Zagreb"
};

app.get('/rezultati/:round/:folder/', (req, res, next) => {
  const { round, folder } = req.params;
  const rest = req.params[0]; // hvata ostatak URL-a nakon foldera

  const decodedFolder = decodeURIComponent(folder);
  const realFolder = folderMap[decodedFolder] || decodedFolder;

  req.url = `/rezultati/${round}/${realFolder}/${rest}`;
  next();
});

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, () => {
  console.log(`Server radi na http://localhost:${port}`);
});
