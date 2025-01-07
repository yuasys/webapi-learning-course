INSERT INTO products (title, created_at)
SELECT 
    'Product Title ' || i AS title,
    NOW() - (INTERVAL '1 day' * FLOOR(random() * 365)) AS created_at
FROM generate_series(1, 1000) AS s(i);

