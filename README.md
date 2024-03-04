[![CC BY 4.0][cc-by-sa-shield]][cc-by-sa]

# Збирка задатака из Сигнала и система у инжењерству - Радна верзија 

У овом репозиторијуму се налази текућа верзија Збирке. Аутор збирке држи 
рачунске вежбе на предмету „Сигнали и системи“ на Електротехничком факултету
Универзитета у Београду. 
Званична страница предмета доступна је на адреси
[http://tnt.etf.rs/~oe2sis](). На основу материјала са рачунских вежби, као и испитних
задатака, Аутор је почео израду збирке задатака која треба да у неком тренутку
прође и званичну процедуру и рецензију и постане званично 
наставно средство на предмету. 
Због идеолошких убеђења, Аутор објављује збирку 
задатака онлајн бесплатно, отвореног кода. 
До тог тренутка, студенти могу слободно да користе овај садржај као најажурнији 
облик материјала за вежбе на Предмету, за потребе припремања предиспитних обавеза и испита.

## Како можете да допринесете?
### Пријављивање грешака у тексту
Аутор ће бити захвалан **свима** који пријаве грешке у Збирци, било какве 
природе. 
Циљ је да се у једном централном систему окупе сви до сада сачињени материјали, и да се све уочене грешке поуздано исправе. За пријаву грешака видети последњу тачку. За пријаву грешака најбоље 
је користити уграђени систем за пријаву проблема [_Issues_](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue) који се користи 
на [**Git**](https://git-scm.com/)-у. 

### Давање идеја за развој збирке
Студенти могу да предлажу идеје користећи исти 
__Issues__ систем (при чему и тада треба ставити 
одговарајући таг). Уколико разумете како 
функционише развој збирке, односно, имате идеју 
како бисте унапредили наставни материјал, 
написали нови задатак, или унапредили постојеће, 
можете се испод упознати са начином на који је 
репозиторијум организован па онда можете и 
клонирати репозиторијум код себе, направити
измене које желите и направити 
[**Pull Request**](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)


## Организација репозиторијума

Основни садржај збирке пише се у језику $\LaTeX$, слике су 
сачињене у програмима 
[xcircuit](http://opencircuitdesign.com/xcircuit/)
и 
[inkscape](https://inkscape.org/). Структура збирке подељена
је по фолдерима. Директоријуми у кореном 
фолдеру представљају поглавља, 
а њихови непосредни подфолдери представљају 
подпоглавља ``.tex`` фајлови унутар њих 
представљају поједине задатке. Поредак поглавља, 
подпоглавља, и задатака у њима, уређен је именима 
фолдера и фајлова. Том приликом, сваки фајл се 
назива у облику ``[реалан број]_...``, односно
почиње једним реалним бројем (са, или без, 
децималне тачке) и доњом цртом. 
Унутар сваког поглавља треба да постоји фајл 
назван ``title.txt`` у коме је исписан
назив поглавља, односно подпоглавља. 

Поредак поглавља, 
подпоглавља и задатака онда је директно 
одређен поретком реалних бројева у називу. Будући да 
су у питању реални бројеви, а између свака
два различита реална броја постоји барем један 
другачији реални број, то значи да ће увек бити
могуће додати ново поглавље или задатак у средиште садржаја.

Тако уређен систем задатака онда обрађује скрипта 
написана у програмском језику ``Python`` која   онда формира коначни ``.tex`` фајл који се 
компајлира и даје коначни ``.pdf`` збирке. 

Да бисте сами компајлирали збирку, потребно је само покренути [__bash__](https://www.gnu.org/software/bash/) скрипту ``compile.sh``

## Лиценцирање

Збирка се објављује под лиценцом
[*Creative Commons* 4.0 Ауторство - делити под истим условима ](https://creativecommons.org/licenses/by-sa/4.0/deed.sr-latn).

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/deed.sr-latn
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

