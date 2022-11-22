from pydantic import BaseModel
from pydantic import Field
from pydantic import validator


class InputData(BaseModel):
    gender: str = Field(default="F", title="Пол")
    age: int = Field(default=24, title="Возраст", ge=18, lt=75)
    marital_status: str = Field(default="MAR", title="Семейный статус")
    job_position: str = Field(default="UMN", title="Сфера деятельности")
    credit_sum: float = Field(default=10889.00, title="Сумма кредита")
    credit_month: int = Field(default=12, title="Срок кредита")
    tariff_id: float = Field(default=1.10, title="Тарифный план обслуживания")
    score_shk: float = Field(default=0.24, title="Внутренний рейтинг")
    education: str = Field(default="GRD", title="Степень бразования")
    living_region: str = Field(default="ОБЛ САРАТОВСКАЯ", title="Регион проживания")
    monthly_income: float = Field(default=17000.0, title="Ежемесячный доход")
    credit_count: float = Field(
        default=2.0, title="Кол-во кредитов на момент подачи заявки"
    )
    overdue_credit_count: float = Field(default=1.0, title="Просроченный кредит")

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
            raise ValueError("marital_status possible options: " + "; ".join(values))
        return v
