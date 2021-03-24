{
    'name' : 'Security stuff for sarrz.ru',
    'version' : '1.0.0',
    'author' : 'IT-Projects LLC, Ivan Yelizariev',
    'category' : 'Base',
    'website' : 'https://twitter.com/OdooFree',
    'description': """
Tested for 7.0-20140206-002714

    КОММЕНТАРИЙ по использованию.

    После установки модуля в меню Настройки/Пользователи/Пользователи/карточка пользователя появятся галочки с соответсвующими правами, например, "СарРЗ: Менеджер продаж".

    Чтобы назначить пользователя, например, Менеджером продаж, нужно снять все галочки(здесь и далее под галочками понимается также Select Box (выбор из варианта)) и установить только  "СарРЗ: Менеджер продаж". После сохранения некоторые другие галочки станут активными (будут наследованы). Если далее нужно будет убрать у пользователя права менеджера продаж, то нужно снять галочку "СарРЗ: Менеджер продаж". При этом наследованные галочки останутся и их нужно будет убрать вручную.


ТЗ

Задача 1 - Создать разделение прав по группам

Группы:

1. Менеджеры продаж

2. Начальники отделов продаж

3. Снабженцы (пока не делаем)

4. Начальники отделов снабжения (пока не делаем)

5. Бухгалтеры

6. Главбух (пока не делаем)

7. ВЕБ, секретарь.

8. Нач производства (пока не делаем)

9. Директор.



1. Менеджер продаж

1.1. Пользователь видит модули Продажи, Сообщения, Отчетность - только в разрезе своих(моя панель, СРМ, продажи, sales)

1.2. В модуле Продажи закрыть доступ к Настройкам.

1.3. Пользователь может создавать Заказчиков, Звонки, Предложения, Предложения цен, Заказы продаж.

1.4. В поле продавец - обязательно подставляется создающий пользователь.

1.5. Пользователь в пункте меню Заказчики,Звонки, Предложения, Предложения цен, Заказы продаж-  видит  и может изменять только своих ( у которых в поле Продавец указан текущий пользователь.)

    КОММЕНТАРИЙ.

    В меню Заказчики Пользователь также может видеть всех, у кого не указан продавец  или не отмечена галочка "Заказчик" (например, коллеги, свой профиль).

    Eсли у заказчика указан родительский контакт (компания), то такой заказчик будет доступен пользователю, только если ему доступен родительский контакт.

1.6. Поиск - Пользователь в фильтре пункта меню Заказчики может находить названия всех введенных в систему компаний (для проверки наличия компании перед ее созданием). Фильтр должен быть не менее чем по трем символам.

1.7. Пользователь может создать счет по заказу продаж (не может регистрировать оплату - делает бухгалтер) и утвердить его (временное решение - должен быть признак, позволяющий разрешать или запрещеть действие либо строчка кода, где это меняется).

    КОММЕНТАРИЙ.

    Как удалить право утверждения счета:

    *  в файле security_sarrz/security.xml удалить кусок 

    , (4,ref('security_sarrz.group_validate_invoice'))

    (вместе с запятой)

    * обновить модуль "Security stuff for sarrz.ru"

    * у каждого менеждера продаж удалить галочку "утвердить счет"


1.8. Создавать, просматривать и изменять ТМЦ.



2. Начальник отдела.

2.1. Все, что может менеджер по всем менеджерам своего отдела.

   КОММЕНТАРИЙ.

   Отдел продаж указывается в карточке пользователя (res.partner,
   например, можно зайти в продажи-заказчики, убрать фильтр
   "заказчики"). То есть у начальника и менеджера продаж должен быть
   один и тот же отдел продаж.

   Настройки в меню Продажи/Настройки/Отделы продаж -- не учитываются

3. Бухгалтер

3.1. Видит только модуль Учет и Сообщения.

3.2. Видит в меню Касса только записи, относящиеся к журналу кассы BNK1 (не видит кассу директора).



4. ВЕБ- секретарь

4.1. Все, что менеджер.

4.2. Видеть Всех заказчиков, имеющих тэг Сайт и их предложения, звонки. 



5. Директор

5.1. может все, кроме модуля Настройка

    КОММЕНТАРИЙ.

    Моудль "Настройка" доступна только тем, у кого установлена опция "Администрирование" в меню Настройки/пользователи/пользователи.

    Таким образом для директора следует установить все необходимые галочки, кроме "Администрирование". Поскольку разные модули могут вводить разные права, то всего нельзя учесть заранее. Важно отметить, что некоторые Галочки в настройках пользователя не добавляют, а наоборот вводят ограничения. Поэтому полный доступ не всегда означает, что нужно отметить все галочки.

    """,
    'depends' : ['base', 'account', 'sale', 'crm', 'res_partner_default_user_id'],
    'data':[
        'views.xml',
        'security.xml',
        'ir.model.access.csv',
        ],
    'demo':[
        'demo.xml'
    ],
    'installable': True
}
