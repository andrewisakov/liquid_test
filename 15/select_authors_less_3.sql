select b.isbn, b.name, count(ba.*)
from books b
join books_autohors ba on (ba.book_id=b.id)
group by ba.isbn, ba.name
where count(ba.*) < 3;

+---------------+
| BOOKS         |
+---------------+
|*ISBN          | --> BOOKS_AUTHORS.BOOK_ID
| NAME          |
+---------------+

+---------------+
| BOOKS_AUTHORS |
+---------------+
|*BOOK_ID       | <-- BOOKS.ID
|*AUTHOR_ID     | --> AUTHORS.ID
+---------------+

+---------------+
| AUTHORS       |
+---------------+
|*ID            | <-- BOOKS_AUTHORS.AUTHOR_ID
| NAME          |
+---------------+

* - primary_key
