Описание проекта
=======================================

В этом проекте мы создаем модель, которая на основе условий жизни учащегося в возрасте от 15 до 22 лет пытается отследить успеваемость по математике. Таким образом, можно будет заранее найти ребят из группы риска.

Модель создаем на основе набора данных, размещенного в файле __stud_math.csv__.

## Цель проекта

Подготовить модель, на основе которой можно будет заранее определять ребят из группы риска.

## Описание полей набора данных

1. __school__ — аббревиатура школы, в которой учится ученик
2. __sex__ — пол ученика ('F' - женский, 'M' - мужской)
3. __age__ — возраст ученика (от 15 до 22)
4. __address__ — тип адреса ученика ('U' - городской, 'R' - за городом)
5. __famsize__ — размер семьи('LE3' <= 3, 'GT3' >3)
6. __pstatus__ — статус совместного жилья родителей ('T' - живут вместе 'A' - раздельно)
7. __medu__ — образование матери (0 - нет, 1 - 4 класса, 2 - 5-9 классы, 3 - среднее специальное или 11 классов, 4 - высшее)
8. __fedu__ — образование отца (0 - нет, 1 - 4 класса, 2 - 5-9 классы, 3 - среднее специальное или 11 классов, 4 - высшее)
9. __mjob__ — работа матери ('teacher' - учитель, 'health' - сфера здравоохранения, 'services' - гос служба, 'at_home' - не работает, 'other' - другое)
10. __fjob__ — работа отца ('teacher' - учитель, 'health' - сфера здравоохранения, 'services' - гос служба, 'at_home' - не работает, 'other' - другое)
11. __reason__ — причина выбора школы ('home' - близость к дому, 'reputation' - репутация школы, 'course' - образовательная программа, 'other' - другое)
12. __guardian__ — опекун ('mother' - мать, 'father' - отец, 'other' - другое)
13. __traveltime__ — время в пути до школы (1 - <15 мин., 2 - 15-30 мин., 3 - 30-60 мин., 4 - >60 мин.)
14. __studytime__ — время на учёбу помимо школы в неделю (1 - <2 часов, 2 - 2-5 часов, 3 - 5-10 часов, 4 - >10 часов)
15. __failures__ — количество внеучебных неудач (n, если 1<=n<3, иначе 0)
16. __schoolsup__ — дополнительная образовательная поддержка (yes или no)
17. __famsup__ — семейная образовательная поддержка (yes или no)
18. __paid__ — дополнительные платные занятия по математике (yes или no)
19. __activities__ — дополнительные внеучебные занятия (yes или no)
20. __nursery__ — посещал детский сад (yes или no)
21. __higher__ — хочет получить высшее образование (yes или no)
22. __internet__ — наличие интернета дома (yes или no)
23. __romantic__ — в романтических отношениях (yes или no)
24. __famrel__ — семейные отношения (от 1 - очень плохо до 5 - очень хорошо)
25. __freetime__ — свободное время после школы (от 1 - очень мало до 5 - очень мого)
26. __goout__ — проведение времени с друзьями (от 1 - очень мало до 5 - очень много)
27. __health__ — текущее состояние здоровья (от 1 - очень плохо до 5 - очень хорошо)
28. __absences__ — количество пропущенных занятий
29. __score__ — баллы по госэкзамену по математике

## Выполненные этапы

- Сделан предварительный анализ набора.
- Выполнен анализ чесленных переменных.
- Выполнен анализ номинативных переменных.
- Отобраны величины для построеня модели.
- Сделаны выводы о данных.

## Вопросы саморефлексии.

1. **Вопрос:** Какова была ваша роль в команде? **Ответ:** в команде я был слушатель. Шатался по чатикам и тырил идеи, подбирал заметки, говорил задумчиво "Ага!", когда хотел сделать умный вид.
2. **Вопрос:** Какой частью своей работы вы остались особенно довольны? **Ответ:** Практически такой части там нет. Мне все время казалось, что я что-то забыл или упустил из виду.
3. **Вопрос**: Что не получилось сделать так, как хотелось? Над чем ещё стоит поработать? **Ответ**: Не до конца уверен в результатах. Не могу для себя решить, достаточно ли я сделал, чтобы закрыть этот проект. Кажется имело бы смысл сопоставить столбцы не только со score, но и между собой. Вообще проект получился немного узконаправлен. Хотелось бы понять, что из него еще можно вытащить, помимо нашей цели про сопоставление успехов в математике с условиями жизни.
4. **Вопрос**: Что интересного и полезного вы узнали в этом модуле? **Ответ**: Здорово было позаниматься математикой и статистикой. Давно ничего такого не делал и как в универе, конспекты не писал.
5. **Вопрос**: Что является вашим главным результатом при прохождении этого проекта? **Ответ**: Оснонвы основ статистики, которые мне тут попытались дать. Немного по другому стал смотреть на всю область анализа данных.
6. **Вопрос**: Какие навыки вы уже можете применить в текущей деятельности? **Ответ**: Оценка статистической значимости - вот что я хочу попробовать использовать.
7. **Вопрос**: Планируете ли вы дополнительно изучать материалы по теме проекта? **Ответ**: Да, скорее всего. Если будет время на это.

## Результаты работы

Все детали и итоговые результаты работы можно найти в stud_math.ipynb.

Выводы:

__1.__ В данных не так много пустых значений. Не более 40 в каждом из столбце из набора в 395 строк. Итоговый размер после чистки строк с невалидными значениями в score их осталось 330. 

__2.__ Выбросы есть, но их не так много. Был отсеян один 22-летний учащийся, а также учащиеся, прогулявшие более 24 занятий, кроме того были отсеяны учащиеся с оценкой по математике в 0 балов и вообще без оценок. В целом, данные достаточно чистые. 

__3.__ Можно заметить, что у нас есть слабая обратная корреляция между оценкой и количеством прогулов, а также между оценкой и возрастом. Получается, чем старше учащийся, тем меньше у него бал по математике, что может говорить о том, что с возрастом люди могут относится к предмету проще, либо для более взрослых учащихся дается более сложная программа. С прогулами ситуация вполне закономерная - чем больше человек прогуливает, тем хуже он учится. Но так, как характер корреляции довольно слабый, говорить о каком-то катострафическом влиянии десятка прогулов или слишком большого возраста учащегося тут не приходится.

По номинативным переменным можно отметить, что:

- Городские учащиеся показывают лучшие результаты, чем ребята из загорода. Может объяснятся и другими приоритетами, особенностью воспитания, дополнительными потерями времени на дорогу до школуы и многим другим. 
- Образование родителей похожим образом влияют на успеваемость, только в случае матерей, тенденция более ярко выраженная. Удивительно, что дети родителей без образования получают в среднем более высокие оценки, но возможно, что таких детей крайне мало в выборке (на это указывает высокая кучность результатов). 
- Если мать является учителем, то ее дети показывают достаточно высокие результаты, что вполне соответствует обычным представлениям.
- Учащиеся, занимающиеся дополнительно помимо школы, учатся по математике лучше.
- У учащихся с большим количеством неудач имеются более низкие баллы по математике.
- Учащимся с низкими оценками предоставляют дополнительную образовательную поддержку, я бы не стал говорить, что она является причиной низких оценок, скорее это их следствие.
- Чем больше учащиеся гуляют с друзьями, тем хуже учатся, что логично. А если совсем не гуляют, то успеваемость также достаточно низкая. 


__4.__ Статистически значимыми столбцами у нас являются:

- address; 
- medu;
- fedu;
- mjob;
- studytime;
- failures;
- schoolsup;
- goout.

Коррелирующими переменными:
- absences;
- age

И плюс самый важный столбец: score. 

Все эти столбы предлагается включить в модель.