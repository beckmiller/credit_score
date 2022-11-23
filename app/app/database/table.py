from .connection import Database


def create_table():
    """CREATE tables"""
    with Database("./app/app/database/bank.db") as db:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS clients(
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                gender TEXT NOT NULL,
                age INTEGER NOT NULL,
                marital_status TEXT NOT NULL,
                job_position TEXT NOT NULL,
                credit_sum REAL NOT NULL,
                credit_month INTEGER NOT NULL,
                tariff_id REAL NOT NULL,
                score_shk REAL NOT NULL,
                education TEXT NOT NULL,
                living_region TEXT NOT NULL,
                monthly_income REAL NOT NULL,
                credit_count REAL NOT NULL,
                overdue_credit_count REAL NOT NULL,
                open_account_flg INTEGER NOT NULL
            );"""
        )


def insertData(data, predicted_value):
    """
    Insert user data and predicted value into table
    :param data:
    :param target:
    """

    sql_insert = """INSERT INTO clients
                        VALUES (?,?,?,?,
                                ?,?,?,?,
                                ?,?,?,?,
                                ?,?,?);"""

    with Database("./app/app/database/bank.db") as db:
        db.execute(
            sql_insert,
            (
                None,
                data["gender"],
                data["age"],
                data["marital_status"],
                data["job_position"],
                data["credit_sum"],
                data["credit_month"],
                data["tariff_id"],
                data["score_shk"],
                data["education"],
                data["living_region"],
                data["monthly_income"],
                data["credit_count"],
                data["overdue_credit_count"],
                predicted_value,
            ),
        )
