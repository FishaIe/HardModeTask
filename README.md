# Задание

Поднять virtualbox с ubuntu в которой будет запущен сервис с docker контейнером в котором будет запущен python тесты через pytest которые используя playwright модуль проверят на любой веб странице несколько полей.
результат тестов оформить в виде allure репорта

# План автоматизации

## 1.	Начальное состояние страницы.

* текст `GitHub User Search` при наведении курсора загорается зелёным и кликабелен;
* текст `the GitHub API` горит зелёным и кликабелен;
* в строке пользователя находится плейсхолдер `Search for a user, e.g. simonsmith`;
* основная область страницы пустая;
* текст в нижнем колонтитуле страницы `source on GitHub` горит зелёным и кликабелен;
* числовые значения в нижнем колонтитуле страницы в разделе `API requests` равняются `Profile:60 Search:10`.

## 2.	Перечень автоматизируемых сценариев.
- ### Позитивные сценарии:

#### 1.	Переход по ссылке в шапке страницы "the GitHub API".
**Этапы воспроизведения:**
* Заходим на сайт **https://simonsmith.github.io/github-user-search/#/search**;
* Кликаем на зелёный текста в шапке странцы `the GitHub API`.

**Ожидаемый результат:** Происходит переадресация на сайт **https://docs.github.com/ru/rest?apiVersion=2022-11-28**.

#### 2.	Переход по ссылке в нижнем колонтитуле страницы "source on GitHub".
**Этапы воспроизведения:**
* Заходим на сайт **https://simonsmith.github.io/github-user-search/#/search**;
* Кликаем на зелёный текста в нижнем колонтитуле страницы `source on GitHub`.

**Ожидаемый результат:** Происходит переадресация на сайт **https://github.com/simonsmith/github-user-search**      

#### 3.	Ввод английского текста в поисковую строку переход на профиль
**Этапы воспроизведения:**
* Заходим на сайт **https://simonsmith.github.io/github-user-search/#/search**;
* Вводим текст в поисковую строку справа сверху `Bob-1`;
* Нажимаем клавишу Enter;
* Кликаем на любой профиль пользователя.

**Ожидаемый результат:**
* Открывается профиль пользователя;
* В нижнем колонтитуле страницы значение `Search:` становится 9 (изначально 10);
* В нижнем колонтитуле страницы значение `Search:` становится 57 (изначально 60).

#### 4.	Возврат на начальную страницу из профиля.
**Этапы воспроизведения:**
* Заходим на сайт **https://simonsmith.github.io/github-user-search/#/search**;
* Вводим текст в поисковую строку справа сверху `Bob-1`;
* Нажимаем клавишу Enter;
* Кликаем на любой профиль пользователя.
* Кликаем на текст в шапке сайта `GitHub User Search`

**Ожидаемый результат:**
* Возврат на начальную страницу сайта - **https://simonsmith.github.io/github-user-search/#/search**;
* В нижнем колонтитуле страницы значение `Search:` становится 9 (изначально 10);
* В нижнем колонтитуле страницы значение `Search:` становится 57 (изначально 60).

#### 5.	Переход по элементу пагинации.
**Этапы воспроизведения:**
* Заходим на сайт **https://simonsmith.github.io/github-user-search/#/search**;
* Вводим текст в поисковую строку справа сверху `Bob-1`;
* Нажимаем клавишу Enter;
* Кликаем на кнопку **Next =>** внизу страницы.

**Ожидаемый результат:**
* Переход на 2'ю страницу результатов поиска;
* В нижнем колонтитуле страницы значение `Search:` становится 8 (изначально 10);
* В нижнем колонтитуле страницы значение `Search:` становится 57 (изначально 60).



- ### Негативные сценарии 
#### 1. Ввод не английского текста в поисковую строку :
Этапы воспроизведения:
* Заходим на сайт **https://simonsmith.github.io/github-user-search/#/search**;
* Вводим текст в поисковую строку справа сверху `Где Что`, `سيدنا`, `描`;
* Нажимаем клавишу Enter.

**Ожидаемый результат:**
* Появляется текст на желтом фоне `Found X result for Z` (Где **X** любое числовое значение, а **Z** поисковой запрос);
* В нижнем колонтитуле страницы значение `Search:` становится 7 (изначально 10);

 #### 2. Произвести поиск при Search:0 :
**Этапы воспроизведения:**
* Заходим на сайт **https://simonsmith.github.io/github-user-search/#/search**;
* Вводим в поисковую строку справа сверху 12 запросов:`A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`, `I`, `J`, `K`, `BOB`.

*Ожидаемый результат:* Поиск по запросу `BOB` не производится, а остается на запросе `K`.

 #### 3. Открыть новый профиль при Profile:0 :
**Этапы воспроизведения:**
* Заходим на сайт **https://simonsmith.github.io/github-user-search/#/search**;
* Вводим текст в поисковую строку справа сверху `Bob`;
* Нажимаем клавишу Enter;
* Кликаем на 21 разных профелей пользователя.

*Ожидаемый результат:* На 21'ый клик откроется профиль который был на 20'ый клик.

# План автоматизации

По итогу автоматицации прикрепляю скрины Allure отчета: 

![img.png](screenshots/img.png)

![img_1.png](screenshots/img_1.png)

![img_2.png](screenshots/img_2.png)

![img_3.png](screenshots/img_3.png)