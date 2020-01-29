from rss_reader.content_loader import ContentLoader
from rss_reader.database_helper import DBHelper
from rss_reader.xml_parser import XmlParser

data = """
<rss xmlns:media="http://search.yahoo.com/mrss/" version="2.0">
<channel>
<title>Чемпионат.com (cтатьи)</title>
<link>https://www.championat.com/</link>
<description>
Все новости и статистика чемпионата России по футболу, ведущих европейских футбольных чемпионатов, еврокубков, чемпионатов Европы и Мира
</description>
<image>...</image>
<item>...</item>
<item>...</item>
<item>...</item>
<item>
<title>
«Сарагоса» — «Реал Мадрид». Прогноз: Зидан побережёт лидеров перед дерби с «Атлетико»
</title>
<link>
https://www.championat.com/bets/article-3958389-saragosa---real-madrid-29-janvarja-prognoz-na-match-kubka-ispanii.html
</link>
<pubDate>Tue, 28 Jan 2020 21:30:08 +0300</pubDate>
<guid>
https://www.championat.com/bets/article-3958389-saragosa---real-madrid-29-janvarja-prognoz-na-match-kubka-ispanii.html
</guid>
<description>
Уже 1 февраля Модрича и компанию ожидает встреча с командой Диего Симеоне.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/h/j/saragosa-real-madrid-prognoz_1580214570907692082.jpg
</url>
<author>Denis Doyle/Getty Images</author>
</image>
<enclosure length="350359" url="https://img.championat.com/news/big/h/j/saragosa-real-madrid-prognoz_1580214570907692082.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>bets</category>
<sport rus="Ставки">bets</sport>
<sections>
<section id="551">Прогнозы</section>
</sections>
<tags>
<tag id="551">ФК Реал Мадрид</tag>
<tag id="22224">Бесплатные прогнозы</tag>
<tag id="2202">ФК Сарагоса</tag>
</tags>
</item>
<item>
<title>
Их не узнать. Как изменились лица девушек, похудевших на десятки килограммов
</title>
<link>
https://www.championat.com/lifestyle/article-3957859-kak-menjajutsja-lica-silno-pohudevshih-devushek-gagarina-adel-foto-do-i-posle.html
</link>
<pubDate>Tue, 28 Jan 2020 21:20:07 +0300</pubDate>
<guid>
https://www.championat.com/lifestyle/article-3957859-kak-menjajutsja-lica-silno-pohudevshih-devushek-gagarina-adel-foto-do-i-posle.html
</guid>
<description>
Их пример доказывает, что лишний вес отражается не только на фигуре.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/d/r/devushki-pohudevshie-na-desjatki-kilogrammov_15801548041751495462.jpg
</url>
<author>instagram.com/tanya_change/</author>
</image>
<enclosure length="271676" url="https://img.championat.com/news/big/d/r/devushki-pohudevshie-na-desjatki-kilogrammov_15801548041751495462.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>lifestyle</category>
<sport rus="Lifestyle">lifestyle</sport>
<sections>
<section id="523">Город</section>
</sections>
<tags>
<tag id="28025">Питание</tag>
<tag id="29249">Похудение</tag>
</tags>
</item>
<item>
<title>
«От грузовиков летят камни – мы их шлемом отбиваем!» Как россияне взяли серебро «Дакара»
</title>
<link>
https://www.championat.com/auto/article-3958623-serebrjanyj-prizjor-dakara-2020-karjakin-i-ego-kollega-shmotev--o-gonke-i-skandale.html
</link>
<pubDate>Tue, 28 Jan 2020 21:00:08 +0300</pubDate>
<guid>
https://www.championat.com/auto/article-3958623-serebrjanyj-prizjor-dakara-2020-karjakin-i-ego-kollega-shmotev--o-gonke-i-skandale.html
</guid>
<description>
Серебряный призёр «Дакара» Карякин и его партнёр по команде Шмотьев – о нарушении регламента конкурентами и том, что лишило россиян победы.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/e/j/dakar--2020_15802370351768813414.jpg
</url>
<author>snagracing.ru</author>
</image>
<enclosure length="470962" url="https://img.championat.com/news/big/e/j/dakar--2020_15802370351768813414.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>auto</category>
<sport rus="Авто">auto</sport>
<sections>
<section id="106">Дакар 2020</section>
</sections>
<tags>
<tag id="28133">Эксклюзив</tag>
<tag id="24463">Сергей Карякин — Ралли-рейды</tag>
<tag id="25996">Дакар — мотовездеходы</tag>
</tags>
</item>
<item>
<title>
«Локомотив» подал в суд на бывшего гендиректора Илью Геркуса. Похоже, всё серьёзно
</title>
<link>
https://www.championat.com/football/article-3958601-za-chto-lokomotiv-podal-v-sud-na-byvshego-gendirektora-ilju-gerkusa.html
</link>
<pubDate>Tue, 28 Jan 2020 20:10:08 +0300</pubDate>
<guid>
https://www.championat.com/football/article-3958601-za-chto-lokomotiv-podal-v-sud-na-byvshego-gendirektora-ilju-gerkusa.html
</guid>
<description>Претензии исчисляются десятками миллионов рублей.</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/u/d/lokomotiv-podal-v-sud-na-byvshego-gendirektora_1580231316715847092.jpg
</url>
<author>Дмитрий Голубович, «Чемпионат»</author>
</image>
<enclosure length="364090" url="https://img.championat.com/news/big/u/d/lokomotiv-podal-v-sud-na-byvshego-gendirektora_1580231316715847092.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>football</category>
<sport rus="Футбол">football</sport>
<sections>
<section id="2">РПЛ</section>
</sections>
<tags>
<tag id="3">ФК Локомотив</tag>
<tag id="19395">Илья Геркус</tag>
</tags>
</item>
<item>
<title>
Шарапова скоро выйдет замуж? Россиянка опубликовала фото с кольцом на безымянном пальце
</title>
<link>
https://www.championat.com/tennis/article-3958559-bojfrend-marii-sharapovoj-sdelal-ej-predlozhenie-marija-vylozhila-foto-s-kolcom-na-palce.html
</link>
<pubDate>Tue, 28 Jan 2020 19:30:08 +0300</pubDate>
<guid>
https://www.championat.com/tennis/article-3958559-bojfrend-marii-sharapovoj-sdelal-ej-predlozhenie-marija-vylozhila-foto-s-kolcom-na-palce.html
</guid>
<description>
В «инстаграме» Шараповой появилась фотография с кольцом. Мария встречается с британским миллионером Гилксом с 2018 года.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/p/v/marija-sharapova-i-aleksandr-gilks_1580227690442920274.jpg
</url>
<author>Dimitrios Kambouris/Getty Images</author>
</image>
<enclosure length="376502" url="https://img.championat.com/news/big/p/v/marija-sharapova-i-aleksandr-gilks_1580227690442920274.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>tennis</category>
<sport rus="Теннис">tennis</sport>
<sections>
<section id="35">WTA</section>
</sections>
<tags>
<tag id="34">Мария Шарапова</tag>
</tags>
</item>
<item>
<title>
«Манчестер Сити» — «Манчестер Юнайтед». Прогноз: Гвардиола не даст Сульшеру шанса на чудо
</title>
<link>
https://www.championat.com/bets/article-3958481-manchester-siti---man-junajted-29-janvarja-prognoz-na-match-kubka-ligi.html
</link>
<pubDate>Tue, 28 Jan 2020 19:15:07 +0300</pubDate>
<guid>
https://www.championat.com/bets/article-3958481-manchester-siti---man-junajted-29-janvarja-prognoz-na-match-kubka-ligi.html
</guid>
<description>
Без Маркуса Рашфорда Сульшеру нечего предложить «горожанам».
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/g/k/manchester-siti-manchester-junajted-prognoz_1580222126780807606.jpg
</url>
<author>Michael Regan/Getty Images</author>
</image>
<enclosure length="276946" url="https://img.championat.com/news/big/g/k/manchester-siti-manchester-junajted-prognoz_1580222126780807606.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>bets</category>
<sport rus="Ставки">bets</sport>
<sections>
<section id="551">Прогнозы</section>
</sections>
<tags>
<tag id="546">Манчестер Юнайтед</tag>
<tag id="602">Манчестер Сити</tag>
<tag id="22224">Бесплатные прогнозы</tag>
</tags>
</item>
<item>
<title>
Хет-трик в овертайме и пятиминутная смена Ковалёва. Самые необычные рекорды НХЛ
</title>
<link>
https://www.championat.com/hockey/article-3958547-samye-neobychnye-rekordy-nhl-pjatiminutnaja-smena-kovaljova.html
</link>
<pubDate>Tue, 28 Jan 2020 19:00:00 +0300</pubDate>
<guid>
https://www.championat.com/hockey/article-3958547-samye-neobychnye-rekordy-nhl-pjatiminutnaja-smena-kovaljova.html
</guid>
<description>
Здесь о тех, кто забил гол, не принимая участия в игре, и о тех, кто не пропустил ни одной шайбы, но всё равно проиграл.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/i/o/aleksej-kovaljov_1580227177829007220.jpg
</url>
<author>Robert Laberge /Getty Images</author>
</image>
<enclosure length="332742" url="https://img.championat.com/news/big/i/o/aleksej-kovaljov_1580227177829007220.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>hockey</category>
<sport rus="Хоккей">hockey</sport>
<sections>
<section id="25">НХЛ</section>
</sections>
<tags>
<tag id="6559">Бостон Брюинз</tag>
<tag id="6585">Чикаго Блэкхоукс</tag>
<tag id="6603">Нью-Джерси Дэвилз</tag>
<tag id="6607">Оттава Сенаторз</tag>
<tag id="160">Алексей Ковалёв</tag>
</tags>
</item>
<item>
<title>
13-летняя дочь Коби собиралась позаботиться о величии отца. И погибла звездой
</title>
<link>
https://www.championat.com/basketball/article-3958541-pogibshaja-doch-kobi-brajanta-mogla-stat-zvezdoj-basketbola.html
</link>
<pubDate>Tue, 28 Jan 2020 18:50:07 +0300</pubDate>
<guid>
https://www.championat.com/basketball/article-3958541-pogibshaja-doch-kobi-brajanta-mogla-stat-zvezdoj-basketbola.html
</guid>
<description>
Джиджи готовилась стать Мамбой женского баскетбола. Отец в неё безгранично верил.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/b/e/kobi-brajant-s-docherju-dzhiannoj_15802264932081803907.jpg
</url>
<author>Ethan Miller/Getty Images</author>
</image>
<enclosure length="367960" url="https://img.championat.com/news/big/b/e/kobi-brajant-s-docherju-dzhiannoj_15802264932081803907.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>basketball</category>
<sport rus="Баскетбол">basketball</sport>
<sections>
<section id="42">НБА</section>
</sections>
<tags>
<tag id="211">Коби Брайант</tag>
</tags>
</item>
<item>
<title>
Последняя надежда России. Павлюченкова сражается с двукратной победительницей «Шлемов»
</title>
<link>
https://www.championat.com/tennis/article-3958501-pavljuchenkova-halep-nadal-29-janvarja-raspisanie-matchej-setka-australian-open-2020.html
</link>
<pubDate>Tue, 28 Jan 2020 18:00:08 +0300</pubDate>
<guid>
https://www.championat.com/tennis/article-3958501-pavljuchenkova-halep-nadal-29-janvarja-raspisanie-matchej-setka-australian-open-2020.html
</guid>
<description>
Анастасия осталось последней россиянкой на Australian Open. Она будет противостоять Мугурусе – бывшей подопечной своего тренера Сьюмика.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/g/m/anastasija-pavljuchenkova_15802232291381229874.jpg
</url>
<author>Mike Owen/Getty Images</author>
</image>
<enclosure length="234024" url="https://img.championat.com/news/big/g/m/anastasija-pavljuchenkova_15802232291381229874.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>tennis</category>
<sport rus="Теннис">tennis</sport>
<sections>
<section id="51">Australian Open 2020</section>
</sections>
<tags>
<tag id="1925">Анастасия Павлюченкова</tag>
<tag id="20050">Australian Open</tag>
</tags>
</item>
<item>
<title>
«Вест Хэм» — «Ливерпуль». Прогноз: Клопп сделает ещё один шаг к чемпионскому титулу
</title>
<link>
https://www.championat.com/bets/article-3958355-vest-hem---liverpul-29-janvarja-prognoz-na-match-apl-v-londone.html
</link>
<pubDate>Tue, 28 Jan 2020 17:15:04 +0300</pubDate>
<guid>
https://www.championat.com/bets/article-3958355-vest-hem---liverpul-29-janvarja-prognoz-na-match-apl-v-londone.html
</guid>
<description>
Матч 18-го тура АПЛ перенесли из-за участия мерсисайдцев в клубном чемпионате мира.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/n/n/vest-hem-liverpul-prognoz_1580211740989688031.jpg
</url>
<author>Matthew Ashton — AMA/Getty Images</author>
</image>
<enclosure length="239683" url="https://img.championat.com/news/big/n/n/vest-hem-liverpul-prognoz_1580211740989688031.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>bets</category>
<sport rus="Ставки">bets</sport>
<sections>
<section id="551">Прогнозы</section>
</sections>
<tags>
<tag id="549">Ливерпуль</tag>
<tag id="22224">Бесплатные прогнозы</tag>
<tag id="1025">Вест Хэм Юнайтед</tag>
</tags>
</item>
<item>
<title>
6 футболистов, которые совершили самый крутой прорыв в карьере за последние 5 лет
</title>
<link>
https://www.championat.com/football/article-3958395-kto-smog-stat-zvezdoj-apl-za-poslednie-5-let.html
</link>
<pubDate>Tue, 28 Jan 2020 17:00:04 +0300</pubDate>
<guid>
https://www.championat.com/football/article-3958395-kto-smog-stat-zvezdoj-apl-za-poslednie-5-let.html
</guid>
<description>Прошли через сложности на пути к своей мечте.</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/k/t/kto-smog-stat-zvezdoj-apl-za-poslednie-5-let_1580217226880791843.jpg
</url>
<author>Getty Images</author>
</image>
<enclosure length="357381" url="https://img.championat.com/news/big/k/t/kto-smog-stat-zvezdoj-apl-za-poslednie-5-let_1580217226880791843.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>football</category>
<sport rus="Футбол">football</sport>
<sections>
<section id="6">Англия</section>
</sections>
<tags>
<tag id="21249">Мохамед Салах</tag>
<tag id="22446">Садио Мане</tag>
<tag id="21657">Вирджил ван Дейк</tag>
<tag id="24662">Н'Голо Канте</tag>
<tag id="26759">Гарри Магуайр</tag>
<tag id="26212">Эдерсон Мораес</tag>
</tags>
</item>
<item>
<title>
Великого чемпиона Джонса не били 12 лет. Его хейтеры ждут чуда от Рейеса. UFC 247: LIVE
</title>
<link>
https://www.championat.com/boxing/article-3958337-dzhon-dzhons---dominik-rejes-na-ufc-247-data-boja-vremja-transljacii-live-do-boja.html
</link>
<pubDate>Tue, 28 Jan 2020 16:35:04 +0300</pubDate>
<guid>
https://www.championat.com/boxing/article-3958337-dzhon-dzhons---dominik-rejes-na-ufc-247-data-boja-vremja-transljacii-live-do-boja.html
</guid>
<description>
На этот раз скандальному Джону Джонсу подобрали реально опасного и большого соперника. Доминик Рейес попробует свергнуть короля 9 февраля.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/i/j/dzhon-dzhons_1580212622937693757.jpg
</url>
<author>Sean M. Haffey/Getty Images</author>
</image>
<enclosure length="202604" url="https://img.championat.com/news/big/i/j/dzhon-dzhons_1580212622937693757.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>boxing</category>
<sport rus="Бокс/ММА">boxing</sport>
<sections>
<section id="549">UFC</section>
</sections>
<tags>
<tag id="5612">Джон Джонс</tag>
</tags>
</item>
<item>
<title>
«Я не заслужил победу». Федерер снова едва не провалился на «Шлеме»
</title>
<link>
https://www.championat.com/tennis/article-3958413-rezultaty-australian-open-2020-federer-chudom-vyshel-v-polufinal-na-dzhokovicha.html
</link>
<pubDate>Tue, 28 Jan 2020 16:15:04 +0300</pubDate>
<guid>
https://www.championat.com/tennis/article-3958413-rezultaty-australian-open-2020-federer-chudom-vyshel-v-polufinal-na-dzhokovicha.html
</guid>
<description>
Всё чаще Роджер сенсационно проигрывает на мэйджорах. В Мельбурне он умудрился уйти с семи матчболов — и встретится с Новаком Джоковичем.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/r/o/federer-snova-edva-ne-provalilsja-na-shleme_15802166791284042147.jpg
</url>
<author>Hannah Peters/Getty Images</author>
</image>
<enclosure length="254832" url="https://img.championat.com/news/big/r/o/federer-snova-edva-ne-provalilsja-na-shleme_15802166791284042147.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>tennis</category>
<sport rus="Теннис">tennis</sport>
<sections>
<section id="51">Australian Open 2020</section>
</sections>
<tags>
<tag id="23">Роджер Федерер</tag>
<tag id="32">Новак Джокович</tag>
<tag id="20050">Australian Open</tag>
</tags>
</item>
<item>
<title>
Фигурному катанию в Европе конец. Российские девочки и в этом виноваты?
</title>
<link>
https://www.championat.com/other/article-3958383-chempionat-evropy-po-figurnomu-kataniju-v-germanii-zavidujut-triumfu-rossii.html
</link>
<pubDate>Tue, 28 Jan 2020 16:00:05 +0300</pubDate>
<guid>
https://www.championat.com/other/article-3958383-chempionat-evropy-po-figurnomu-kataniju-v-germanii-zavidujut-triumfu-rossii.html
</guid>
<description>
Немецкий чиновник раскритиковал юных российских фигуристок. Ох, лучше бы он этого не делал!
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/t/i/chempionat-evropy-po-figurnomu-kataniju_15802144671014423313.jpg
</url>
<author>Maja Hitij/Getty Images</author>
</image>
<enclosure length="300759" url="https://img.championat.com/news/big/t/i/chempionat-evropy-po-figurnomu-kataniju_15802144671014423313.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>other</category>
<sport rus="Другие">other</sport>
<sections>
<section id="104">Фигурное катание</section>
</sections>
<tags>
<tag id="26509">Алина Загитова</tag>
<tag id="28301">Александра Трусова</tag>
<tag id="28303">Алёна Косторная</tag>
<tag id="28307">Анна Щербакова</tag>
</tags>
</item>
<item>
<title>
Провалила допинг-секс. Как необычно канадская чемпионка избежала дисквалификации
</title>
<link>
https://www.championat.com/other/article-3958371-kanadskaja-chempionka-opravdala-polozhitelnuju-doping-probu-seksom.html
</link>
<pubDate>Tue, 28 Jan 2020 15:30:07 +0300</pubDate>
<guid>
https://www.championat.com/other/article-3958371-kanadskaja-chempionka-opravdala-polozhitelnuju-doping-probu-seksom.html
</guid>
<description>
Адвокат смог доказать, что Лоренс Венсан-Лапуант пострадала от страстной любви.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/s/t/lorens-vensan-lapuant_15802132102021924728.jpg
</url>
<author>instagram.com/laurence_vincentlapointe</author>
</image>
<enclosure length="245244" url="https://img.championat.com/news/big/s/t/lorens-vensan-lapuant_15802132102021924728.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>other</category>
<sport rus="Другие">other</sport>
<sections>
<section id="93">Прочие виды спорта</section>
</sections>
<tags>
<tag id="354">Допинг</tag>
</tags>
</item>
<item>
<title>
«Витязь» — «Ак Барс». Прогноз: Билялов справится с Сёминым и Няттиненом
</title>
<link>
https://www.championat.com/bets/article-3958259-vitjaz---ak-bars-29-janvarja-prognoz-na-match-khl.html
</link>
<pubDate>Tue, 28 Jan 2020 15:15:05 +0300</pubDate>
<guid>
https://www.championat.com/bets/article-3958259-vitjaz---ak-bars-29-janvarja-prognoz-na-match-khl.html
</guid>
<description>
Казанцы одержали четыре победы подряд, впереди — непростой выезд в Подольск.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/k/x/vitjaz-ak-bars-prognoz_15802045842126660287.jpg
</url>
<author>Светлана Садыкова, photo.khl.ru</author>
</image>
<enclosure length="414180" url="https://img.championat.com/news/big/k/x/vitjaz-ak-bars-prognoz_15802045842126660287.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>bets</category>
<sport rus="Ставки">bets</sport>
<sections>
<section id="551">Прогнозы</section>
</sections>
<tags>
<tag id="129">ХК Ак Барс</tag>
<tag id="22224">Бесплатные прогнозы</tag>
<tag id="133">ХК Витязь</tag>
</tags>
</item>
<item>
<title>
Самые молодые игроки на сборах «Спартака». Кто такие Дмитрий Маркитесов и Никита Бакалюк
</title>
<link>
https://www.championat.com/football/article-3958301-spartak-rpl-sezon-201920-tedesko-zimnie-sbory-markitesov-i-bakaljuk.html
</link>
<pubDate>Tue, 28 Jan 2020 15:00:04 +0300</pubDate>
<guid>
https://www.championat.com/football/article-3958301-spartak-rpl-sezon-201920-tedesko-zimnie-sbory-markitesov-i-bakaljuk.html
</guid>
<description>
Рассказываем о двух футболистах, в которых поверил Доменико Тедеско.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/j/f/dmitrij-markitesov-i-nikita-bakaljuk_15802173212007749133.jpg
</url>
<author>spartak.com</author>
</image>
<enclosure length="353413" url="https://img.championat.com/news/big/j/f/dmitrij-markitesov-i-nikita-bakaljuk_15802173212007749133.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>football</category>
<sport rus="Футбол">football</sport>
<sections>
<section id="2">РПЛ</section>
</sections>
<tags>
<tag id="1">ФК Спартак</tag>
</tags>
</item>
<item>
<title>
10 игроков, проваливших регулярку КХЛ. От них ждали большего
</title>
<link>
https://www.championat.com/hockey/article-3958287-igroki-provalivshie-reguljarnyj-chempionat-khl-201920.html
</link>
<pubDate>Tue, 28 Jan 2020 14:00:06 +0300</pubDate>
<guid>
https://www.championat.com/hockey/article-3958287-igroki-provalivshie-reguljarnyj-chempionat-khl-201920.html
</guid>
<description>
Эти хоккеисты должны были делать результат, но они разочаровали.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/q/o/10-igrokov-provalivshih-reguljarku-khl_1580206603989609746.jpg
</url>
<author>Максим Шмаков/Сергей Бабунов, photo.khl.ru</author>
</image>
<enclosure length="356694" url="https://img.championat.com/news/big/q/o/10-igrokov-provalivshih-reguljarku-khl_1580206603989609746.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>hockey</category>
<sport rus="Хоккей">hockey</sport>
<sections>
<section id="22">КХЛ</section>
</sections>
<tags>
<tag id="136">ХК СКА</tag>
<tag id="135">ХК ЦСКА</tag>
<tag id="129">ХК Ак Барс</tag>
<tag id="127">ХК Салават Юлаев</tag>
<tag id="126">ХК Металлург Мг</tag>
<tag id="128">ХК Локомотив</tag>
<tag id="179">ХК Динамо Рига</tag>
<tag id="19235">ХК Йокерит</tag>
<tag id="25148">Сергей Андронов</tag>
<tag id="19628">Артём Лукоянов</tag>
<tag id="2406">Никита Бурмистров</tag>
<tag id="23338">Андрей Локтионов</tag>
<tag id="20172">Егор Аверин</tag>
<tag id="25514">Йоонас Кемппайнен</tag>
<tag id="27911">Мэтью Майоне</tag>
</tags>
</item>
<item>
<title>
«Какой позор!» Фигу скопировал сообщение Роналду в связи с гибелью Коби Брайанта
</title>
<link>
https://www.championat.com/football/article-3958289-ronaldu-i-figu-opublikovali-odinakovye-soobschenija-v-pamjat-o-kobi-brajante.html
</link>
<pubDate>Tue, 28 Jan 2020 13:24:07 +0300</pubDate>
<guid>
https://www.championat.com/football/article-3958289-ronaldu-i-figu-opublikovali-odinakovye-soobschenija-v-pamjat-o-kobi-brajante.html
</guid>
<description>Тот случай, когда лучше было промолчать.</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/y/b/figu-skopiroval-soobschenie-ronaldu_1580206579493770607.jpg
</url>
<author>Francesco Pecoraro/Getty Images</author>
</image>
<enclosure length="277793" url="https://img.championat.com/news/big/y/b/figu-skopiroval-soobschenie-ronaldu_1580206579493770607.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>football</category>
<sport rus="Футбол">football</sport>
<sections> </sections>
<tags>
<tag id="584">Криштиану Роналду</tag>
<tag id="211">Коби Брайант</tag>
<tag id="2006">Луиш Фигу</tag>
</tags>
</item>
<item>
<title>
«Адмирал» — ЦСКА. Прогноз: Слепышев продолжит голевую серию во Владивостоке
</title>
<link>
https://www.championat.com/bets/article-3958115-admiral---cska-29-janvarja-prognoz-na-match-khl.html
</link>
<pubDate>Tue, 28 Jan 2020 13:00:07 +0300</pubDate>
<guid>
https://www.championat.com/bets/article-3958115-admiral---cska-29-janvarja-prognoz-na-match-khl.html
</guid>
<description>
«Моряки» продолжают бороться за плей-офф, но в 13 последних матчах добыли лишь три победы.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/g/a/admiral-cska-prognoz_15801919541174210614.jpg
</url>
<author>Сергей Бабунов, photo.khl.ru</author>
</image>
<enclosure length="332531" url="https://img.championat.com/news/big/g/a/admiral-cska-prognoz_15801919541174210614.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>bets</category>
<sport rus="Ставки">bets</sport>
<sections>
<section id="551">Прогнозы</section>
</sections>
<tags>
<tag id="135">ХК ЦСКА</tag>
<tag id="22224">Бесплатные прогнозы</tag>
<tag id="15937">ХК Адмирал</tag>
</tags>
</item>
<item>
<title>
Боженик вместо ЦСКА перешёл к Адвокату. Главные трансферы Европы
</title>
<link>
https://www.championat.com/football/article-3957949-transfery-v-evrope-28-janvarja-2020-goda.html
</link>
<pubDate>Tue, 28 Jan 2020 11:00:07 +0300</pubDate>
<guid>
https://www.championat.com/football/article-3957949-transfery-v-evrope-28-janvarja-2020-goda.html
</guid>
<description>
Два несостоявшихся «армейца» сменили клубы на неделе.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/w/l/robert-bozhenik_1580156545883632346.jpg
</url>
<author>twitter.com/Feyenoord_int</author>
</image>
<enclosure length="283946" url="https://img.championat.com/news/big/w/l/robert-bozhenik_1580156545883632346.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>football</category>
<sport rus="Футбол">football</sport>
<sections> </sections>
<tags>
<tag id="544">Трансферы</tag>
<tag id="4324">Эвер Банега</tag>
<tag id="13912">Виктор Мозес</tag>
<tag id="24595">Эзекил Хенти</tag>
<tag id="26264">Марко Петкович</tag>
<tag id="29273">Даниэль Ольмо</tag>
<tag id="26777">Хесус Вальехо</tag>
</tags>
</item>
<item>
<title>
Рафаэль Надаль — Доминик Тим. Прогноз: Король и Принц грунта выдадут королевский матч
</title>
<link>
https://www.championat.com/bets/article-3957907-rafael-nadal---dominik-tim-28-janvarja-prognoz-na-match-australian-open.html
</link>
<pubDate>Tue, 28 Jan 2020 10:45:08 +0300</pubDate>
<guid>
https://www.championat.com/bets/article-3957907-rafael-nadal---dominik-tim-28-janvarja-prognoz-na-match-australian-open.html
</guid>
<description>
Любопытный факт: соперники встречались 13 раз, но лишь один из них — на харде.
</description>
<image>
<url width="920" height="614">
https://img.championat.com/news/big/e/o/rafael-nadal-dominik-tim-prognoz_15801547471158193352.jpg
</url>
<author>Hannah Peters/Getty Images</author>
</image>
<enclosure length="229119" url="https://img.championat.com/news/big/e/o/rafael-nadal-dominik-tim-prognoz_15801547471158193352.jpg" type="image/jpeg"/>
<category>article</category>
<category>breaking</category>
<category>bets</category>
<sport rus="Ставки">bets</sport>
<sections>
<section id="551">Прогнозы</section>
</sections>
<tags>
<tag id="22224">Бесплатные прогнозы</tag>
<tag id="27">Рафаэль Надаль</tag>
<tag id="21736">Доминик Тим</tag>
</tags>
</item>
</channel>
</rss>
"""


helper = DBHelper()

parser = XmlParser(helper)
parser.parse_xml(data)

loader = ContentLoader()
xml = loader.load_page('https://www.championat.com/rss/news/hockey/superleague/')
print(xml)
# parser.parse_xml(xml)