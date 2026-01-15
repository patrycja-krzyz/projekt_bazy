CREATE TABLE IF NOT EXISTS attractions (
    attraction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    attraction_name TEXT,
    built_date TEXT
);

CREATE TABLE IF NOT EXISTS usage (
    usage_id INTEGER PRIMARY KEY AUTOINCREMENT,
    attraction_id INTEGER,
    FOREIGN KEY (attraction_id) REFERENCES attractions(attraction_id)
);
        
CREATE TABLE IF NOT EXISTS accident (
    accident_id INTEGER PRIMARY KEY AUTOINCREMENT,
    accident_date TEXT,
    fix_date TEXT,
    comment TEXT
);
 