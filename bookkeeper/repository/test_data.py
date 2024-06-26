
test_categories = {
    'Продукты питания': 'Затраты на покупку еды и напитков',
    'Аренда': 'Расходы на оплату жилья или офисного помещения',
    'Транспорт': 'Затраты на общественный транспорт или ТС',
    'Коммунальные услуги': 'Платежи за электричество, воду, газ и прочие коммунальные услуги',
    'Здоровье': 'Расходы на медицинские услуги, лекарства и страховку',
    'Развлечения': 'Затраты на развлечения, походы в кино, рестораны и прочие мероприятия',
    'Одежда и обувь': 'Затраты на покупку новой одежды, обуви и аксессуаров',
    'Образование': 'Затраты на образовательные курсы, книги и другие образовательные ресурсы',
    'Домашние животные': 'Расходы на кормление, уход и ветеринарные услуги для домашних животных',
    'Наличные деньги': 'Расходы на мелкие покупки и наличные расходы',
    'Путешествия': 'Затраты на путешествия, билеты, проживание и развлечения во время поездок',
    'Автомобиль': 'Затраты на покупку, обслуживание и ремонт автомобиля',
    'Техника и электроника': 'Расходы на приобретение новой техники и электроники',
    'Спорт и фитнес': 'Расходы на занятия спортом, тренажерный зал и спортивное оборудование',
    'Ремонт и обслуживание': 'Затраты на ремонт и обслуживание жилья или автомобиля',
    'Красота и уход': 'Расходы на косметику, парикмахера, косметические процедуры и уход за собой',
    'Профессиональное развитие': 'Затраты на курсы, конференции и тренинги по профессиональному развитию',
    'Благотворительность': 'Пожертвования и благотворительные взносы',
    'Сбережения': 'Затраты на накопления и инвестиции',
    'Подарки и праздники': 'Расходы на подарки в праздники и особые события'
}

test_expenses = [
    {
        'expense': 'Покупка продуктов',
        'category': 'Продукты питания',
        'total': 500,
        'date': '2022-10-01',
        'comment': 'Ежемесячные продукты'
    },
    {
        'expense': 'Оплата аренды',
        'category': 'Аренда',
        'total': 1500,
        'date': '2022-10-01',
        'comment': 'Ежемесячная аренда жилья'
    },
    {
        'expense': 'Транспортные расходы',
        'category': 'Транспорт',
        'total': 200,
        'date': '2022-10-01',
        'comment': 'Транспорт до работы'
    },
    {
        'expense': 'Коммунальные платежи',
        'category': 'Коммунальные услуги',
        'total': 300,
        'date': '2022-10-01',
        'comment': 'Электричество, вода, газ'
    },
    {
        'expense': 'Покупка лекарств',
        'category': 'Здоровье',
        'total': 100,
        'date': '2022-10-01',
        'comment': 'Лекарства от простуды'
    },
    {
        'expense': 'Развлечения в кино',
        'category': 'Развлечения',
        'total': 350,
        'date': '2022-10-01',
        'comment': 'Посещение кинотеатра'
    },
    {
        'expense': 'Покупка новой одежды',
        'category': 'Одежда и обувь',
        'total': 800,
        'date': '2022-10-01',
        'comment': 'Шоппинг по распродаже'
    },
    {
        'expense': 'Курсы по образованию',
        'category': 'Образование',
        'total': 2000,
        'date': '2022-10-01',
        'comment': 'Курсы для повышения квалификации'
    },
    {
        'expense': 'Покупка корма для собаки',
        'category': 'Домашние животные',
        'total': 50,
        'date': '2022-10-01',
        'comment': 'Корм для нашего питомца'
    },
    {
        'expense': 'Наличные расходы',
        'category': 'Наличные деньги',
        'total': 1000,
        'date': '2022-10-01',
        'comment': 'Наличные для мелких трат'
    },
    {
        'expense': 'Путешествие на выходные',
        'category': 'Путешествия',
        'total': 2000,
        'date': '2022-10-01',
        'comment': 'Короткий отдых за городом'
    },
    {
        'expense': 'Топливо для автомобиля',
        'category': 'Автомобиль',
        'total': 500,
        'date': '2022-10-01',
        'comment': 'Заправка автомобиля'
    },
    {
        'expense': 'Покупка нового телефона',
        'category': 'Техника и электроника',
        'total': 10000,
        'date': '2022-10-01',
        'comment': 'Покупка смартфона'
    },
    {
        'expense': 'Абонемент в тренажерный зал',
        'category': 'Спорт и фитнес',
        'total': 500,
        'date': '2022-10-01',
        'comment': 'Абонемент на тренировки'
    },
    {
        'expense': 'Ремонт крана в ванной',
        'category': 'Ремонт и обслуживание',
        'total': 800,
        'date': '2022-10-01',
        'comment': 'Диагностика и ремонт сантехники'
    },
    {
        'expense': 'Покупка косметики',
        'category': 'Красота и уход',
        'total': 300,
        'date': '2022-10-01',
        'comment': 'Косметика для ухода за кожей'
    },
    {
        'expense': 'Курс по профессиональному развитию',
        'category': 'Профессиональное развитие',
        'total': 1500,
        'date': '2022-10-01',
        'comment': 'Онлайн-курс для развития навыков'
    },
    {
        'expense': 'Пожертвование благотворительности',
        'category': 'Благотворительность',
        'total': 200,
        'date': '2022-10-01',
        'comment': 'Помощь нуждающимся'
    },
    {
        'expense': 'Отложить на сбережения',
        'category': 'Сбережения',
        'total': 1000,

        'date': '2022-10-01',
        'comment': 'Накопления на будущее'
    },
    {
        'expense': 'Покупка подарка другу',
        'category': 'Подарки и праздники',
        'total': 500,
        'date': '2022-10-01',
        'comment': 'Подарок для друга на день рождения'
    },
    {
        'expense': 'Покупка канцтоваров',
        'category': 'Разное',
        'total': 200,
        'date': '2022-10-01',
        'comment': 'Приобретение канцелярских принадлежностей'
    },
    {
        'expense': 'Оплата интернет-сервисов',
        'category': 'Коммунальные услуги',
        'total': 100,
        'date': '2022-10-01',
        'comment': 'Ежемесячная оплата интернета'
    },
    {
        'expense': 'Посещение зубного врача',
        'category': 'Здоровье',
        'total': 500,
        'date': '2022-10-01',
        'comment': 'Предварительный осмотр и профилактическое лечение'
    },
    {
        'expense': 'Покупка продуктов',
        'category': 'Продукты питания',
        'total': 550,
        'date': '2022-11-01',
        'comment': 'Ежемесячные продукты'
    },
    {
        'expense': 'Оплата аренды',
        'category': 'Аренда',
        'total': 1500,
        'date': '2022-11-02',
        'comment': 'Ежемесячная аренда жилья'
    },
    {
        'expense': 'Транспортные расходы',
        'category': 'Транспорт',
        'total': 250,
        'date': '2022-11-03',
        'comment': 'Транспорт до работы'
    },
    {
        'expense': 'Коммунальные платежи',
        'category': 'Коммунальные услуги',
        'total': 300,
        'date': '2022-11-05',
        'comment': 'Электричество, вода, газ'
    },
    {
        'expense': 'Покупка лекарств',
        'category': 'Здоровье',
        'total': 200,
        'date': '2022-11-08',
        'comment': 'Лекарства от простуды'
    }
    # ... другие расходы ...
]



test_expenses_no_comment = [
    {
        'expense': 'Покупка продуктов',
        'category': 'Продукты питания',
        'total': 500,
        'date': '2022-10-01'
    },
    {
        'expense': 'Оплата аренды',
        'category': 'Аренда',
        'total': 1500,
        'date': '2022-10-01'
    },
    {
        'expense': 'Транспортные расходы',
        'category': 'Транспорт',
        'total': 200,
        'date': '2022-10-01'
    },
    {
        'expense': 'Коммунальные платежи',
        'category': 'Коммунальные услуги',
        'total': 300,
        'date': '2022-10-01'
    },
    {
        'expense': 'Покупка лекарств',
        'category': 'Здоровье',
        'total': 100,
        'date': '2022-10-01'
    },
    {
        'expense': 'Развлечения в кино',
        'category': 'Развлечения',
        'total': 350,
        'date': '2022-10-01'
    },
    {
        'expense': 'Покупка новой одежды',
        'category': 'Одежда и обувь',
        'total': 800,
        'date': '2022-10-01'
    },
    {
        'expense': 'Курсы по образованию',
        'category': 'Образование',
        'total': 2000,
        'date': '2022-10-01'
    },
    {
        'expense': 'Покупка корма для собаки',
        'category': 'Домашние животные',
        'total': 50,
        'date': '2022-10-01'
    },
    {
        'expense': 'Наличные расходы',
        'category': 'Наличные деньги',
        'total': 1000,
        'date': '2022-10-01'
    },
    {
        'expense': 'Путешествие на выходные',
        'category': 'Путешествия',
        'total': 2000,
        'date': '2022-10-01'
    },
    {
        'expense': 'Топливо для автомобиля',
        'category': 'Автомобиль',
        'total': 500,
        'date': '2022-10-01'
    },
    {
        'expense': 'Покупка нового телефона',
        'category': 'Техника и электроника',
        'total': 10000,
        'date': '2022-10-01'
    },
    {
        'expense': 'Абонемент в тренажерный зал',
        'category': 'Спорт и фитнес',
        'total': 500,
        'date': '2022-10-01'
    },
    {
        'expense': 'Ремонт крана в ванной',
        'category': 'Ремонт и обслуживание',
        'total': 800,
        'date': '2022-10-01'
    },
    {
        'expense': 'Покупка косметики',
        'category': 'Красота и уход',
        'total': 300,
        'date': '2022-10-01'
    },
    {
        'expense': 'Курс по профессиональному развитию',
        'category': 'Профессиональное развитие',
        'total': 1500,
        'date': '2022-10-01'
    },
    {
        'expense': 'Пожертвование благотворительности',
        'category': 'Благотворительность',
        'total': 200,
        'date': '2022-10-01'
    },
    {
        'expense': 'Отложить на сбережения',
        'category': 'Сбережения',
        'total': 1000,
        'date': '2022-10-01'
    },
    {
        'expense': 'Покупка подарка другу',
        'category': 'Подарки и праздники',
        'total': 500,
        'date': '2022-10-01'
    },
    {
        'expense': 'Покупка канцтоваров',
        'category': 'Разное',
        'total': 200,
        'date': '2022-10-01'
    },
    {
        'expense': 'Оплата интернет-сервисов',
        'category': 'Коммунальные услуги',
        'total': 100,
        'date': '2022-10-01'
    },
    {
        'expense': 'Посещение зубного врача',
        'category': 'Здоровье',
        'total': 500,
        'date': '2022-10-01'
    },
    {
        'expense': 'Покупка продуктов',
        'category': 'Продукты питания',
        'total': 550,
        'date': '2022-11-01'
    },
    {
        'expense': 'Оплата аренды',
        'category': 'Аренда',
        'total': 1500,
        'date': '2022-11-02'
    },
    {
        'expense': 'Транспортные расходы',
        'category': 'Транспорт',
        'total': 250,
        'date': '2022-11-03'
    },
    {
        'expense': 'Коммунальные платежи',
        'category': 'Коммунальные услуги',
        'total': 300,
        'date': '2022-11-05'
    },
    {
        'expense': 'Покупка лекарств',
        'category': 'Здоровье',
        'total': 200,
        'date': '2022-11-08'
    },
    {
        'expense': 'Развлечения в кино',
        'category': 'Развлечения',
        'total': 350,
        'date': '2022-11-10'
    },
    {
        'expense': 'Покупка новой одежды',
        'category': 'Одежда и обувь',
        'total': 800,
        'date': '2022-11-12'
    },
    {
        'expense': 'Курсы по образованию',
        'category': 'Образование',
        'total': 2000,
        'date': '2022-11-15'
    },
    {
        'expense': 'Покупка корма для собаки',
        'category': 'Домашние животные',
        'total': 50,
        'date': '2022-11-18'
    },
    {
        'expense': 'Наличные расходы',
        'category': 'Наличные деньги',
        'total': 1000,
        'date': '2022-11-20'
    },
    {
        'expense': 'Путешествие на выходные',
        'category': 'Путешествия',
        'total': 2000,
        'date': '2022-11-23'
    },
    {
        'expense': 'Заправка автомобиля',
        'category': 'Автомобиль',
        'total': 500,
        'date': '2022-11-25'
    },
    {
        'expense': 'Покупка нового телефона',
        'category': 'Техника и электроника',
        'total': 10000,
        'date': '2022-11-27'
    },
    {
        'expense': 'Абонемент в тренажерный зал',
        'category': 'Спорт и фитнес',
        'total': 500,
        'date': '2022-11-29'
    },
    {
        'expense': 'Ремонт крана в ванной',
        'category': 'Ремонт и обслуживание',
        'total': 800,
        'date': '2022-11-30'
    },
    {
        'expense': 'Покупка косметики',
        'category': 'Красота и уход',
        'total': 300,
        'date': '2022-12-02'
    }
]



