from tasks import add

result = add.delay(4, 5)

result.get(propagate=False)