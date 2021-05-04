# ABCNotesAi är mitt AI-projekt för kursen Teknikspecialisering: Systemoptimering och Artificiell Intelligens
### *"The Fosbury Flop of AI-generated music"*- Ludvig Bylund

## Originalidén:
### Mitt projekt började egentligen så fort jag fick höra om [GPT-2](https://openai.com/blog/tags/gpt-2/ "ApenAi GPT-2") och textgenerande AI via övningarna, och en tanke satte sig i min hjärna:
### Skulle det gå att få en AI att generera musik?

Jag började direkt tänka på hur man skulle kunna konvertera musik till text, eftersom att det är det formatet som GPT-2 använder, och hur jag skulle kunna hitta tillräckligt stora mängder data för att träna AIn på. Jag funderade först på ett sätt att konvertera midi-signaler, något som min klasskamrat William hann före mig med, men strök den idén när jag kom till tablatur. Tablatur är ett noteringssätt som uppfanns egentligen för att utrycka hur ett stycke ska spelas för de stränginstrument där samma not kan spelas på flera olika strängar, och är egentigen ett mycket sämre sätt att notera musik än vanlig notation, på grund av dess avsaknad av rytm, och att man behöver specificera hur man ska stämma instrumentet, vilket också betyder att det är svårt att översätta till andra instrument och stämningar.

Jag, som amatör-bassist, tänkte också att det hade varit roligare att använda tablatur för bas, vilket skulle betyda en stor simplifiering, på grund av det att baslinjer ofta har bara en ton åt taget, medan gitarrer oftast spelar på flera strängar, ackord, osv. det skulle dessutom vara roligare för mig om jag kunde försöka spela dessa baslinjer som generades. 

Så jag googlade fram tablatur för den legendariska Funk-låten What Is Hip av Tower of Power, vald på grund av dess väldigt linjära (och väldigt funky)Baslinje. Jag kopierade in tablaturen i en textfil, tryckte ctrl+s och skrev in WhatIsBass.txt och tryckte enter. Det är den filen som syns här bland ABC-noteringen, men den kommer vi till sen. Jag insåg att det inte skulle räcka med en låt för att träna en AI, och satte ut över nätet för att jaga efter fler texter, och insåg snart att det skulle vara otroligt svårt att hitta fler låtar i samma format, med rätt antal tecken per rad, och med rätt spacing mellan noter. Jag tänkte i min lathet att det skulle gå bra ändå, så jag ignorerade dessa detaljer, och skrev ett program i python för att lägga till låtar i min fil från formen på låten och tablaturen till dess delar, vilket var ett betydligt vanligare format.

Efter ett antal timmar av arbete med att hitta och formattera tablatur satte jag igång GPT-2 på min fil, och väntade halvtimmen på resultatet. 

Först hade den lite svårt med formen, och producerade något som skulle kunna se ut som tablatur, för nåt freak-instrument med varierande antal strängar, och den hade inte överhuvudtaget förstått poängen med att spela en not i taget. Så, jag tränade den lite mer, och det började faktiskt se bättre ut! Den hade däremot helt fastnat på att spela baslinjen till Billie Jean av micheal jackson däremot, så det var ändå inte så originellt, även om det hade gått att spela bas till den. 

Jag tänkte att jag hade lite för lite data, det var ändå en väldigt liten mängd låtar som jag hade formatterat, och de var aldrig riktigt likadana, så jag satte mig ut för att skaffa mer. Efter en kort stund av arbete med det helvetet som är tablatur-formattering insåg jag att jag helt enkelt använde fel format. Jag var tvungen att hitta något nytt. 

Det var här ABC-notation dök upp. I min uppgivenhet googlade jag då på text-baserade musikformat, och hamnade efter några sidospår in på [ABC-notation](https://abcnotation.com). Enligt vad jag har förstått från mitt korta sammanträffande med abc-sytemet så är det ett notatonsystem designat av folkmusiker, för folkmusiker, för att snabbt och lätt kunna skriva ner noterna till en låt, inte med samma specificitet på informationen som tablatur, men mycket lättare att skriva ner, och till min fördel, mycket mer standardiserat. Dessutom finns det olika [spelare](https://www.abcjs.net/abcjs-editor.html) online där jag faktiskt kunde spela upp det som genereras av min AI, vilket hjälper otroligt mycket i att se resultat. 

Jag bestämde mig naturligtvis därför för att skita i allt jag gjort hittils med tablatur och börja leta efter data i ABC-format. Det var lite klurigt att hitta låtar i detta nya system, men efter lite trevande på abc-notationens webbsida hittade jag [jackpotten](http://trillian.mit.edu/~jc/cgi/abc/get.cgi?n=1&x=1&F=ABC&S=0.65&X=0&T=ANDERSONSBUDGETOFSTRATHSPEYSREELSCOUNTRYDANCES&U=/~jc/music/book/AndersonsBudgetV1/AndersonsBudgetV1.abc&N=/AndersonsBudgetOfStrathspeysReelsCountryDances.abc). En samling folkmusik och låtar, gratis online i text-format, allting formatterat så det enda jag beövde göra var att ta bort onödig information och kopiera in i en textfil, 403 olika kompositioner, med 403 olika titlar, gratis. Tidigare hade jag haft tålamodet att kopiera in kanske 9-10 låtar i tablatur, och nu hade jag 403.

"Needless to say", AIn genererade mycket bättre resultat. Den behövdes nästan inte tränas alls, på den minsta modellen av GPT-2(124M), och resultatet, bortsett från det at det gick att spela upp direkt, var, kort och gott, musik. Kanske inte de bästa kompositionerna jag hört i mitt liv, men det var musik, med en klar och tydlig tonart, och melodier och rytmer. Jag justerade lite med temperaturen, och resultatet ska gå att hitta i Githuben. 

Och det var min process. Mer dataanalys än programmering, men roligt och lärorikt ändå, generellt ett lyckat projekt. 

Tack för mig. 
