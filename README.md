# Django Signals Assessment

## Repository
https://github.com/naveenpodisetti/django-signal-syno-demo

### Q1: Are Django signals synchronous?
Demonstrated using a signal handler with time.sleep(5).

### Q2: Do Django signals run in the same thread?
Demonstrated by comparing threading.get_ident() values.

### Q3: Do Django signals run in the same transaction?
Demonstrated using transaction.atomic() and rollback behavior.
