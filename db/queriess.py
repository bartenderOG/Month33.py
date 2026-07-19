

# -- Create TABLE --




CREATE_USERS_TABLE = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER NOT NULL UNIQUE,
        username TEXT
    )
"""


CREATE_QUESTIONS_TABLE = """
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        questions_text TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
"""

CREATE_RESULTS_TABLE = """
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        questions_id INTEGER NOT NULL,
        is_correct BOOLEAN NOT NULL DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (questions_id) REFERENCES questions(id) ON DELETE CASCADE
    )
"""



# C - R - U -D

# -- USERS --

GET_USER_BY_TG_ID = 'SELECT * FROM users WHERE telegram_id = ?'

INSERT_USER = 'INSERT OR IGNORE INTO users (telegram_id, username) VALUES (?, ?)'

UPDATE_USER_USERNAME = 'UPDATE users SET usernmae = ? WHERE telegram_id = ?'

DELETE_USER = 'DELETE FROM users WHERE telegram_id = ?'


# -- RESULTS --

INSERT_RESULT = """
    INSERT INTO results (user_id, questions_id, is_correct) VALUES (?, ?, ?)
"""

GET_SCORE_BY_USER_ID = """
    SELECT COUNT(*) AS total, SUM(is_correct) AS correct FROM results WHERE user_id = ? 
"""

# -- QUESTIONS --

GET_ALL_QUESTIONS = 'SELECT * FROM questions'

GET_QUESTION_BY_ID = 'SELECT * FROM questions WHERE id = ?'

INSERT_QUESTION = 'INSERT INTO questions (questions_text, correct_answer) VALUES (?, ?)'

DELETE_QUESTION = 'DELETE FROM questions WHERE id = ?'


# -- STATS --

GET_HISTORY = """
    SELECT q.questions_text,r.is_correct
    FROM results AS r
    INNER JOIN users AS u
        ON r.user_id = u.id

    INNER JOIN questions AS q
        ON r.questions_id = q.id

    WHERE u.telegram_id = ?
    
    ORDER BY r.id DESC
    LIMIT 5
"""


GET_TOP = """
    SELECT u.username,
    COUNT(*) AS total,
    SUM(is_correct) AS correct

    FROM results AS r

    INNER JOIN users AS u
        ON r.user_id = u.id

    GROUP BY r.user_id
    ORDER BY correct DESC
    LIMIT ?
"""

GET_HARDEST = """
    SELECT q.questions_text,
        ROUND(AVG(r.is_correct) * 100, 1) AS success_rate
    FROM results AS r
    INNER JOIN questions AS q
        ON r.questions_id = q.id
    GROUP BY r.questions_id
    ORDER BY success_rate
    LIMIT 1
"""