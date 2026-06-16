# Django Signals Assessment Submission

Repository:
https://github.com/naveenpodisetti/django-signal-syno-demo

## Topics Covered

### Question 1

Are Django signals executed synchronously or asynchronously by default?

Answer:
Django signals are executed synchronously by default. The project demonstrates this by introducing a delay inside a signal handler and showing that the caller waits until the signal finishes execution.

### Question 2

Do Django signals run in the same thread as the caller?

Answer:
Yes. By default, Django signal handlers execute in the same thread as the caller. The project demonstrates this by printing and comparing thread identifiers from both the caller and the signal handler.

### Question 3

Do Django signals run in the same database transaction as the caller?

Answer:
Yes. By default, Django signals execute within the same database transaction as the caller. The project demonstrates this using a transaction block and rollback scenario, showing that database operations performed by the signal are rolled back together with the caller's transaction.

## Project Structure

```text
django_signal_demo/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── django_signal_demo/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── employees/
    ├── apps.py
    ├── models.py
    ├── signals.py
    ├── views.py
    ├── urls.py
    └── migrations/
```

Each question includes:

* Source code
* Execution steps
* Expected output
* Explanation of the observed behavior
* Conclusion based on the results

The implementation is intentionally simple and designed to conclusively demonstrate Django signal behavior rather than production-ready architecture.
