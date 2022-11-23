from pydantic import BaseModel, Field
from pydantic import validator


class InputData(BaseModel):
    gender: str = Field(
        default="F",
        title="Пол"
    )
    age: int = Field(
        default=24,
        title="Возраст",
        ge=18,
        lt=75
    )
    marital_status: str = Field(
        default="MAR",
        title="Семейный статус",
    )
    job_position: str = Field(
        default="UMN",
        title="Сфера деятельности"
    )
    credit_sum: float = Field(
        default=10889.00,
        title="Сумма кредита"
    )
    credit_month: int = Field(
        default=12,
        title="Срок кредита"
    )
    tariff_id: float = Field(
        default=1.10,
        title="Тарифный план обслуживания"
    )
    score_shk: float = Field(
        default=0.24,
        title="Внутренний рейтинг"
    )
    education: str = Field(
        default="GRD",
        title="Степень бразования"
    )
    living_region: str = Field(
        default="ОБЛ САРАТОВСКАЯ",
        title="Регион проживания"
    )
    monthly_income: float = Field(
        default=17000.0,
        title="Ежемесячный доход"
    )
    credit_count: float = Field(
        default=2.0,
        title="Кол-во кредитов на момент подачи заявки"
    )
    overdue_credit_count: float = Field(
        default=1.0,
        title="Просроченный кредит"
    )

    # validations
    @validator("gender")
    def genderValue(cls, v):
        values = ["F", "M"]
        if v not in values:
            raise ValueError("gender possible options: " + "; ".join(values))
        return v

    @validator("marital_status")
    def maritalStatus(cls, v):
        values = ["MAR", "DIV", "UNM", "WID", "CIV"]
        if v not in values:
            raise ValueError(
                "marital_status possible options: " + "; ".join(values))
        return v

    @validator("job_position")
    def jobPosition(cls, v):
        values = [
            "UMN", "SPC", "INP",
            "DIR", "ATP", "BIS",
            "PNA", "WOI", "NOR",
            "WRK", "WRP", "PNV",
            "BIU", "PNI", "HSK",
            "PNS", "INV"
        ]
        if v not in values:
            raise ValueError(
                "job_position possible options: " + "; ".join(values))
        return v

    @validator("education")
    def educationValue(cls, v):
        values = ["GRD", "SCH", "UGR", "PGR", "ACD"]
        if v not in values:
            raise ValueError(
                "education possible options: " + "; ".join(values))
        return v

    @validator('living_region')
    def livingRegion(cls, v):
        values = [
            'МОСКВА', 'ОБЛ САРАТОВСКАЯ', 'ОБЛ ВОЛГОГРАДСКАЯ',
            'ЧЕЛЯБИНСКАЯ ОБЛАСТЬ', 'СТАВРОПОЛЬСКИЙ КРАЙ', 'ОБЛ НИЖЕГОРОДСКАЯ',
            'МОСКОВСКАЯ ОБЛ', 'ХАНТЫ-МАНСИЙСКИЙ АВТОНОМНЫЙ ОКРУГ - ЮГРА',
            'КРАЙ СТАВРОПОЛЬСКИЙ', 'САНКТ-ПЕТЕРБУРГ', 'РЕСП. БАШКОРТОСТАН',
            'ОБЛ АРХАНГЕЛЬСКАЯ', 'ХАНТЫ-МАНСИЙСКИЙ АО', 'РЕСП БАШКОРТОСТАН',
            'ПЕРМСКИЙ КРАЙ', 'КРАСНОДАРСКИЙ КРАЙ', 'РЕСП КАРАЧАЕВО-ЧЕРКЕССКАЯ',
            'САРАТОВСКАЯ ОБЛ', 'ОБЛ КАЛУЖСКАЯ', 'ОБЛ ВОЛОГОДСКАЯ',
            'РОСТОВСКАЯ ОБЛ', 'УДМУРТСКАЯ РЕСП', 'ОБЛ ИРКУТСКАЯ',
            'ПРИВОЛЖСКИЙ ФЕДЕРАЛЬНЫЙ ОКРУГ', 'ОБЛ МОСКОВСКАЯ', 'ОБЛ ТЮМЕНСКАЯ',
            'ОБЛ БЕЛГОРОДСКАЯ', 'РОСТОВСКАЯ ОБЛАСТЬ', 'ОБЛ КОСТРОМСКАЯ',
            'РЕСП ХАКАСИЯ', 'РЕСПУБЛИКА ТАТАРСТАН', 'ИРКУТСКАЯ ОБЛАСТЬ',
            'ОБЛ СВЕРДЛОВСКАЯ', 'ОБЛ ПСКОВСКАЯ', 'КРАЙ ЗАБАЙКАЛЬСКИЙ',
            'СВЕРДЛОВСКАЯ ОБЛ', 'ОБЛ ОРЕНБУРГСКАЯ', 'ОБЛ ВОРОНЕЖСКАЯ',
            'ОБЛ АСТРАХАНСКАЯ', 'ОБЛ ЧЕЛЯБИНСКАЯ', 'ОРЕНБУРГСКАЯ ОБЛ',
            'СВЕРДЛОВСКАЯ ОБЛАСТЬ', 'ЧЕЛЯБИНСКАЯ ОБЛ', 'ТАТАРСТАН РЕСП',
            'УЛЬЯНОВСКАЯ ОБЛ', 'МОСКВА Г', 'ОБЛ НОВОСИБИРСКАЯ',
            'ОБЛ МУРМАНСКАЯ', 'РЕСП. САХА (ЯКУТИЯ)', 'ОБЛ АМУРСКАЯ',
            'ХАБАРОВСКИЙ КРАЙ', 'САНКТ-ПЕТЕРБУРГ Г', 'ЯМАЛО-НЕНЕЦКИЙ АО',
            'ТВЕРСКАЯ ОБЛАСТЬ', 'ЯРОСЛАВСКАЯ ОБЛАСТЬ', 'ОБЛ САМАРСКАЯ',
            'ОБЛ ВЛАДИМИРСКАЯ', 'ОБЛ ЛЕНИНГРАДСКАЯ', 'ОРЛОВСКАЯ ОБЛ',
            'ОБЛ КЕМЕРОВСКАЯ', 'ТЮМЕНСКАЯ ОБЛАСТЬ', 'КРАСНОЯРСКИЙ КРАЙ',
            'ОМСКАЯ ОБЛ', 'ОБЛ КУРСКАЯ', 'ТУЛЬСКАЯ ОБЛ', 'РЕСПУБЛИКА КОМИ',
            'ПРИМОРСКИЙ КРАЙ', 'СМОЛЕНСКАЯ ОБЛАСТЬ', 'ОБЛ КИРОВСКАЯ',
            'САМАРСКАЯ ОБЛАСТЬ', 'ПЕНЗЕНСКАЯ ОБЛ', 'ТВЕРСКАЯ ОБЛ',
            'УДМУРТСКАЯ РЕСПУБЛИКА', 'РЕСП КАРЕЛИЯ', 'РЕСПУБЛИКА БУРЯТИЯ',
            'ОБЛ МАГАДАНСКАЯ', 'РЕСП КОМИ', 'ОРЛОВСКАЯ ОБЛАСТЬ',
            'ТОМСКАЯ ОБЛАСТЬ', 'РЕСП МАРИЙ ЭЛ', 'ОБЛ ИВАНОВСКАЯ',
            'КРАЙ КРАСНОДАРСКИЙ', 'РЕСПУБЛИКА АДЫГЕЯ', 'САРАТОВСКАЯ ОБЛАСТЬ',
            'РЕСП БУРЯТИЯ', 'ЕВРЕЙСКАЯ АОБЛ', 'ХАКАСИЯ РЕСП', 'ПСКОВСКАЯ ОБЛ',
            'САМАРСКАЯ ОБЛ', 'КРАЙ АЛТАЙСКИЙ', 'РЕСП КАБАРДИНО-БАЛКАРСКАЯ',
            'ЯРОСЛАВСКАЯ ОБЛ', 'ТЮМЕНСКАЯ ОБЛ', 'КРАЙ ПЕРМСКИЙ',
            'БАШКОРТОСТАН', 'ОБЛ ТАМБОВСКАЯ', 'ТЫВА РЕСП', 'ОБЛ НОВГОРОДСКАЯ',
            'ОБЛ ТУЛЬСКАЯ', 'АО ХАНТЫ-МАНСИЙСКИЙ АВТОНОМНЫЙ ОКРУГ - Ю',
            'ОБЛ КУРГАНСКАЯ', 'ОБЛ ЛИПЕЦКАЯ', 'АРХАНГЕЛЬСКАЯ ОБЛАСТЬ',
            'ТАМБОВСКАЯ ОБЛ', 'САХА /ЯКУТИЯ/ РЕСП',
            'РЕСП СЕВЕРНАЯ ОСЕТИЯ - АЛАНИЯ', 'ОБЛ ТВЕРСКАЯ',
            'ПЕНЗЕНСКАЯ ОБЛАСТЬ', 'УЛЬЯНОВСКАЯ ОБЛАСТЬ', 'СМОЛЕНСКАЯ ОБЛ',
            'Г. САНКТ-ПЕТЕРБУРГ', 'ТОМСКАЯ ОБЛ', 'САХАЛИНСКАЯ ОБЛАСТЬ',
            'ЧУВАШСКАЯ РЕСПУБЛИКА - ЧУВАШИЯ', 'БАШКОРТОСТАН РЕСП',
            'ЛЕНИНГРАДСКАЯ ОБЛ', 'РЕСП МОРДОВИЯ', 'ТУЛЬСКАЯ ОБЛАСТЬ',
            'РЕСПУБЛИКА КАЛМЫКИЯ', 'РЕСП АЛТАЙ', 'РЕСП АДЫГЕЯ', 'ОБЛ БРЯНСКАЯ',
            'ОМСКАЯ ОБЛАСТЬ', 'РЕСП ТАТАРСТАН', 'КАБАРДИНО-БАЛКАРСКАЯ РЕСП',
            'ЧУВАШСКАЯ РЕСПУБЛИКА', 'АО ЯМАЛО-НЕНЕЦКИЙ', 'ОБЛ ПЕНЗЕНСКАЯ',
            'КРАЙ ПРИМОРСКИЙ', 'КРАЙ КАМЧАТСКИЙ', 'САХАЛИНСКАЯ ОБЛ',
            'КРАЙ КРАСНОЯРСКИЙ', 'ОРЕНБУРГСКАЯ ОБЛАСТЬ', 'РЯЗАНСКАЯ ОБЛАСТЬ',
            'РЕСПУБЛИКА КАРЕЛИЯ', 'ОБЛ СМОЛЕНСКАЯ', 'ОБЛ КАЛИНИНГРАДСКАЯ',
            'РЕСПУБЛИКА ТЫВА', 'МУРМАНСКАЯ ОБЛ', 'РЯЗАНСКАЯ ОБЛ',
            'ТАМБОВСКАЯ ОБЛАСТЬ', 'ОБЛ РОСТОВСКАЯ', 'РЕСПУБЛИКА МАРИЙ ЭЛ',
            'АСТРАХАНСКАЯ ОБЛАСТЬ', 'КУРСКАЯ ОБЛ', 'НИЖЕГОРОДСКАЯ ОБЛ',
            'РЕСПУБЛИКА МОРДОВИЯ', 'СЕВЕРНАЯ ОСЕТИЯ - АЛАНИЯ РЕСП',
            'НОВОСИБИРСКАЯ ОБЛ', 'ПСКОВСКАЯ ОБЛАСТЬ',
            'ЧУВАШСКАЯ - ЧУВАШИЯ РЕСП', 'РЕСП САХА /ЯКУТИЯ/', 'РЕСП КАЛМЫКИЯ',
            'НЕНЕЦКИЙ АО', 'МОСКОВСКАЯ ОБЛАСТЬ', 'АРХАНГЕЛЬСКАЯ', 'Г МОСКВА',
            'БУРЯТИЯ РЕСП', 'РЕСП ТЫВА', 'НИЖЕГОРОДСКАЯ ОБЛАСТЬ',
            'ПЕРМСКАЯ ОБЛ', 'ОБЛ РЯЗАНСКАЯ', 'КАЛМЫКИЯ РЕСП',
            'ЗАБАЙКАЛЬСКИЙ КРАЙ', 'КЕМЕРОВСКАЯ ОБЛ', 'РЕСП УДМУРТСКАЯ',
            'КАБАРДИНО-БАЛКАРСКАЯ', 'ОБЛ ЯРОСЛАВСКАЯ', 'ВОЛОГОДСКАЯ ОБЛАСТЬ',
            'МУРМАНСКАЯ ОБЛАСТЬ', 'ВОЛОГОДСКАЯ ОБЛ', 'КЕМЕРОВСКАЯ ОБЛАСТЬ',
            'ИРКУТСКАЯ ОБЛ', 'ВЛАДИМИРСКАЯ ОБЛ', 'АСТРАХАНСКАЯ ОБЛ',
            'КУРСКАЯ ОБЛАСТЬ', 'КУРГАНСКАЯ ОБЛАСТЬ', 'ОБЛ ТОМСКАЯ',
            'ВОРОНЕЖСКАЯ ОБЛ', 'ОБЛ САХАЛИНСКАЯ', 'БЕЛГОРОДСКАЯ ОБЛ',
            'ЛЕНИНГРАДСКАЯ ОБЛАСТЬ', 'РОСТОВСКАЯ', 'ВОЛГОГРАДСКАЯ ОБЛАСТЬ',
            'ВОЛОГОДСКАЯ', 'ГОРЬКОВСКАЯ ОБЛ', 'НОВГОРОДСКАЯ ОБЛ',
            'КАЛИНИНГРАДСКАЯ ОБЛ', 'ОМСКАЯ', 'КОМИ РЕСП',
            'СЕВ. ОСЕТИЯ - АЛАНИЯ', 'РЕСП ДАГЕСТАН', 'САМАРСКАЯ', 'Г. МОСКВА',
            'ОБЛ ОРЛОВСКАЯ', 'АСТРАХАНСКАЯ', 'ВЛАДИМИРСКАЯ ОБЛАСТЬ',
            'КРАЙ ХАБАРОВСКИЙ', 'ВОЛГОГРАДСКАЯ ОБЛ',
            'ЧУВАШИЯ ЧУВАШСКАЯ РЕСПУБЛИКА -', 'КРАСНОДАРСКИЙ',
            'АМУРСКАЯ ОБЛАСТЬ', 'КУРГАНСКАЯ ОБЛ', 'БРЯНСКАЯ ОБЛ',
            'ЧУКОТСКИЙ АО', 'ЧЕЧЕНСКАЯ РЕСПУБЛИКА', 'РЕСПУБЛИКАТАТАРСТАН',
            'ОБЛ УЛЬЯНОВСКАЯ', 'БЕЛГОРОДСКАЯ ОБЛАСТЬ', 'АДЫГЕЯ РЕСП',
            'ОБЛ ОМСКАЯ', 'ТОМСКАЯ', 'РОССИЯ', 'РЕСП ЧЕЧЕНСКАЯ',
            'МАРИЙ ЭЛ РЕСП', 'КИРОВСКАЯ ОБЛ', 'ВОРОНЕЖСКАЯ ОБЛАСТЬ',
            'ЛЕНИНГРАДСКАЯ', 'ЛИПЕЦКАЯ ОБЛ', 'ХАКАСИЯ', 'КОСТРОМСКАЯ ОБЛ',
            'КОМИ', 'БУРЯТИЯ', 'КАЛУЖСКАЯ ОБЛ', 'ЧИТИНСКАЯ ОБЛ',
            'РЕСП ИНГУШЕТИЯ', 'БРЯНСКАЯ ОБЛАСТЬ', 'МОРДОВИЯ РЕСП',
            'АМУРСКАЯ ОБЛ', 'КАРАЧАЕВО-ЧЕРКЕССКАЯ РЕСП', '98',
            'МЫТИЩИНСКИЙ Р-Н', 'АРХАНГЕЛЬСКАЯ ОБЛ', 'СТАВРОПОЛЬСКИЙ',
            'ИВАНОВСКАЯ ОБЛАСТЬ', 'КАЛУЖСКАЯ ОБЛАСТЬ', 'РЕСПУБЛИКА ДАГЕСТАН',
            'ИВАНОВСКАЯ ОБЛ', 'КРАЙ.ПЕРМСКИЙ', 'КАЛУЖСКАЯ',
            'КРАЙ. СТАВРОПОЛЬСКИЙ', 'РЕСПУБЛИКА ХАКАСИЯ', 'ЧЕЧЕНСКАЯ РЕСП',
            'РЕСПУБЛИКА САХА', 'КОСТРОМСКАЯ ОБЛАСТЬ', 'АО НЕНЕЦКИЙ',
            'МОСКОВСКАЯ', 'ДАГЕСТАН РЕСП', 'ОБЛ.РОСТОВСКАЯ',
            'ЛИПЕЦКАЯ ОБЛАСТЬ', 'ЕВРЕЙСКАЯ АВТОНОМНАЯ', 'ЭВЕНКИЙСКИЙ АО',
            'КАМЧАТСКАЯ ОБЛАСТЬ', 'РЕСПУБЛИКА АЛТАЙ', 'АЛТАЙСКИЙ КРАЙ',
            'НОВОСИБИРСКАЯ ОБЛАСТЬ', 'КАМЧАТСКИЙ КРАЙ', 'КАРЕЛИЯ РЕСП',
            'ГУСЬ-ХРУСТАЛЬНЫЙ Р-Н', 'КАЛМЫКИЯ', 'ИНГУШЕТИЯ РЕСП', 'АЛТАЙСКИЙ',
            'КИРОВСКАЯ ОБЛАСТЬ', 'ОБЛ. МУРМАНСКАЯ', 'КАРЕЛИЯ', 'ОБЛ. ЛИПЕЦКАЯ',
            'НОВГОРОДСКАЯ ОБЛАСТЬ', 'БРЯНСКИЙ', 'ПЕРМСКИЙ', 'ОРЁЛ',
            'ОБЛ.НИЖЕГОРОДСКАЯ', 'АОБЛ ЕВРЕЙСКАЯ', 'СВЕРДЛОВСКАЯ',
            'ОБЛ.МОСКОВСКАЯ', 'ОБЛ.САРАТОВСКАЯ', 'ОБЛ. СВЕРДЛОВСКАЯ',
            'ОБЛ. НОВОСИБИРСКАЯ', 'ОБЛ. КУРГАНСКАЯ', 'МАГАДАНСКАЯ ОБЛАСТЬ',
            'ВОЛОГОДСКАЯ ОБЛ.', 'ТЮМЕНСКАЯ', 'КАРАЧАЕВО-ЧЕРКЕССКАЯ',
            'ОБЛ. ЧЕЛЯБИНСКАЯ', 'САХА /ЯКУТИЯ/', 'НОВОСИБИРСКАЯ',
            'КРАЙ. ПЕРМСКИЙ', 'РЕСП ЧУВАШСКАЯ - ЧУВАШИЯ', 'ОБЛ. КИРОВСКАЯ',
            'КАЛИНИНГРАДСКАЯ ОБЛ.'
        ]
        if v not in values:
            raise ValueError(
                "living_region possible options: " + "; ".join(values))
        return v