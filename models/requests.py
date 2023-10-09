from datetime import date

from pydantic import BaseModel


class GroupRequest(BaseModel):
    id: None | int = None,
    types: None | str = None,
    date_from: None | date = None,
    date_to: None | date = None,
    statuses: None | str = None,
    office_or_company_id: None | int = None,
    location_id: None | list[int] = None,
    disciplines: None | list[str] = None,
    levels: None | str = None,
    maturities: None | str = None,
    corporative: None | bool = None,
    learning_types: None | list[str] = None,
    teacher_id: None | int = None,
    query_days: None | bool = None,
    query_fiscal_info: None | bool = None,
    query_teacher_prices: None | bool = None


class StudentRequest(BaseModel):
    ed_unit_id: None | int = None,
    ed_unit_types: None | str = None,
    ed_unit_office_or_company_id: None | int = None,
    ed_unit_office_or_company: None | str = None,
    student_client_id: None | int = None,
    date_from: None | date = None,
    date_to: None | date = None,
    statuses: None | str = None,
    query_payers: None | bool = None,
    query_days: None | bool = None
