
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
        'title': 'Покупка продуктов',
        'category': 'Продукты питания',
        'total': 500,
        'date': '2022-10-01'
    },
    {
        'title': 'Оплата аренды',
        'category': 'Аренда',
        'total': 1500,
        'date': '2022-10-01'
    },
    {
        'title': 'Транспортные расходы',
        'category': 'Транспорт',
        'total': 200,
        'date': '2022-10-01'
    },
    {
        'title': 'Коммунальные платежи',
        'category': 'Коммунальные услуги',
        'total': 300,
        'date': '2022-10-01'
    },
    {
        'title': 'Покупка лекарств',
        'category': 'Здоровье',
        'total': 100,
        'date': '2022-10-01'
    },
    {
        'title': 'Развлечения в кино',
        'category': 'Развлечения',
        'total': 350,
        'date': '2022-10-01'
    },
    {
        'title': 'Покупка новой одежды',
        'category': 'Одежда и обувь',
        'total': 800,
        'date': '2022-10-01'
    },
    {
        'title': 'Курсы по образованию',
        'category': 'Образование',
        'total': 2000,
        'date': '2022-10-01'
    },
    {
        'title': 'Покупка корма для собаки',
        'category': 'Домашние животные',
        'total': 50,
        'date': '2022-10-01'
    },
    {
        'title': 'Наличные расходы',
        'category': 'Наличные деньги',
        'total': 1000,
        'date': '2022-10-01'
    },
    {
        'title': 'Путешествие на выходные',
        'category': 'Путешествия',
        'total': 2000,
        'date': '2022-10-01'
    },
    {
        'title': 'Топливо для автомобиля',
        'category': 'Автомобиль',
        'total': 500,
        'date': '2022-10-01'
    },
    {
        'title': 'Покупка нового телефона',
        'category': 'Техника и электроника',
        'total': 10000,
        'date': '2022-10-01'
    },
    {
        'title': 'Абонемент в тренажерный зал',
        'category': 'Спорт и фитнес',
        'total': 500,
        'date': '2022-10-01'
    },
    {
        'title': 'Ремонт крана в ванной',
        'category': 'Ремонт и обслуживание',
        'total': 800,
        'date': '2022-10-01'
    },
    {
        'title': 'Покупка косметики',
        'category': 'Красота и уход',
        'total': 300,
        'date': '2022-10-01'
    },
    {
        'title': 'Курс по профессиональному развитию',
        'category': 'Профессиональное развитие',
        'total': 1500,
        'date': '2022-10-01'
    },
    {
        'title': 'Пожертвование благотворительности',
        'category': 'Благотворительность',
        'total': 200,
        'date': '2022-10-01'
    },
    {
        'title': 'Отложить на сбережения',
        'category': 'Сбережения',
        'total': 1000,
        'date': '2022-10-01'
    },
    {
        'title': 'Покупка подарка другу',
        'category': 'Подарки и праздники',
        'total': 500,
        'date': '2022-10-01'
    },
    {
        'title': 'Покупка канцтоваров',
        'category': 'Разное',
        'total': 200,
        'date': '2022-10-01'
    },
    {
        'title': 'Оплата интернет-сервисов',
        'category': 'Коммунальные услуги',
        'total': 100,
        'date': '2022-10-01'
    },
    {
        'title': 'Посещение зубного врача',
        'category': 'Здоровье',
        'total': 500,
        'date': '2022-10-01'
    },
    {
        'title': 'Покупка продуктов',
        'category': 'Продукты питания',
        'total': 550,
        'date': '2022-11-01'
    },
    {
        'title': 'Оплата аренды',
        'category': 'Аренда',
        'total': 1500,
        'date': '2022-11-02'
    },
    {
        'title': 'Транспортные расходы',
        'category': 'Транспорт',
        'total': 250,
        'date': '2022-11-03'
    },
    {
        'title': 'Коммунальные платежи',
        'category': 'Коммунальные услуги',
        'total': 300,
        'date': '2022-11-05'
    },
    {
        'title': 'Покупка лекарств',
        'category': 'Здоровье',
        'total': 200,
        'date': '2022-11-08'
    },
    {
        'title': 'Развлечения в кино',
        'category': 'Развлечения',
        'total': 350,
        'date': '2022-11-10'
    },
    {
        'title': 'Покупка новой одежды',
        'category': 'Одежда и обувь',
        'total': 800,
        'date': '2022-11-12'
    },
    {
        'title': 'Курсы по образованию',
        'category': 'Образование',
        'total': 2000,
        'date': '2022-11-15'
    },
    {
        'title': 'Покупка корма для собаки',
        'category': 'Домашние животные',
        'total': 50,
        'date': '2022-11-18'
    },
    {
        'title': 'Наличные расходы',
        'category': 'Наличные деньги',
        'total': 1000,
        'date': '2022-11-20'
    },
    {
        'title': 'Путешествие на выходные',
        'category': 'Путешествия',
        'total': 2000,
        'date': '2022-11-23'
    },
    {
        'title': 'Заправка автомобиля',
        'category': 'Автомобиль',
        'total': 500,
        'date': '2022-11-25'
    },
    {
        'title': 'Покупка нового телефона',
        'category': 'Техника и электроника',
        'total': 10000,
        'date': '2022-11-27'
    },
    {
        'title': 'Абонемент в тренажерный зал',
        'category': 'Спорт и фитнес',
        'total': 500,
        'date': '2022-11-29'
    },
    {
        'title': 'Ремонт крана в ванной',
        'category': 'Ремонт и обслуживание',
        'total': 800,
        'date': '2022-11-30'
    },
    {
        'title': 'Покупка косметики',
        'category': 'Красота и уход',
        'total': 300,
        'date': '2022-12-02'
    }
]



